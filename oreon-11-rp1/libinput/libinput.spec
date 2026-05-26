%global udevdir %(pkg-config --variable=udevdir udev)

#global gitdate 20141211
%global gitversion 58abea394

Name:           libinput
Version:        1.31.0
Release:        2%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
Summary:        Input device library

# SPDX
License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libinput/
%if 0%{?gitdate}
Source0:        https://gitlab.freedesktop.org/libinput/libinput/-/archive/1.31.0/libinput-1.31.0.tar.bz2
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        https://gitlab.freedesktop.org/libinput/libinput/-/archive/%{version}/libinput-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 af04645cef8ec4ef9b571664828086ea5a610c6f3e872880055c7fe2c9377de5
%global source0_file libinput-1.31.0.tar.bz2
# oreon url source checksums end
%endif

BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev) >= 1.1.0
BuildRequires:  pkgconfig(libevdev) >= 0.4
BuildRequires:  pkgconfig(libwacom) >= 0.20
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3-rpm-macros

BuildRequires:  lua-devel

%description
libinput is a library that handles input devices for display servers and other
applications that need to directly deal with input devices.

It provides device detection, device handling, input device event processing
and abstraction so minimize the amount of custom input code the user of
libinput need to provide the common set of functionality that users expect.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities and tools for debugging %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-pyudev python3-libevdev

%description    utils
The %{name}-utils package contains tools to debug hardware and analyze
%{name}.

%package        test
Summary:        libinput integration test suite
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
The %{name}-test package contains the libinput test suite. It is not
intended to be run by users.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libinput-1.31.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "af04645cef8ec4ef9b571664828086ea5a610c6f3e872880055c7fe2c9377de5" || { echo "oreon: Source0 SHA256 mismatch for libinput-1.31.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git -p1
# Replace whatever the source uses with the approved call
%py3_shebang_fix $(git grep -l  '#!/usr/bin/.*python3')

%build
%meson -Ddebug-gui=false \
       -Ddocumentation=false \
       -Dtests=true \
       -Dinstall-tests=true \
       -Dautoload-plugins=true \
       -Dudev-dir=%{udevdir}
%meson_build

%install
%meson_install

%post
%{?ldconfig}

%ldconfig_postun


%files
%doc COPYING
%{_libdir}/libinput.so.*
%{udevdir}/libinput-device-group
%{udevdir}/libinput-fuzz-to-zero
%{udevdir}/libinput-fuzz-extract
%{udevdir}/rules.d/80-libinput-device-groups.rules
%{udevdir}/rules.d/90-libinput-fuzz-override.rules
%{_bindir}/libinput
%dir %{_libexecdir}/libinput/
%{_libexecdir}/libinput/libinput-debug-events
%{_libexecdir}/libinput/libinput-list-devices
%{_mandir}/man1/libinput.1*
%dir %{_datadir}/libinput
%{_datadir}/libinput/*.quirks
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*
%{_mandir}/man1/libinput-list-devices.1*
%{_mandir}/man1/libinput-debug-events.1*

%files devel
%{_includedir}/libinput.h
%{_libdir}/libinput.so
%{_libdir}/pkgconfig/libinput.pc

%files utils
%{_libexecdir}/libinput/libinput-analyze
%{_libexecdir}/libinput/libinput-analyze-buttons
%{_libexecdir}/libinput/libinput-analyze-per-slot-delta
%{_libexecdir}/libinput/libinput-analyze-recording
%{_libexecdir}/libinput/libinput-analyze-touch-down-state
%{_libexecdir}/libinput/libinput-debug-tablet
%{_libexecdir}/libinput/libinput-debug-tablet-pad
%{_libexecdir}/libinput/libinput-list-kernel-devices
%{_libexecdir}/libinput/libinput-measure
%{_libexecdir}/libinput/libinput-measure-fuzz
%{_libexecdir}/libinput/libinput-measure-touchpad-tap
%{_libexecdir}/libinput/libinput-measure-touchpad-pressure
%{_libexecdir}/libinput/libinput-measure-touchpad-size
%{_libexecdir}/libinput/libinput-measure-touch-size
%{_libexecdir}/libinput/libinput-quirks
%{_libexecdir}/libinput/libinput-record
%{_libexecdir}/libinput/libinput-replay
%{_mandir}/man1/libinput-analyze.1*
%{_mandir}/man1/libinput-analyze-buttons.1*
%{_mandir}/man1/libinput-analyze-per-slot-delta.1*
%{_mandir}/man1/libinput-analyze-recording.1*
%{_mandir}/man1/libinput-analyze-touch-down-state.1*
%{_mandir}/man1/libinput-debug-tablet.1*
%{_mandir}/man1/libinput-debug-tablet-pad.1*
%{_mandir}/man1/libinput-list-kernel-devices.1*
%{_mandir}/man1/libinput-measure.1*
%{_mandir}/man1/libinput-measure-fuzz.1*
%{_mandir}/man1/libinput-measure-touchpad-tap.1*
%{_mandir}/man1/libinput-measure-touch-size.1*
%{_mandir}/man1/libinput-measure-touchpad-pressure.1*
%{_mandir}/man1/libinput-measure-touchpad-size.1*
%{_mandir}/man1/libinput-quirks.1*
%{_mandir}/man1/libinput-quirks-list.1*
%{_mandir}/man1/libinput-quirks-validate.1*
%{_mandir}/man1/libinput-record.1*
%{_mandir}/man1/libinput-replay.1*

%files test
%{_libexecdir}/libinput/libinput-test
%{_libexecdir}/libinput/libinput-test-suite
%{_libexecdir}/libinput/libinput-test-utils
%{_mandir}/man1/libinput-test.1*
%{_mandir}/man1/libinput-test-suite.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31.0-2
- Prepare for Oreon 11 (RP1)
