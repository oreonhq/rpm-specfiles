%global source0_hash none

Name:           lbd
Version:        0.4
Release:        22%{?dist}
Summary:        A DNS/HTTP load balancing detector

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/craig/ge.mine.nu/tree/master/lbd
Source0:        https://raw.githubusercontent.com/craig/ge.mine.nu/master/lbd/%{name}.sh#/%{name}
BuildArch:      noarch

Requires:       bind-utils
Requires:       nc

%description
lbd (load balancing detector) detects if a given domain uses DNS and/or HTTP 
Load-Balancing (via Server: and Date: header and diffs between server answers).

%prep
# Nothing to prep

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/

%files
%{_bindir}/lbd

%changelog
%autochangelog
