# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d9ec76cbe34db98eec3539fe2c899d26b0c837cb3eb466a56b0f109cabf658f7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global _preprocessor_defines %{?_preprocessor_defines} -DOPENSSL_NO_ENGINE

Name:		libssh2
Version:        1.11.1
Release:        1%{?dist}
Summary:	A library implementing the SSH2 protocol
License:	BSD-3-Clause
URL:		https://www.libssh2.org/
Source0:        https://libssh2.org/download/libssh2-%{version}.tar.gz
Source1:        libssh2-1.11.1.tar.gz.asc
# Daniel Stenberg's GPG keys; linked from https://daniel.haxx.se/address.html
Source2:        mykey.asc
Patch0:        libssh2-1.11.1-CVE-2026-7598.patch
Patch1:        97acf3dfda80c91c3a8c9f2372546301d4a1a7a8-libssh2-1.11.1.patch
Patch2:        17626857d20b3c9a1addfa45979dadcee1cd84a4.patch
Patch3:        2dae302-libssh2-1.11.1.patch

BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	make
BuildRequires:	openssl-devel > 1:1.0.2
BuildRequires:	pkgconfig
BuildRequires:	sed
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/man

# Test suite requirements
# Full groff (not just groff-base) needed for the mansyntax check
BuildRequires:	groff
# We run the OpenSSH server and try to connect to it
BuildRequires:	openssh-server
# Need a valid locale to run the mansyntax check
BuildRequires:	glibc-langpack-en
BuildRequires:  oreon-rpm-macros

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package	devel
Summary:	Development files for libssh2
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The libssh2-devel package contains libraries and header files for
developing applications that use libssh2.

%package	docs
Summary:	Documentation for libssh2
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	docs
The libssh2-docs package contains man pages and examples for
developing applications that use libssh2.

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%setup -q

# CVE-2026-7598 libssh2: integer overflow via large username or password arguments
# https://github.com/libssh2/libssh2/pull/1858
%patch -P0

# CVE-2026-55200 transport.c: Additional boundary checks for packet length
# Patch modified for downstream
# https://github.com/libssh2/libssh2/pull/2052
%patch -p1 -P1

# CVE-2026-55199 packet.c: check _libssh2_get_string() return in EXT_INFO handler
# https://github.com/libssh2/libssh2/pull/1864
%patch -p1 -P2

# CVE-2025-15661: Information disclosure and denial of service via crafted SFTP response
# https://github.com/libssh2/libssh2/pull/1705
# https://github.com/libssh2/libssh2/pull/1717
%patch -p1 -P3

# Replace hard wired port number in the test suite to avoid collisions
# between 32-bit and 64-bit builds running on a single build-host
sed -i s/4711/47%{?__isa_bits}/ tests/{openssh_fixture.c,test_ssh{2.c,d.test}}

%build
%configure \
	--disable-rpath \
	--disable-silent-rules \
	--disable-static \
	--enable-shared \
	--disable-docker-tests
%{make_build}

%install
%{make_install} INSTALL="install -p"
find %{buildroot} -name '*.la' -delete

# Clean things up a bit for packaging
make -C example clean
find example/ -type f \
	'(' -name '*.am' -o -name '*.in' -o -name CMakeLists.txt ')' \
	-print -delete

# Remove redundant references to libdir in pkg-config file
sed -i	-e 's|-L%{_libdir} ||g' \
	-e 's|-L[$]{libdir} ||g' %{buildroot}%{_libdir}/pkgconfig/libssh2.pc

# Avoid multilib conflict on libssh2-devel
mv -v example example.%{_arch}

%check
LC_ALL=en_US.UTF-8 make -C tests check

%ldconfig_scriptlets

%files
%license COPYING
%doc docs/AUTHORS README RELEASE-NOTES
%{_libdir}/libssh2.so.1
%{_libdir}/libssh2.so.1.*

%files docs
%doc docs/BINDINGS.md docs/HACKING.md docs/TODO NEWS
%{_mandir}/man3/libssh2_*.3*

%files devel
%doc example.%{_arch}/
%{_includedir}/libssh2.h
%{_includedir}/libssh2_publickey.h
%{_includedir}/libssh2_sftp.h
%{_libdir}/libssh2.so
%{_libdir}/pkgconfig/libssh2.pc

