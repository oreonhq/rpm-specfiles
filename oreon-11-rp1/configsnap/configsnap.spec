%global source0_hash 248b260176593225c603c3800170bf342f033ed376aedb153169022b4581faa2
Name:           configsnap
Version:        0.21.1
Release:        1%{?dist}
Summary:        Record and compare system state
License:        Apache-2.0
URL:            https://github.com/rackerlabs/%{name}
Source0:        https://github.com/rackerlabs/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  help2man
BuildRequires:  python3-devel
# /oreon:deps
%description
configsnap records important system state information and can optionally compare
with a previous state and identify changes

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

help2man --include=%{name}.help2man --no-info ./%{name} -o %{name}.man
%install
mkdir -p %{buildroot}%{_sbindir} \
  %{buildroot}%{_mandir}/man1 \
  %{buildroot}%{_sysconfdir}/%{name}
install -p -m 0755 %{name} %{buildroot}%{_sbindir}
install -p -m 0644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1
install -p -m 0600 additional.conf %{buildroot}%{_sysconfdir}/%{name}/additional.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
