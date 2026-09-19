%global source0_hash dd8592eeb6512ad0a8cf5c8be8c72e76f74bfe6b23e4dd93f0756ee0716804c7

# uhttpmock is not available in RHEL, and F40 version is too new
%bcond tests %[!(0%{?rhel} || 0%{?fedora} >= 40)]

Name:           libgdata
Version:        0.18.1
Release:        16%{?dist}
Summary:        Library for the GData protocol

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/libgdata
Source0:        https://download.gnome.org/sources/%{name}/0.18/%{name}-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/libgdata/-/merge_requests/47
# Build against gcr 4
Patch0:         47.patch

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
%if %{with tests}
BuildRequires:  pkgconfig(libuhttpmock-0.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
%endif
BuildRequires:  vala

%if 0%{?fedora}
Obsoletes:      compat-libgdata19 < 0.17.1
%endif

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

%autosetup -p1

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

%check
# Only the general test can be run without network access
# Actually, the general test doesn't work either without gconf
#cd gdata/tests
#./general

%ldconfig_scriptlets

%files -f gdata.lang
%license COPYING
%doc NEWS README AUTHORS
%{_libdir}/libgdata.so.22*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GData-0.0.typelib

%files devel
%{_includedir}/*
%{_libdir}/libgdata.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GData-0.0.gir
%{_datadir}/vala/

%changelog
%autochangelog
