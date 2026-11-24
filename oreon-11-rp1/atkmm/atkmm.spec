# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ae449192a582a2582a95e0602b15d792bbd639e836339b81ef916aa87540ac5c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global apiver 1.6
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glibmm24_version 2.46.2

Name:           atkmm
Version:        2.28.5
Release:        1%{?dist}
Summary:        C++ interface for the ATK library

License:        LGPL-2.1-or-later
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/atkmm/%{release_version}/atkmm-%{version}.tar.xz
BuildRequires: oreon-rpm-macros
BuildRequires:  atk-devel
BuildRequires:  doxygen
BuildRequires:  clang
BuildRequires:  pkgconfig(glibmm-2.4) >= %{glibmm24_version}
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common

Requires:       glibmm24%{?_isa} >= %{glibmm24_version}

%description
atkmm provides a C++ interface for the ATK library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer's documentation for the atkmm library
BuildArch:      noarch
License:        LGPL-2.1-or-later AND MIT AND GPL-2.0-or-later AND (MIT OR GPL-2.0-or-later)
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-doc

%description    doc
This package contains developer's documentation for the atkmm
library. Atkmm is the C++ API for the ATK accessibility toolkit library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep
%oreon_sha256
%setup -q

%build
%meson -Dbuild-documentation=true
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libatkmm-%{apiver}.so.1*

%files devel
%{_includedir}/atkmm-%{apiver}/
%{_libdir}/libatkmm-%{apiver}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/atkmm-%{apiver}/

%files doc
%doc %{_docdir}/atkmm-%{apiver}/
%doc %{_datadir}/devhelp/

%changelog
%autochangelog
