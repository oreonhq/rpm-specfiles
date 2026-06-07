%global source0_hash 437bea850961ad4bf3fab8fadb8ab26f0e1ce4f59e1c0c025dad46255ca33b8a

# https://fedoraproject.org/wiki/Packaging:Guidelines#Compiler_flags
%global _hardened_build 1

# v1.0.34-11
%global commit0      5e78a2d8c86dc2639d2c4d5c974c3fb20a076a46
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:               fcoe-utils
Version:            1.0.34
Release:            15.git%{shortcommit0}%{?dist}
Summary:            Fibre Channel over Ethernet utilities
License:            GPL-2.0-only
URL:                http://www.open-fcoe.org
Source0:            https://github.com/openSUSE/fcoe-utils/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz
ExcludeArch:        ppc s390
BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      libtool
BuildRequires:      libpciaccess-devel
BuildRequires:      lldpad-devel >= 0.9.43
BuildRequires:      systemd
BuildRequires:      make
Requires:           lldpad >= 0.9.43
Requires:           iproute
Requires:           device-mapper-multipath
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
Fibre Channel over Ethernet utilities
fcoeadm - command line tool for configuring FCoE interfaces
fcoemon - service to configure DCB Ethernet QOS filters, works with lldpad

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n fcoe-utils-%{commit0}
%if 0%{?rhel} >= 8
# RHEL dropped support for software fcoe (fcoe.ko)
sed -i 's/^\(SUPPORTED_DRIVERS\)=".*"$/\1="bnx2fc qedf"/' etc/config
# make the defaults sane for supported offload drivers
sed -i 's/^\(DCB_REQUIRED\)=".*"$/\1="no"/' etc/cfg-ethx
%endif

%build
./bootstrap.sh
%configure --with-systemdsystemunitdir=%{_unitdir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/etc/init.d
mkdir -p %{buildroot}%{_libexecdir}/fcoe
for file in \
    contrib/*.sh \
    debug/*sh
    do install -m 755 ${file} %{buildroot}%{_libexecdir}/fcoe/
done

%post
%systemd_post fcoe.service fcoemon.socket

%preun
%systemd_preun fcoe.service fcoemon.socket

%postun
%systemd_postun_with_restart fcoe.service fcoemon.socket

%files
%doc README COPYING QUICKSTART
%{_sbindir}/*
%{_mandir}/man8/*
%{_unitdir}/fcoe.service
%{_unitdir}/fcoemon.socket
%{_sysconfdir}/fcoe/
%config(noreplace) %{_sysconfdir}/fcoe/cfg-ethx
%config(noreplace) %{_sysconfdir}/fcoe/config
%{_datadir}/bash-completion/completions/*
%{_libexecdir}/fcoe/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.34-15.git
- Prepare for Oreon 11 (RP1)
