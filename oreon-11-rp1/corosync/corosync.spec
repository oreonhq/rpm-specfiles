%global source0_hash be361c827f99b215b3bd3fa2fb071c03dac6831c2a351963d938caef62604bc8
%bcond_with watchdog
%bcond_with monitoring
%bcond_without snmp
%bcond_without dbus
%bcond_without systemd
%bcond_without xmlconf
%bcond_without nozzle
%bcond_without vqsim
%bcond_without runautogen
%bcond_without userflags
Name: corosync
Summary:        The Corosync Cluster Engine and Application Programming Interfaces
Version: 3.1.10
Release:        1%{?dist}
License: BSD-3-Clause
URL: http://corosync.github.io/corosync/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires: corosynclib%{?_isa} = %{version}-%{release}
Requires: libknet1 >= 1.18
Requires: libknet1-crypto-nss-plugin >= 1.18
%if %{with runautogen}
%endif
%if %{with monitoring}
%endif
%if %{with snmp}
%endif
%if %{with dbus}
%endif
%if %{with nozzle}
%endif
%if %{with systemd}
%{?systemd_requires}
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
%endif
%if %{with xmlconf}
Requires: libxslt
%endif
%if %{with vqsim}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  groff
BuildRequires:  libknet1-devel
BuildRequires:  libnozzle1-devel
BuildRequires:  libqb-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  net-snmp-devel
BuildRequires:  readline-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with runautogen}
./autogen.sh
%endif
%{configure} \
%if %{with watchdog}
	--enable-watchdog \
%endif
%if %{with monitoring}
	--enable-monitoring \
%endif
%if %{with snmp}
	--enable-snmp \
%endif
%if %{with dbus}
	--enable-dbus \
%endif
%if %{with systemd}
	--enable-systemd \
%endif
%if %{with xmlconf}
	--enable-xmlconf \
%endif
%if %{with nozzle}
	--enable-nozzle \
%endif
%if %{with vqsim}
	--enable-vqsim \
%endif
%if %{with userflags}
	--enable-user-flags \
%endif
	--with-initddir=%{_initrddir} \
	--with-systemddir=%{_unitdir} \
	--docdir=%{_docdir}
%make_build
%install
%make_install
%if %{with dbus}
mkdir -p -m 0700 %{buildroot}/%{_sysconfdir}/dbus-1/system.d
install -m 644 %{_builddir}/%{name}-%{version}/conf/corosync-signals.conf %{buildroot}/%{_datadir}/dbus-1/system.d/corosync-signals.conf
%endif
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}/*
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 tools/corosync-notifyd.sysconfig.example \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync-notifyd
install -m 644 init/corosync.sysconfig.example \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync
%oreon_autofiles corosynclib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles corosynclib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles corosync-vqsim usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%description
This package contains the Corosync Cluster Engine Executive, several default
APIs and libraries, default configuration files, and an init script.

%post

%if %{with systemd} && 0%{?systemd_post:1}
%systemd_post corosync.service
%else
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add corosync || :
fi
%endif
%preun

%if %{with systemd} && 0%{?systemd_preun:1}
%systemd_preun corosync.service
%else
if [ $1 -eq 0 ]; then
	/sbin/service corosync stop &>/dev/null || :
	/sbin/chkconfig --del corosync || :
fi
%endif
%postun

%if %{with systemd} && 0%{?systemd_postun:1}
%systemd_postun corosync.service
%endif
%package -n corosynclib
Summary: The Corosync Cluster Engine Libraries
%description -n corosynclib
This package contains corosync libraries.

%package -n corosynclib-devel
Summary: The Corosync Cluster Engine Development Kit
Requires: corosynclib%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Provides: corosync-devel = %{version}-%{release}
Provides: corosync-devel%{?_isa} = %{version}-%{release}
%description -n corosynclib-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%package -n corosync-vqsim
Summary: The Corosync Cluster Engine - Votequorum Simulator
Requires: corosynclib%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description -n corosync-vqsim
A command-line simulator for the corosync votequorum subsystem.
It uses the same code as the corosync quorum system but forks
them into subprocesses to simulate nodes.
Nodes can be added and removed as well as partitioned (to simulate
network splits)

%files -f %{oreon_filedir}/main.list
%files -n corosynclib -f %{oreon_filedir}/corosynclib.list
%files -n corosynclib-devel -f %{oreon_filedir}/corosynclib-devel.list
%files -n corosync-vqsim -f %{oreon_filedir}/corosync-vqsim.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.10-4
- Prepare for Oreon 11 (RP1)
