%global source0_hash f95c2b73797c4a0341a42a7b3c43efb60954c4130d082ad348fd40da554b4e85
Name:             freeipmi
Version:          1.6.19
Release:        1%{?dist}
Summary:        IPMI remote console and system management software
License:          GPL-3.0-or-later
URL:              https://www.gnu.org/software/freeipmi/
Source0:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:          bmc-watchdog.service
Source2:          ipmidetectd.service
Source3:          ipmiseld.service
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  texinfo
# /oreon:deps
%description
The FreeIPMI project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

%package          devel
Summary:          Development package for FreeIPMI
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      devel
Development package for FreeIPMI. This package includes the FreeIPMI
header files and libraries.

%package          bmc-watchdog
Summary:          IPMI BMC watchdog
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      bmc-watchdog
Provides a watchdog daemon for OS monitoring and recovery.

%package          ipmidetectd
Summary:          IPMI node detection monitoring daemon
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      ipmidetectd
Provides a tool and a daemon for IPMI node detection.

%package          ipmiseld
Summary:          IPMI SEL syslog logging daemon
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      ipmiseld
IPMI SEL syslog logging daemon.

%if %{?_with_debug:1}%{!?_with_debug:0}
  %global _enable_debug --enable-debug --enable-trace --enable-syslog
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
autoreconf -f -v -i

%build

export CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS"
%configure --program-prefix=%{?_program_prefix:%{_program_prefix}} \
           %{?_enable_debug} --disable-static
%make_build
%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir
echo freeipmi > %{buildroot}%{_localstatedir}/lib/freeipmi/ipckey
find %{buildroot} -name '*.la' -delete -print
install -m755 -d %{buildroot}%{_unitdir}
install -pm644 %SOURCE1 %SOURCE2 %SOURCE3 %{buildroot}%{_unitdir}/
rm -frv %{buildroot}%{_initrddir} %{buildroot}%{_sysconfdir}/init.d
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post bmc-watchdog

%systemd_post bmc-watchdog.service
%preun bmc-watchdog

%systemd_preun bmc-watchdog.service
%postun bmc-watchdog

%systemd_postun_with_restart bmc-watchdog.service
%post ipmiseld

%systemd_post ipmiseld.service
%preun ipmiseld

%systemd_preun ipmiseld.service
%postun ipmiseld

%systemd_postun_with_restart ipmiseld.service
%post ipmidetectd

%systemd_post ipmidetectd.service
%preun ipmidetectd

%systemd_preun ipmidetectd.service
%postun ipmidetectd

%systemd_postun_with_restart ipmidetectd.service
%triggerun -- freeipmi-bmc-watchdog < 1.1.1-2

/usr/bin/systemd-sysv-convert --save bmc-watchdog >/dev/null 2>&1 ||:
/sbin/chkconfig --del bmc-watchdog >/dev/null 2>&1 || :
/bin/systemctl try-restart bmc-watchdog.service >/dev/null 2>&1 || :
%triggerun -- freeipmi-ipmidetectd < 1.1.1-2

/usr/bin/systemd-sysv-convert --save ipmidetectd >/dev/null 2>&1 ||:
/sbin/chkconfig --del ipmidetectd >/dev/null 2>&1 || :
/bin/systemctl try-restart ipmidetectd.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n freeipmi-devel -f %{oreon_filedir}/freeipmi-devel.list
%files -n freeipmi-bmc-watchdog -f %{oreon_filedir}/freeipmi-bmc-watchdog.list
%files -n freeipmi-ipmidetectd -f %{oreon_filedir}/freeipmi-ipmidetectd.list
%files -n freeipmi-ipmiseld -f %{oreon_filedir}/freeipmi-ipmiseld.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.15-1
- Prepare for Oreon 11 (RP1)
