%global source0_hash 7fd9cea356e7d3b74bf7d2a51d7e0e6763f3f9f1cddc5e77c8b0b5b7fa9d5e5a
%global apiver 4.0
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global glibmm_version 2.75.0
%global gtk4_version 4.19.2
%global cairomm_version 1.15.4
%global pangomm_version 2.50.0
%global gdk_pixbuf2_version 2.35.5
%global epoxy_version 1.2
Name:           gtkmm4.0
Version:        4.24.0
Release:        1%{?dist}
Summary:        C++ interface for the GTK+ library
License:        LGPL-2.1-or-later
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gtkmm/%{release_version}/gtkmm-%{version}.tar.xz
Requires:       cairomm1.16%{?_isa} >= %{cairomm_version}
Requires:       gdk-pixbuf2%{?_isa} >= %{gdk_pixbuf2_version}
Requires:       glibmm2.68%{?_isa} >= %{glibmm_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       pangomm2.48%{?_isa} >= %{pangomm_version}
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig(cairomm-1.16)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(pangomm-2.48)
# /oreon:deps
%description
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm2.68-doc
%description    doc
This package contains the full API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n gtkmm-%{version}

# Copy demos before build to avoid including built binaries in -doc package
mkdir -p _docs
cp -a demos/ _docs/

%build

%meson --wrap-mode=nofallback -Dbuild-documentation=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtkmm4.0-devel -f %{oreon_filedir}/gtkmm4.0-devel.list
%files -n gtkmm4.0-doc -f %{oreon_filedir}/gtkmm4.0-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.22.0-1
- Prepare for Oreon 11 (RP1)
