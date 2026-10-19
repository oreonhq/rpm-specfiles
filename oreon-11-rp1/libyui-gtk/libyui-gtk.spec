%global source0_hash 94be307ad831d086bad877186bdbd78bdc9513bd5374a859743c0b5bba75e13a
%undefine __cmake_in_source_build
%define		major	15
Name:		libyui-gtk
Version:	2.52.5
Release:        1%{?dist}
Summary:        Gtk3 User Interface for libyui
License:	LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:		https://github.com/libyui/%{name}
Source0:        https://github.com/libyui/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Supplements:	(libyui%{?_isa} and gtk3%{?_isa})
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libyui-devel
BuildRequires:  sane-backends-devel
# /oreon:deps
%description
This package contains the Gtk3 user interface component
for libyui.

%package devel
Summary:	Files needed for developing with %{name}
Requires:	gtk3-devel%{?_isa}
Requires:	libyui-devel%{?_isa}
Requires:	%{name}%{?_isa}		== %{version}-%{release}
%description devel
libyui can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with libyui.
Usinglibyui-devel is sufficient for such purpose. This
package is only needed when you want to develop an extension
for %{name} which is not covered within the UI-plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake							\
	-DENABLE_WERROR=OFF				\
	-DYPREFIX=%{_prefix}				\
	-DLIB_DIR=%{_libdir}				\
	-DCMAKE_BUILD_TYPE=RELEASE			\
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libyui-gtk-devel -f %{oreon_filedir}/libyui-gtk-devel.list

%changelog

%autochangelog
