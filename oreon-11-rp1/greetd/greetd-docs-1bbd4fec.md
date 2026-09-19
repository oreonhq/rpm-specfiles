[greetd](https://git.sr.ht/~kennylevinsen/greetd) is a login manager daemon. greetd on its own does not have any user interface, but instead offloads that to *greeters*, which are arbitrary applications that implement the greetd IPC protocol.

# FAQ

## What can greetd start?

As a rule of thumb, anything you can start from a TTY can be started by greetd.

All applications are attached to a TTY with the VT in text-mode, so both textual and graphical applications can be used. You can log straight into `htop` if you want.

## What is a session?

A greetd session is the state that tracks authentication flow, and when done, the run of a command-line using the provided credentials.

Sessions can be created dynamically using the IPC protocol by a greeter, or in case of the greeter itself, be pre-configured in the configuration file.

## What is a greeter?

When greetd starts, it will start the pre-configured default session (also known as the *greeter*), which consists of the command-line specified in the configuration file. This greeter can then use the IPC protocol to start user sessions. The default session is restarted every time a user session exits.

Examples of greeter command-lines could be `agreety` (which is the included text-based greeter) and `cage gtkgreet` (which would run gtkgreet within the `cage` Wayland compositor).

The only thing required for a greeter to be able to fullfil its role is the ability to speak the greetd IPC protocol over a UNIX socket.

## Which greeters can I pick from?

The currently known greeters are:

- [agreety](https://git.sr.ht/~kennylevinsen/greetd) (text-based, included with greetd)
- [gtkgreet](https://git.sr.ht/~kennylevinsen/gtkgreet) (graphical, Gtk-based)
- [ReGreet](https://github.com/rharish101/ReGreet) (graphical, Gtk-based)
- [qtgreet](https://gitlab.com/marcusbritanicus/QtGreet) (graphical, Qt-based)
- [wlgreet](https://git.sr.ht/~kennylevinsen/wlgreet) (graphical, raw Wayland client)
- [dlm](https://git.sr.ht/~kennylevinsen/dlm) (graphical, raw fbdev client, semi-deprecated)
- [ddlm](https://github.com/deathowl/ddlm) (graphical, raw fbdev client)
- [tuigreet](https://github.com/apognu/tuigreet) (console UI)

## How do I develop my own greeter?

See the `greetd-ipc(7)` manpage, and look at `agreety` or `gtkgreet` for inspiration.

# Setting up greetd

## Setting up greetd with agreety

1. Install [greetd](https://git.sr.ht/~kennylevinsen/greetd). If you are using Arch Linux, you can do this from [the official \[Extra\]-repo](https://archlinux.org/packages/extra/x86_64/greetd) or the [AUR](https://aur.archlinux.org/packages/greetd-git) for the latest development version. Otherwise, follow the build instructions in the README of the project. This includes creating a user and installing the service file.

2. Open /etc/greetd/config.toml. The greeter should be set to `agreety --cmd /bin/sh`, which logs you into a normal terminal session. Change this to `agreety --cmd sway` if you want it to start `sway`.

## Setting up greetd with gtkgreet

1. Follow the steps from "Setting up greetd with agreety".

2. Install [gtkgreet](https://git.sr.ht/~kennylevinsen/gtkgreet). If you are using Arch Linux, you can do this from [the official \[Extra\]-repo](https://archlinux.org/packages/extra/x86_64/greetd-gtkgreet) or the [AUR](https://aur.archlinux.org/packages/greetd-gtkgreet-git) for the latest development version. Otherwise, follow the build instructions in the README of the project. It is recommended to build gtkgreet with wlr-layer-shell-unstable support.

3. Install a Wayland compositor, such as `sway` or `cage`. For the full experience, a compositor with wlr-layer-shell-unstable support is required.

4. Edit /etc/greetd/config.toml to set the new greeter as the default session. If using cage:

```toml
[terminal]
vt = 1

[default_session]
command = "cage -s -- gtkgreet"
user = "greeter"
```

The `-s` argument enables VT switching in cage (0.1.2 and newer only), which is highly recommended to prevent locking yourself out.

5. Edit gtkgreet list of login environments, which is by default read from `/etc/greetd/environments`. Example:

```
sway
bash
```

### Using sway for gtkgreet

At the time of writing, cage does not have wlr-layer-shell-unstable support, which is required for good multi-monitor support. Sway can be used in its stead.

To use sway, we must create a dedicated sway config that runs the greeter, and terminates when it dies. Save this configuration in /etc/greetd/sway-config (any location can be used, but the next step assumes this location):

```
# `-l` activates layer-shell mode. Notice that `swaymsg exit` will run after gtkgreet.
exec "gtkgreet -l; swaymsg exit"

bindsym Mod4+shift+e exec swaynag \
	-t warning \
	-m 'What do you want to do?' \
	-b 'Poweroff' 'systemctl poweroff' \
	-b 'Reboot' 'systemctl reboot'

include /etc/sway/config.d/*
```

Then, set the greeter in `/etc/greetd/config.toml` to start sway:

```toml
[terminal]
vt = 1

[default_session]
command = "sway --config /etc/greetd/sway-config"
user = "greeter"
```

Restart greetd and you're good!

## Setting up greetd with wlgreet

[wlgreet](https://git.sr.ht/~kennylevinsen/wlgreet) only supports wlr-layer-shell-unstable, so it must currently be used with something like `sway`. Follow "Using sway for gtkgreet", with the following changes:

1. Install [wlgreet](https://git.sr.ht/~kennylevinsen/wlgreet) instead of gtkgreet. If you are using Arch Linux, you can do this from [AUR](https://aur.archlinux.org/packages/greetd-wlgreet-git). Otherwise, follow the build instructions in the README of the project.

2. Use the following sway config:

```
exec "wlgreet --command sway; swaymsg exit"

bindsym Mod4+shift+e exec swaynag \
	-t warning \
	-m 'What do you want to do?' \
	-b 'Poweroff' 'systemctl poweroff' \
	-b 'Reboot' 'systemctl reboot'

include /etc/sway/config.d/*
```

## Setting up auto-login

Auto-login can be achieved by configuring an initial session, which takes the place of the default session on the very first start. The default session will be started once the initial session exits.

```toml
[terminal]
vt = 1

[default_session]
command = "cage gtkgreet"
user = "greeter"

[initial_session]
command = "sway"
user = "john"
```

## How to set XDG_SESSION_TYPE=wayland/...?

While you *could* set this in your `.profile`, the recommended way to handle this is with a wrapper script. Doing it this way allows you to start multiple login environments without having weird env vars mess with things.

* /usr/local/bin/sway-run (should be made executable)

```sh
#!/bin/sh

# Session
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=sway
export XDG_CURRENT_DESKTOP=sway

# Wayland stuff
export MOZ_ENABLE_WAYLAND=1
export QT_QPA_PLATFORM=wayland
export SDL_VIDEODRIVER=wayland
export _JAVA_AWT_WM_NONREPARENTING=1

exec sway "$@"

#
# If you use systemd and want sway output to go to the journal, use this
# instead of the `exec sway "$@"` above:
#
#    exec systemd-cat --identifier=sway sway "$@"
#
```

Simply use `sway-run` instead of `sway` to log in.

## Changing target VT

The VT used by greetd is set in the terminal section:

```toml
[terminal]
vt = 1
```

This can be set to the number of any VT. Note that in order to run on a VT, you must first ensure that nothing else uses the VT. For systemd, this is done by setting the "Conflicts=" directive in the systemd unit to block getty from running. If your system uses `/etc/inittab`, remove the command for the intended VT.

# Customization

## Styling gtkgreet

gtkgreet can use Gtk stylesheets to modify its appearance. To apply a stylesheet, place it in a location that gtkgreet will be able to read (e.g. `/etc/greetd/gtkgreet.css`), and add the style parameter (e.g. `gtkgreet -l -s /etc/greetd/gtkgreet.css`).

Note that this is not intended nor able to load full Gtk themes, for reasons outside the scope of this document. It is only intended to make application-specific changes. If your intend is to pick a Gtk theme, use the normal Gtk theme selection mechanisms, such as gsettings.

Style example:

```css
window {
   background-image: url("file:///usr/share/backgrounds/default.png");
   background-size: cover;
   background-position: center;
}

box#body {
   background-color: rgba(50, 50, 50, 0.5);
   border-radius: 10px;
   padding: 50px;
}
```

# Troubleshooting

## I installed and enabled greetd, but everything looks the same!

The default greetd configuration uses `agreety` (which looks just like `agetty` + `login`) to start `/bin/sh`. You shouldn't notice any big difference unless you check the process tree with something like `htop`, and see that you are in fact a child process of `greetd`.

You can change the configuration as mentioned in the steps above to make `agreety` start another login environment of your choice (e.g. `sway`), or use a different greeter altogether.

## greetd fails with `unable to exec: Sys(EACCES)`

This is due to SELinux policies. You will need to run the following commands to
unblock `greetd`:

```sh
semanage fcontext -a -ff -t xdm_exec_t /usr/bin/greetd
restorecon /usr/bin/greetd
```

## greetd fails with `unable to lock pages: Sys(ENOMEM)`

greetd *must* be started as root, as it must perform a few privileged actions. This error is usually the result of attempting to run greetd as another user, which will fail immediately as `mlockall(3)` is attempted at startup (done to block greetd miniscule memory allocations from being swapped to disk). Later PAM operations also expect to be run by root/CAP_SYS_ADMIN as well.

The references to a greeter user in the documentation and configuration file is the user greetd uses to start your greeter/default session, *not* a user meant for starting greetd.

## My greeter cannot start

1. Make sure that your greeter user can read any files it needs. If using gtkgreet with sway, this means that `/etc/greetd/sway-config` should be readable by `greeter`:

```sh
sudo chmod -R go+r /etc/greetd
```

2. Test your greeter command from a TTY. The best test would be to log in as the greeter user on a console (requires temporarily setting a password for the greeter—remember to disable this afterwards!), followed by running the greeter command-line manually.

## I used cage as my greeter, messed up my config, and now I can't log in or switch to another VT!

cage specifically disallows VT switching, unless started with `-s`, which can be slightly frustrating if you have messed up your config.

If this, together with a broken greeter configuration, has rendered you unable to log in, you can temporarily disable greetd by adding the following to your kernel command-line in your bootloader:

```
systemd.mask=greetd.service
```

This will stop the greetd service from starting, in which case you will just be met by agetty/login, and can just fix your config from there.
