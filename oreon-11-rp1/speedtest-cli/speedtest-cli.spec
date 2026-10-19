%global source0_hash 45e3ca21c3ce3c339646100de18db8a26a27d240c29f1c9e07b6c13995a969be
Name: speedtest-cli
Version: 2.1.3
Release:        1%{?dist}
Summary:        Command line interface for testing internet bandwidth
License: Apache-2.0 
URL: https://github.com/sivel/speedtest-cli
Source0:        https://github.com/sivel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
