# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2b61780203aed98e701d3ea57c8f353e7c8ada9706a79be782f6c5153dd035c0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global apiver 2.4
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glib2_version 2.61.2
%global libsigc_version 2.9.1

Name:           glibmm2.4
Version:        2.66.10
Release:        1%{?dist}
Summary:        C++ interface for the GLib library

License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://gtkmm.org/
Source0:        https://download.gnome.org/sources/glibmm/%{release_version}/glibmm-%{version}.tar.xz
Patch0:         glibmm24-gcc11.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  doxygen
BuildRequires:  clang
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(sigc++-2.0) >= %{libsigc_version}

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libsigc++20%{?_isa} >= %{libsigc_version}

Obsoletes:      glibmm24 < %{version}-%{release}
Provides:       glibmm24 = %{version}-%{release}
Provides:       glibmm24%{?_isa} = %{version}-%{release}

%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)

%description
glibmm is the official C++ interface for the popular cross-platform
library GLib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      glibmm24-devel < %{version}-%{release}
Provides:       glibmm24-devel = %{version}-%{release}
Provides:       glibmm24-devel%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       libsigc++20-doc
Obsoletes:      glibmm24-doc < %{version}-%{release}
Provides:       glibmm24-doc = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n glibmm-%{version}

%build
%meson -Dbuild-documentation=true
%meson_build

%install
%meson_install

chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/generate_wrap_init.pl
chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/gmmproc

%files
%license COPYING COPYING.tools
%doc NEWS README.md
%{_libdir}/libgiomm-%{apiver}.so.1*
%{_libdir}/libglibmm-%{apiver}.so.1*
%{_libdir}/libglibmm_generate_extra_defs-%{apiver}.so.1*

%files devel
%{_includedir}/glibmm-%{apiver}/
%{_includedir}/giomm-%{apiver}/
%{_libdir}/*.so
%{_libdir}/glibmm-%{apiver}/
%{_libdir}/giomm-%{apiver}/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_datadir}/devhelp/
%doc %{_docdir}/glibmm-%{apiver}/

%changelog
%autochangelog
