%global source2_hash 6d9d82dc540fae86070db378668e7fd216a2cc978670a0450c35940b1e1484b6
%global source1_hash 22284bcdb8952303cd67c93ec28c50fc92adfdbb01ed4a7e3cd1477e9cc6f530
%global source0_hash 7ea5a75bfcdf04bbb6ef88d03f89dec8101a2d3ea1dd467d8c42cbb0339ed5cb
Summary:        Client for signing certificates with an ACME server
Name: dehydrated
Version: 0.7.2
Release:        1%{?dist}
License: MIT
URL: https://github.com/dehydrated-io/dehydrated
Source0:        https://github.com/dehydrated-io/dehydrated/releases/download/v%{version}/dehydrated-%{version}.tar.gz
Source1: https://github.com/dehydrated-io/dehydrated/releases/download/v%{version}/dehydrated-%{version}.tar.gz.asc
Source2: https://keys.openpgp.org/vks/v1/by-fingerprint/3C2F2605E078A1E18F4793909C4DBE6CF438F333
Source3: dehydrated.tmpfiles
Source4: dehydrated.timer
Source5: dehydrated.service
Source6: 50-dehydrated.preset
Source7: dehydrated-cron
Patch0: dehydrated-autowash.patch
Patch1: dehydrated-improve-trap-handling.patch
Patch2: dehydrated-hook.sh-defaults.patch
BuildArch: noarch
%{?systemd_requires}
Requires: coreutils
Requires: curl
Requires: diffutils
Requires: gawk
Requires: grep
Requires: (/usr/bin/mailx or /bin/mailx)
Requires: openssl
Requires: sed
Requires: util-linux
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This is a client for signing certificates with an ACME-server (currently
only provided by Let's Encrypt) implemented as a relatively simple bash-
script. Dehydrated supports both ACME v1 and the new ACME v2 including
support for wildcard certificates!

Current features:
- Signing of a list of domains (including wildcard domains!)
- Signing of a custom CSR (either standalone or completely automated using
  hooks!)
- Renewal if a certificate is about to expire or defined set of domains changed
- Certificate revocation

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .autowash
%patch -P1 -p1 -b .improve-trap-handling
%patch -P2 -p1

%build

: nothing to do
%install
mkdir -p %{buildroot}%{_rundir}/dehydrated
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/accounts
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/archive
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/certs
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/domains.txt.d
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/hook.d
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/dehydrated.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/dehydrated.timer
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/dehydrated.service
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_presetdir}/50-dehydrated.preset
install -D -p -m 0755 %{SOURCE7} %{buildroot}%{_libexecdir}/dehydrated-cron
sed \
    -e 's|^#LOCKFILE="\${BASEDIR}/lock"|LOCKFILE="%{_rundir}/dehydrated/lock"|' \
    -e 's|^#CONFIG_D=|CONFIG_D="\${BASEDIR}/conf.d"|' \
    -e 's|^#HOOK=|HOOK="\${BASEDIR}/hook.sh"|' \
    -e 's|^#PRIVATE_KEY_RENEW="yes"|PRIVATE_KEY_RENEW="no"|' \
    -e 's|^#AUTO_CLEANUP="no"|AUTO_CLEANUP="yes"|' \
    -e 's|^#KEY_ALGO=secp384r1|KEY_ALGO=rsa|' \
    docs/examples/config >%{buildroot}%{_sysconfdir}/dehydrated/config
touch --reference=docs/examples/config \
    %{buildroot}%{_sysconfdir}/dehydrated/config
sed -i.orig -e 's|^\#!/usr/bin/env bash|#!/bin/bash|' \
    docs/examples/hook.sh
touch --reference=docs/examples/hook.sh.orig \
    docs/examples/hook.sh && rm docs/examples/hook.sh.orig
install -p docs/examples/hook.sh %{buildroot}%{_sysconfdir}/dehydrated/hook.sh
sed -i.orig -e 's|^\#!/usr/bin/env bash|#!/bin/bash|' \
    dehydrated
touch --reference=dehydrated.orig dehydrated && \
    rm dehydrated.orig
install -D -p -m 0755 dehydrated %{buildroot}%{_bindir}/dehydrated
install -D -p -m 0644 docs/man/dehydrated.1 \
    %{buildroot}%{_mandir}/man1/dehydrated.1
rm -rf docs/man/
chmod a-x docs/examples/hook.sh
%oreon_autofiles main

%post

%systemd_post dehydrated.timer dehydrated.service
if [ $1 -eq 1 ]; then
    systemctl start dehydrated.timer >/dev/null 2>&1 || :
fi
umask=$(umask)
umask 027
if [ -z "$(ls -1 %{_sysconfdir}/dehydrated/conf.d/*.sh 2>/dev/null)" ]; then
    touch %{_sysconfdir}/dehydrated/conf.d/local.sh
fi
if [ ! -e %{_sysconfdir}/dehydrated/domains.txt ]; then
    touch %{_sysconfdir}/dehydrated/domains.txt
fi
umask ${umask} || :
%preun

%systemd_preun dehydrated.timer dehydrated.service
%postun

%systemd_postun_with_restart dehydrated.timer
%systemd_postun dehydrated.service
%triggerun -- dehydrated <= 0.7.0-2

systemctl preset dehydrated.timer dehydrated.service >/dev/null 2>&1 || :
systemctl start dehydrated.timer >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
