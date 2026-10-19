%global source0_hash a24e0f9c2a2905b62e53d796d2603747d7fe9f5c818cd93b1a90c774c576aa1c
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0
%global _libyui_major_so_ver 15
%undefine __cmake_in_source_build
Name:			%{libname}-mga-gtk
Version:		1.2.0
Release:        1%{?dist}
Summary:        Libyui-Gtk extensions for Mageia tools
License:		LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:			https://github.com/manatools/%{name}
Source0:        https://github.com/manatools/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Supplements:		(libyui-mga%{?_isa} and libyui-gtk%{?_isa})
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libyui-devel
BuildRequires:  libyui-gtk-devel
BuildRequires:  libyui-mga-devel
# /oreon:deps
%description
This package contains the Libyui-Gtk extensions for Mageia tools.

%package devel
Summary:		Files needed for developing with %{name}
Requires:		%{libname}-devel%{?_isa}		>= %{devel_min_ver}
Requires:		%{libname}-gtk-devel%{?_isa}
Requires:		%{libname}-mga-devel%{?_isa}
Requires:		%{name}%{?_isa} == %{version}-%{release}
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
%files -n libyui-mga-gtk-devel -f %{oreon_filedir}/libyui-mga-gtk-devel.list

%changelog

%autochangelog
