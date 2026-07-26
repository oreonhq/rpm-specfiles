%global source0_hash ea2836c4a718b891175ea34286257de2a5dda55bacd4e404c2797cdc4b06cf8f

%define major 15
%global libsuffix yui
%global libname lib%{libsuffix}

# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build

Name:       %{libname}-mga-qt
Version:    1.2.0
Release:    13%{?dist}
Summary:    Libyui-Qt extensions for Mageia tools

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:        https://github.com/manatools/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(libyui-mga)

BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Svg)

BuildRequires:	ghostscript
BuildRequires:	graphviz
BuildRequires:	pkgconfig(fontconfig)

Requires:	libyui-qt%{?_isa}
Supplements:	(libyui-mga%{?_isa} and libyui-qt%{?_isa})

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

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING*
%{_libdir}/yui/libyui-mga-qt.so.%{major}*

%files devel
%{_includedir}/yui/mga/qt/
%{_libdir}/yui/libyui-mga-qt.so

%changelog
%autochangelog
