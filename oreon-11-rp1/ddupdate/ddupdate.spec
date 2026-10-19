%global source0_hash d6890cde2973f214d5cf2e6a30bde470e1c611c50ef030560017bb8a63778aaf
%global __python __python3
%global gittag      0.7.1
%global shortcommit %{?commit:%(c=%{commit}; echo ${c:0:7})}%{!?commit:%nil}
%global shortdir    %{?gittag}%{?shortcommit}
%global srcdir      %{?gittag}%{?commit}
%{!?_userunitdir: %global _userunitdir /usr/lib/systemd/system}
%{!?python3_pkgversion:%global python3_pkgversion 3}
Name:           ddupdate
Version:        0.7.1
Release:        1%{?dist}
Summary:        Tool updating DNS data for dynamic IP addresses
Group:          Applications/System
License:        MIT
URL:            http://github.com/leamas/ddupdate
BuildArch:      noarch
Source0:        http://github.com/leamas/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-ddupdate_netrc_to_keyring-ddupdate-netrc-to-keyring.patch
Patch2:         0002-plugins-dtdns-Remove-service-seems-dead.patch
Patch3:         0003-Manpages-update.patch
Requires:       python%{python3_pkgversion}-keyring
Requires:       python%{python3_pkgversion}-requests
Requires:       /usr/sbin/ip
Requires:       sudo
%{?systemd_requires}
# oreon:deps
BuildRequires:  /usr/bin/pkg-config
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
