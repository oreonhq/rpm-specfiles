%global source0_hash 9afe075f165c78ec584892887a6411fe1476f2115cf3bba026105bde29292a4b
Summary:        Asynchronous Python 3 Bindings for Qt 5
Name: pyotherside
Version:    1.6.2
Release:        2%{?dist}
Source0:        https://github.com/thp/pyotherside/archive/%{version}/%{name}-%{version}.tar.gz
URL: http://thp.io/2011/pyotherside/
License: ISC
Requires: python3
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
A QML Plugin that provides access to a Python 3 interpreter from QML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{qmake_qt5}
%make_build
%check

xvfb-run ./tests/tests
%install
make INSTALL_ROOT=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
