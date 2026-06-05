%global source0_hash none

Name:     lldpd
Version:  1.0.18
Release:  6%{?dist}
Summary:  ISC-licensed implementation of LLDP
License:  ISC

URL:      https://github.com/lldpd/
Source0:        https://github.com/lldpd/lldpd/archive/refs/tags/%{version}.tar.gz#/lldpd-%{version}.tar.gz
Source1:  %{name}-fedora.service
Source2:  %{name}-tmpfiles
Source3:  %{name}-fedora.sysconfig
Source4:  %{name}-systemd-sysusers.conf

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: check-devel
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: libevent-devel
BuildRequires: make
BuildRequires: net-snmp-devel
BuildRequires: readline-devel
BuildRequires: systemd-devel
%{?systemd_requires}

Requires(pre): shadow-utils

%description
LLDP is an industry standard protocol designed to supplant proprietary
Link-Layer protocols such as EDP or CDP. The goal of LLDP is to provide
an inter-vendor compatible mechanism to deliver Link-Layer notifications
to adjacent network devices.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: %{summary}

%description devel
%{name} development libraries and headers

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
autoreconf -fi
%configure --disable-static --with-snmp --disable-silent-rules \
  --with-privsep-user=%{name} --with-privsep-group=%{name} \
  --with-privsep-chroot=%{_rundir}/%{name}/chroot \
  --with-lldpd-ctl-socket=%{_rundir}/%{name}/%{name}.socket \
  --with-systemdsystemunitdir=%{_unitdir} --with-sysusersdir=no

%make_build


%install
%make_install

install -p -D -m644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -p -D -m644 %{SOURCE3} %{buildroot}/etc/sysconfig/%{name}
install -p -D -m644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf

install -d -D -m 0755 %{buildroot}%{_rundir}/%{name}/chroot
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}
# remove the docs from buildroot
rm -rf %{buildroot}/usr/share/doc/%{name}

# don't include completion conf yet
rm -f %{buildroot}/usr/share/bash-completion/completions/lldpcli
rm -f %{buildroot}/usr/share/zsh/vendor-completions/_lldpcli
rm -f %{buildroot}/usr/share/zsh/site-functions/_lldpcli

# remove static libtool archive
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%pre
%sysusers_create_compat %{SOURCE4}
exit 0

%post
%systemd_post lldpd.service

%preun
%systemd_preun lldpd.service

%postun
%systemd_postun_with_restart lldpd.service

%files
%license LICENSE
%doc NEWS README.md
%config %{_sysconfdir}/%{name}.d
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/lldpcli
%{_sbindir}/lldpctl
%{_sbindir}/%{name}
%{_mandir}/man8/lldpcli.8*
%{_mandir}/man8/lldpctl.8*
%{_mandir}/man8/%{name}.8*
%{_libdir}/liblldpctl.so.4*
%dir %{_rundir}/%{name}
%dir %{_rundir}/%{name}/chroot
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%dir %attr(-,lldpd,lldpd) %{_sharedstatedir}/%{name}

%files devel
%{_includedir}/lldp-const.h
%{_includedir}/lldpctl.h
%{_libdir}/liblldpctl.so
%{_libdir}/pkgconfig/lldpctl.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.18-6
- Import
