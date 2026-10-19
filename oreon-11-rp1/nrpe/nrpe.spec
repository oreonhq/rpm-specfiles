%global source0_hash 5e8947f61e1a4c41b6895c4d64c2dcd70cab32815cb4b49770e1c702b79ed5ed
%define nsport 5666
%global commit 4f7dd1199f1f3f72f9197e8565da339a4a2490b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commdate 20200423
%global fromgit 0
Name: nrpe
Version: 4.1.3
%if 0%{?fromgit}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        Host/service/network monitoring agent for Nagios
License: GPL-2.0-only
URL: http://www.nagios.org
%if 0%{?fromgit}
Source0:        https://github.com/NagiosEnterprises/%{name}/archive/%{name}-%{version}.tar.gz
%else
%endif
Source1: nrpe.sysconfig
Source2: nrpe-tmpfiles.conf
Source3: nrpe.README.SELinux.rst
Source5: nrpe_epel7.te
Source6: nrpe_epel.fc
Source7: nrpe.service.epel
Patch3: nrpe-0003-Include-etc-npre.d-config-directory.patch
Patch5: nrpe-0005-systemd-service.patch
Patch6: nrpe-configure-c99.patch
%if 0%{?fedora} < 28 && 0%{?rhel} < 8 && 0%{?oreon} < 11
%endif
Requires(pre): %{_sbindir}/usermod
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: nagios-common
Provides: nagios-nrpe = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  checkpolicy
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
Nrpe is a system daemon that will execute various Nagios plugins
locally on behalf of a remote (monitoring) host that uses the
check_nrpe plugin. Various plugins that can be executed by the
daemon are available at:
http://sourceforge.net/projects/nagiosplug

This package provides the core agent.

%package -n nagios-plugins-nrpe
Summary: Provides nrpe plugin for Nagios
Requires: nagios-plugins
Provides: check_nrpe = %{version}-%{release}
%description -n nagios-plugins-nrpe
Nrpe is a system daemon that will execute various Nagios plugins
locally on behalf of a remote (monitoring) host that uses the
check_nrpe plugin. Various plugins that can be executed by the
daemon are available at:
http://sourceforge.net/projects/nagiosplug

This package provides the nrpe plugin for Nagios-related applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{fromgit}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-%{name}-%{version}
%endif

# Create a sysusers.d config file
cat >nrpe.sysusers.conf <<EOF
u nrpe - 'NRPE user for the NRPE service' %{_localstatedir}/run/%{name} -
m nrpe nagios
EOF

%build

CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{?__global_ldflags}" \
%configure \
    --with-nrpe-port=%{nsport} \
    --with-nrpe-user=nrpe \
    --with-nrpe-group=nrpe \
    --with-piddir=/run/nrpe \
    --bindir=%{_sbindir} \
    --libdir=/doesnt/matter/ \
    --libexecdir=%{_libdir}/nagios/plugins \
    --datadir=%{_datadir}/nagios \
    --sysconfdir=%{_sysconfdir}/nagios \
    --localstatedir=%{_localstatedir}/run/ \
    --enable-command-args
make %{?_smp_mflags} all
%install
%if 0%{?el7}
install -D -m 0644 -p %{SOURCE7} %{buildroot}%{_unitdir}/%{name}.service
%else
install -D -m 0644 -p startup/default-service %{buildroot}%{_unitdir}/%{name}.service
%endif
install -D -p -m 0644 sample-config/nrpe.cfg %{buildroot}/%{_sysconfdir}/nagios/%{name}.cfg
install -D -p -m 0755 src/nrpe %{buildroot}/%{_sbindir}/nrpe
install -D -p -m 0755 src/check_nrpe %{buildroot}/%{_libdir}/nagios/plugins/check_nrpe
install -D -p -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -d %{buildroot}%{_sysconfdir}/nrpe.d
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -m0644 -D nrpe.sysusers.conf %{buildroot}%{_sysusersdir}/nrpe.conf
%oreon_autofiles nagios-plugins-nrpe usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

getent group nagios >/dev/null && %{_sbindir}/usermod -a -G nagios %{name} || :
%preun

%systemd_preun nrpe.service
%post

%systemd_post nrpe.service
%postun

%systemd_postun_with_restart nrpe.service
%files -f %{oreon_filedir}/main.list
%files -n nagios-plugins-nrpe -f %{oreon_filedir}/nagios-plugins-nrpe.list

%changelog

%autochangelog
