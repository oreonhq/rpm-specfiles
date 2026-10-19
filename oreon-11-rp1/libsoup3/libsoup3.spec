%global source0_hash bbf08fa3e03a88c31a3d27a0d87cb422e9490f2d08e149211103df6d638a2238
%global glib2_version 2.70.0
%global with_mingw 0
Name:    libsoup3
Version: 3.8.0
%global source_series %(echo %{version} | cut -d. -f1-2)
Release:        1%{?dist}
Summary:        Soup, an HTTP library implementation
License: LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/libsoup/%{source_series}/libsoup-%{version}.tar.xz
Patch:   no-ntlm-in-fips-mode.patch
Recommends: glib-networking%{?_isa} >= %{glib2_version}
# oreon:deps
BuildRequires:  /usr/bin/ntlm_auth
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  glib-networking
BuildRequires:  krb5-devel
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-brotli
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libnghttp2
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-brotli
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libnghttp2
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw64-sqlite
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  vala
# /oreon:deps
%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it), but the SOAP parts were removed
long ago.

%package devel
Summary: Header files for the Soup library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Libsoup is an HTTP library implementation in C. This package allows
you to develop applications that use the libsoup library.

%package doc
Summary: Documentation files for %{name}
Recommends: gi-docgen-fonts
BuildArch: noarch
%description doc
This package contains developer documentation for %{name}.

%package -n mingw32-libsoup3
Summary: MinGW library for HTTP functionality
Recommends: mingw32-glib-networking
%description -n mingw32-libsoup3
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of libsoup3

%package -n mingw64-libsoup3
Summary: MinGW library for HTTP functionality
Recommends: mingw64-glib-networking
%description -n mingw64-libsoup3
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of libsoup3

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libsoup-%{version}
%oreon_prep
%build

%meson -Ddocs=enabled -Dautobahn=disabled
%meson_build
%mingw_meson \
    -Ddocs=disabled \
    -Dintrospection=disabled \
    -Dtests=false \
    -Dtls_check=false \
    -Dvapi=disabled
%install
%meson_install
install -m 644 -D tests/libsoup.supp %{buildroot}%{_datadir}/libsoup-3.0/libsoup.supp
%find_lang libsoup-3.0
%mingw_ninja_install
%mingw_find_lang libsoup-3.0
%mingw_debug_install_post
%ifnarch s390x
%oreon_autofiles mingw32-libsoup3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libsoup3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n libsoup3-devel -f %{oreon_filedir}/libsoup3-devel.list
%files -n libsoup3-doc -f %{oreon_filedir}/libsoup3-doc.list
%files -n mingw32-libsoup3 -f %{oreon_filedir}/mingw32-libsoup3.list
%files -n mingw64-libsoup3 -f %{oreon_filedir}/mingw64-libsoup3.list

%changelog

%autochangelog
