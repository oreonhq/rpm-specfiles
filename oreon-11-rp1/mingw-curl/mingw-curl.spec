%global source0_hash 40df79166e74aa20149365e11ee4c798a46ad57c34e4f68fd13100e2c9a91946

%{?mingw_package_header}

Name:           mingw-curl
Version:        8.18.0
Release:        2%{?dist}
Summary:        MinGW Windows port of curl and libcurl

License:        MIT
URL:            https://curl.haxx.se/
Source0:        https://curl.haxx.se/download/curl-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-libidn2
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw32-libssh2
BuildRequires:  mingw32-openssl

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-libidn2
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw64-libssh2
BuildRequires:  mingw64-openssl

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

%autosetup -p1 -n curl-%{version}

%build
MINGW32_CONFIGURE_ARGS="--with-ca-bundle=%{mingw32_sysconfdir}/pki/tls/certs/ca-bundle.crt"
MINGW64_CONFIGURE_ARGS="--with-ca-bundle=%{mingw64_sysconfdir}/pki/tls/certs/ca-bundle.crt"
MINGW_CONFIGURE_ARGS="--with-ssl --enable-ipv6 --enable-threaded-resolver --enable-sspi --with-libidn2 --with-libssh2 --without-random"

MINGW_BUILDDIR_SUFFIX=_static %mingw_configure --enable-static --disable-shared
MINGW_BUILDDIR_SUFFIX=_shared %mingw_configure --disable-static --enable-shared

# It's not clear where to set the --with-ca-bundle path.  This is the
# default for CURLOPT_CAINFO.  If this doesn't exist, you'll get an
# error from all https transfers unless the program sets
# CURLOPT_CAINFO to point to the correct ca-bundle.crt file.

# --without-random disables random number collection (eg. from
# /dev/urandom).  There isn't an obvious alternative for Windows:
# Perhaps we can port EGD or use a library such as Yarrow.

# These are the original flags that we'll work towards as
# more of the dependencies get ported to Fedora MinGW.
#
#  --without-ssl --with-nss=%{mingw32_prefix} --enable-ipv6
#  --with-ca-bundle=%{mingw32_sysconfdir}/pki/tls/certs/ca-bundle.crt
#  --with-gssapi=%{mingw32_prefix}/kerberos --with-libidn
#  --enable-ldaps --disable-static --with-libssh2

MINGW_BUILDDIR_SUFFIX=_static %mingw_make_build
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make_build

%install
MINGW_BUILDDIR_SUFFIX=_static %mingw_make DESTDIR=%{buildroot}/static install
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make_install

# The curl-config script is hard coded to the build type. Keep a static copy.
mv %{buildroot}/static%{mingw32_bindir}/curl-config %{buildroot}%{mingw32_bindir}/curl-config-static
mv %{buildroot}/static%{mingw64_bindir}/curl-config %{buildroot}%{mingw64_bindir}/curl-config-static
# The static library from the static build is the only one of interest to us
mv %{buildroot}/static%{mingw32_libdir}/libcurl.a %{buildroot}%{mingw32_libdir}/libcurl.a
mv %{buildroot}/static%{mingw64_libdir}/libcurl.a %{buildroot}%{mingw64_libdir}/libcurl.a
rm -rf %{buildroot}/static

# Remove .la files
find %{buildroot} -name "*.la" -delete

# Remove the man pages which duplicate documentation in the
# native Fedora package.
rm -r %{buildroot}%{mingw32_mandir}/man{1,3}
rm -r %{buildroot}%{mingw64_mandir}/man{1,3}

# Remove redundant autoconf files
rm -rf %{buildroot}%{mingw32_datadir}/aclocal
rm -rf %{buildroot}%{mingw64_datadir}/aclocal

# sh wrapper not useful on windows
rm -f %{buildroot}%{mingw32_bindir}/wcurl
rm -f %{buildroot}%{mingw64_bindir}/wcurl

# Win32
%files -n mingw32-curl
%license COPYING
%{mingw32_bindir}/curl.exe
%{mingw32_bindir}/curl-config
%{mingw32_bindir}/libcurl-4.dll
%{mingw32_libdir}/libcurl.dll.a
%{mingw32_libdir}/pkgconfig/libcurl.pc
%{mingw32_includedir}/curl/

%files -n mingw32-curl-static
%{mingw32_bindir}/curl-config-static
%{mingw32_libdir}/libcurl.a

# Win64
%files -n mingw64-curl
%license COPYING
%{mingw64_bindir}/curl.exe
%{mingw64_bindir}/curl-config
%{mingw64_bindir}/libcurl-4.dll
%{mingw64_libdir}/libcurl.dll.a
%{mingw64_libdir}/pkgconfig/libcurl.pc
%{mingw64_includedir}/curl/

%files -n mingw64-curl-static
%{mingw64_bindir}/curl-config-static
%{mingw64_libdir}/libcurl.a

%changelog
%autochangelog
