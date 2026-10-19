%global source0_hash 4aa21910b470872df6d870eb36d9e441ed5623b7091b34671290087ad5d9c340
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0
%global  major 15
%global _cmake_build_subdir build-%{?_arch}%{?dist}
Name:       %{libname}-mga-ncurses
Version:    1.2.0
Release:        1%{?dist}
Summary:        Libyui-Ncurses extensions for Mageia tools
License:    LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:        https://github.com/manatools/%{name}
Source0:        https://github.com/manatools/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Supplements:		(libyui-mga%{?_isa} and libyui-ncurses%{?_isa})
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libyui-devel
BuildRequires:  libyui-mga-devel
BuildRequires:  libyui-ncurses-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)
# /oreon:deps
%description
This package contains the Libyui-Ncurses extensions for Mageia tools.

%package devel
Summary:		Files needed for developing with %{name}
Requires:		%{libname}-devel%{?_isa}	>= %{devel_min_ver}
Requires:		%{libname}-ncurses-devel%{?_isa}
Requires:		%{libname}-mga-devel%{?_isa}
Requires:		%{name}%{?_isa}			== %{version}-%{release}
%description devel
%{libname} can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with %{libname}.
Using %{libname}-devel is sufficient for such purpose. This
package is only needed when you want to develop an extension
for %{name}.

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
%files -n libyui-mga-ncurses-devel -f %{oreon_filedir}/libyui-mga-ncurses-devel.list

%changelog

%autochangelog
