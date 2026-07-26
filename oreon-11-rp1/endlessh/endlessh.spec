%global source0_hash 786cea9e2c8e0a37d3d4ecd984ca4a0ae0b2d6e2b8da37e3cdbb9d49ccdecbf0

Summary:	SSH tarpit that slowly sends an endless banner 
Name:		endlessh
Version:	1.1
Release:	16%{?dist}

License:	Unlicense
URL:		https://github.com/skeeto/endlessh
Source0:	https://github.com/skeeto/endlessh/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Fix-binary-path-in-endlessh.service.patch
Patch1:		0002-Config-change-to-port-2222.patch
Patch2:		9e66ab19d6b57ae96b161a8acd11bec1a76670c2.patch
Patch3:         0003-Change-InaccessiblePaths-from-systemd-service.patch
 
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	git-core
BuildRequires:	systemd-rpm-macros
Requires:	systemd

%description
Endlessh is an SSH tarpit that very slowly sends an endless, random SSH banner.
It keeps SSH clients locked up for hours or even days at a time. The purpose is
to put your real SSH server on another port and then let the script kiddies get
stuck in this tarpit instead of bothering a real server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -S git

%build
# Makefile doesn't allow overriding from environment, change it
sed -i -e "s:^CFLAGS.*:CFLAGS = %{optflags}:" Makefile
%make_build

%install
make install PREFIX=%{buildroot}%{_prefix}
install -d -m755 %{buildroot}%{_sysconfdir}/%{name}
install -m644 ./util/smf/endlessh.conf %{buildroot}/%{_sysconfdir}/%{name}/config
install -d -m755 %{buildroot}/%{_unitdir}
install -m644 ./util/endlessh.service %{buildroot}/%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_unitdir}/%{name}.service

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config

%doc README.md
%license UNLICENSE

%changelog
%autochangelog
