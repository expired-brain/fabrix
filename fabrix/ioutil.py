import sys
import os
import os.path
import uuid
import StringIO
import pprint
import fabric.state
from fabric.api import env, abort, local, run, get, put, quiet, settings


def read_local_file(local_filename, abort_on_error=True):
    try:
        with open(local_filename) as local_file:
            content = local_file.read()
    except IOError, ex:
        if abort_on_error:
            abort(str(ex))
        else:
            return None
    return content


def read_remote_file(remote_filename, abort_on_error=True):
    file_like_object = StringIO.StringIO()
    with quiet():
        with settings(warn_only=True):
            if get(local_path=file_like_object, remote_path=remote_filename).failed:
                file_like_object.close()
                if abort_on_error:
                    abort('downloading file ' + remote_filename + ' from remote host %s failed' % env.host_string)
                else:
                    return None
            file_like_object.seek(0)
            content = file_like_object.read()
            file_like_object.close()
    return content


def write_local_file(local_filename, new_content):
    old_content = read_local_file(local_filename, abort_on_error=False)
    if new_content == old_content:
        return False
    else:
        _atomic_write_local_file(local_filename, new_content)
        return True


def write_remote_file(remote_filename, new_content):
    old_content = read_remote_file(remote_filename, abort_on_error=False)
    if new_content == old_content:
        return False
    else:
        _atomic_write_remote_file(remote_filename, new_content)
        return True


def _atomic_write_local_file(local_filename, content):
    old_filename = local_filename
    new_filename = old_filename + '.tmp.' + uuid.uuid4().hex + '.tmp'
    with quiet():
        if not os.path.isabs(old_filename):
            abort('local filename must be absolute, "%s" given' % old_filename)
        if os.path.exists(old_filename):
            if os.path.islink(old_filename):
                abort('local filename must be regular file, symlink "%s" given' % old_filename)
            if os.path.isdir(old_filename) or not os.path.isfile(old_filename):
                abort('local filename must be regular file, directory "%s" given' % old_filename)
            old_file_stat = os.stat(old_filename)
            if old_file_stat.st_nlink > 1:
                abort('file "%s" has %d hardlinks, it can\'t be atomically written' % (old_filename, old_file_stat.st_nlink))
        new_file = open(new_filename, 'w')
        new_file.write(content)
        new_file.close()
        if os.path.exists(old_filename):
            if os.path.exists('/usr/bin/getfacl') and os.path.exists('/usr/bin/setfacl'):
                local('getfacl --absolute-names ' + old_filename + ' | setfacl --set-file=- ' + new_filename)
            os.chown(new_filename, old_file_stat.st_uid, old_file_stat.st_gid)
            os.chmod(new_filename, old_file_stat.st_mode)
            with settings(warn_only=True):
                if os.path.exists('/usr/sbin/getenforce'):
                    if local('getenforce', capture=True) != 'Disabled':
                        if os.path.exists('/usr/bin/chcon'):
                            local('chcon  --reference=' + old_filename + ' ' + new_filename)
        os.rename(new_filename, old_filename)


def _atomic_write_remote_file(remote_filename, content):
    old_filename = remote_filename
    new_filename = old_filename + '.tmp.' + uuid.uuid4().hex + '.tmp'
    with quiet():
        if not os.path.isabs(old_filename):
            abort('remote filename must be absolute, "%s" given' % old_filename)
        if run('if [ -e ' + old_filename + ' ] ; then echo exists ; fi') == 'exists':
            if run('if [ -L ' + old_filename + ' ] ; then echo islink ; fi') == 'islink':
                abort('remote filename must be regular file, symlink "%s" given' % old_filename)
            if (run('if [ -d ' + old_filename + ' ] ; then echo isdir ; fi') == 'isdir' or
                    run('if [ ! -e ' + old_filename + ' ] ; then echo notexists ; fi') == 'notexists'):
                abort('remote filename must be regular file, directory "%s" given' % old_filename)
            nlink = int(run('stat --format "%h" ' + old_filename))
            if nlink > 1:
                abort('file "%s" has %d hardlinks, it can\'t be atomically written' % (old_filename, nlink))
        file_like_object = StringIO.StringIO()
        file_like_object.write(content)
        if put(local_path=file_like_object, remote_path=new_filename).failed:
            abort('uploading file ' + new_filename + ' to remote host failed')
        file_like_object.close()
        if run('if [ -e ' + old_filename + ' ] ; then echo exists ; fi') == 'exists':
            if (run('if [ -e /usr/bin/getfacl ] ; then echo exists ; fi') == 'exists' and
                    run('if [ -e /usr/bin/setfacl ] ; then echo exists ; fi') == 'exists'):
                run('getfacl --absolute-names ' + old_filename + ' | setfacl --set-file=- ' + new_filename)
            run('chown --reference=' + old_filename + ' ' + new_filename)
            run('chmod --reference=' + old_filename + ' ' + new_filename)
            with settings(warn_only=True):
                if run('if [ -e /usr/sbin/getenforce ] ; then echo exists ; fi') == 'exists':
                    if run('getenforce') != 'Disabled':
                        if run('if [ -e /usr/bin/chcon ] ; then echo exists ; fi') == 'exists':
                            run('chcon  --reference=' + old_filename + ' ' + new_filename)
        run('mv -f ' + new_filename + ' ' + old_filename)


def debug(*args):
    if fabric.state.output.debug:
        for arg in args:
            if isinstance(arg, basestring):
                if arg[-1] == '\n':
                    sys.stdout.write(arg)
                else:
                    print arg
            else:
                pprint.PrettyPrinter(indent=4).pprint(arg)
            print '-' * 78
