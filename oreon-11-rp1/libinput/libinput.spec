%global source0_hash 3a6065c07b118c08d0c7b7b85a265ecb050a8cfc91eeb360890d768a51b4cce9
%global udevdir %(pkg-config --variable=udevdir udev)
%global gitversion 58abea394
Name:           libinput
Version:        1.32.0
Release:        1%{?dist}
Summary:        Input device library
License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libinput/
%if 0%{?gitdate}
Source0:        https://gitlab.freedesktop.org/libinput/libinput/-/archive/%{version}/libinput-%{version}.tar.bz2
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  lua-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3-rpm-macros
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%post

%{?ldconfig}
%ldconfig_postun
%files -f %{oreon_filedir}/main.list
%files -n libinput-devel -f %{oreon_filedir}/libinput-devel.list
%files -n libinput-utils -f %{oreon_filedir}/libinput-utils.list
%files -n libinput-test -f %{oreon_filedir}/libinput-test.list

%changelog

%autochangelog
