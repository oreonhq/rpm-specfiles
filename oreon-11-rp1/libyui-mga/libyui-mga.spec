%global source0_hash b584234b00599fb8dc6cf802d6b1ab037906ab5b2b2243b33210f4a30f524e19
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%undefine __cmake_in_source_build
Name:			%{libname}-mga
Version:		1.2.1
Release:        12%{?dist}
Summary:        Libyui extensions for Mageia tools
License:		LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:			https://github.com/manatools/%{name}
Source0:        https://github.com/manatools/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libyui-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libyui)
# /oreon:deps
%description
This package contains the Libyui extensions for Mageia tools.

%package devel
Summary:		Files needed for developing with %{name}
Requires:		%{libname}-devel%{?_isa}	>= %{devel_min_ver}
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

%cmake \
    -DBUILD_EXAMPLES=NO
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libyui-mga-devel -f %{oreon_filedir}/libyui-mga-devel.list

%changelog

%autochangelog
