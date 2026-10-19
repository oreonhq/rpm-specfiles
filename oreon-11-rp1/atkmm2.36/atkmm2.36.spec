%global source0_hash 19cd0758ed752cb89f5bf02247663dfad0926d9351984a20e3c6cf7da62552ac
%global apiver 2.36
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global glibmm_version 2.68.0
Name:           atkmm2.36
Version:        2.36.4
Release:        1%{?dist}
Summary:        C++ interface for the ATK library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/atkmm/%{apiver}/atkmm-%{version}.tar.xz
Requires:       glibmm2.68%{?_isa} >= %{glibmm_version}
# oreon:deps
BuildRequires:  atk-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibmm2.68-devel
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
# /oreon:deps
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
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm2.68-doc
%description    doc
This package contains developer's documentation for the atkmm
library. Atkmm is the C++ API for the ATK accessibility toolkit library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir atkmm-%{version}
%oreon_prep
%build

%meson -Dbuild-documentation=true
%meson_build
%install
%meson_install
%oreon_autofiles atkmm2.36-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles atkmm2.36-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n atkmm2.36-devel -f %{oreon_filedir}/atkmm2.36-devel.list
%files -n atkmm2.36-doc -f %{oreon_filedir}/atkmm2.36-doc.list

%changelog

%autochangelog
