%global source0_hash b584234b00599fb8dc6cf802d6b1ab037906ab5b2b2243b33210f4a30f524e19

# Define libsuffix, minimum libyui-devel version
# and so-version of libyui.
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build

Name:			%{libname}-mga
Version:		1.2.1
Release:		12%{?dist}
Summary:		Libyui extensions for Mageia tools

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:			https://github.com/manatools/%{name}
Source0:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	ghostscript

BuildRequires:	%{libname}-devel >= %{devel_min_ver}

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

%autosetup -p1

%build
%cmake \
    -DBUILD_EXAMPLES=NO
%cmake_build

%install
%cmake_install

%files
%license COPYING*
%{_libdir}/%{name}.so.15*

%files devel
%{_includedir}/yui
%{_libdir}/libyui-mga.so
%{_libdir}/pkgconfig/libyui-mga.pc

%changelog
%autochangelog
