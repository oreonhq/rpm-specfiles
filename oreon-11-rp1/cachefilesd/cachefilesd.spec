# % define buildid .local

Name:		cachefilesd
Version:	0.10.10
Release:	23%{?dist}%{?buildid}
Summary:	CacheFiles user-space management daemon
License:	GPL-2.0-or-later
URL:		http://people.redhat.com/~dhowells/fscache/
Source0:	http://people.redhat.com/dhowells/fscache/cachefilesd-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires: systemd-units
BuildRequires: make
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: selinux-policy-base >= 3.7.19-5

%define _hardened_build 1

%description
The cachefilesd daemon manages the caching files and directory that are that
are used by network file systems such a AFS and NFS to do persistent caching to
the local disk.

%global docdir %{_docdir}/cachefilesd

%prep
%setup -q

%build
make all \
	ETCDIR=%{_sysconfdir} \
	SBINDIR=%{_sbindir} \
	MANDIR=%{_mandir} \
	CFLAGS="-Wall -Werror $RPM_OPT_FLAGS $RPM_LD_FLAGS $ARCH_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_mandir}/{man5,man8}
mkdir -p %{buildroot}%{_localstatedir}/cache/fscache
make DESTDIR=%{buildroot} install \
	ETCDIR=%{_sysconfdir} \
	SBINDIR=%{_sbindir} \
	MANDIR=%{_mandir} \
	CFLAGS="-Wall $RPM_OPT_FLAGS -Werror"

install -m 644 cachefilesd.conf %{buildroot}%{_sysconfdir}
install -m 644 cachefilesd.service %{buildroot}%{_unitdir}/cachefilesd.service

%post
%systemd_post cachefilesd.service

%preun
%systemd_preun cachefilesd.service

%postun
%systemd_postun_with_restart cachefilesd.service

%files
%doc README
%doc howto.txt
%doc selinux/move-cache.txt
%doc selinux/*.fc
%doc selinux/*.if
%doc selinux/*.te
%config(noreplace) %{_sysconfdir}/cachefilesd.conf
%{_sbindir}/*
%{_unitdir}/*
%{_mandir}/*/*
%{_localstatedir}/cache/fscache

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.10-23
- Prepare for Oreon 11 (RP1)
