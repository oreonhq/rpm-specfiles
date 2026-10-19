%global source0_hash e341956acc142cfb29b6be3bbe6ce7a663409eb63f6ff68f8d5921bfffb71ab3
%define apiver 1.4
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global glibmm_version 2.48.0
%global cairomm_version 1.2.2
%global pango_version 1.45.1
Name:           pangomm
Version:        2.58.0
Release:        1%{?dist}
Summary:        C++ interface for Pango
License:        LGPL-2.1-or-later AND GPL-2.0-only
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
Requires:       glibmm2.4%{?_isa} >= %{glibmm_version}
Requires:       cairomm1.0%{?_isa} >= %{cairomm_version}
Requires:       pango%{?_isa} >= %{pango_version}
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(glibmm-2.4)
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
License:          GPL-2.0-or-later AND AGPL-3.0-only AND MIT AND (GPL-2.0-only OR MIT)
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}
Requires:         libsigc++20-doc
Requires:         glibmm2.4-doc
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
%files -n pangomm-devel -f %{oreon_filedir}/pangomm-devel.list
%files -n pangomm-doc -f %{oreon_filedir}/pangomm-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.46.4-1
- Prepare for Oreon 11 (RP1)
