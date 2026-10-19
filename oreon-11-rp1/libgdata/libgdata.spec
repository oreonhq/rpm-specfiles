%global source0_hash dd8592eeb6512ad0a8cf5c8be8c72e76f74bfe6b23e4dd93f0756ee0716804c7
%bcond tests %[!(0%{?rhel} || 0%{?fedora} >= 40)]
Name:           libgdata
Version:        0.18.1
Release:        16%{?dist}
Summary:        Library for the GData protocol
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/libgdata
Source0:        https://download.gnome.org/sources/%{name}/0.18/%{name}-%{version}.tar.xz
Patch0:         47.patch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libuhttpmock-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala
# /oreon:deps
%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%meson \
%if %{with tests}
  -Dalways_build_tests=true \
%else
  -Dalways_build_tests=false \
%endif
  -Dinstalled_tests=false \
  -Dgtk_doc=true \
  -Doauth1=disabled \
  %{nil}
%meson_build
%install
%meson_install
%find_lang gdata
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libgdata-devel -f %{oreon_filedir}/libgdata-devel.list

%changelog

%autochangelog
