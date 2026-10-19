%global source0_hash 19e383c82d5dd89db275e00b82864e90414d4c3fb3d100b2f996bcc2338a4cc7
%global apiver 3.0
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global glibmm24_version 2.54.0
%global gtk3_version 3.24.0
%global cairomm_version 1.12.0
%global pangomm_version 2.38.2
%global gdk_pixbuf2_version 2.35.5
%global atkmm_version 2.24.2
Name:           gtkmm3.0
Version:        3.24.11
Release:        1%{?dist}
Summary:        C++ interface for the GTK+ library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gtkmm/%{release_version}/gtkmm-%{version}.tar.xz
Requires:       atkmm%{?_isa} >= %{atkmm_version}
Requires:       cairomm%{?_isa} >= %{cairomm_version}
Requires:       gdk-pixbuf2%{?_isa} >= %{gdk_pixbuf2_version}
Requires:       glibmm2.4%{?_isa} >= %{glibmm24_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       pangomm%{?_isa} >= %{pangomm_version}
Obsoletes:      gtkmm30 < %{version}-%{release}
Provides:       gtkmm30 = %{version}-%{release}
Provides:       gtkmm30%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig(atkmm-1.6)
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pangomm-1.4)
# /oreon:deps
%description
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      gtkmm30-devel < %{version}-%{release}
Provides:       gtkmm30-devel = %{version}-%{release}
Provides:       gtkmm30-devel%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm2.4-doc
Obsoletes:      gtkmm30-doc < %{version}-%{release}
Provides:       gtkmm30-doc = %{version}-%{release}
%description    doc
This package contains the full API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n gtkmm-%{version}

# Copy demos before build to avoid including built binaries in -doc package
mkdir -p _docs
cp -a demos/ _docs/

%build

%meson -Dbuild-documentation=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtkmm3.0-devel -f %{oreon_filedir}/gtkmm3.0-devel.list
%files -n gtkmm3.0-doc -f %{oreon_filedir}/gtkmm3.0-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.24.10-1
- Prepare for Oreon 11 (RP1)
