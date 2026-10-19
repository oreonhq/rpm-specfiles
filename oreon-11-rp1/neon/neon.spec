%global source0_hash a99b7262525a454d1065cf76dd17240fd808dfc4ef15636990ff83a5d0d9e740
%bcond tests 1
%bcond pkcs11 %[0%{?fedora} < 43 && %{undefined rhel} && %{undefined oreon}]
%bcond libproxy %{undefined rhel}
%global __brp_remove_la_files %nil
Summary:        An HTTP and WebDAV client library
Name: neon
Version: 0.37.1
Release:        1%{?dist}
License: LGPL-2.0-or-later
URL: https://notroj.github.io/neon/
Source0:        https://notroj.github.io/neon/neon-%{version}.tar.gz
Patch0: neon-0.34.0-multilib.patch
%if %{with pkcs11}
%endif
%if %{with libproxy}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  /usr/bin/certutil
BuildRequires:  /usr/bin/openssl
BuildRequires:  /usr/bin/perl
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  libntlm-devel
BuildRequires:  libproxy-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  zlib-devel
# /oreon:deps
%description
neon is an HTTP and WebDAV client library, with a C interface;
providing a high-level interface to HTTP and WebDAV methods along
with a low-level interface for HTTP request handling.  neon
supports persistent connections, proxy servers, Basic, Digest and
Kerberos authentication, and has complete SSL/TLS support.

%package devel
Summary: Development libraries and C header files for the neon library
Requires: neon = %{version}-%{release}, openssl-devel, zlib-devel, expat-devel
Requires: pkgconfig
License: LGPL-2.0-or-later AND GPL-2.0-or-later
%description devel
The development library for the C language HTTP and WebDAV client library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -S gendiff

# prevent installation of HTML docs
sed -i '/^install-docs/s/install-html//' Makefile.in

%build

%configure --with-expat --enable-shared --disable-static \
        --enable-warnings \
        --with-ssl=openssl --enable-threadsafe-ssl=posix \
%ifarch s390x
        --without-libntlm \
%endif
%if %{with libproxy}
        --with-libproxy \
%else
        --without-libproxy \
%endif
%if %{with pkcs11}
        --with-pakchois
%else
        --without-pakchois
%endif
%make_build
%install
rm -rf $RPM_BUILD_ROOT
%make_install
sed -ri "/^dependency_libs/{s,-l[^ ']*,,g}" \
      $RPM_BUILD_ROOT%{_libdir}/libneon.la
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

export TEST_QUIET=0
if make %{?_smp_mflags} check; then
    : PASS
else
    : FAIL
    cat test/child.log || true
    cat test/debug.log || true
    exit 1
fi
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n neon-devel -f %{oreon_filedir}/neon-devel.list

%changelog

%autochangelog
