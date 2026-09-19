%global source0_hash 3f5f3e9a28ffd7cf50bfc8e7f9ead54b5e54638e34e01f003340206373c4a443

%global __python __python3

%global gittag      0.7.1
#global commit      eb302484417d85cbf497958ba2a651f738ad7420

%global shortcommit %{?commit:%(c=%{commit}; echo ${c:0:7})}%{!?commit:%nil}
%global shortdir    %{?gittag}%{?shortcommit}
%global srcdir      %{?gittag}%{?commit}

# mageia 6- fix:
%{!?_userunitdir: %global _userunitdir /usr/lib/systemd/system}

#Suse fix:
%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           ddupdate
Version:        0.7.1
Release:        19%{?dist}
Summary:        Tool updating DNS data for dynamic IP addresses

Group:          Applications/System
License:        MIT
URL:            http://github.com/leamas/ddupdate
BuildArch:      noarch
Source0:        %{url}/archive/%{srcdir}/%{name}-%{shortdir}.tar.gz
Patch1:         0001-ddupdate_netrc_to_keyring-ddupdate-netrc-to-keyring.patch
Patch2:         0002-plugins-dtdns-Remove-service-seems-dead.patch
Patch3:         0003-Manpages-update.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  systemd
BuildRequires:  /usr/bin/pkg-config

Requires:       python%{python3_pkgversion}-keyring
Requires:       python%{python3_pkgversion}-requests
Requires:       /usr/sbin/ip
Requires:       sudo

%{?systemd_requires}

%description

A tool to update dynamic IP addresses typically obtained using DHCP
with dynamic DNS services such as changeip.com, duckdns.org or no-ip.com.
It makes it  possible to access a machine with a fixed name like
myhost.duckdns.org even if the ip address changes. ddupdate caches the
address, and only attempts the update if the address actually is changed.

The tool has a plugin structure with plugins for obtaining the actual
address (typically hardware-dependent) and to update it (service depen‐
dent). For supported services, it's a linux-centric, user-friendly and
flexible alternative to the ubiquitous ddclient.

ddupdate is distributed with systemd support to run at regular intervals,
and with NetworkManager templates to run when interfaces goes up or down.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{srcdir}
sed -i '/ExecStart/s|/usr/local|/usr|' systemd/ddupdate.service
sed -i 's|systemd_unitdir(),|"lib/systemd/user",|' setup.py

%build
%py3_build

%install
export FINAL_PREFIX=/
%py3_install
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/ddupdate/plugins

%files
%license LICENSE.txt
%doc README.md NEWS CONTRIBUTE.md CONFIGURATION.md
%{_bindir}/ddupdate
%{_bindir}/ddupdate-config
%{_bindir}/ddupdate-netrc-to-keyring
%{_userunitdir}/ddupdate*
%{_datadir}/ddupdate
%{_datadir}/bash-completion/completions/ddupdate
%{_mandir}/man8/ddupdate.8*
%{_mandir}/man8/ddupdate-config.8*
%{_mandir}/man8/ddupdate-netrc-to-keyring.8*
%{_mandir}/man5/ddupdate.conf.5*
%{python3_sitelib}/*

%changelog
%autochangelog
