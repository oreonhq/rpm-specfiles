# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8e7438ccd6b3a2ab05182d0846e112a56a7f557ecdee40de07bf67820008bef7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           stunnel
Version:        5.82
Release:        1%{?dist}
Summary:        TLS offloading and load-balancing proxy
License:        GPL-2.0-or-later WITH stunnel-exception
URL:            https://www.stunnel.org/
Source0:        https://www.stunnel.org/downloads/stunnel-%{version}.tar.gz
Source1:        stunnel-%{version}.tar.gz.asc
Source2:        gpgkey-2BC7E4E67E3CC0C1BEA72F8C2EFC7FF0D416E014.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  openssl-devel

%description
stunnel is a TLS offloading and load-balancing proxy. It can be used to add
TLS encryption to existing clients and servers without code changes.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup

%build
%configure --enable-ipv6
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
mkdir -p %{buildroot}%{_sysconfdir}/stunnel

%check
make check

%files
%license COPYING.md COPYRIGHT.md
%doc AUTHORS.md NEWS.md README.md tools/stunnel.conf-sample
%{_bindir}/stunnel
%{_bindir}/stunnel3
%{_libdir}/stunnel/
%{_mandir}/man8/stunnel.8*
%dir %{_sysconfdir}/stunnel

%changelog
%autochangelog
