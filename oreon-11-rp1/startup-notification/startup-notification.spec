%global source0_hash 3c391f7e930c583095045cd2d10eb73a64f085c7fde9d260f2652c7cb3cfbe4a
Name:    startup-notification
Version: 0.12
Release:        33%{?dist}
Summary:        Library for tracking application startup
License: LGPL-2.0-or-later AND MIT
URL:     https://www.freedesktop.org/wiki/Software/startup-notification/
Source0:        http://www.freedesktop.org/software/startup-notification/releases/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  pkgconfig(xcb-event)
# /oreon:deps
%description
This package contains libstartup-notification which implements a
startup notification protocol. Using this protocol a desktop
environment can track the launch of an application and provide
feedback such as a busy cursor, among other features.

%package devel
Summary: Development portions of startup-notification
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libX11-devel
%description devel
Header files and static libraries for libstartup-notification.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
mkdir examples
cp -p test/*.c test/*.h examples

%build

%configure --disable-static
%make_build
%install
%make_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n startup-notification-devel -f %{oreon_filedir}/startup-notification-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12-33
- Prepare for Oreon 11 (RP1)
