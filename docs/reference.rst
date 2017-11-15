.. meta::
    :description: Fabrix Reference

.. _reference:

Reference
=========

**Configuration**
  - :obj:`~fabrix.config.conf`
  - :obj:`~fabrix.config.local_conf`
  - :func:`~fabrix.config.read_config`

----------------------------------------

**Editor functions**
  - :func:`~fabrix.editor.append_line`
  - :func:`~fabrix.editor.delete_line`
  - :func:`~fabrix.editor.edit_file`
  - :func:`~fabrix.editor.edit_ini_section`
  - :func:`~fabrix.editor.edit_local_file`
  - :func:`~fabrix.editor.edit_text`
  - :func:`~fabrix.editor.insert_line`
  - :func:`~fabrix.editor.prepend_line`
  - :func:`~fabrix.editor.replace_line`
  - :func:`~fabrix.editor.strip_line`
  - :func:`~fabrix.editor.strip_text`
  - :func:`~fabrix.editor.substitute_line`

----------------------------------------

**Input/Output functions**
  - :func:`~fabrix.ioutil.chmod`
  - :func:`~fabrix.ioutil.chown`
  - :func:`~fabrix.ioutil.copy_file`
  - :func:`~fabrix.ioutil.create_directory`
  - :func:`~fabrix.ioutil.create_file`
  - :func:`~fabrix.ioutil.debug_print`
  - :func:`~fabrix.ioutil.is_directory_exists`
  - :func:`~fabrix.ioutil.is_directory_not_exists`
  - :func:`~fabrix.ioutil.is_file_exists`
  - :func:`~fabrix.ioutil.is_file_not_exists`
  - :func:`~fabrix.ioutil.name`
  - :func:`~fabrix.ioutil.read_file`
  - :func:`~fabrix.ioutil.read_local_file`
  - :func:`~fabrix.ioutil.remove_directory`
  - :func:`~fabrix.ioutil.remove_file`
  - :func:`~fabrix.ioutil.rsync`
  - :func:`~fabrix.ioutil.run`
  - :func:`~fabrix.ioutil.warn`
  - :func:`~fabrix.ioutil.write_file`
  - :func:`~fabrix.ioutil.write_local_file`

----------------------------------------

**User/Group management**
  - :func:`~fabrix.passwd.add_user_ssh_authorized_keys`
  - :func:`~fabrix.passwd.add_user_to_group`
  - :func:`~fabrix.passwd.create_group`
  - :func:`~fabrix.passwd.create_user`
  - :func:`~fabrix.passwd.delete_user_from_group`
  - :func:`~fabrix.passwd.get_user_home_directory`
  - :func:`~fabrix.passwd.is_group_exists`
  - :func:`~fabrix.passwd.is_group_not_exists`
  - :func:`~fabrix.passwd.is_user_exists`
  - :func:`~fabrix.passwd.is_user_in_group`
  - :func:`~fabrix.passwd.is_user_not_exists`
  - :func:`~fabrix.passwd.is_user_not_in_group`
  - :func:`~fabrix.passwd.remove_group`
  - :func:`~fabrix.passwd.remove_user`

----------------------------------------

**Template rendering**
  - :func:`~fabrix.render.render`
  - :func:`~fabrix.render.render_template`

----------------------------------------

**Package management**
  - :func:`~fabrix.rpmyum.yum_install`
  - :func:`~fabrix.rpmyum.yum_remove`
  - :func:`~fabrix.rpmyum.yum_update`

----------------------------------------

**System management**
  - :func:`~fabrix.system.disable_selinux`
  - :func:`~fabrix.system.get_virtualization_type`
  - :func:`~fabrix.system.is_reboot_required`
  - :func:`~fabrix.system.localectl_set_locale`
  - :func:`~fabrix.system.reboot_and_wait`
  - :func:`~fabrix.system.systemctl_disable`
  - :func:`~fabrix.system.systemctl_edit`
  - :func:`~fabrix.system.systemctl_enable`
  - :func:`~fabrix.system.systemctl_get_default`
  - :func:`~fabrix.system.systemctl_mask`
  - :func:`~fabrix.system.systemctl_preset`
  - :func:`~fabrix.system.systemctl_reload`
  - :func:`~fabrix.system.systemctl_restart`
  - :func:`~fabrix.system.systemctl_set_default`
  - :func:`~fabrix.system.systemctl_start`
  - :func:`~fabrix.system.systemctl_stop`
  - :func:`~fabrix.system.systemctl_unmask`
  - :func:`~fabrix.system.timedatectl_set_timezone`

----------------------------------------

.. seealso::
    * :ref:`Overview <overview>`
    * :ref:`installation`
    * :ref:`tutorial`
    * Reference
    * :ref:`changelog`

.. toctree::
    :maxdepth: 2
    :hidden:

    reference/config
    reference/editor
    reference/ioutil
    reference/passwd
    reference/render
    reference/rpmyum
    reference/system

