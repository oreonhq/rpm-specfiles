%global source0_hash 0d6fa529d15e15fb7eebfaa54558da05b4534ab46874040c8dfee844a253167e

Name:            libnxt
%global forgeurl https://github.com/schodet/%{name}
%global tag      0.4.2
Version:         %{tag}

%forgemeta

Release:         10%{?dist}
Summary:         Utility for flashing LEGO Mindstorms NXT firmware
License:         GPL-2.0-or-later
Url:             %{forgeurl}
Source0:         %{forgesource}
# Short document describing how to reflash the NXT firmware
Source1:         file://%{name}-NXT-REFLASH-HOWTO

BuildRequires:   gcc
BuildRequires:   /usr/bin/git
BuildRequires:   python3
BuildRequires:   libusb1-devel
BuildRequires:   meson
BuildRequires:   scdoc
BuildRequires:   arm-none-eabi-gcc-cs

%if 0%{?fedora} > 39
# As per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# This is needed because arm-none-eabi-gcc-cs does the same thing.
ExcludeArch:    %{ix86}
%endif

%description
LibNXT is an utility library for talking to the LEGO Mindstorms NXT.
 It currently does:
 * Handling USB communication and locating the NXT in the USB tree.
 * Interaction with the Atmel AT91SAM boot assistant.
 * Flashing of a firmware image to the NXT.
 * Execution of code directly in RAM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -S git
cp -p %{SOURCE1} NXT-REFLASH-HOWTO

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README NXT-REFLASH-HOWTO
%{_bindir}/fwexec
%{_bindir}/fwflash
%{_mandir}/man1/fwexec.1*
%{_mandir}/man1/fwflash.1*

%changelog
%autochangelog
