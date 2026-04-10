# OpenSSL ENGINE support
# This is deprecated by OpenSSL since OpenSSL 3.0 and by Fedora since Fedora 41
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
# Change the bcond to 0 to turn off ENGINE support by default
%bcond openssl_engine_support %[%{defined fedora} || 0%{?rhel} < 10]

# HTTP/3 support
# This is using ngtcp2 with OpenSSL 3.5 QUIC support instead of curl's
# experimental native OpenSSL 3.5 support.
%bcond http3 %[0%{?fedora} >= 43]

Summary: A utility for getting files from remote servers (FTP, HTTP, and others)
Name: curl
Version: 8.19.0
%global version_no_tilde %(echo %{version} | sed 's/~/-/g')
Release: 2%{?dist}
License: curl
Source0: https://curl.se/download/%{name}-%{version_no_tilde}.tar.xz
Source1: https://curl.se/download/%{name}-%{version_no_tilde}.tar.xz.asc
# The curl download page ( https://curl.se/download.html ) links
# to Daniel's address page https://daniel.haxx.se/address.html for the GPG Key,
# which points to the GPG key as of April 7th 2016 of https://daniel.haxx.se/mykey.asc
Source2: mykey.asc

# patch making libcurl multilib ready
Patch101: 0101-curl-7.32.0-multilib.patch

Provides: curl-full = %{version}-%{release}
# do not fail when trying to install curl-minimal after drop
Provides: curl-minimal = %{version}-%{release}
Provides: webclient
URL: https://curl.se/

%if 0%{?fedora}
# instead of bundled wcurl utility, recommend wcurl package
Recommends: wcurl
%endif

# The reason for maintaining two separate packages for curl is no longer valid.
# The curl-minimal is currently almost identical to curl-full, so let's drop curl-minimal.
# For more details, see https://bugzilla.redhat.com/show_bug.cgi?id=2262096
Obsoletes: curl-minimal < 8.6.0-4

BuildRequires: automake
BuildRequires: brotli-devel
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: groff
BuildRequires: krb5-devel
BuildRequires: libidn2-devel
BuildRequires: libnghttp2-devel
%if %{with http3}
BuildRequires: libnghttp3-devel
%endif
BuildRequires: libpsl-devel
BuildRequires: libssh-devel
BuildRequires: libtool
BuildRequires: make
%if %{with http3}
BuildRequires: ngtcp2-crypto-ossl-devel
%endif
BuildRequires: openldap-devel
BuildRequires: openssh-clients
BuildRequires: openssh-server
BuildRequires: openssl
BuildRequires: openssl-devel
%if %{with openssl_engine_support} && 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
BuildRequires: perl-interpreter
BuildRequires: pkgconfig
BuildRequires: python-unversioned-command
BuildRequires: python3-devel
BuildRequires: sed
BuildRequires: zlib-devel

# For gpg verification of source tarball
BuildRequires: gnupg2

# needed to compress content of tool_hugehelp.c after changing curl.1 man page
BuildRequires: perl(IO::Compress::Gzip)

# needed for generation of shell completions
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

# needed for test1560 to succeed
BuildRequires: glibc-langpack-en

# gnutls-serv is used by the upstream test-suite
BuildRequires: gnutls-utils

# hostname(1) is used by the test-suite but it is missing in armv7hl buildroot
BuildRequires: hostname

# nghttpx (an HTTP/2 proxy) is used by the upstream test-suite
BuildRequires: nghttp2

# perl modules used in the test suite
BuildRequires: perl(B)
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildRequires: perl(Cwd)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Spec)
BuildRequires: perl(I18N::Langinfo)
BuildRequires: perl(IPC::Open2)
BuildRequires: perl(List::Util)
BuildRequires: perl(Memoize)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(POSIX)
BuildRequires: perl(Storable)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Time::Local)
BuildRequires: perl(vars)

%if 0%{?fedora}
# needed for upstream test 1451
BuildRequires: python3-impacket
%endif

# The test-suite runs automatically through valgrind if valgrind is available
# on the system.  By not installing valgrind into mock's chroot, we disable
# this feature for production builds on architectures where valgrind is known
# to be less reliable, in order to avoid unnecessary build failures (see RHBZ
# #810992, #816175, and #886891).  Nevertheless developers are free to install
# valgrind manually to improve test coverage on any architecture.
%ifarch x86_64
BuildRequires: valgrind
%endif

# stunnel is used by upstream tests but it does not seem to work reliably
# on aarch64/s390x and occasionally breaks some tests (mainly 1561 and 1562)
%ifnarch aarch64 s390x
BuildRequires: stunnel
%endif

# using an older version of libcurl could result in CURLE_UNKNOWN_OPTION
Requires: libcurl%{?_isa} >= %{version}-%{release}

# Define OPENSSL_NO_ENGINE to avoid inclusion of <openssl/engine.h>
%if %{without openssl_engine_support}
%global _preprocessor_defines %{?_preprocessor_defines} -DOPENSSL_NO_ENGINE
%endif

# require at least the version of libnghttp2 that we were built against,
# to ensure that we have the necessary symbols available (#2144277)
%global libnghttp2_version %(pkg-config --modversion libnghttp2 2>/dev/null || echo 0)

# require at least the version of libnghttp3 that we were built against,
# to ensure that we have the necessary symbols available
%global libnghttp3_version %(pkg-config --modversion libnghttp3 2>/dev/null || echo 0)

# require at least the version of libpsl that we were built against,
# to ensure that we have the necessary symbols available (#1631804)
%global libpsl_version %(pkg-config --modversion libpsl 2>/dev/null || echo 0)

# require at least the version of libssh that we were built against,
# to ensure that we have the necessary symbols available (#525002, #642796)
%global libssh_version %(pkg-config --modversion libssh 2>/dev/null || echo 0)

# require at least the version of ngtcp2 that we were built against,
# to ensure that we have the necessary symbols available
%global ngtcp2_version %(pkg-config --modversion libngtcp2 2>/dev/null || echo 0)

# require at least the version of openssl-libs that we were built against,
# to ensure that we have the necessary symbols available (#1462184, #1462211)
# (we need to translate 3.0.0-alpha16 -> 3.0.0-0.alpha16 and 3.0.0-beta1 -> 3.0.0-0.beta1 though)
%global openssl_version %({ pkg-config --modversion openssl 2>/dev/null || echo 0;} | sed 's|-|-0.|')

%description
curl is a command line tool for transferring data with URL syntax, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP.  curl supports SSL certificates, HTTP POST, HTTP PUT, FTP
uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, kerberos...), file transfer
resume, proxy tunneling and a busload of other useful tricks. 

%package -n libcurl
Summary: A library for getting files from web servers
Requires: libnghttp2%{?_isa} >= %{libnghttp2_version}
%if %{with http3}
Requires: libnghttp3%{?_isa} >= %{libnghttp3_version}
%endif
Requires: libpsl%{?_isa} >= %{libpsl_version}
Requires: libssh%{?_isa} >= %{libssh_version}
%if %{with http3}
Requires: ngtcp2%{?_isa} >= %{ngtcp2_version}
%endif
Requires: openssl-libs%{?_isa} >= 1:%{openssl_version}
Provides: libcurl-full = %{version}-%{release}
Provides: libcurl-full%{?_isa} = %{version}-%{release}

%description -n libcurl
libcurl is a free and easy-to-use client-side URL transfer library, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT,
FTP uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer
resume, http proxy tunneling and more.

%package -n libcurl-devel
Summary: Files needed for building applications with libcurl
Requires: libcurl%{?_isa} = %{version}-%{release}

Provides: curl-devel = %{version}-%{release}
Provides: curl-devel%{?_isa} = %{version}-%{release}
Obsoletes: curl-devel < %{version}-%{release}

%description -n libcurl-devel
The libcurl-devel package includes header files and libraries necessary for
developing programs which use the libcurl library. It contains the API
documentation of the library, too.

%package -n libcurl-minimal
Summary: Conservatively configured build of libcurl for minimal installations
Requires: libnghttp2%{?_isa} >= %{libnghttp2_version}
Requires: openssl-libs%{?_isa} >= 1:%{openssl_version}
Provides: libcurl = %{version}-%{release}
Provides: libcurl%{?_isa} = %{version}-%{release}
Conflicts: libcurl%{?_isa}
RemovePathPostfixes: .minimal
# needed for RemovePathPostfixes to work with shared libraries
%undefine __brp_ldconfig

%description -n libcurl-minimal
This is a replacement of the 'libcurl' package for minimal installations.  It
comes with a limited set of features compared to the 'libcurl' package.  On the
other hand, the package is smaller and requires fewer run-time dependencies to
be installed.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version_no_tilde} -p1

# disable test 1801
# <https://github.com/bagder/curl/commit/21e82bd6#commitcomment-12226582>
printf "1801\n" >>tests/data/DISABLED

# test3026: avoid pthread_create() failure due to resource exhaustion on i386
%ifarch %{ix86}
sed -e 's|NUM_THREADS 1000$|NUM_THREADS 256|' \
    -i tests/libtest/lib3026.c
%endif

# adapt test 323 for updated OpenSSL
sed -e 's|^35$|35,52|' -i tests/data/test323

# use localhost6 instead of ip6-localhost in the curl test-suite
(
    # avoid glob expansion in the trace output of `bash -x`
    { set +x; } 2>/dev/null
    cmd="sed -e 's|ip6-localhost|localhost6|' -i tests/data/test[0-9]*"
    printf "+ %s\n" "$cmd" >&2
    eval "$cmd"
)

# avoid unnecessary arch-dependent line in the processed file
sed -e '/# Used in @libdir@/d' \
    -i curl-config.in

%build
# regenerate the configure script and Makefile.in files
autoreconf -fiv

mkdir build-{full,minimal}
export common_configure_opts="          \
    --cache-file=../config.cache        \
    --disable-manual                    \
    --disable-static                    \
    --enable-hsts                       \
    --enable-ipv6                       \
    --enable-symbol-hiding              \
    --enable-threaded-resolver          \
    --without-zstd                      \
    --with-gssapi                       \
    --with-libidn2                      \
    --with-nghttp2                      \
    --with-ssl --with-ca-bundle=%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
    --with-zsh-functions-dir"

%global _configure ../configure

# configure minimal build
(
    cd build-minimal
    %configure $common_configure_opts   \
        --disable-dict                  \
        --disable-gopher                \
        --disable-imap                  \
        --disable-ldap                  \
        --disable-ldaps                 \
        --disable-mqtt                  \
        --disable-ntlm                  \
        --disable-pop3                  \
        --disable-rtsp                  \
        --disable-smb                   \
        --disable-smtp                  \
        --disable-telnet                \
        --disable-tftp                  \
        --disable-tls-srp               \
        --disable-websockets            \
        --without-brotli                \
        --without-libpsl                \
        --without-libssh
)

# configure full build
(
    cd build-full
    %configure $common_configure_opts   \
        --enable-dict                   \
        --enable-gopher                 \
        --enable-imap                   \
        --enable-ldap                   \
        --enable-ldaps                  \
        --enable-mqtt                   \
        --enable-ntlm                   \
        --enable-pop3                   \
        --enable-rtsp                   \
        --enable-smb                    \
        --enable-smtp                   \
        --enable-telnet                 \
        --enable-tftp                   \
        --enable-tls-srp                \
        --enable-websockets             \
        --with-brotli                   \
        --with-libpsl                   \
        --with-libssh                   \
%if %{with http3}
        --with-nghttp3                  \
        --with-ngtcp2                   \
%endif
)

# avoid using rpath
sed -e 's/^runpath_var=.*/runpath_var=/' \
    -e 's/^hardcode_libdir_flag_spec=".*"$/hardcode_libdir_flag_spec=""/' \
    -i build-{full,minimal}/libtool

%make_build V=1 -C build-minimal
%make_build V=1 -C build-full

%check
# compile upstream test-cases
%make_build V=1 -C build-minimal/tests
%make_build V=1 -C build-full/tests

# relax crypto policy for the test-suite to make it pass again (#1610888)
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=XXX
export OPENSSL_CONF=

# make runtests.pl work for out-of-tree builds
export srcdir=../../tests

# prevent valgrind from being extremely slow (#1662656)
# https://fedoraproject.org/wiki/Changes/DebuginfodByDefault
unset DEBUGINFOD_URLS

# run the upstream test-suite for both curl-minimal and curl-full
for size in minimal full; do (
    cd build-${size}

    # we have to override LD_LIBRARY_PATH because we eliminated rpath
    export LD_LIBRARY_PATH="${PWD}/lib/.libs"

    cd tests
    perl -I../../tests ../../tests/runtests.pl -a -p -v '!flaky'
)
done


%install
# install and rename the library that will be packaged as libcurl-minimal
%make_install -C build-minimal/lib
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libcurl.{la,so}
for i in ${RPM_BUILD_ROOT}%{_libdir}/*; do
    mv -v $i $i.minimal
done

# install libcurl.m4
install -d $RPM_BUILD_ROOT%{_datadir}/aclocal
install -m 644 docs/libcurl/libcurl.m4 $RPM_BUILD_ROOT%{_datadir}/aclocal

# install the executable and library that will be packaged as curl and libcurl
cd build-full
%make_install

# do not install /usr/share/fish/completions/curl.fish which is also installed
# by fish-3.0.2-1.module_f31+3716+57207597 and would trigger a conflict
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/fish

rm -f ${RPM_BUILD_ROOT}%{_libdir}/libcurl.la

# do not install bundled wcurl utility
# it is provided by the wcurl package
rm -f ${RPM_BUILD_ROOT}%{_bindir}/wcurl
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/wcurl.1*

%ldconfig_scriptlets -n libcurl

%ldconfig_scriptlets -n libcurl-minimal

%files
%doc CHANGES.md
%doc README
%doc docs/BUGS.md
%doc docs/DISTROS.md
%doc docs/FAQ.md
%doc docs/FEATURES.md
%doc docs/KNOWN_BUGS.md
%doc docs/TODO.md
%doc docs/TheArtOfHttpScripting.md
%{_bindir}/curl
%{_mandir}/man1/curl.1*
%{_datadir}/zsh

%files -n libcurl
%license COPYING
%{_libdir}/libcurl.so.4
%{_libdir}/libcurl.so.4.[0-9].[0-9]

%files -n libcurl-devel
%doc docs/examples/*.c docs/examples/Makefile.example docs/INTERNALS.md
%doc docs/CONTRIBUTE.md docs/libcurl/ABI.md
%{_bindir}/curl-config*
%{_includedir}/curl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/curl-config.1*
%{_mandir}/man3/*
%{_datadir}/aclocal/libcurl.m4

%files -n libcurl-minimal
%license COPYING
%{_libdir}/libcurl.so.4.minimal
%{_libdir}/libcurl.so.4.[0-9].[0-9].minimal

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.19.0-2
- 8.19.0 stable tarballs on curl.se (RC snapshots 404 there)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.19.0~rc3-1
- Prepare for Oreon 11 (RP1)
