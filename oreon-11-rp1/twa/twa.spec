%global source0_hash 486a09ea2e9142beb9ce61c058649bab0a4910904396ca3b71f2ba05cd65a2f5

Name:    twa
Version: 1.11.0
Release: 5%{?dist}
Summary: Tiny web auditor with strong opinions
License: MIT

URL:     https://github.com/trailofbits/twa
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: sed

Requires: bash >= 4.0.0
Requires: curl
Requires: gawk
Requires: jq
Requires: nc
Requires: /usr/bin/dig

Recommends: testssl

%description
%{name} is a website auditing tool that can be used to detect
HTTPS issues, missing security headers, information-leaking headers,
and other potential security headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Fix shebang
sed -e 's|^#!/usr/bin/env bash$|#!%{_bindir}/bash|' -i twa

# Remove the bash version check
sed -e '/Expected GNU Bash 4.0 or later/d' -i twa

# Remove the "ensure dependency is installed" checks
sed -e '/^ensure installed .*/d' -i twa

%build
# Nothing to do here - this is a shell script

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -p twa    %{buildroot}%{_bindir}/
install -m 755 -p tscore %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p twa.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md
%{_bindir}/twa
%{_bindir}/tscore
%{_mandir}/man1/twa.*

%changelog
%autochangelog
