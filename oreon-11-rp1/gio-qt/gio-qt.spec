%global source0_hash b0ff9c2281fc1cff5da308066a9c853f3f6cd91d603a5175b91be05ef3bb345a
Name:           gio-qt
Version:        0.0.16
Release:        1%{?dist}
Summary:        Gio wrapper for Qt applications
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/%{name}
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  qt5-doctools
# /oreon:deps
%description
This package provides a GIO wrapper class for Qt.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}
Requires:       glibmm24-devel%{?isa}
%description devel
Header files and libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# fix doc path
sed -i 's|qt5/doc|doc/qt5|' CMakeLists.txt

%build

export PATH=%{_qt5_bindir}:$PATH
%cmake -DBUILD_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n gio-qt-devel -f %{oreon_filedir}/gio-qt-devel.list

%changelog

%autochangelog
