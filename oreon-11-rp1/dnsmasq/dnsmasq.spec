%global source4_hash 1fdd9f50b20b8f9d812270e91f9450cd54ccaed2f751611d62afe3b01cdcee98
%global source3_hash 895a58fcc2096d344cb4cb1d862df730a314ec20f286716593f3caf4b84c0479
%global source0_hash 4bf50c2c1018f9fbc26037df51b90ecea0cb73d46162846763b92df0d6c3a458
%bcond_without i18n
%define testrelease 0
%define releasecandidate 0
%if 0%{testrelease}
  %define extrapath test-releases/
  %define extraversion test%{testrelease}
%endif
%if 0%{releasecandidate}
  %define extrapath release-candidates/
  %define extraversion rc%{releasecandidate}
%endif
%define _hardened_build 1
%global forgeurl0 git://thekelleys.org.uk/dnsmasq.git
%global gittag v%{version}%{?extraversion}
%bcond_with sourcegit
%bcond_without annocheck
Name:           dnsmasq
Version:        2.93
Release:        1%{?dist}
Summary:        A lightweight DHCP/caching DNS server
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://www.thekelleys.org.uk/dnsmasq/
VCS:            git:%{forgeurl0}
Source0:        https://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.92.tar.xz
Source1:        %{name}.service
Source2:        dnsmasq-systemd-sysusers.conf
Source3:        https://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.92.tar.xz.asc
%if 0%{?testrelease} || 0%{?releasecandidate}
Source4:        https://www.thekelleys.org.uk/srkgpg.txt
%else
%endif
Source5:        tmpfiles-dnsmasq.conf
Patch1:         dnsmasq-2.77-underflow.patch
Patch2:         dnsmasq-2.81-configuration.patch
Patch3:         dnsmasq-2.78-fips.patch
Patch7:         dnsmasq-2.90-dbus-interfaces.patch
Patch8:         https://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=patch;h=f603a4f920e6953b11667d424956fd47373870e9#/dnsmasq-2.92-dnssec-wildcard.patch
Patch9:         https://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=patch;h=1269f074f86bb959863012063060a3a082d37dc4#/dnsmasq-2.93-dnssec-rrsig-owner.patch
Requires:       nettle
%{?systemd_ordering}
%if %{with sourcegit}
%endif
%if %{with i18n}
%endif
%if %{with annocheck}
%endif
# oreon:deps
BuildRequires:  annobin-annocheck
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libidn2-devel
BuildRequires:  make
BuildRequires:  nettle-devel
BuildRequires:  nftables-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  sequoia-sqv
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server.
It is designed to provide DNS and, optionally, DHCP, to a small network.
It can serve the names of local machines which are not in the global
DNS. The DHCP server integrates with the DNS server and allows machines
with DHCP-allocated addresses to appear in the DNS with names configured
either in each host or in a central configuration file. Dnsmasq supports
static and dynamic DHCP leases and BOOTP for network booting of disk-less
machines.

%package        utils
Summary:        Utilities for manipulating DHCP server leases
%description    utils
Utilities that use the standard DHCP protocol to query/remove a DHCP
server's leases.

%if %{with i18n}
%package        langpack
Summary:        Translations for few languages
License:        LicenseRef-Fedora-Public-Domain AND GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and (langpacks-de or langpacks-es or langpacks-fi or langpacks-fr or langpacks-id or langpacks-it or langpacks-ka or langpacks-no or langpacks-pl or langpacks-pt_BR or langpacks-ro) )
%description    langpack
Translations for few languages on dnsmasq.

%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{with sourcegit}
%autosetup -n %{name}-2.92 -N -S git_am
# If preparing with sourcegit, drop again source directory
# and clone git repository
# FIXME: deleting just unpacked sources is dangerous
# But using %%setup changes used directories in %%build and %%install
rm -rf %{_builddir}/%{name}-%{version}%{?extraversion}
cd %{_builddir}
git clone -b %{gittag} %{forgeurl0} %{name}-%{version}%{?extraversion}
cd %{name}-%{version}%{?extraversion}
git checkout -b rpmbuild
%else
%autosetup -n %{name}-2.92 -N
%endif
# Apply patches on top
%autopatch -p1

# use /var/lib/dnsmasq instead of /var/lib/misc
for file in dnsmasq.conf.example man/dnsmasq.8 man/es/dnsmasq.8 src/config.h; do
    sed -i 's|/var/lib/misc/dnsmasq.leases|/var/lib/dnsmasq/dnsmasq.leases|g' "$file"
done

#set default user /group in src/config.h
sed -i 's|#define CHUSER "nobody"|#define CHUSER "dnsmasq"|' src/config.h
sed -i 's|#define CHGRP "dip"|#define CHGRP "dnsmasq"|' src/config.h
sed -i "s|\(#\s*define RUNFILE\) \"/var/run/dnsmasq.pid\"|\1 \"%{_rundir}/dnsmasq.pid\"|" src/config.h

# optional parts
sed -i 's|^COPTS[[:space:]]*=|\0 -DHAVE_DBUS -DHAVE_LIBIDN2 -DHAVE_DNSSEC -DHAVE_CONNTRACK -DHAVE_NFTSET|' Makefile

%build

%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" BINDIR=%{_sbindir} \
%if %{with i18n}
  all-i18n
%else
  all
%endif
%make_build -C contrib/lease-tools CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" BINDIR=%{_sbindir}
%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir} \
        $RPM_BUILD_ROOT%{_mandir}/man8 \
        $RPM_BUILD_ROOT%{_var}/lib/dnsmasq \
        $RPM_BUILD_ROOT%{_sysconfdir}/dnsmasq.d \
        $RPM_BUILD_ROOT%{_datadir}/dbus-1/system.d
install -p src/dnsmasq $RPM_BUILD_ROOT%{_sbindir}/dnsmasq
install -p -m 0644 dnsmasq.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/dnsmasq.conf
install -p -m 0644 dbus/dnsmasq.conf $RPM_BUILD_ROOT%{_datadir}/dbus-1/system.d/
install -p -m 0644 man/dnsmasq.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install -p -D -m 0644 trust-anchors.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/trust-anchors.conf
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
         $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 755 contrib/lease-tools/dhcp_release $RPM_BUILD_ROOT%{_bindir}/dhcp_release
install -p -m 644 contrib/lease-tools/dhcp_release.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_release.1
install -p -m 755 contrib/lease-tools/dhcp_release6 $RPM_BUILD_ROOT%{_bindir}/dhcp_release6
install -p -m 644 contrib/lease-tools/dhcp_release6.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_release6.1
install -p -m 755 contrib/lease-tools/dhcp_lease_time $RPM_BUILD_ROOT%{_bindir}/dhcp_lease_time
install -p -m 644 contrib/lease-tools/dhcp_lease_time.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_lease_time.1
mkdir -p %{buildroot}%{_unitdir}
install -p -m644 %{SOURCE1} %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_initrddir}
install -p -Dpm 644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
install -Dpm 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%if %{with i18n}
%make_install PREFIX=%{_prefix} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" BINDIR=%{_sbindir} install-i18n
%find_lang %{name} --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --help
$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --help dhcp
$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --help dhcp6
$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --test --conf-file=$RPM_BUILD_ROOT%{_datadir}/%{name}/trust-anchors.conf
if [ -d "%{_sysconfdir}/dnsmasq.d" ]; then
  $RPM_BUILD_ROOT%{_sbindir}/dnsmasq --test --conf-file=$RPM_BUILD_ROOT%{_sysconfdir}/dnsmasq.conf
fi
if type -p annocheck; then
  annocheck --no-use-debuginfod --ignore-unknown --verbose --debug-dir=$RPM_BUILD_ROOT%{_prefix}/lib/debug/%{_sbindir} $RPM_BUILD_ROOT%{_sbindir}/dnsmasq
fi
%post

%systemd_post dnsmasq.service
%preun

%systemd_preun dnsmasq.service
%postun

%systemd_postun_with_restart dnsmasq.service
%files -f %{oreon_filedir}/main.list
%files -n dnsmasq-utils -f %{oreon_filedir}/dnsmasq-utils.list
%files -n dnsmasq-langpack -f %{oreon_filedir}/dnsmasq-langpack.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.92-5
- Prepare for Oreon 11 (RP1)
