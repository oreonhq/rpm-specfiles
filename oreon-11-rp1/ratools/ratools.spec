%global source0_hash 12ca66264f985278957ccbbe198ddfa5878372dbb0dcc5753314e29ae91fdda8
%global _hardened_build 1
Name:			ratools
Version:		0.6.2
Release:        1%{?dist}
Summary:        Framework for IPv6 Router Advertisements
License:		Apache-2.0
URL:			https://www.nonattached.net/ratools
Source0:        https://github.com/danrl/ratools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if 0%{?with_systemd}
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%endif # with_systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles main

%post

%systemd_post ratools-rad.service
%preun

%systemd_preun ratools-rad.service
%postun

%systemd_postun_with_restart ratools-rad.service
%endif # with_systemd
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
