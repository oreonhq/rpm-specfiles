%global source0_hash aad9e240fdffbe85e390f46ee0a567e251baea5c29c3d8690260388683dc8d0a
Name:           libgexiv2
Version:        0.16.2
Release:        1%{?dist}
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library
%global gexiv2_series %(echo %{version} | cut -d. -f1-2)
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://download.gnome.org/sources/gexiv2/%{gexiv2_series}/gexiv2-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  vala
# /oreon:deps
%description
libgexiv2 is a GObject-based wrapper around the Exiv2 library. 
It makes the basic features of Exiv2 available to GNOME applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python3-gexiv2
Summary:        Python3 bindings for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       python3-gobject-base-noarch
%description -n python3-gexiv2
This package contains the python3 bindings for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gexiv2-%{version}
%oreon_prep
%build

%meson \
  -Dgtk_doc=true \
  -Dtests=true \
  %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles python3-gexiv2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifnarch s390x
%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n libgexiv2-devel -f %{oreon_filedir}/libgexiv2-devel.list
%files -n python3-gexiv2 -f %{oreon_filedir}/python3-gexiv2.list

%changelog

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-3
- Fix Source0 path use GNOME series dir %%{gexiv2_series} (0.16) not %%{version} (0.16.0)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-2
- Prepare for Oreon 11 (RP1)
