%global source0_hash 4da29745c782b7db18f5f37c49e77bf163121dd3761e2fc7636fa0cbf35c2456
%global udevdir %(pkg-config --variable=udevdir udev)
Name:           linuxconsoletools
Version:        1.8.1
Release:        1%{?dist}
Summary:        Tools for connecting joysticks & legacy devices to the kernel's input subsystem
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/linuxconsole/
Source0:        https://downloads.sourceforge.net/linuxconsole/%{name}-%{version}.tar.bz2
Provides:       joystick = %{version}-%{release}
Provides:       ff-utils = 1:%{version}-%{release}
Obsoletes:      joystick < 1.2.16-1
Obsoletes:      ff-utils < 2.4.22-1
Conflicts:      gpm < 1.20.6-26
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  systemd-udev
# /oreon:deps
%description
This package contains utilities for testing and configuring joysticks,
connecting legacy devices to the kernel's input subsystem (providing support
for serial mice, touchscreens etc.), and test the input event layer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{set_build_flags}
%{make_build} PREFIX=%{_prefix}
sed -i "s|%{_datadir}/joystick|%{_libexecdir}/joystick|g" utils/jscal-restore utils/jscal-store
%install
%{make_install} PREFIX=%{_prefix}
install -d -m 0755 %{buildroot}%{_libexecdir}/joystick
mv -f %{buildroot}%{_datadir}/joystick/* %{buildroot}%{_libexecdir}/joystick/
mv -f %{buildroot}/lib %{buildroot}/usr/
chmod -x %{buildroot}%{_mandir}/man1/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-11
- Prepare for Oreon 11 (RP1)
