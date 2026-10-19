%global source6_hash 1befb643fe95138d7301eddecd15794680f41787ccced9a6334983693df64aa6
%global source5_hash ed27588d9777582f21cac05da9b4c64c8eaa733ae29b01a1a46ba2ff322094db
%global source4_hash eecb45f6b6bfa19f5bab3179997e0498653a5eafca1e36f1257cc3015d6b32af
%global source0_hash b874af8a67b7c85b9b7a4c3c979bf741c0e7c548df2127005ac8755b4ba7ae46
%global forgeurl https://github.com/pemensik/get-trust-anchor
%global gitcommit e68840988f15155a0be80ae5c36c33a79862ce42
%global upload_sources %{SOURCE0} %{SOURCE3} %{SOURCE5}
Name:           dns-root-data
Version:        2026260100
Release:        1%{?dist}
Summary:        DNS root hints and DNSSEC trust anchor
License:        BSD-2-Clause and CC0-1.0
URL:            https://data.iana.org/root-anchors/
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{gitcommit}/%{name}-%{version}.tar.gz
Source1:        %{url}/icannbundle.pem
Source2:        %{url}/root-anchors.xml
Source3:        %{url}/root-anchors.p7s
Source4:        https://www.internic.net/domain/named.root
Source5:        https://www.internic.net/domain/named.root.sig
Source6:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf0cb1a326bdf3f3efa3a01fa937bb869e3a238c5#/registry-admin.key
BuildArch:      noarch
# oreon:deps
BuildRequires:  bind-dnssec-utils
BuildRequires:  gnupg2
BuildRequires:  gnupg2-verify
BuildRequires:  openssl
BuildRequires:  python3
BuildRequires:  python3-dns
BuildRequires:  sed
# /oreon:deps
%description
This package contains various root zone related data as published
by IANA to be used by various DNS software as a common source
of DNS root zone data, namely:
 * Root Hints (root.hints)
 * Root Trust Anchors (root.key, root.ds)

%package utils
Summary:        Tool for fetching and verifying DNSSEC trust anchor
Requires:       %{name} = %{version}-%{release}
Requires:       python3
Requires:       python3-dns
Requires:       openssl
BuildArch:      noarch
%description utils
Python trust anchor verification and fetching tool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n get-trust-anchor-%{gitcommit} -p1

_gpgvdir=$(mktemp -d)
gpg2 --homedir="$_gpgvdir" --yes --output "$_gpgvdir/ring.gpg" --dearmor '%{SOURCE6}'
gpgv2 --homedir="$_gpgvdir" --keyring="$_gpgvdir/ring.gpg" '%{SOURCE5}' '%{SOURCE4}'
rm -rf "$_gpgvdir"
openssl smime -verify -CAfile %{SOURCE1} -inform DER -in %{SOURCE3} -content %{SOURCE2} -out /dev/null

%build

sed -e "1 s,^#\!/usr/bin/env python,#\!%{_bindir}/python3," -i get_trust_anchor.py
python3 ./get_trust_anchor.py --root-ca=%{SOURCE1} --local=%{SOURCE2} --local-sig=%{SOURCE3} --ksks-from-trust-anchor
touch -r %{SOURCE2} ksk-as-ds.txt
touch -r %{SOURCE2} ksk-as-dnskey.txt
%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/icannbundle.pem
install -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/root-anchors.xml
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/root-anchors.p7s
install -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/root.hints
install -p -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/%{name}/root.hints.sig
install -p -m 0644 ksk-as-ds.txt %{buildroot}%{_datadir}/%{name}/root.ds
install -p -m 0644 ksk-as-dnskey.txt %{buildroot}%{_datadir}/%{name}/root.key
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 get_trust_anchor.py %{buildroot}%{_bindir}/get_dnssec_trust_anchor
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

openssl smime -verify -CAfile %{buildroot}%{_datadir}/%{name}/icannbundle.pem \
              -inform DER -in %{buildroot}%{_datadir}/%{name}/root-anchors.p7s \
              -content %{buildroot}%{_datadir}/%{name}/root-anchors.xml
dnssec-importkey %{buildroot}%{_datadir}/%{name}/root.key
grep -w DS %{buildroot}%{_datadir}/%{name}/root.ds
grep -w DNSKEY %{buildroot}%{_datadir}/%{name}/root.key
%files -f %{oreon_filedir}/main.list
%files -n dns-root-data-utils -f %{oreon_filedir}/dns-root-data-utils.list

%changelog

* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2026260100-1
- Import for Oreon 11
