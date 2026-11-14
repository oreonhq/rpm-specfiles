# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c1012c8871d71b65872fd5ff1a9d6b0838a55683a03e85ba97479ce57129c736

%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
Name:           libfido2

Version:        1.17.0
Release:        1%{?dist}
Summary:        FIDO2 library

License:        BSD-2-Clause
URL:            https://github.com/Yubico/%{name}
Source0:        https://developers.yubico.com/libfido2/Releases/libfido2-%{version}.tar.gz
Source1:        libfido2-1.17.0.tar.gz.sig
#
# Yubico does not provide a central gpg keyring download file. Instead, they
# provide a list of individuals that release code and their fingerprints at
#   https://developers.yubico.com/Software_Projects/Software_Signing.html
#
# One must import all the keys and then export into the keyfile.
#   gpg2 --homedir /tmp/ --receive-keys "keyid0"
#   gpg2 --homedir /tmp/ --receive-keys "keyid1"
#   gpg2 --homedir /tmp/ --export --armor --output yubico-release-gpgkeys.asc
#
# or using the equivalent Sequoia CLI:
#
#   sq network keyserver search "keyid0" --output keyid0.pgp
#   sq network keyserver search "keyid1" --output keyid1.pgp
#   (and combine all the pgp kets into yubico-release-gpgkeys.asc)
#
Source2:        yubico-release-gpgkeys.asc

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcbor)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  oreon-rpm-macros

%description
%{name} is an open source library to support the FIDO2 protocol.  FIDO2 is
an open authentication standard that consists of the W3C Web Authentication
specification (WebAuthn API), and the Client to Authentication Protocol
(CTAP).  CTAP is an application layer protocol used for communication
between a client (browser) or a platform (operating system) with an external
authentication device (for example the Yubico Security Key).

################################################################################

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel contains development libraries and header files for %{name}.

################################################################################

%package -n fido2-tools

Summary:        FIDO2 tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n fido2-tools
FIDO2 command line tools to access and configure a FIDO2 compliant
authentication device.

################################################################################


%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1 -n %{name}-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install
# Remove static files per packaging guidelines
find %{buildroot} -type f -name "*.a" -delete -print


%check
%ctest \-E regress_cred


%files
%doc NEWS README.adoc
%license LICENSE
%{_libdir}/libfido2.so.1{,.*}

%files devel
%{_libdir}/pkgconfig/libfido2.pc
%{_libdir}/libfido2.so
%{_includedir}/fido.h
%{_includedir}/fido
%{_mandir}/man3/fido_*.3{,.*}
%{_mandir}/man3/eddsa_pk_*.3{,.*}
%{_mandir}/man3/es256_pk_*.3{,.*}
%{_mandir}/man3/es384_pk_*.3{,.*}
%{_mandir}/man3/rs256_pk_*.3{,.*}

%files -n fido2-tools
%{_bindir}/fido2-assert
%{_bindir}/fido2-cred
%{_bindir}/fido2-token
%{_mandir}/man1/fido2-assert.1{,.*}
%{_mandir}/man1/fido2-cred.1{,.*}
%{_mandir}/man1/fido2-token.1{,.*}


