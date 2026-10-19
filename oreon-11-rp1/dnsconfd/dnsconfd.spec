%global source0_hash e81d64333514907f15b38e01ed34eac75b092599cb14b4985ad59133d55abf95
%global modulename dnsconfd
%global selinuxtype targeted
Name:           dnsconfd
Version:        2.2.2
Release:        1%{?dist}
Summary:        Local DNS cache configuration daemon
License:        MIT
URL:            https://github.com/InfrastructureServices/dnsconfd
Source0:        https://github.com/InfrastructureServices/dnsconfd/archive/refs/tags/2.2.2.tar.gz#/dnsconfd-2.1.0.tar.gz
Source1:        dnsconfd.sysusers
%if 0%{?with_asan}
%endif
Requires:  (%{name}-selinux if selinux-policy-%{selinuxtype})
Requires:  dbus-common
Requires:  %{name}-cache
Suggests:  %{name}-unbound
Requires:  (%{name}-unbound = %{version}-%{release} if %{name}-unbound)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(liburiparser)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Dnsconfd configures local DNS cache services.

# SELinux subpackage
%package selinux
Summary:             dnsconfd SELinux policy
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}
%description selinux
Dnsconfd SELinux policy module.

%package unbound
Summary:             dnsconfd unbound module
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}
Requires:            unbound
Provides:            %{name}-cache = %{version}-%{release}
%description unbound
Dnsconfd management of unbound server

%package dracut
Summary:            dnsconfd dracut module
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           unbound
Requires:           dracut
Requires:           dracut-network
Requires:           unbound-dracut
%description dracut
Dnsconfd dracut module

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if 0%{?with_asan}
%meson -Db_sanitize=address -Doptimization=g
%else
%meson
%endif
%meson_build
%if 0%{?with_asan}
    echo 'allow dnsconfd_t dnsconfd_t:process ptrace;' >> distribution/dnsconfd.te
%endif
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%install
%meson_install
mkdir   -m 0755 -p %{buildroot}%{_datadir}/dbus-1/system.d/
mkdir   -m 0755 -p %{buildroot}%{_datadir}/dbus-1/system-services/
mkdir   -m 0755 -p %{buildroot}%{_sysconfdir}/unbound/conf.d/
mkdir   -m 0755 -p %{buildroot}%{_unitdir}
mkdir   -m 0755 -p %{buildroot}%{_unitdir}/unbound.service.d
mkdir   -m 0755 -p %{buildroot}%{_unitdir}/dnsconfd.service.d
mkdir   -m 0755 -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir   -m 0755 -p %{buildroot}/%{_mandir}/man8
mkdir   -m 0755 -p %{buildroot}/%{_mandir}/man5
mkdir   -m 0755 -p %{buildroot}%{_rundir}/dnsconfd
mkdir   -m 0755 -p %{buildroot}%{_tmpfilesdir}
mkdir   -m 0755 -p %{buildroot}%{_prefix}/lib/dracut/modules.d/99dnsconfd
mkdir   -m 0755 -p %{buildroot}%{_libexecdir}
install -m 0644 -p distribution/com.redhat.dnsconfd.conf %{buildroot}%{_datadir}/dbus-1/system.d/com.redhat.dnsconfd.conf
install -m 0644 -p distribution/com.redhat.dnsconfd.service %{buildroot}%{_datadir}/dbus-1/system-services/com.redhat.dnsconfd.service
install -m 0644 -p distribution/dnsconfd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/dnsconfd
install -m 0644 -p distribution/dnsconfd.service %{buildroot}%{_unitdir}/dnsconfd.service
install -m 0644 -p distribution/dnsconfd-unbound-control.path %{buildroot}%{_unitdir}/dnsconfd-unbound-control.path
install -m 0644 -p distribution/dnsconfd-unbound-control.service %{buildroot}%{_unitdir}/dnsconfd-unbound-control.service
install -m 0644 -p distribution/dnsconfd.conf %{buildroot}%{_sysconfdir}/dnsconfd.conf
install -m 0644 -p distribution/dnsconfd-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -m 0644 -p distribution/dnsconfd-unbound-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}-unbound.conf
install -m 0755 -p distribution/dracut_module/module-setup.sh %{buildroot}%{_prefix}/lib/dracut/modules.d/99dnsconfd
install -m 0755 -p distribution/dnsconfd-prepare.sh %{buildroot}%{_libexecdir}/dnsconfd-prepare
install -m 0755 -p distribution/dnsconfd-prepare.sh %{buildroot}%{_libexecdir}/dnsconfd-cleanup
install -m 0755 -p distribution/dnsconfd-unbound-control.sh %{buildroot}%{_libexecdir}/dnsconfd-unbound-control.sh
for f in distribution/dracut_module/*.conf; do
  test -f "$f" || continue
  install -m 0644 -p "$f" %{buildroot}%{_prefix}/lib/dracut/modules.d/99dnsconfd
done
touch %{buildroot}%{_rundir}/dnsconfd/unbound.conf
chmod 0644 %{buildroot}%{_rundir}/dnsconfd/unbound.conf
install -m 0644 -p distribution/dnsconfd.service.d-unbound.conf %{buildroot}%{_unitdir}/unbound.service.d/dnsconfd.conf
install -m 0644 -p distribution/dnsconfd-unbound-control.conf %{buildroot}%{_unitdir}/dnsconfd.service.d/dnsconfd-unbound-control.conf
install -m 0644 -p distribution/unbound-dnsconfd.conf %{buildroot}%{_sysconfdir}/unbound/conf.d/unbound.conf
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -m 0644 -p distribution/dnsconfd.8 %{buildroot}/%{_mandir}/man8/dnsconfd.8
install -m 0644 -p distribution/dnsconfd-config.8 %{buildroot}/%{_mandir}/man8/dnsconfd-config.8
install -m 0644 -p distribution/dnsconfd-reload.8 %{buildroot}/%{_mandir}/man8/dnsconfd-reload.8
install -m 0644 -p distribution/dnsconfd-status.8 %{buildroot}/%{_mandir}/man8/dnsconfd-status.8
install -m 0644 -p distribution/dnsconfd.conf.5 %{buildroot}/%{_mandir}/man5/dnsconfd.conf.5
install -p -D -m 0644 distribution/dnsconfd.sysusers %{buildroot}%{_sysusersdir}/dnsconfd.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{modulename}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%post unbound

%systemd_post dnsconfd-unbound-control.path
%preun unbound

%systemd_preun dnsconfd-unbound-control.path
%postun unbound

%systemd_postun_with_restart dnsconfd-unbound-control.path
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n dnsconfd-selinux -f %{oreon_filedir}/dnsconfd-selinux.list
%files -n dnsconfd-unbound -f %{oreon_filedir}/dnsconfd-unbound.list
%files -n dnsconfd-dracut -f %{oreon_filedir}/dnsconfd-dracut.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-1
- Prepare for Oreon 11 (RP1)
