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
# path to upstream git repository
%global forgeurl0 git://thekelleys.org.uk/dnsmasq.git
# tag of selected version
%global gittag v%{version}%{?extraversion}


# Attempt to prepare source-git with downstream repos
%bcond_with sourcegit
%bcond_without annocheck

Name:           dnsmasq
Version:        2.92
Release:        5%{?extraversion:.%{extraversion}}%{?dist}
Summary:        A lightweight DHCP/caching DNS server

# SPDX identifiers already
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://www.thekelleys.org.uk/dnsmasq/
VCS:            git:%{forgeurl0}
Source0:        http://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.92.tar.xz
Source1:        %{name}.service
Source2:        dnsmasq-systemd-sysusers.conf
Source3:        http://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.92.tar.xz.asc
# GPG public key
%if 0%{?testrelease} || 0%{?releasecandidate}
Source4:        http://www.thekelleys.org.uk/srkgpg.txt
%else
Source4:        http://www.thekelleys.org.uk/srkgpg.txt
%endif
Source5:        tmpfiles-dnsmasq.conf

# https://bugzilla.redhat.com/show_bug.cgi?id=1495409
Patch1:         dnsmasq-2.77-underflow.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1852373
Patch2:         dnsmasq-2.81-configuration.patch
Patch3:         dnsmasq-2.78-fips.patch
Patch7:         dnsmasq-2.90-dbus-interfaces.patch
# https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q1/018378.html
Patch8:         https://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=patch;h=f603a4f920e6953b11667d424956fd47373870e9#/dnsmasq-2.92-dnssec-wildcard.patch
# https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q1/018383.html
Patch9:         https://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=patch;h=1269f074f86bb959863012063060a3a082d37dc4#/dnsmasq-2.93-dnssec-rrsig-owner.patch


Requires:       nettle

BuildRequires:  dbus-devel
BuildRequires:  pkgconfig
BuildRequires:  libidn2-devel
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  nettle-devel
BuildRequires:  nftables-devel
Buildrequires:  gcc
BuildRequires:  sequoia-sqv

BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
%if %{with sourcegit}
BuildRequires:  git-core
%endif
BuildRequires: make
%if %{with i18n}
BuildRequires: gettext
%endif
%if %{with annocheck}
BuildRequires: annobin-annocheck
%endif

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
# Will not do separate packages for every single language, those translations are small enough
Supplements:    (%{name} = %{version}-%{release} and (langpacks-de or langpacks-es or langpacks-fi or langpacks-fr or langpacks-id or langpacks-it or langpacks-ka or langpacks-no or langpacks-pl or langpacks-pt_BR or langpacks-ro) )

%description    langpack
Translations for few languages on dnsmasq.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?fedora}
sqv --keyring=%{SOURCE4} --signature-file=%{SOURCE3} %{SOURCE0}
%endif
%if %{with sourcegit}
%autosetup -n %{name}-%{version}%{?extraversion} -N -S git_am
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
%autosetup -n %{name}-%{version}%{?extraversion} -N
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
# normally i'd do 'make install'...it's a bit messy, though
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

# utils sub package
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
         $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 755 contrib/lease-tools/dhcp_release $RPM_BUILD_ROOT%{_bindir}/dhcp_release
install -p -m 644 contrib/lease-tools/dhcp_release.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_release.1
install -p -m 755 contrib/lease-tools/dhcp_release6 $RPM_BUILD_ROOT%{_bindir}/dhcp_release6
install -p -m 644 contrib/lease-tools/dhcp_release6.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_release6.1
install -p -m 755 contrib/lease-tools/dhcp_lease_time $RPM_BUILD_ROOT%{_bindir}/dhcp_lease_time
install -p -m 644 contrib/lease-tools/dhcp_lease_time.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_lease_time.1

# Systemd
mkdir -p %{buildroot}%{_unitdir}
install -p -m644 %{SOURCE1} %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_initrddir}

#install systemd sysuser file
install -p -Dpm 644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

# install tmpfiles.d config
install -Dpm 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%if %{with i18n}
%make_install PREFIX=%{_prefix} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" BINDIR=%{_sbindir} install-i18n
%find_lang %{name} --with-man
%endif

%check
# Minimalistic build check
$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --help
$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --help dhcp
$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --help dhcp6
$RPM_BUILD_ROOT%{_sbindir}/dnsmasq --test --conf-file=$RPM_BUILD_ROOT%{_datadir}/%{name}/trust-anchors.conf
if [ -d "%{_sysconfdir}/dnsmasq.d" ]; then
  # this would fail in mock if that directory does not exist
  $RPM_BUILD_ROOT%{_sbindir}/dnsmasq --test --conf-file=$RPM_BUILD_ROOT%{_sysconfdir}/dnsmasq.conf
fi
# check link flags
if type -p annocheck; then
  annocheck --no-use-debuginfod --ignore-unknown --verbose --debug-dir=$RPM_BUILD_ROOT%{_prefix}/lib/debug/%{_sbindir} $RPM_BUILD_ROOT%{_sbindir}/dnsmasq
fi

%post
%systemd_post dnsmasq.service

%preun
%systemd_preun dnsmasq.service

%postun
%systemd_postun_with_restart dnsmasq.service

%files
%doc CHANGELOG FAQ doc.html setup.html dbus/DBus-interface
%license COPYING COPYING-v3
%config(noreplace) %{_sysconfdir}/dnsmasq.conf
%dir %{_sysconfdir}/dnsmasq.d
%dir %attr(0755,root,dnsmasq) %{_var}/lib/dnsmasq
%{_datadir}/dbus-1/system.d/dnsmasq.conf
%{_unitdir}/%{name}.service
%{_sbindir}/dnsmasq
%{_mandir}/man8/dnsmasq*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/trust-anchors.conf
%{_sysusersdir}/dnsmasq.conf
%{_tmpfilesdir}/dnsmasq.conf

%files utils
%license COPYING COPYING-v3
%{_bindir}/dhcp_*
%{_mandir}/man1/dhcp_*

%if %{with i18n}
%files langpack -f %{name}.lang
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.92-5
- Prepare for Oreon 11 (RP1)
