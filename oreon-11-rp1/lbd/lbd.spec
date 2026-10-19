%global source0_hash b1aa78bb7fcff006b76a8f1072cb34489ee876d1b14f8a99180db123a20775ba
Name:           lbd
Version:        0.4
Release:        22%{?dist}
Summary:        A DNS/HTTP load balancing detector
License:        GPL-2.0-or-later
URL:            https://github.com/craig/ge.mine.nu/tree/master/lbd
Source0:        https://raw.githubusercontent.com/craig/ge.mine.nu/master/lbd/%{name}.sh#/%{name}
BuildArch:      noarch
Requires:       bind-utils
Requires:       nc
# oreon:deps

# /oreon:deps
%description
lbd (load balancing detector) detects if a given domain uses DNS and/or HTTP 
Load-Balancing (via Server: and Date: header and diffs between server answers).

%prep

# Nothing to prep

%build

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
