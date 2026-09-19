# Updating Packages in Oreon 11 - Release Pack 1 (maintainers guide)

This file is for people who already know how to edit a spec and refresh sources. This is what top-level packages to queue in Oreon Build Service so layer planning looks through BuildRequires/Requires and builds the rest.

https://build.oreonhq.com/

---

## Layer planning (chains are now deprecated)

Chain builds have been deprecated. Oreon Build Service now uses a new layering system.

You only submit top-level packages. It resolves build/runtime deps for what you queued, groups packages into layers that can build once deps exist, then builds layer by layer until it finishes.

Package names are directory names under this oreon-11-rp1 folder.

Workflow

1. Bump versions in the specs and refresh Source URLs or vendor scripts the way you always do. ALso don't forget to update the checksums.
2. Commit and push, then open a PR, then Oreon Build Service can see the change. If you want to skip the PR for now, just make sure to specify your branch name before submitting the builds.
3. Pick the stack section below and queue those (plus any bootstrap deps noted).
4. Let layer planning run. If anything fails, wait until the whole layer halts, then fix individual specs and resume the layer.
5. If something you bumped never shows up in the plan, BR is wrong/renamed or it is a top-level package you have to queue yourself. Fix the spec or add the package name.

Note: if you find any errors or missing top-level package names here, PLEASE let one of us know, or fix it in your PR.

When KDE or Qt does a coordinated release, bump the whole stack in git first, then queue top-levels in waves if newer Qt is not published yet

1. Qt tops (after TeX/firebird deps if needed)
2. KF6 tops
3. Plasma tops
4. Gear tops

make sure to do it right

---

## Kernel and boot-adjacent stack

### When to use

You touched kernel, firmware, or other packages that depend on the kernel version.

### Tops to queue

```text
kernel
```

### Extras if needed

```text
linux-firmware
bpftool
dracut
kmod
kernel-srpm-macros
```

linux-firmware often updates on its own schedule.

Optional only if you actually changed them

```text
systemtap
kernelshark
```

---

## Graphics userspace (Mesa path)

### When to use

You are rebasing Mesa or the low-level GL/Vulkan stack.

### Tops to queue

```text
mesa
```

If LLVM used by Mesa also moved, queue the LLVM tops first (see LLVM section), then mesa.

---

## TeX Live/firebird bootstrap deps

### When to use

libtommath docs, dblatex, latexmk, or anything that BuildRequires texlive-*/tex(*). Also when qt6-qtbase-ibase/firebird is blocked on those deps.

### Tops to queue

These are deps the planner may not pull in for a Qt tip. Queue them when the failure is missing TeX or firebird bits.

```text
texlive-collection-latex
firebird
```

If that still cannot resolve, also queue

```text
libseccomp
teckit
ghostscript
texlive-base
texlive-collection-basic
libtiff
libtommath
libtomcrypt
```

---

## Qt 6 stack

### When to use

Any bump to qt6-qtbase or a coordinated Qt release. Do not rebuild KF6 or Plasma until the new Qt is published.

### Tops to queue

```text
qt6-qtwebengine
qt6-qtwebview
qt6-doc
```

Those pull most of the Qt module graph. If planning stops short of something you know you bumped, add that module as another root.

### Bootstrap deps (only if missing from oreon-base)

```text
cmake
firebird
texlive-collection-latex
```

---

## KDE Frameworks 6 (KF6)

### When to use

Frameworks point release or any rebuild after Qt ABI changed.

### Notes

extra-cmake-modules BuildRequires pkgconfig(Qt5Core) for tests, so qt5-qtbase has to be buildable first. qt5-qtbase BuildRequires freetds-devel. Those are one-time deps, not something to rebuild on every KF6 bump once published.

### Tops to queue

```text
kf6-baloo
kf6-ktexteditor
kf6-frameworkintegration
kf6-kirigami-addons
kf6-kpeople
kf6-purpose
kf6-kdav
```

extra-cmake-modules and the rest of kf6-* should layer under those.

### One-time deps if missing

```text
freetds
qt5-qtbase
extra-cmake-modules
```

kf6-kglobalacceld is Plasma-versioned. Rebuild it with Plasma packages top-level.

---

## Plasma desktop stack

### When to use

Plasma update or rebuild after KF6 or Qt changed.

### Tops to queue

```text
plasma-desktop
plasma-workspace
plasma-workspace-x11
kwin
kwin-x11
plasma-systemsettings
powerdevil
plasma-discover
plasma-mobile
plasma-setup
spectacle
```

### Optional backend deps (queue only if needed)

```text
liboath
gocryptfs
p8-platform
libcec
snapd
snapd-glib
translate-shell
xsel
libcallaudio
mariadb-server
pipewire
wireplumber
```

---

## KDE Gear apps

### When to use

Gear bump after KF6 (and Plasma if workspace-facing apps changed).

### Tops to queue

```text
dolphin
kate
okular
konsole
gwenview
kde-connect
kmail
korganizer
kontact
merkuro
neochat
tokodon
ark
yakuake
```

PIM libs and other Gear packages should layer under those. If a bumped app is not pulled in, add that app dir as another root.

---

## LLVM and Clang

### When to use

About to rebuild Mesa, Rust, or anything that needs a matching Clang from the same LLVM drop.

### Tops to queue

```text
clang
```

That should pull llvm/compiler-rt style deps as layers. Add llvm explicitly if planning does not.

---

## GCC and binutils

### When to use

Toolchain refresh before kernel or before mass rebuilds.

### Tops to queue

```text
gcc
```

Add binutils as a root if you bumped it and it is not already under gcc in the plan.

---

## Rust

### When to use

Rust bumped and Firefox or other Rust-heavy packages need the new compiler.

### Tops to queue

```text
rust
```

If you bumped LLVM for that Rust, queue Clang/LLVM tops first so the new toolchain is published.

---

## Grub and boot branding (optional)

### When to use

Kernel command line defaults, theme files, or installer media templates.

### Tops to queue

```text
grub2
lorax-templates-rhel
```

Add shim only if your update needs it.

---

## Crypto/TLS deps

### When to use

Firefox, curl, or desktop rebuilds failing on NSS or OpenSSL sonames.

### Notes

There is no separate nspr package dir. The nss SRPM builds the nspr subpackages.

### Tops to queue

```text
nss
openssl
```

Then queue the failing consumer (firefox, NetworkManager, etc) if it is not already planned.

---

## OpenSSH, NSS, and libssh

### When to use

OpenSSH upgrade, nss spec changes, or %check/BR needing a newer ssh stack.

### Tops to queue

Full security core moved together

```text
libssh
openssh
nss
openssl
```

OpenSSH only

```text
libssh
openssh
```

NSS only

```text
nss
```

---

## NetworkManager

### When to use

You bumped NetworkManager itself or need it before plasma-nm.

### Tops to queue

```text
NetworkManager
```

If NSS just moved, queue nss too.

Directory name under oreon-11-rp1 is NetworkManager.

---

## NetworkManager VPN plugins

### When to use

You need the VPN plugin family that plasma-nm optionally pulls, or you are bringing one of these into the tree for the first time.

### Tops to queue

```text
NetworkManager-openconnect
NetworkManager-vpnc
NetworkManager-sstp
NetworkManager-iodine
NetworkManager-l2tp
NetworkManager-pptp
NetworkManager-fortisslvpn
NetworkManager-ssh
```

Protocol packages if missing from the plan

```text
openconnect
vpnc
sstp-client
iodine
strongswan
xl2tpd
```

---

## systemd

### When to use

systemd point release or security rebuild that touches libsystemd consumers.

### Tops to queue

```text
systemd
```

Expect follow-up consumer rebuilds if ABI shifted. Queue those when logs say so.

---

## App tips (examples)

Not full closures. Just the tip you queue when the lower stack is already current.

### Firefox

```text
firefox
```

If link fails on NSS or SQLite, queue those deps (grep Firefox BuildRequires) then queue firefox again.

### Flatpak

```text
flatpak
```

If CMake wants OSTree/bubblewrap bits that are not planned, queue those package dirs as roots.

---

## Perl minor bump (bootstrap)

When dual-life perl-* in the repo already want the new MODULE_COMPAT but perl itself is still old, a normal perl builddeps install loops on PathTools etc.

perl.spec uses %bcond_without perl_bootstrap 1 during the transition.

IMPORTANT after bootstrapped perl is in the repo

1. Flip back to %bcond_with perl_bootstrap in perl.spec
2. Rebuild perl (queue perl)
3. Rebuild dual-life modules that jumped ahead (queue those perl-* dirs)
4. Then queue perl-generators and oreon-rpm-config if they need it

Update gendep.macros for the new MODULE_COMPAT before the bootstrap build. Regenerate from the build log with ./generatedependencies after a normal rebuild for the next bump.

---

## Maintaining this document

Please propose any changes if you think they are needed.
