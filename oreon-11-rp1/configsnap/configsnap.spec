%global source0_hash 12eaa00c3438f8f648f10a05ed4219657a73cc2c46956cd47cbf6d02ad72c68c

Name:           configsnap
Version:        0.20.1
Release:        15%{?dist}
Summary:        Record and compare system state
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/rackerlabs/%{name}
Source0:        https://github.com/rackerlabs/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  help2man
%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires:  python3-devel
%else
BuildRequires:  python2-devel
%endif

%description
configsnap records important system state information and can optionally compare
with a previous state and identify changes

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%if 0%{?rhel} >= 8 || 0%{?fedora}
sed -i 's#/bin/python$#/bin/python3#g' ./%{name}
%endif
help2man --include=%{name}.help2man --no-info ./%{name} -o %{name}.man

%install
mkdir -p %{buildroot}%{_sbindir} \
  %{buildroot}%{_mandir}/man1 \
  %{buildroot}%{_sysconfdir}/%{name}
install -p -m 0755 %{name} %{buildroot}%{_sbindir}
install -p -m 0644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1
install -p -m 0600 additional.conf %{buildroot}%{_sysconfdir}/%{name}/additional.conf

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%doc NEWS
%doc MAINTAINERS.md
%config(noreplace) %{_sysconfdir}/%{name}/additional.conf
%{_mandir}/man1/%{name}.1*
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}

%changelog
%autochangelog
