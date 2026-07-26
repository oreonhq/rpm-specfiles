%global source0_hash 67593491a64b7dd93e8e8b58ec24863f0e51327177b81efa513ad04b8e5b1a49

Name: dnstwist
Summary: Domain name permutation engine
License: Apache-2.0

Version: 20250130
Release: 4%{?dist}

URL:     https://github.com/elceef/%{name}/
Source0: %{url}archive/%{version}/%{name}-%{version}.tar.gz

# Remove all "are we on MS Windows?" checks
Patch0: 0000--no-win32-check.patch
# Remove all "is this Python import present?" checks
Patch1: 0001--modules-always-present.patch

%global geolite_version 2016.09

BuildRequires: GeoIP-GeoLite-data >= %{geolite_version}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildArch: noarch

Requires: GeoIP-GeoLite-data >= %{geolite_version}
Requires: python3dist(dnspython) >= 1.16.0
Requires: python3dist(geoip) >= 1.3.2
Requires: python3dist(geoip2) >= 4.0.0
Requires: python3dist(idna) >= 2.8
Requires: python3dist(ssdeep) >= 3.1
Requires: python3dist(tld) >= 0.9.1
Requires: python3dist(tlsh) >= 4.5

Requires: ((python3dist(pillow) >= 7.0.0-0) if chromedriver)
Requires: ((python3dist(selenium) >= 4.0.0-0) if chromedriver)

%{?python_enable_dependency_generator}

%description
See what sort of trouble users can get in trying to type your domain name.
Find similar-looking domains that adversaries can use to attack you.
Detect typosquatters, phishing attacks, fraud and corporate espionage.
Useful as an additional source of targeted threat intelligence.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
GEOIP_PATH="$(find %{_datadir}/GeoIP -name GeoLite2-Country.mmdb)"
sed -e "s|__GEOIP__COUNTRY__PATH__|'${GEOIP_PATH}'|g" -i dnstwist.py

%build
# Nothing to do here

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -p %{name}.py  %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a dictionaries/ %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 -p docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc docs/README.md docs/THANKS.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
