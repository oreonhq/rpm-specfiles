%global source2_hash a615bd439e01357e82ea1202bc08cd2a334994c9beb0424c29217f5afe21eb7e
%global source0_hash 36b5bcbe257a940c884f0d74321a47407baabab9e265e38859851c8311f6f0b0
%global manext .gz
%global forgeurl0 https://github.com/NetworkConfiguration/openresolv
Name:           openresolv
Version:        3.17.4
Release:        1%{?dist}
Summary:        DNS management framework
License:        LicenseRef-Callaway-BSD
URL:            https://roy.marples.name/projects/openresolv
VCS:            git:%{forgeurl0}
Source0:        %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xa785ed2755955d9e93ea59f6597f97ea9ad45549#/roy.marples.asc
Requires:       bash
BuildArch:      noarch
Provides:       resolvconf = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
/etc/resolv.conf is a file that holds the configuration for the local resolution of domain names.
Normally this file is either static or maintained by a local daemon, normally a DHCP daemon.
openresolv will make sure, that multiple processes (eg. dhcpcd, NetworkManager, openvpn)
can write the resolv.conf without overwriting each others changes.

openresolv can generate a combined resolv.conf or a configuration file for a local nameserver
(like unbound, dnsmasq or bind) that will route the dns requests according to the search domain.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
for F in *.in; do
  [ "$F" != "resolvconf.in" ] && sed -i -e '1 s,^#!/bin/sh$,#,' $F
done

%build

./configure --bindir=%{_sbindir} --libexecdir=%{_prefix}/lib/resolvconf
%make_build
%install
%make_install
mv %{buildroot}%{_sbindir}/resolvconf{,.%{name}}
mv %{buildroot}%{_mandir}/man8/resolvconf{,.%{name}}.8
touch %{buildroot}%{_sbindir}/resolvconf %{buildroot}%{_mandir}/man8/resolvconf.8%{?manext}
%oreon_autofiles main

%post

%{_sbindir}/update-alternatives \
  --install %{_sbindir}/resolvconf resolvconf %{_sbindir}/resolvconf.%{name} 30 \
  --slave %{_mandir}/man8/resolvconf.8%{?manext} resolvconf.8%{?manext} %{_mandir}/man8/resolvconf.%{name}.8%{?manext}
%postun

if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove resolvconf %{_sbindir}/resolvconf.%{name}
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
