%global source0_hash 0caf824971108f15bb2ad356433bae198d7d3bf1e82d43f63626e069e060bfa6
Name:           libevdev
Version:        1.13.7
Release:        1%{?dist}
Summary:        Kernel Evdev Device Wrapper Library
License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libevdev
Source0:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  python3-rpm-macros
# /oreon:deps
%description
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package devel
Summary:        Kernel Evdev Device Wrapper Library Development Package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Kernel Evdev Device Wrapper Library Development Package.

%package utils
Summary:        Kernel Evdev Device Wrapper Library Utilities Package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description utils
Utilities to handle and/or debug evdev devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git
# Replace whatever the source uses with the approved call
%py3_shebang_fix $(git grep -l  '#!/usr/bin/.*python3')

%build

%meson -Dtests=disabled -Ddocumentation=disabled -Dcoverity=false
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libevdev-devel -f %{oreon_filedir}/libevdev-devel.list
%files -n libevdev-utils -f %{oreon_filedir}/libevdev-utils.list

%changelog

%autochangelog
