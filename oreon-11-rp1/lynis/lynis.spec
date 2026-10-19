%global source0_hash b5314a07fd85fa3ffc7da57b508f0108ec3280d84e4af823f805d95cbbc2428c
%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)
Name:           lynis
Version:        3.1.7
Release:        1%{?dist}
Summary:        Security and system auditing tool
License:        GPL-3.0-only
URL:            https://cisofy.com/lynis/
Source0:        https://cisofy.com/files/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?el6}
%else
%endif
Requires:       audit
Requires:       e2fsprogs
Requires:       module-init-tools
# oreon:deps
BuildRequires:  git-core
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  procps-ng
# /oreon:deps
%description
Lynis is an auditing and hardening tool for Unix/Linux and you might even call
it a compliance tool. It scans the system and installed software. Then it 
performs many individual security control checks. It determines the hardening 
state of the machine, detects security issues and provides suggestions to 
improve the security defense of the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -p default.prf %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
install -p lynis %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
install -p lynis.8 %{buildroot}%{_mandir}/man8
mkdir -p  %{buildroot}%{_datadir}/%{name}/include/
install -p include/* %{buildroot}%{_datadir}/%{name}/include/
chmod 644 %{buildroot}%{_datadir}/%{name}/include/*
mkdir -p  %{buildroot}%{_datadir}/%{name}/plugins/
install -p plugins/* %{buildroot}%{_datadir}/%{name}/plugins/
cp -pR db/ %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{bashcompdir}
install -p extras/bash_completion.d/lynis %{buildroot}%{bashcompdir}/
mkdir -p %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/lynis.log
touch %{buildroot}%{_localstatedir}/log/lynis-report.dat
%oreon_autofiles main

%check

./lynis audit system --quick --pentest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
