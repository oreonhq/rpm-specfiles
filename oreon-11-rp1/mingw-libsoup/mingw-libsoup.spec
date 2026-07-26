%global source0_hash e4b77c41cfc4c8c5a035fcdc320c7bc6cfb75ef7c5a034153df1413fa1d92f13

%{?mingw_package_header}

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:		mingw-libsoup
Version:	2.74.3
Release:	17%{?dist}
Summary:	MinGW library for HTTP and XML-RPC functionality

License:	LGPL-2.0-only
URL:		https://wiki.gnome.org/Projects/libsoup
Source0:	https://download.gnome.org/sources/libsoup/%{release_version}/libsoup-%{version}.tar.xz
# Fix initialization from incompatible pointer type
Patch0:         libsoup-incompat-pointer-type.patch
# Backport fix for CVE-2024-52532
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/6adc0e3eb74c257ed4e2a23eb4b2774fdb0d67be
Patch1:         CVE-2024-52532.patch
# Backport fix for CVE-2024-52530
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/04df03bc092ac20607f3e150936624d4f536e68b
Patch2:         CVE-2024-52530.patch
# Backport fix for CVE-2025-32050
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/9bb0a55de55c6940ced811a64fbca82fe93a9323
Patch3:         CVE-2025-32050.patch
# Backport fix for CVE-2025-32052
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/f182429e5b1fc034050510da20c93256c4fa9652
Patch4:         CVE-2025-32052.patch
# Backport fix for CVE-2025-32053
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/eaed42ca8d40cd9ab63764e3d63641180505f40a
Patch5:         CVE-2025-32053.patch
# Backport fix for CVE-2025-32906
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/af5b9a4a3945c52b940d5ac181ef51bb12011f1f
Patch6:         CVE-2025-32906.patch
# Backport fix for CVE-2025-32907
# https://gitlab.gnome.org/GNOME/libsoup/-/merge_requests/452
Patch7:         CVE-2025-32907.patch
# Backport fix for CVE-2025-32909
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/ba4c3a6f988beff59e45801ab36067293d24ce92
Patch8:         CVE-2025-32909.patch
# Backport fix for CVE-2025-32910
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/ea16eeacb052e423eb5c3b0b705e5eab34b13832
Patch9:         CVE-2025-32910.patch
# Backport fix for CVE-2025-32911 + CVE-2025-32913
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/f4a761fb66512fff59798765e8ac5b9e57dceef0
Patch10:         CVE-2025-32911.patch
# Backport fix for CVE-2025-4476
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/e64c221f9c7d09b48b610c5626b3b8c400f0907c
Patch11:         CVE-2025-4476.patch
# Backport fix for CVE-2025-4948
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/f2f28afe0b3b2b3009ab67d6874457ec6bac70c0
Patch12:         CVE-2025-4948.patch
# Backport fix for CVE-2025-4969
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/b5b4dd10d4810f0c87b4eaffe88504f06e502f33
Patch13:         CVE-2025-4969.patch
# Backport fix for CVE-2025-46420
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/c9083869ec2a3037e6df4bd86b45c419ba295f8e
Patch14:         CVE-2025-46420.patch
# Backport fix for CVE-2025-46421
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/3e5c26415811f19e7737238bb23305ffaf96f66b
Patch15:         CVE-2025-46421.patch
# Backport proposed fix for CVE-2025-4945
# https://gitlab.gnome.org/GNOME/libsoup/-/merge_requests/462
Patch16:         CVE-2025-4945.patch
# Backport fix for CVE-2025-11021
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/9e1a427d2f047439d0320defe1593e6352595788
Patch17:         CVE-2025-11021.patch
# Backport patch for CVE-2025-14523
# https://gitlab.gnome.org/GNOME/libsoup/-/commit/2137d6f75a32a6facb2ffc2062f11a8d9748e0c2
Patch18:        CVE-2025-14523.patch
# Backport fix for CVE-2026-0716
# https://gitlab.gnome.org/GNOME/libsoup/-/merge_requests/494
Patch19:        CVE-2026-0716.patch
# Backport fix for CVE-2026-0719
# https://gitlab.gnome.org/GNOME/libsoup/-/merge_requests/493
Patch20:        CVE-2026-0719.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-brotli
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw32-sqlite

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-brotli
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw64-sqlite

# For glib-genmarshal
BuildRequires: glib2-devel
BuildRequires: intltool

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
# Dropped in F25
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
# Dropped in F25
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

%autosetup -p1 -n libsoup-%{version}

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

# Remove the .la files
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la

%mingw_find_lang libsoup

# Win32
%files -n mingw32-libsoup -f mingw32-libsoup.lang
%license COPYING
%{mingw32_bindir}/libsoup-2.4-1.dll
%{mingw32_bindir}/libsoup-gnome-2.4-1.dll
%{mingw32_includedir}/libsoup-2.4
%{mingw32_includedir}/libsoup-gnome-2.4
%{mingw32_libdir}/libsoup-2.4.dll.a
%{mingw32_libdir}/libsoup-gnome-2.4.dll.a
%{mingw32_libdir}/pkgconfig/libsoup-2.4.pc
%{mingw32_libdir}/pkgconfig/libsoup-gnome-2.4.pc

# Win64
%files -n mingw64-libsoup -f mingw64-libsoup.lang
%license COPYING
%{mingw64_bindir}/libsoup-2.4-1.dll
%{mingw64_bindir}/libsoup-gnome-2.4-1.dll
%{mingw64_includedir}/libsoup-2.4
%{mingw64_includedir}/libsoup-gnome-2.4
%{mingw64_libdir}/libsoup-2.4.dll.a
%{mingw64_libdir}/libsoup-gnome-2.4.dll.a
%{mingw64_libdir}/pkgconfig/libsoup-2.4.pc
%{mingw64_libdir}/pkgconfig/libsoup-gnome-2.4.pc

%changelog
%autochangelog
