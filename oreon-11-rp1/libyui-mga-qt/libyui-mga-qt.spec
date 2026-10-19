%global source0_hash ea2836c4a718b891175ea34286257de2a5dda55bacd4e404c2797cdc4b06cf8f
%define major 15
%global libsuffix yui
%global libname lib%{libsuffix}
%undefine __cmake_in_source_build
Name:       %{libname}-mga-qt
Version:    1.2.0
Release:        1%{?dist}
Summary:        Libyui-Qt extensions for Mageia tools
License:    LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:        https://github.com/manatools/%{name}
Source0:        https://github.com/manatools/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:	libyui-qt%{?_isa}
Supplements:	(libyui-mga%{?_isa} and libyui-qt%{?_isa})
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  ghostscript
BuildRequires:  graphviz
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libyui)
BuildRequires:  pkgconfig(libyui-mga)
BuildRequires:  pkgconfig(libyui-qt)
# /oreon:deps
%description
This package contains the Libyui-Qt extensions for Mageia tools.

%package devel
Summary:		Files needed for developing with %{name}
Requires:	libyui-devel
Requires:	%{name} = %{version}-%{release}
Provides:	yui-mga-qt-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
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
%files -n libyui-mga-qt-devel -f %{oreon_filedir}/libyui-mga-qt-devel.list

%changelog

%autochangelog
