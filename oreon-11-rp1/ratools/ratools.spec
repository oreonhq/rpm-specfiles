%global source0_hash 12ca66264f985278957ccbbe198ddfa5878372dbb0dcc5753314e29ae91fdda8

%global _hardened_build 1

%if 0%{?fedora} || 0%{?rhel} >= 7
    %global with_systemd 1
%endif # 0%{?fedora} || 0%{?rhel} >= 7

Name:			ratools
Version:		0.6.2
Release:		28%{?dist}
Summary:		Framework for IPv6 Router Advertisements
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:		Apache-2.0
URL:			https://www.nonattached.net/ratools
Source0:		https://github.com/danrl/ratools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
%if 0%{?with_systemd}
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd
%endif # with_systemd

BuildRequires:		gcc

%description
Ratools is a fast, dynamic, multi-threading framework for creating, modifying
and sending IPv6 Router Advertisements (RA).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
CFLAGS="%{?optflags}"				\
LDFLAGS="%{?__global_ldflags}"		\
make %{?_smp_mflags} -C src/

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/rad %{buildroot}%{_bindir}/rad
install -pm 0755 bin/ractl %{buildroot}%{_bindir}/ractl

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/*
install -pm 0644 bash-completion.d/ractl.sh %{buildroot}%{_sysconfdir}/bash_completion.d/ractl

mkdir -p %{buildroot}%{_mandir}/man8
install -pm 0644 man/*.8 %{buildroot}%{_mandir}/man8

%if 0%{?with_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -pm 0644 systemd/ratools-rad.service %{buildroot}%{_unitdir}/ratools-rad.service
install -pm 0644 systemd/ratools-rad.socket %{buildroot}%{_unitdir}/ratools-rad.socket

%post
%systemd_post ratools-rad.service

%preun
%systemd_preun ratools-rad.service

%postun
%systemd_postun_with_restart ratools-rad.service
%endif # with_systemd

%files
%doc README.md example.conf
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/rad
%{_bindir}/ractl
# Setting (noreplace) for the bash-completion is a bad idea,
# since this file is NOT config as meant to be customized by the user.
# https://bugzilla.redhat.com/show_bug.cgi?id=1100899#c6
%config %{_sysconfdir}/bash_completion.d/ractl
%{_mandir}/man8/*.8*
%if 0%{?with_systemd}
%{_unitdir}/ratools-rad.service
%{_unitdir}/ratools-rad.socket
%endif # with_systemd

%changelog
%autochangelog
