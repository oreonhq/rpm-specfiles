%global source0_hash 404f97ce3db0804b7704a387db88cdf3d3e2bf623f89f7c3b1ddb19b99c3eace
%global source1_hash ae5fc2d53f34ec8b71cd01281624680ee1caa5d9122eb77e2814f87fa8fd29c0
%define required_base 266
%if 0%{?centos}
%define rhel %{centos}
%endif
%define _hardened_build 1
%define __lib lib
%if 0%{?suse_version} > 1500
%define pamconfdir %{_pam_vendordir}
%define pamconfig tools/cockpit.suse.pam
%else
%define pamconfdir %{_sysconfdir}/pam.d
%define pamconfig tools/cockpit.pam
%endif
%if %{defined _pamdir}
%define pamdir %{_pamdir}
%else
%define pamdir %{_libdir}/security
%endif
Name:           cockpit
Summary:        Web Console for Linux servers
License:        LGPL-2.1-or-later AND GPL-3.0-or-later AND MIT AND CC-BY-SA-3.0 AND BSD-3-Clause
URL:            https://cockpit-project.org/
Version:        368
Release:        1%{?dist}
Source0:        https://github.com/cockpit-project/cockpit/releases/download/%{version}/cockpit-%{version}.tar.xz
Source1:        https://github.com/cockpit-project/cockpit/releases/download/%{version}/cockpit-node-%{version}.tar.xz
%define enable_multihost 1
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%define enable_multihost 0
%endif
%define selinuxtype targeted
%define selinux_configure_arg --enable-selinux-policy=%{selinuxtype}
%if 0%{?suse_version}
%else
%endif
%if 0%{?rebuild_bundle}
%endif
%if !%{defined bundle_docs}
%if 0%{?suse_version}
%else
%endif
%endif
Requires: cockpit-bridge
Requires: cockpit-ws
Requires: cockpit-system
Recommends: (cockpit-storaged if udisks2)
Recommends: (cockpit-packagekit if dnf)
%if 0%{?suse_version} == 0
Recommends: (dnf5daemon-server if dnf5)
%endif
Suggests: python3-pcp
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  asciidoctor
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gdb
BuildRequires:  gettext
BuildRequires:  glib-networking
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  make
BuildRequires:  nodejs
BuildRequires:  nodejs-esbuild
BuildRequires:  openssh-clients
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-timeout
BuildRequires:  sed
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n cockpit-%{version}
%if 0%{?rebuild_bundle}
%setup -q -D -T -a 1 -n cockpit-%{version}
%endif

%build

%if 0%{?rebuild_bundle}
rm -rf dist
NODE_ENV=production NODE_PATH=/usr/lib/node_modules:$(echo /usr/lib/node_modules_*) ./build.js
%else
%endif
%configure \
    %{?selinux_configure_arg} \
%if 0%{?suse_version}
    --docdir=%_defaultdocdir/%{name} \
%endif
    --with-pamdir='%{pamdir}' \
%if %{enable_multihost}
    --enable-multihost \
%endif
%if %{defined bundle_docs}
    --disable-doc \
%endif
%make_build
%check

make -j$(nproc) check
%install
%if 0%{?suse_version}
export NO_BRP_STALE_LINK_ERROR="yes"
%endif
%make_install
mkdir -p $RPM_BUILD_ROOT%{pamconfdir}
install -p -m 644 %{pamconfig} $RPM_BUILD_ROOT%{pamconfdir}/cockpit
rm -f %{buildroot}/%{_libdir}/cockpit/*.so
install -D -p -m 644 AUTHORS README.md %{buildroot}%{_docdir}/cockpit/
%if %{defined bundle_docs}
%define docbundledir %{_builddir}/%{name}-%{version}/doc/output/html
install -d %{buildroot}%{_docdir}/cockpit/guide
cp -rp %{docbundledir}/* %{buildroot}%{_docdir}/cockpit/guide/
%define manbundledir %{_builddir}/%{name}-%{version}/doc/output/man
for section in 1 5 8; do
  for manpage in %{manbundledir}/*.${section}; do
    install -D -p -m 644 "$manpage" %{buildroot}%{_mandir}/man${section}/$(basename "$manpage")
  done
done
%endif
echo '%dir %{_datadir}/cockpit' > base.list
echo '%dir %{_datadir}/cockpit/base1' >> base.list
find %{buildroot}%{_datadir}/cockpit/base1 -type f -o -type l >> base.list
echo '%{_sysconfdir}/cockpit/machines.d' >> base.list
echo %{buildroot}%{_datadir}/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy >> base.list
echo '%dir %{_datadir}/cockpit/shell' >> system.list
find %{buildroot}%{_datadir}/cockpit/shell -type f >> system.list
echo '%dir %{_datadir}/cockpit/systemd' >> system.list
find %{buildroot}%{_datadir}/cockpit/systemd -type f >> system.list
echo '%dir %{_datadir}/cockpit/users' >> system.list
find %{buildroot}%{_datadir}/cockpit/users -type f >> system.list
echo '%dir %{_datadir}/cockpit/metrics' >> system.list
find %{buildroot}%{_datadir}/cockpit/metrics -type f >> system.list
echo '%dir %{_datadir}/cockpit/kdump' > kdump.list
find %{buildroot}%{_datadir}/cockpit/kdump -type f >> kdump.list
echo '%dir %{_datadir}/cockpit/sosreport' > sosreport.list
find %{buildroot}%{_datadir}/cockpit/sosreport -type f >> sosreport.list
echo '%dir %{_datadir}/cockpit/storaged' > storaged.list
find %{buildroot}%{_datadir}/cockpit/storaged -type f >> storaged.list
echo '%dir %{_datadir}/cockpit/networkmanager' > networkmanager.list
find %{buildroot}%{_datadir}/cockpit/networkmanager -type f >> networkmanager.list
echo '%dir %{_datadir}/cockpit/packagekit' > packagekit.list
find %{buildroot}%{_datadir}/cockpit/packagekit -type f >> packagekit.list
echo '%dir %{_datadir}/cockpit/apps' >> packagekit.list
find %{buildroot}%{_datadir}/cockpit/apps -type f >> packagekit.list
echo '%dir %{_datadir}/cockpit/selinux' > selinux.list
find %{buildroot}%{_datadir}/cockpit/selinux -type f >> selinux.list
echo '%dir %{_datadir}/cockpit/static' > static.list
echo '%dir %{_datadir}/cockpit/static/fonts' >> static.list
find %{buildroot}%{_datadir}/cockpit/static -type f >> static.list
sed -i "s|%{buildroot}||" *.list
%if 0%{?suse_version}
rm -r %{buildroot}%{_datadir}/cockpit/sosreport
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit_project.cockpit_sosreport.metainfo.xml
rm -f %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/cockpit-sosreport.png
%else
%global _debugsource_packages 1
%global _debuginfo_subpackages 0
%define find_debug_info %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_include_minidebuginfo:-m} %{?_find_debuginfo_dwz_opts} %{?_find_debuginfo_opts} %{?_debugsource_packages:-S debugsourcefiles.list} "%{_builddir}/%{?buildsubdir}"
%endif
rm -rf %{buildroot}/usr/src/debug
%oreon_autofiles cockpit-storaged usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cockpit-packagekit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%description
The Cockpit Web Console enables users to administer GNU/Linux servers using a
web browser.

It offers network configuration, log inspection, diagnostic reports, SELinux
troubleshooting, interactive command-line sessions, and more.

%package bridge
Summary: Cockpit bridge server-side component
BuildArch: noarch
%description bridge
The Cockpit bridge component installed server side and runs commands on the
system on behalf of the web based user interface.

%package doc
Summary: Cockpit deployment and developer guide
BuildArch: noarch
%description doc
The Cockpit Deployment and Developer Guide shows sysadmins how to
deploy Cockpit on their machines as well as helps developers who want to
embed or extend Cockpit.

%package system
Summary: Cockpit admin interface package for configuring and troubleshooting a system
BuildArch: noarch
Requires: cockpit-bridge >= %{version}-%{release}
%if !0%{?suse_version}
Requires: shadow-utils
%endif
Requires: grep
Requires: /usr/bin/pwscore
Requires: /usr/bin/date
Provides: cockpit-shell = %{version}-%{release}
Provides: cockpit-systemd = %{version}-%{release}
Provides: cockpit-tuned = %{version}-%{release}
Provides: cockpit-users = %{version}-%{release}
Provides: bundled(npm(@patternfly/patternfly)) = 6.4.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-table)) = 6.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(@xterm/addon-webgl)) = 0.19.0
Provides: bundled(npm(@xterm/xterm)) = 6.0.0
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(ipaddr.js)) = 2.3.0
Provides: bundled(npm(json-stable-stringify-without-jsonify)) = 1.0.1
Provides: bundled(npm(lodash)) = 4.17.23
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(remarkable)) = 2.0.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.4.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.1
Provides: bundled(npm(uuid)) = 13.0.0
%description system
This package contains the Cockpit shell and system configuration interfaces.

%package ws
Summary: Cockpit Web Service
Requires: openssl
Requires: glib2 >= 2.68.0
Requires: (%{name}-ws-selinux = %{version}-%{release} if selinux-policy-base)
Recommends: sscg >= 2.3
Recommends: system-logos
Suggests: sssd-dbus >= 2.6.2
Suggests: python3
Obsoletes: cockpit-tests < 331
%global __requires_exclude_from ^%{_libexecdir}/cockpit-client$
%description ws
The Cockpit Web Service listens on the network, and authenticates users.

If sssd-dbus is installed, you can enable client certificate/smart card
authentication via sssd/FreeIPA.

%post ws

if [ "$1" = 1 ]; then
    mkdir -p /etc/motd.d /etc/issue.d
    ln -s ../../run/cockpit/issue /etc/motd.d/cockpit
    ln -s ../../run/cockpit/issue /etc/issue.d/cockpit.issue
    printf "# List of users which are not allowed to login to Cockpit\n" > /etc/cockpit/disallowed-users
    printf "root\n" >> /etc/cockpit/disallowed-users
    chmod 644 /etc/cockpit/disallowed-users
fi
if [ "$1" = 2 ]; then
    if [ "$(readlink /etc/motd.d/cockpit 2>/dev/null)" = "../../run/cockpit/motd" ]; then
        ln -sfn ../../run/cockpit/issue /etc/motd.d/cockpit
    fi
    if [ "$(readlink /etc/issue.d/cockpit.issue 2>/dev/null)" = "../../run/cockpit/motd" ]; then
        ln -sfn ../../run/cockpit/issue /etc/issue.d/cockpit.issue
    fi
fi
%tmpfiles_create cockpit-ws.conf
%systemd_post cockpit.socket cockpit.service
test -f %{_bindir}/firewall-cmd && firewall-cmd --reload --quiet || true
if getent passwd cockpit-wsinstance >/dev/null; then
    userdel cockpit-wsinstance
fi
%preun ws

%systemd_preun cockpit.socket cockpit.service
%postun ws

%systemd_postun_with_restart cockpit.socket cockpit.service
%package ws-selinux
Summary: SELinux security policy for cockpit-ws
Conflicts: %{name}-ws < 337-1.2025
Requires(post): selinux-policy-%{selinuxtype} >= %{_selinux_policy_version}
Requires(post): libselinux-utils
Requires(post): policycoreutils
%description ws-selinux
SELinux policy module for the cockpit-ws package.

%pre ws-selinux

%selinux_relabel_pre -s %{selinuxtype}
%post ws-selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
%postun ws-selinux

%selinux_modules_uninstall -s %{selinuxtype} %{name}
%selinux_relabel_post -s %{selinuxtype}
%if 0%{?suse_version}
%endif
%if !0%{?suse_version}
%endif
%if !0%{?is_smo} || ( 0%{?is_smo} && 0%{?sle_version} >= 150500 )
%endif
%package -n cockpit-storaged
Summary: Cockpit user interface for storage, using udisks
Requires: cockpit-shell >= %{required_base}
Requires: udisks2 >= 2.9
Recommends: udisks2-lvm2 >= 2.9
Recommends: udisks2-iscsi >= 2.9
Recommends: device-mapper-multipath
Recommends: clevis-luks
Requires: %{__python3}
%if 0%{?suse_version}
Requires: python3-dbus-python
%else
Requires: python3-dbus
%endif
BuildArch: noarch
%description -n cockpit-storaged
The Cockpit component for managing storage.  This package uses udisks.

%post storaged

if [ "$1" = 2 ] && [ -d /var/lib/cockpit/btrfs ]; then
    rm -rf --one-file-system  /var/lib/cockpit/btrfs || true
fi
%package -n cockpit-packagekit
Summary: Cockpit user interface for packages
BuildArch: noarch
Requires: cockpit-bridge >= %{required_base}
Requires: PackageKit
Recommends: python3-tracer
Requires: polkit
%description -n cockpit-packagekit
The Cockpit components for installing OS updates and Cockpit add-ons,
via PackageKit.

%files -f %{oreon_filedir}/main.list
%files -n cockpit-storaged -f %{oreon_filedir}/cockpit-storaged.list
%files -n cockpit-packagekit -f %{oreon_filedir}/cockpit-packagekit.list

%changelog

%autochangelog
