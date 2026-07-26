%global source0_hash 0513f62ba5ab615c4333827b804237d58cf7bd623d09e1b4918d3fc85f08fc70

%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)

Name:           lynis
Version:        3.1.6
Release:        2%{?dist}
Summary:        Security and system auditing tool
License:        GPL-3.0-only
URL:            https://cisofy.com/lynis/
Source0:        https://cisofy.com/files/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  git-core
%if 0%{?el6}
BuildRequires:  procps
%else
BuildRequires:  procps-ng
%endif
Requires:       audit
Requires:       e2fsprogs
Requires:       module-init-tools

%description
Lynis is an auditing and hardening tool for Unix/Linux and you might even call
it a compliance tool. It scans the system and installed software. Then it 
performs many individual security control checks. It determines the hardening 
state of the machine, detects security issues and provides suggestions to 
improve the security defense of the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{name} 

%build
# Empty build.

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -p default.prf %{buildroot}%{_sysconfdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
install -p lynis %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man8
install -p lynis.8 %{buildroot}%{_mandir}/man8

mkdir -p  %{buildroot}%{_datadir}/%{name}/include/
# Forced by upstream. Otherwise these scripts can't be executed.
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

%check
# Sanity check
./lynis audit system --quick --pentest

%files
%doc CHANGELOG* CONTRIBUTORS* FAQ* README*
%doc extras/systemd/
%license LICENSE
%{_bindir}/lynis
%{bashcompdir}/*
%{_datadir}/lynis/
%{_mandir}/man8/lynis.8*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/default.prf
%ghost %{_localstatedir}/log/lynis.log
%ghost %{_localstatedir}/log/lynis-report.dat

%changelog
%autochangelog
