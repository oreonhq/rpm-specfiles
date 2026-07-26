%global source0_hash 60b7e97f36dc1ad8cceb38ce1de1489803cb16d892b67a1e858161dac4a2772d

Summary:          Gluster block storage utility
Name:             gluster-block
Version:          0.5
Release:          18%{?dist}
# Automatically converted from old format: GPLv2 or LGPLv3+ - review is highly recommended.
License:          GPL-2.0-only OR LGPL-3.0-or-later
URL:              https://github.com/gluster/gluster-block
Source0:          https://github.com/gluster/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:    pkgconfig(glusterfs-api)
BuildRequires:    pkgconfig(json-c)
BuildRequires:    help2man >= 1.36
BuildRequires:    libtirpc-devel
BuildRequires:    rpcgen
BuildRequires:    systemd
# tarball releases require running ./autogen.sh
BuildRequires:    automake, autoconf, libtool, git
BuildRequires: make

Requires:         tcmu-runner >= 1.1.3
Requires:         targetcli >= 2.1.fb49
Requires:         python3-rtslib >= 2.1.fb69
Requires:         rpcbind

%{?systemd_requires}

%description
gluster-block is a CLI utility, which aims at making gluster backed block
storage creation and maintenance as simple as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
echo %{version} > VERSION
./autogen.sh
%configure
%make_build

%install
%make_install
touch %{buildroot}%{_sharedstatedir}/gluster-block/gb_upgrade.status

%post
%systemd_post gluster-block-target.service gluster-blockd.service

%preun
%systemd_preun gluster-block-target.service gluster-blockd.service

%postun
%systemd_postun_with_restart gluster-block-target.service gluster-blockd.service

%files
%license COPYING-GPLV2 COPYING-LGPLV3
%doc README.md
%{_sbindir}/gluster-block
%{_sbindir}/gluster-blockd
%doc %{_mandir}/man8/gluster-block*.8*
%{_unitdir}/gluster-blockd.service
%{_unitdir}/gluster-block-target.service
%config(noreplace) %{_sysconfdir}/sysconfig/gluster-blockd
%config(noreplace) %{_sysconfdir}/logrotate.d/gluster-block
%{_libexecdir}/gluster-block
%dir %{_localstatedir}/log/gluster-block
%dir %{_sharedstatedir}/gluster-block
%ghost %{_sharedstatedir}/gluster-block/gb_upgrade.status
%config(noreplace) %{_sharedstatedir}/gluster-block/gluster-block-caps.info

%changelog
%autochangelog
