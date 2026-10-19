%global source0_hash 9b6bd256adf2578bff154d2ef575ffb60eb8245f6fe9bb6edfb23e782e4152ed
Name:          libdbusmenu-lxqt
Summary:        Library providing a way to implement DBusMenu protocol for LXQt
Version:       0.3.0
Release:        3%{?dist}
License:       LGPL-2.0-or-later
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Qt - development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Files used for developing and building software that uses %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdbusmenu-lxqt-devel -f %{oreon_filedir}/libdbusmenu-lxqt-devel.list

%changelog

%autochangelog
