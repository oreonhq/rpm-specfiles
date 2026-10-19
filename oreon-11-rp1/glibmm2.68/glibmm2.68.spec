%global source0_hash e2efa45643f16b9fea2d6299f2f403d672eaeacddf0ff7f8094e1af9b0f5980b
%global apiver 2.68
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global libsigc_version 3.0.0
%global glib2_version 2.81.0
Name:           glibmm2.68
Version:        2.90.0
Release:        1%{?dist}
Summary:        C++ interface for the GLib library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/glibmm/%{release_version}/glibmm-%{version}.tar.xz
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libsigc++30%{?_isa} >= %{libsigc_version}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sigc++-3.0)
# /oreon:deps
%description
glibmm is the official C++ interface for the popular cross-platform
library GLib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the static libraries and header files needed for
developing glibmm applications.

%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       libsigc++30-doc
%description    doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir glibmm-%{version}
%oreon_prep
%build

%meson -Dbuild-documentation=true
%meson_build
%install
%meson_install
chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/generate_wrap_init.pl
chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/gmmproc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n glibmm2.68-devel -f %{oreon_filedir}/glibmm2.68-devel.list
%files -n glibmm2.68-doc -f %{oreon_filedir}/glibmm2.68-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.86.0-1
- Prepare for Oreon 11 (RP1)
