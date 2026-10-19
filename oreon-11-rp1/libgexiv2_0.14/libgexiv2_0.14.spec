%global source0_hash 373b67b24f1a7b5c0606aaf0ea00b352f9511751e21deba0bac650bd5159c93d
Name:           libgexiv2_0.14
Version:        0.14.7
Release:        1%{?dist}
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://download.gnome.org/sources/gexiv2/0.14/gexiv2-%{version}.tar.xz
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch s390x
%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n libgexiv2_0.14-devel -f %{oreon_filedir}/libgexiv2_0.14-devel.list

%changelog

%autochangelog
