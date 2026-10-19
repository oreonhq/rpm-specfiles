%global source0_hash 3e68565653acab7a2caaec9791bbf132e83fb43973234826660cbcd13efc80ae
%global project skiboot
Name:		opal-prd
Version:	7.1
Release:        1%{?dist}
Summary:        OPAL Processor Recovery Diagnostics Daemon
License:	Apache-2.0
URL:		http://github.com/open-power/skiboot
ExclusiveArch:	ppc64le
Requires(post):	systemd
Requires(preun):	systemd
Requires(postun):	systemd
Source0:        https://github.com/open-power/%{project}/archive/v%{version}/%{project}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        opal-prd-rsyslog
Source2:        opal-prd-logrotate
Source3:        ffspart.man
Patch0:        opal-prd-ffspart-annocheck.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  systemd
# /oreon:deps
%description
This package provides a daemon to load and run the OpenPower firmware's
Processor Recovery Diagnostics binary. This is responsible for run time
maintenance of OpenPower Systems hardware.

%package -n	opal-utils
Summary:	OPAL firmware utilities
%description -n opal-utils
This package contains utility programs.

The 'gard' utility, can read, parse and clear hardware gard partitions
on OpenPower platforms. The 'getscom' and 'putscom' utilities provide
an interface to query or modify the registers of the different chipsets
of an OpenPower system. 'pflash' is a tool to access the flash modules
on such systems and update the OpenPower firmware.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{project}-%{version}

# update for 
sed -i -e 's|/usr/sbin|%{_sbindir}|' external/opal-prd/opal-prd.service

%build

OPAL_PRD_VERSION=%{version} make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" ASFLAGS="-m64 -Wa,--generate-missing-build-notes=yes" -C external/opal-prd
GARD_VERSION=%{version}     make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/gard
PFLASH_VERSION=%{version}   make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/pflash
XSCOM_VERSION=%{version}    make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/xscom-utils
FFSPART_VERSION=%{version}  make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/ffspart
%install
OPAL_PRD_VERSION=%{version} make -C external/opal-prd install DESTDIR=%{buildroot} prefix=/usr sbindir="\$(prefix)/bin"
GARD_VERSION=%{version}     make -C external/gard install DESTDIR=%{buildroot} prefix=/usr sbindir="\$(prefix)/bin"
PFLASH_VERSION=%{version}   make -C external/pflash install DESTDIR=%{buildroot} prefix=/usr sbindir="\$(prefix)/bin"
XSCOM_VERSION=%{version}    make -C external/xscom-utils install DESTDIR=%{buildroot} prefix=/usr sbindir="\$(prefix)/bin"
FFSPART_VERSION=%{version}  make -C external/ffspart install DESTDIR=%{buildroot} prefix=/usr sbindir="\$(prefix)/bin"
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p external/opal-prd/opal-prd.service %{buildroot}%{_unitdir}/opal-prd.service
mkdir -p %{buildroot}%{_sysconfdir}/{rsyslog.d,logrotate.d}
install -m 644 -p %{SOURCE1} %{buildroot}/%{_sysconfdir}/rsyslog.d/opal-prd.conf
install -m 644 -p %{SOURCE2} %{buildroot}/%{_sysconfdir}/logrotate.d/opal-prd
install -D -p -m 644 external/pci-scripts/ppc.py %{buildroot}%{python3_sitelib}/ppc/__init__.py
install -D -p -m 755 external/pci-scripts/phberr.py %{buildroot}%{_bindir}/phberr
install -m 644 -p %{SOURCE3} %{buildroot}%{_mandir}/man1/ffspart.1
%oreon_autofiles opal-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post opal-prd.service
%preun

%systemd_preun opal-prd.service
%postun

%systemd_postun_with_restart opal-prd.service
%files -f %{oreon_filedir}/main.list
%files -n opal-utils -f %{oreon_filedir}/opal-utils.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.1-9
- Import
