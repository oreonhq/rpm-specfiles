%global source0_hash 4aa21910b470872df6d870eb36d9e441ed5623b7091b34671290087ad5d9c340

# Define libsuffix, minimum libyui-devel version
# and so-version of libyui.
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0
%global  major 15

# CMake-builds go out-of-tree.
%global _cmake_build_subdir build-%{?_arch}%{?dist}

Name:       %{libname}-mga-ncurses
Version:    1.2.0
Release:    11%{?dist}
Summary:    Libyui-Ncurses extensions for Mageia tools

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:        https://github.com/manatools/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:    gcc-c++
BuildRequires:    boost-devel
BuildRequires:    cmake
BuildRequires:    %{libname}-devel		>= %{devel_min_ver}
BuildRequires:    %{libname}-mga-devel		>= 1.1.0
BuildRequires:    %{libname}-ncurses-devel	>= 2.55.0

BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(ncurses)

Supplements:		(libyui-mga%{?_isa} and libyui-ncurses%{?_isa})

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

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING*
%{_libdir}/%{libsuffix}/%{name}.so.%{major}*

%files devel
%{_includedir}/yui/mga/ncurses/
%{_libdir}/yui/libyui-mga-ncurses.so

%changelog
%autochangelog
