%global source0_hash a5a00362f62eaeb761c54de5bea4a109a7b2fdcd24247868aed39eddcc57a852

Name: ServiceReport
Version: 2.2.4
Release: 10%{?dist}
Summary: A tool to validate and repair First Failure Data Capture (FFDC) configuration

License: GPL-2.0-or-later
URL: https://github.com/linux-ras/ServiceReport
Source0: https://github.com/linux-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel python3-setuptools
BuildRequires: systemd-rpm-macros

%description
ServiceReport is a python based tool that investigates the incorrect
First Failure Data Capture (FFDC) configuration and optionally repairs
the incorrect configuration

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%py3_build

%install
%py3_install

%post
%systemd_post servicereport.service

%preun
%systemd_preun servicereport.service

%postun
%systemd_postun servicereport.service

%files
%doc README.md
%license COPYING
%{_mandir}/man8/*
%{_bindir}/servicereport
%{_unitdir}/servicereport.service
%{python3_sitelib}/servicereportpkg
%{python3_sitelib}/ServiceReport*.egg-info

%changelog
%autochangelog
