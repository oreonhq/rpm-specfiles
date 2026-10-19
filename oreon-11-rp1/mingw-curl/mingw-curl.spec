%global source0_hash f7ef3ae8a22e521f289803fe93543eb64c329b58aa73a9e224dfd915a2a5f4f7
%{?mingw_package_header}
Name:           mingw-curl
Version:        8.22.0
Release:        1%{?dist}
Summary:        MinGW Windows port of curl and libcurl
License:        MIT
URL:            https://curl.haxx.se/
Source0:        https://curl.haxx.se/download/curl-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-libidn2
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw32-libssh2
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-libidn2
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw64-libssh2
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
cURL is a tool for getting files from HTTP, FTP, FILE, LDAP, LDAPS,
DICT, TELNET and TFTP servers, using any of the supported protocols.
cURL is designed to work without user interaction or any kind of
interactivity. cURL offers many useful capabilities, like proxy
support, user authentication, FTP upload, HTTP post, and file transfer
resume.

This is the MinGW cross-compiled Windows library.

# Win32
%package -n mingw32-curl
Summary:        MinGW Windows port of curl and libcurl
Requires:       pkgconfig
%description -n mingw32-curl
cURL is a tool for getting files from HTTP, FTP, FILE, LDAP, LDAPS,
DICT, TELNET and TFTP servers, using any of the supported protocols.
cURL is designed to work without user interaction or any kind of
interactivity. cURL offers many useful capabilities, like proxy
support, user authentication, FTP upload, HTTP post, and file transfer
resume.

This is the MinGW cross-compiled Windows library.

%package -n mingw32-curl-static
Summary:        Static version of the MinGW Windows Curl library
Requires:       mingw32-curl = %{version}-%{release}
%description -n mingw32-curl-static
Static version of the MinGW Windows Curl library.

# Win64
%package -n mingw64-curl
Summary:        MinGW Windows port of curl and libcurl
Requires:       pkgconfig
%description -n mingw64-curl
cURL is a tool for getting files from HTTP, FTP, FILE, LDAP, LDAPS,
DICT, TELNET and TFTP servers, using any of the supported protocols.
cURL is designed to work without user interaction or any kind of
interactivity. cURL offers many useful capabilities, like proxy
support, user authentication, FTP upload, HTTP post, and file transfer
resume.

This is the MinGW cross-compiled Windows library.

%package -n mingw64-curl-static
Summary:        Static version of the MinGW Windows Curl library
Requires:       mingw64-curl = %{version}-%{release}
%description -n mingw64-curl-static
Static version of the MinGW Windows Curl library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir curl-%{version}
%oreon_prep
%build

MINGW32_CONFIGURE_ARGS="--with-ca-bundle=%{mingw32_sysconfdir}/pki/tls/certs/ca-bundle.crt"
MINGW64_CONFIGURE_ARGS="--with-ca-bundle=%{mingw64_sysconfdir}/pki/tls/certs/ca-bundle.crt"
MINGW_CONFIGURE_ARGS="--with-ssl --enable-ipv6 --enable-threaded-resolver --enable-sspi --with-libidn2 --with-libssh2 --without-random"
MINGW_BUILDDIR_SUFFIX=_static %mingw_configure --enable-static --disable-shared
MINGW_BUILDDIR_SUFFIX=_shared %mingw_configure --disable-static --enable-shared
MINGW_BUILDDIR_SUFFIX=_static %mingw_make_build
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make_build
%install
MINGW_BUILDDIR_SUFFIX=_static %mingw_make DESTDIR=%{buildroot}/static install
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make_install
mv %{buildroot}/static%{mingw32_bindir}/curl-config %{buildroot}%{mingw32_bindir}/curl-config-static
mv %{buildroot}/static%{mingw64_bindir}/curl-config %{buildroot}%{mingw64_bindir}/curl-config-static
mv %{buildroot}/static%{mingw32_libdir}/libcurl.a %{buildroot}%{mingw32_libdir}/libcurl.a
mv %{buildroot}/static%{mingw64_libdir}/libcurl.a %{buildroot}%{mingw64_libdir}/libcurl.a
rm -rf %{buildroot}/static
find %{buildroot} -name "*.la" -delete
rm -r %{buildroot}%{mingw32_mandir}/man{1,3}
rm -r %{buildroot}%{mingw64_mandir}/man{1,3}
rm -rf %{buildroot}%{mingw32_datadir}/aclocal
rm -rf %{buildroot}%{mingw64_datadir}/aclocal
rm -f %{buildroot}%{mingw32_bindir}/wcurl
rm -f %{buildroot}%{mingw64_bindir}/wcurl
%oreon_autofiles mingw32-curl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-curl-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-curl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-curl-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-curl -f %{oreon_filedir}/mingw32-curl.list
%files -n mingw32-curl-static -f %{oreon_filedir}/mingw32-curl-static.list
%files -n mingw64-curl -f %{oreon_filedir}/mingw64-curl.list
%files -n mingw64-curl-static -f %{oreon_filedir}/mingw64-curl-static.list

%changelog

%autochangelog
