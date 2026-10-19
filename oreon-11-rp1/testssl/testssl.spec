%global source0_hash 98528f8a0ac07f1e226efaa8ead438247df8efcb8fee4e056a937ab82a305490
Name:    testssl
Version: 3.2.4
Release:        1%{?dist}
Summary:        Testing TLS/SSL encryption
License: GPL-2.0-only
URL:     https://testssl.sh/
Source0:        https://github.com/drwetter/testssl.sh/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch
Requires: bash
Requires: bind-utils
Requires: ca-certificates
Requires: coreutils
Requires: gawk
Requires: glibc-common
Requires: grep
Requires: hostname
Requires: ncurses
Requires: openssl >= 1
Requires: procps-ng
Requires: sed
Requires: util-linux
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  sed
# /oreon:deps
%description
testssl.sh is a free command line tool which checks a server's service on any
port for the support of TLS/SSL ciphers, protocols as well as recent
cryptographic flaws and more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}.sh-%{version}
# remove pre-compiled binaries
rm -rf bin/*
sed --in-place '1s#^\#!/usr/bin/env bash$#\#!/bin/bash#' %{name}.sh etc/client-simulation.txt
sed --in-place 's#^TESTSSL_INSTALL_DIR=.*$#TESTSSL_INSTALL_DIR="%{_datadir}/%{name}"#' %{name}.sh
sed --in-place 's#^CA_BUNDLES_PATH=.*$#CA_BUNDLES_PATH="/etc/pki/tls"#' %{name}.sh
sed --in-place '0,/.SH "COPYRIGHT"/s#testssl\\.sh#testssl#g' doc/%{name}.1

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}
for file in ca_hashes.txt cipher-mapping.txt client-simulation.txt common-primes.txt tls_data.txt README.md
do
        install -D --preserve-timestamps --mode=0644 etc/${file} %{buildroot}%{_datadir}/%{name}/etc/${file}
done
install -d %{buildroot}%{_mandir}/man1
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
