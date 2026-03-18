%global udevdir %(pkg-config --variable=udevdir udev)

Name:           linuxconsoletools
Version:        1.8.1
Release:        11%{?dist}
Summary:        Tools for connecting joysticks & legacy devices to the kernel's input subsystem
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/linuxconsole/
Source:         http://downloads.sourceforge.net/linuxconsole/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  systemd-udev
BuildRequires: make

Provides:       joystick = %{version}-%{release}
Provides:       ff-utils = 1:%{version}-%{release}
Obsoletes:      joystick < 1.2.16-1
Obsoletes:      ff-utils < 2.4.22-1
Conflicts:      gpm < 1.20.6-26


%description
This package contains utilities for testing and configuring joysticks,
connecting legacy devices to the kernel's input subsystem (providing support
for serial mice, touchscreens etc.), and test the input event layer.


%prep
%autosetup


%build
%{set_build_flags}
%{make_build} PREFIX=%{_prefix}

# moving helper scripts from /usr/share/joystick to /usr/libexec/joystick
sed -i "s|%{_datadir}/joystick|%{_libexecdir}/joystick|g" utils/jscal-restore utils/jscal-store


%install
%{make_install} PREFIX=%{_prefix}

# moving helper scripts from /usr/share/joystick to /usr/libexec/joystick
install -d -m 0755 %{buildroot}%{_libexecdir}/joystick
mv -f %{buildroot}%{_datadir}/joystick/* %{buildroot}%{_libexecdir}/joystick/

# fixing udev dir
mv -f %{buildroot}/lib %{buildroot}/usr/

# fixing man permissions
chmod -x %{buildroot}%{_mandir}/man1/*


%files
%doc README NEWS
%license COPYING
%{_bindir}/ffcfstress
%{_bindir}/ffmvforce
%{_bindir}/ffset
%{_bindir}/fftest
%{_bindir}/inputattach
%{_bindir}/jscal
%{_bindir}/jscal-restore
%{_bindir}/jscal-store
%{_bindir}/jstest
%{_bindir}/evdev-joystick

%{_libexecdir}/joystick

%{udevdir}/js-set-enum-leds
%{_udevrulesdir}/80-stelladaptor-joystick.rules

%{_mandir}/man1/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-11
- Prepare for Oreon 11 (RP1)
