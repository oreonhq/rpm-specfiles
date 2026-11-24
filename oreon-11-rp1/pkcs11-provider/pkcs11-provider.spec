# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b8bbc30cfb7865603fff1dd0fb516cce90437d8ddb267e331cd89d6121960538
%global source1_hash 394f5912e2971bdf92c41904b7c085da1056d963fdb7b720909d55bf76dc648c
%global source2_hash a88480961f4aa0ff5b0b7b84bd3c0b9564140f4fc012b5e27ff87428dbc82a21
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond gpgcheck 1

Name:          pkcs11-provider
Version:       1.3.0
Release:       1%{?dist}
Summary:       A PKCS#11 provider for OpenSSL 3.0+
License:       Apache-2.0
URL:           https://github.com/latchset/pkcs11-provider
Source0:        https://github.com/latchset/pkcs11-provider/releases/download/v%{version}/%{name}-%{version}.tar.xz
%if %{with gpgcheck}
Source1:        https://github.com/latchset/pkcs11-provider/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:       simo_redhat.asc
%endif
Source3:       pkcs11-provider.conf

BuildRequires: oreon-rpm-macros
BuildRequires: openssl-devel >= 3.0.7
BuildRequires: clang
BuildRequires: meson
%if %{with gpgcheck}
BuildRequires: gnupg2
%endif

BuildRequires: nss-devel
BuildRequires: nss-softokn
BuildRequires: nss-softokn-devel
BuildRequires: nss-tools
BuildRequires: openssl
BuildRequires: softhsm
BuildRequires: opensc
BuildRequires: p11-kit-devel
BuildRequires: gnutls-utils
BuildRequires: xz
BuildRequires: expect
BuildRequires: xxd

%description
This is an Openssl 3.x provider to access Hardware or Software Tokens using
the PKCS#11 Cryptographic Token Interface.
This code targets version 3.0 of the interface but should be backwards
compatible to previous versions as well.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%if %{with gpgcheck}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/openssl.d
install -m644 '%{SOURCE3}' \
        $RPM_BUILD_ROOT/%{_sysconfdir}/pki/tls/openssl.d/pkcs11-provider.conf

%check
%meson_test --num-processes 1 --timeout-multiplier 4

%files
%license COPYING
%{_mandir}/man7/provider-pkcs11.*
%doc README.md
%{_libdir}/ossl-modules/pkcs11.so
%config(noreplace) %{_sysconfdir}/pki/tls/openssl.d/pkcs11-provider.conf

%changelog
%autochangelog
