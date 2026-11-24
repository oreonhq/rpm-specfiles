# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0680a53b7bf90b4e4bf444d1d89e6df41c777e0bacc96e9c09fc4dd2f5fe6b72
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define release_version 2.24
%global tarname gtkmm
%global api_ver 2.4

Name:           gtkmm2.4
Version:        2.24.5
Release:        1%{?dist}

Summary:        C++ interface for GTK2 (a GUI library for X)

License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gtkmm/%{release_version}/gtkmm-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  atkmm-devel
BuildRequires:  cairomm-devel
BuildRequires:  glibmm2.4-devel
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  pangomm-devel

Obsoletes:      gtkmm24 < %{version}-%{release}
Provides:       gtkmm24 = %{version}-%{release}
Provides:       gtkmm24%{?_isa} = %{version}-%{release}

%description
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
Obsoletes:      gtkmm24-devel < %{version}-%{release}
Provides:       gtkmm24-devel = %{version}-%{release}
Provides:       gtkmm24-devel%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm2.4-doc
Obsoletes:      gtkmm24-docs < %{version}-%{release}
Provides:       gtkmm24-docs = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.

%prep
%oreon_sha256
%setup -q -n gtkmm-%{version}

%build
%configure --enable-shared
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files devel
%doc PORTING demos/gtk-demo/
%{_includedir}/gtkmm-2.4/
%{_includedir}/gdkmm-2.4/
%{_libdir}/*.so
%{_libdir}/gtkmm-2.4/
%{_libdir}/gdkmm-2.4/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/%{tarname}-%{api_ver}
%doc %{_datadir}/devhelp/

%changelog
%autochangelog
