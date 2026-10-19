%global source0_hash 4e6a67fb8ff1376577afc24a26c842a347b0034eabf71ef13d0382b1c5bc05e7
%{?mingw_package_header}
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:		mingw-libsoup
Version:	3.7.3
Release:        1%{?dist}
Summary:        MinGW library for HTTP and XML-RPC functionality
License:	LGPL-2.0-only
URL:		https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/libsoup/%{release_version}/libsoup-%{version}.tar.xz
Patch0:         libsoup-incompat-pointer-type.patch
Patch1:         CVE-2024-52532.patch
Patch2:         CVE-2024-52530.patch
Patch3:         CVE-2025-32050.patch
Patch4:         CVE-2025-32052.patch
Patch5:         CVE-2025-32053.patch
Patch6:         CVE-2025-32906.patch
Patch7:         CVE-2025-32907.patch
Patch8:         CVE-2025-32909.patch
Patch9:         CVE-2025-32910.patch
Patch10:         CVE-2025-32911.patch
Patch11:         CVE-2025-4476.patch
Patch12:         CVE-2025-4948.patch
Patch13:         CVE-2025-4969.patch
Patch14:         CVE-2025-46420.patch
Patch15:         CVE-2025-46421.patch
Patch16:         CVE-2025-4945.patch
Patch17:         CVE-2025-11021.patch
Patch18:        CVE-2025-14523.patch
Patch19:        CVE-2026-0716.patch
Patch20:        CVE-2026-0719.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-brotli
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-brotli
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-sqlite
# /oreon:deps
%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of Libsoup

# Win32
%package -n mingw32-libsoup
Summary:	MinGW library for HTTP and XML-RPC functionality
Requires:       pkgconfig
Requires:       mingw32-glib-networking
Obsoletes:      mingw32-libsoup-static < 2.54.1
%description -n mingw32-libsoup
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of Libsoup

# Win64
%package -n mingw64-libsoup
Summary:        MinGW library for HTTP and XML-RPC functionality
Requires:       pkgconfig
Requires:       mingw64-glib-networking
Obsoletes:      mingw64-libsoup-static < 2.54.1
%description -n mingw64-libsoup
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of Libsoup

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libsoup-%{version}
%oreon_prep
%build

%mingw_meson \
    -Dgtk_doc=false \
    -Dgssapi=disabled \
    -Dintrospection=disabled \
    -Dtests=false \
    -Dtls_check=false \
    -Dvapi=disabled
%mingw_ninja
%install
%mingw_ninja_install
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
%mingw_find_lang libsoup
%oreon_autofiles mingw32-libsoup usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libsoup usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libsoup -f %{oreon_filedir}/mingw32-libsoup.list
%files -n mingw64-libsoup -f %{oreon_filedir}/mingw64-libsoup.list

%changelog

%autochangelog
