%global source0_hash 3ea46986821070ed06fef5215b2a83a9076115a865da70874e19f214db2c8d83
%bcond_with     testsuite
Name:           checksec
Version:        3.2.0
Release:        1%{?dist}
Summary:        Tool to check system for binary-hardening
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/slimm609/%{name}.sh
Source0:        https://github.com/slimm609/%{name}.sh/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Fix-compatibility-with-binutils-2.41-on-ppc64le.patch
BuildArch:      noarch
%if %{with testsuite}
%endif
Requires:       binutils
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       which
Requires:       /usr/bin/nm
# oreon:deps
BuildRequires:  /usr/bin/jsonlint
BuildRequires:  binutils
BuildRequires:  file
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  libxml2
BuildRequires:  openssl
BuildRequires:  procps-ng
# /oreon:deps
%description
Modern Linux distributions offer some mitigation techniques to make it harder
to exploit software vulnerabilities reliably. Mitigations such as RELRO,
NoExecute (NX), Stack Canaries, Address Space Layout Randomization (ASLR) and
Position Independent Executables (PIE) have made reliably exploiting any
vulnerabilities that do exist far more challenging. The checksec script is
designed to test what *standard* Linux OS and PaX (http://pax.grsecurity.net/)
security features are being used.

As of version 1.3 the script also lists the status of various Linux kernel
protection mechanisms.

%{name} can check binary-files and running processes for hardening features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p 1

# Fix shebang.
sed -i 's~^#!/usr/bin/env bash~#!/usr/bin/bash~' checksec

# Disable --update command.
sed -i 's/pkg_release=false/pkg_release=true/' checksec

%build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -pm 0755 %{name} %{buildroot}%{_bindir}
install -pm 0644 extras/man/%{name}.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main
%if %{with testsuite}
%check

pushd tests
./xml-checks.sh || exit 2
popd
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
