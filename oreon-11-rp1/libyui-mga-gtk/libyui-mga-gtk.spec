%global source0_hash a24e0f9c2a2905b62e53d796d2603747d7fe9f5c818cd93b1a90c774c576aa1c

# Define libsuffix, minimum libyui-devel version
# and so-version of libyui.
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0
%global _libyui_major_so_ver 15

# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build

Name:			%{libname}-mga-gtk
Version:		1.2.0
Release:		17%{?git_rel}%{?dist}
Summary:		Libyui-Gtk extensions for Mageia tools

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:			https://github.com/manatools/%{name}
Source0:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:		gcc-c++
BuildRequires:		boost-devel
BuildRequires:		cmake
BuildRequires:		%{libname}-devel			>= %{devel_min_ver}
BuildRequires:		%{libname}-mga-devel		>= 1.2.0
BuildRequires:		%{libname}-gtk-devel		>= 2.49.0

Supplements:		(libyui-mga%{?_isa} and libyui-gtk%{?_isa})

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

%autosetup -p1

%build
%cmake						
%cmake_build

%install
%cmake_install

%files
%license COPYING*
%doc README.md
%{_libdir}/%{libsuffix}/%{name}.so.%{_libyui_major_so_ver}*

%files devel 
%doc ChangeLog 
%{_includedir}/yui/mga/gtk/
%{_libdir}/%{libsuffix}/%{name}.so

%changelog
%autochangelog
