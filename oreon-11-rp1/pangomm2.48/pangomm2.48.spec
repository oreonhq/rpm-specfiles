%global source0_hash 217514c1a65035c2fce6e69e33b0d92bafa2594cc474e995a4473441b10f3a33
%define apiver 2.48
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global glibmm_version 2.68.0
%global cairomm_version 1.15.1
%global pango_version 1.56.0
Name:           pangomm2.48
Version:        2.58.0
Release:        1%{?dist}
Summary:        C++ interface for Pango
License:        LGPL-2.1-or-later
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/pangomm/%{release_version}/pangomm-%{version}.tar.xz
Requires:       glibmm2.68%{?_isa} >= %{glibmm_version}
Requires:       cairomm1.16%{?_isa} >= %{cairomm_version}
Requires:       pango%{?_isa} >= %{pango_version}
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig(cairomm-1.16)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
# /oreon:deps
%description
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries and header files needed for
developing pangomm applications.

%package          doc
Summary:          Developer's documentation for the pangomm library
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}
Requires:         libsigc++30-doc
Requires:         glibmm2.68-doc
%description      doc
This package contains developer's documentation for the pangomm
library. Pangomm is the C++ API for the Pango font layout library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pangomm-%{version}
%oreon_prep
%build

%meson --wrap-mode=nofallback -Dbuild-documentation=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pangomm2.48-devel -f %{oreon_filedir}/pangomm2.48-devel.list
%files -n pangomm2.48-doc -f %{oreon_filedir}/pangomm2.48-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.56.1-1
- Prepare for Oreon 11 (RP1)
