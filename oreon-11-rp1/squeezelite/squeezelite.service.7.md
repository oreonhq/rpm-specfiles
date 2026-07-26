# NAME

squeezelite.service -  Systemd units for Squeezelite

# DESCRIPTION

Automatically start the Squeezelite music streaming client each time a user logs in, or each time a system boots.

# EXAMPLES

To run `squeezelite` as part of your user desktop session:

    systemctl --user enable squeezelite
    systemctl --user start squeezelite

To configure `squeezelite` as part of your user desktop session, edit the command line options passed to it:

    systemctl --user edit --full squeezelite

To start `squeezelite` at system boot:

    systemctl enable squeezelite
    systemctl start squeezelite

To configure `squeezelite` started at system boot, edit the file `/etc/sysconfig/squeezelite`.

If running outside of a user session, you will probably need to specify the ALSA output device using `squeezelite`’s `-o` option.  Get a list of available devices with:

    squeezelite -l


# SEE ALSO

squeezelite(1), systemctl(1)

---
title: squeezelite.service
section: 7
date: April 2018
author: Peter Oliver <rpm@mavit.org.uk>
...
