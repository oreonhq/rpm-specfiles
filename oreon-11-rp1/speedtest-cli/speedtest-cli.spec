%global source0_hash 45e3ca21c3ce3c339646100de18db8a26a27d240c29f1c9e07b6c13995a969be

Name: speedtest-cli
Version: 2.1.3
Release: 17%{?dist}
Summary: Command line interface for testing internet bandwidth

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0 
URL: https://github.com/sivel/speedtest-cli
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools

BuildArch: noarch

%description
Command line interface for testing internet bandwidth using speedtest.net

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i -e '/^#!\//, 1d' *.py

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 644 speedtest-cli.1 %{buildroot}%{_mandir}/man1/speedtest-cli.1
rm -f %{buildroot}%{_bindir}/speedtest

%files
%doc CONTRIBUTING.md README.rst
%license LICENSE
%exclude %{python3_sitelib}/__pycache__/
%{_bindir}/speedtest-cli
%{python3_sitelib}/speedtest_cli*
%{python3_sitelib}/speedtest.py
%{_mandir}/man1/speedtest-cli.1.*

%changelog
%autochangelog
