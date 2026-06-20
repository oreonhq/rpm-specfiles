# Updating Packages in Oreon 11 - Release Pack 1 (maintainers guide)

This file is for people who already know how to edit a spec and refresh sources. The goal here is to guide maintainers through what order to build things in when using Oreon Build Service so you do not burn an afternoon on missing `-devel` packages or dependency hell as some call it.

Nothing here replaces reading the spec `BuildRequires` lines. Treat these chains as a default ordering that matches how this tree is usually stacked. If packages change dependencies, update this doc when you update the specs.

---

## Chain build syntax (Oreon Build Service)

The UI explains it with two patterns.

### Sequential only

Spaces between names. Each package waits for the previous one to finish. This is the safest default when you are touching a desktop stack or anything with messy deps. Example:

```text
bash grep coreutils
```

### Parallel group, then next step

Space inside a group means those builds run together. A colon means wait for the whole group to finish before the next token or group. Example:

```text
libwidget libaselib : libgizmo
```

Here `libwidget` and `libaselib` build at the same time, then `libgizmo` runs after both finish.

### What we recommend here

Use sequential chains below unless you know two neighbors are truly independent. Parallel saves waiting time but will piss you off the second anything expects dependency ordering that chain did not order correctly, so be careful when initiating chain builds.

Package names in the strings are directory names under this `oreon-11-rp1` folder, same as what you put in the build service when it asks for the package name.

---

## General workflow (short)

1. Bump versions in the specs and refresh `Source` URLs or vendor scripts the way you always do.
2. Commit so Oreon Build Service can see the change.
3. Pick the stack section below that matches your work.
4. Paste the chain string into the chain build field while logged into Oreon Build Service. https://build.oreonhq.com/
5. If something fails, check build logs, then fix the spec/package sources or fix this doc. Do not just rebuild again and hope for it to work. (UNLESS ITS A WORKER RESOURCE FAILURE)

When KDE or Qt does a coordinated release, bump the whole stack in git first, then run the Qt chain, then the KF6 chain, then the Plasma chain. Skipping steps is how you get mismatched `cmake(KF6*)` errors.

---

## Kernel and boot-adjacent stack

### When to use

You touched `kernel`, firmware blobs, or userspace tools that hard-track the kernel version.

### Notes

- `linux-firmware` often ships on its own schedule but if you are coordinating a bump with the kernel, build firmware first so the kernel metapackage logic and QA expectations line up.
- `bpftool` is compiled against the kernel tree in many workflows. If your bump includes bpftool sources tied to that kernel tag, keep it right after `kernel`.
- `dracut` consumes what the running build root knows about the kernel package set. Rebuild it after the kernel when initrd-related stuff changed.
- `kmod` is mostly standalone userspace. It is last here so you do not accidentally assume it drags the kernel forward.

### Chain (sequential)

```text
kernel-srpm-macros linux-firmware kernel bpftool dracut kmod
```

### Optional extras

Only if you actually changed them in the same maintenance window:

```text
systemtap kernelshark
```

`systemtap` and `kernelshark` pull extra deps. Do not add them to the main chain unless you need them.

---

## Graphics userspace (Mesa path)

### When to use

You are rebasing Mesa or the low-level GL/Vulkan stack and want the smallest sane ordering before KDE or games stacks scream.

### Chain

```text
libdrm libglvnd mesa
```

If your change also touched LLVM used by Mesa, see the LLVM or toolchain section and run that before this block.

---

## TeX Live stack

### When to use

libtommath doc builds, dblatex, latexmk, or anything else in this tree that BuildRequires texlive-* or tex(*). Run this before the Qt chain if firebird/libtommath is blocking qt6-qtbase-ibase.

### Chain

```text
libseccomp teckit ghostscript : texlive-base : texlive-collection-basic : texlive-collection-latex : libtiff : libtommath libtomcrypt : firebird
```

---

## Qt 6 stack (all Qt6 SRPMs in this tree)

### When to use

Any bump to `qt6-qtbase` or a coordinated Qt release. KF6 and Plasma must not be rebuilt until this finishes. If libtommath or firebird are not in the repo yet, run the TeX Live stack section first.

### Chain

```text
cmake qt6 : libseccomp teckit ghostscript : texlive-base : texlive-collection-basic : texlive-collection-latex : libtiff : libtommath libtomcrypt : firebird : qt6-qtbase : qt6-qtshadertools qt6-qtlanguageserver qt6-qtsvg qt6-qtimageformats qt6-qtserialport qt6-qtnetworkauth : qt6-qtdeclarative : qt6-qttools qt6-qt5compat qt6-qtwebsockets qt6-qtconnectivity qt6-qtcharts qt6-qtdatavis3d qt6-qtremoteobjects qt6-qtscxml qt6-qtlottie qt6-qtquicktimeline : qt6-qtpositioning qt6-qtserialbus qt6-qtvirtualkeyboard qt6-qtwayland qt6-qthttpserver qt6-qtwebchannel qt6-qtsensors : qt6-qtlocation qt6-qtquick3d qt6-qt3d : qt6-qtmultimedia qt6-qtgraphs : qt6-qtspeech qt6-qttranslations : qt6-qtwebengine : qt6-qtwebview qt6-doc
```

---

## KDE Frameworks 6 stack (KF6)

### When to use

Frameworks point release or any rebuild after Qt changed ABI.

### Chain

```text
extra-cmake-modules kf6 : kf6-breeze-icons kf6-kapidox kf6-attica kf6-karchive kf6-kcodecs kf6-kconfig kf6-kcoreaddons kf6-kdbusaddons kf6-kdnssd kf6-kguiaddons kf6-ki18n kf6-kidletime kf6-kitemmodels kf6-kitemviews kf6-kplotting kf6-kwidgetsaddons kf6-kwindowsystem kf6-solid kf6-sonnet kf6-syntax-highlighting kf6-threadweaver kf6-kirigami kf6-bluez-qt kf6-modemmanager-qt kf6-networkmanager-qt kf6-prison kf6-kholidays kf6-kpty kf6-ktexttemplate kf6-kunitconversion kf6-kuserfeedback kf6-kcalendarcore kf6-kquickcharts kf6-kstatusnotifieritem : kf6-kauth kf6-kcompletion kf6-kcrash kf6-kdoctools kf6-kfilemetadata kf6-kimageformats kf6-kjobwidgets kf6-knotifications kf6-kcolorscheme kf6-kconfigwidgets kf6-kglobalaccel kf6-kcontacts : kf6-kpackage kf6-kservice kf6-kiconthemes kf6-kwallet kf6-kded kf6-syndication kf6-kdesu : kf6-kio kf6-ktextwidgets kf6-kxmlgui : kf6-kbookmarks kf6-knotifyconfig kf6-knewstuff kf6-kparts kf6-krunner kf6-kdav : kf6-kcmutils kf6-kdeclarative kf6-ksvg kf6-qqc2-desktop-style kf6-purpose : kf6-ktexteditor kf6-frameworkintegration kf6-kirigami-addons kf6-kpeople kf6-baloo kf6-kglobalacceld
```

---

## Plasma desktop stack (workspace and friends)

### When to use

Coordinated Plasma bump, or rebuild after KF6 or Qt changes.

### Chain

```text
polkit-qt-1 plasma-wayland-protocols plasma-activities kdecoration libdisplay-info knighttime libksysguard kinfocenter plasma-drkonqi plasma-disks plasma-firewall plasma-thunderbolt plasma-workspace-wallpapers packagekit-qt phonon plasma-keyboard plasma-settings : layer-shell-qt kwayland libkscreen plasma-activities-stats plasma-breeze qqc2-breeze-style kpipewire plasma-integration : libplasma : kscreenlocker plasma-aurorae plasma5support ksystemstats bluedevil plasma-milou plasma-nm plasma-pa plasma-vault plasma-welcome plasma-oxygen plasma-bigscreen plasma-login-manager plasma-dialer plasma-systemmonitor plasma-sdk xdg-desktop-portal-kde : kwin kwin-x11 : plasma-workspace plasma-workspace-x11 : plasma-desktop plasma-systemsettings powerdevil plasma-browser-integration kde-cli-tools kdeplasma-addons : phonon-backend-gstreamer phonon-backend-vlc plasma-discover plasma-print-manager : plasma-nano kde-gtk-config kwayland-integration ocean-sound-theme oxygen-sounds : plasma-applet-translator plasma-pk-updates plasma-pass plasma-wallpapers-dynamic plasma-camera plasma-phonebook : plasma-setup plasma-mobile-sounds : plasma-mobile
```

---

## PipeWire and Plasma multimedia stuff

### When to use

You bumped PipeWire or WirePlumber and need KDE bits that wrap PipeWire for the session.

### Notes

`kpipewire` belongs to Plasma but depends on PipeWire client libraries. If you are only touching `kpipewire`, you can build it alone after a successful PipeWire build. If you are rebasing PipeWire itself, use this chain.

### Chain

```text
pipewire wireplumber kpipewire
```

---

## LLVM and Clang (subset)

### When to use

You are about to rebuild Mesa, Rust, or anything that needs a matching Clang built from the same LLVM drop.

### Notes

This is a conservative ordering. Your exact Requires may vary if Red Hat carried patches that split subpackages differently.

### Chain

```text
llvm compiler-rt clang
```

---

## GCC and binutils (subset)

### When to use

Toolchain refresh before kernel or before mass rebuilds.

### Chain

```text
binutils gcc
```

---

## Rust

### When to use

Rust bumped and Firefox or other Rust-heavy packages need the new compiler.

### Notes

Rust often wants an LLVM stack that matches what the package was tested against. If you bumped LLVM, run the LLVM chain before `rust`.

### Chain

```text
rust
```

---

## Grub and generic boot branding (optional)

### When to use

Kernel command line defaults, theme files, or template churn that touches how installers build media.

### Chain

```text
grub2 lorax-templates-rhel
```

Add `shim` or other firmware packages only if your update actually needs them.

---

## Crypto and TLS-shaped deps (small leaf stack)

### When to use

Firefox, curl, or half the desktop rebuilt and you know the failure is NSS or OpenSSL sonames.

### Notes

There is no separate `nspr` package dir here. The `nss` SRPM builds the nspr subpackages. Queue `nss` only, then NSS consumers.

### Chain

```text
nss openssl
```

---

## OpenSSH, NSS, and libssh (after security fixes or upgrade)

### When to use

OpenSSH upgrade, nss spec changes, etc... mainly where `%check` or `BuildRequires` need a newer ssh stack.

### Notes

- openssh builds against openssl. If you bumped crypto and openssh together, put openssl (and nss if that spec moved) before openssh.
- libssh BRs `openssh-clients` and `openssh-server` for ctests that run sshd. Build openssh before libssh. Missing sshd in `%check` is usually wrong chain order.
- If NSS ABI or tooling changed, add failing consumers after you read logs and `grep BuildRequires`, not a random full-tree rebuild.

### Chain (full security core, sequential)

When more than one of those layers changed in the same commit or tag:

```text
nss openssl openssh libssh
```

Strip packages you did not touch.

OpenSSH only (rest of tag already good):

```text
openssh libssh
```

NSS only (no openssh spec change):

```text
nss
```

---

## NetworkManager

### When to use

You bumped NetworkManager itself or its VPN plugins and want a boring default ordering before plasma-nm screams.

### Notes

This tree usually builds NetworkManager with NSS in the mix. If you just rebased NSS, run the crypto stack above first.

### Chain

```text
nss NetworkManager
```

If your failure mentions `libnm` from an older split package, open the NetworkManager spec and add whatever subpackage name the build service uses for that SRPM. Here `NetworkManager` is the directory name under `oreon-11-rp1`.

---

## systemd

### When to use

systemd point release or security rebuild that touches libsystemd consumers across the distro.

### Notes

systemd is wide. Expect follow-up rebuilds for anything that links `libsystemd` if ABI shifted. This chain is only "build systemd".

### Chain

```text
systemd
```

---

## Apps that sit on top (examples)

These are not full dependency closures. They are reminders so you do not rebuild Firefox alone and wonder why link failed.

### Firefox

Build after crypto and NSS style deps are stable. Minimal intentional ordering when everything else is already current:

```text
firefox
```

If you hit NSS or SQLite related link errors, rebuild those leaf deps first (grep Firefox spec `BuildRequires` for the exact package names in this tree).

### Flatpak

```text
flatpak
```

Flatpak pulls a bubblewrap and OSTree shaped graph. If CMake screams about missing OSTree, rebuild from the spec order bottom-up starting at what failed.

---

## Quick reference, colon syntax

Sequential (recommended default):

```text
pkg-a pkg-b pkg-c
```

Parallel batch then next:

```text
pkg-a pkg-b : pkg-c
```

---

## Perl minor bump (bootstrap)

When dual-life `perl-*` in the repo already want the new `MODULE_COMPAT` but `perl` itself is still the old release, a normal `perl` builddeps install loops on PathTools etc.

`perl.spec` uses `%bcond_without perl_bootstrap 1` during the transition so builds bootstrap properly.

IMPORTANT -- after bootstrapped `perl` is in the repo:

1. Flip back to `%bcond_with perl_bootstrap` in `perl.spec`
2. Rebuild `perl` normally
3. Rebuild dual-life modules that jumped ahead (e.g. `perl-PathTools`, `perl-version`, etc.)
4. Then `perl-generators`, `oreon-rpm-config`, and rest of stack

Update `gendep.macros` for the new `MODULE_COMPAT` before the bootstrap build. Regenerate from build log with `./generatedependencies` after a normal rebuild for the next bump.

---

## oreon-base bootstrap (Fedora mock on build service)

### When to use

or11 mock `dnf builddep` fails because a BuildRequires exists in Fedora but is not published to oreon-base yet. common case: ghostscript needs gtk3-devel, gdk-pixbuf2-devel pulls glycin-devel, glycin-devel needs libseccomp-devel.

do not strip spec BuildRequires or disable subpackages to dodge this.

### How

on Oreon Build Service pick a **Fedora mock env** for the bootstrap package (e.g. `fedora-44-x86_64` / `fedora-44-aarch64` instead of `oreon-11-rp1-*`). fedora mock resolves builddeps from Fedora repos (valgrind for libseccomp, etc.) while the spec still builds oreon-tagged RPMs.

1. queue `libseccomp` on **fedora-44** mock for each arch you need
2. once those RPMs land in oreon-base, switch back to **oreon-11-rp1** mock for dependents
3. run `ghostscript` or the full TeX chain

### After bootstrap

rebuild the same package on or11 mock later only if you need it compiled strictly against oreon-base devel headers. for libseccomp that is usually optional once devel is in the repo.

### Other bootstrap candidates

same trick for any package where the builddep error says `nothing provides` and Fedora already ships that provider. grep the error, build the missing leaf on fedora mock, publish to oreon-base, then continue on or11 mock.

---

## Maintaining this document

When you add a new Plasma or KF6 package directory, insert it into the right chain in this file in the same MR as the spec. When you delete or rename a package, delete or rename it here.

If you are not sure where something goes, `grep BuildRequires` on the consumer spec and walk backwards until you hit something already in the chain. That is how the next person should fix gaps too.
