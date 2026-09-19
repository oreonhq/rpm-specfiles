%global source0_hash 9b6bd256adf2578bff154d2ef575ffb60eb8245f6fe9bb6edfb23e782e4152ed

Name:          libdbusmenu-lxqt
Summary:       Library providing a way to implement DBusMenu protocol for LXQt
Version:       0.3.0
Release:       3%{?dist}
License:       LGPL-2.0-or-later
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)

%description
%{summary}.

%package devel
Summary:        Qt - development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files used for developing and building software that uses %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/libdbusmenu-lxqt.so.0
%{_libdir}/libdbusmenu-lxqt.so.%{version}

%files devel
%{_libdir}/cmake/dbusmenu-lxqt
%{_includedir}/dbusmenu-lxqt
%{_libdir}/libdbusmenu-lxqt.so
%{_libdir}/pkgconfig/dbusmenu-lxqt.pc

%changelog
%autochangelog
