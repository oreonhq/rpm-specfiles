%global source0_hash c2821329ed1efd6bf8f82e2878f75ca66889439d27c788785fd0ccc972ac307c
%bcond_without userflags
%bcond_with runautogen
Name: corosync-qdevice
Summary:        The Corosync Cluster Engine Qdevice
Version: 3.0.4
Release:        1%{?dist}
License: BSD-3-Clause
URL: https://github.com/corosync/corosync-qdevice
Source0:        https://github.com/corosync/corosync-qdevice/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires: corosync >= 2.4.0
Requires: corosynclib >= 2.4.0
Requires: nss-tools
%{?systemd_requires}
%if %{with runautogen}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  corosynclib-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  groff
BuildRequires:  libqb-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nss-devel
BuildRequires:  sed
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with runautogen}
./autogen.sh
%endif
%{configure} \
%if %{with userflags}
	--enable-user-flags \
%endif
	--enable-systemd \
	--enable-qdevices \
	--enable-qnetd \
	--with-initddir=%{_initrddir} \
	--with-systemddir=%{_unitdir} \
	--docdir=%{_docdir}
%make_build
%install
%make_install
rm -rf %{buildroot}%{_docdir}/*
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 init/corosync-qdevice.sysconfig.example \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync-qdevice
install -p -m 644 init/corosync-qnetd.sysconfig.example \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync-qnetd
sed -i -e 's/^#User=/User=/' \
   %{buildroot}%{_unitdir}/corosync-qnetd.service
install -m0644 -D init/corosync-qnetd.sysusers.conf.example %{buildroot}%{_sysusersdir}/corosync-qnetd.conf
%oreon_autofiles corosync-qdevice-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles corosync-qnetd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%description
This package contains the Corosync Cluster Engine Qdevice, script for creating
NSS certificates and an init script.

%post

%systemd_post corosync-qdevice.service
%preun

%systemd_preun corosync-qdevice.service
%postun

%systemd_postun corosync-qdevice.service
%package -n corosync-qdevice-devel
Summary: The Corosync Cluster Engine Qdevice Network Development Kit
Requires: pkgconfig
%description -n corosync-qdevice-devel
This package contains files used to develop using
The Corosync Cluster Engine Qdevice

%package -n corosync-qnetd
Summary: The Corosync Cluster Engine Qdevice Network Daemon
Requires: nss-tools
%{?systemd_requires}
%description -n corosync-qnetd
This package contains the Corosync Cluster Engine Qdevice Network Daemon,
script for creating NSS certificates and an init script.

%post -n corosync-qnetd

%systemd_post corosync-qnetd.service
%preun -n corosync-qnetd

%systemd_preun corosync-qnetd.service
%postun -n corosync-qnetd

%systemd_postun corosync-qnetd.service
%files -f %{oreon_filedir}/main.list
%files -n corosync-qdevice-devel -f %{oreon_filedir}/corosync-qdevice-devel.list
%files -n corosync-qnetd -f %{oreon_filedir}/corosync-qnetd.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.4-3
- Prepare for Oreon 11 (RP1)
