%global source0_hash 7b8488e687971ae56729ff4e2e5209ff8806cf8cd57718bfd7e521be130621b4
Name:           taskd
Version:        1.1.0
Release:        1%{?dist}
Summary:        Secure server providing multi-user, multi-client access to task data
License:        MIT
URL:            https://github.com/goldenHairDafo/taskd/
Source0:        http://taskwarrior.org/download/%{name}-%{version}.tar.gz
Source1:        taskd.service
Source2:        taskd-config
Source3:        taskd.xml
Source4:        README.Fedora
Requires:       gnutls-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libuuid-devel
BuildRequires:  shadow-utils
BuildRequires:  systemd
# /oreon:deps
%description
The Taskserver is a lightweight, secure server providing multi-user,
multi-client access to task data.  This allows true syncing between desktop and
mobile clients.

Users want task list access from multiple devices running software of differing
sophistication levels to synchronize data seamlessly.  Synchronization requires
the ability to exchange transactions between devices that may not have
continuous connectivity, and may not have feature parity.

The Taskserver provides this and builds a framework to go several steps beyond
merely synchronizing data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

cp -a %{SOURCE4} .

# Create a sysusers.d config file
cat >taskd.sysusers.conf <<EOF
u taskd - 'Task Server system user' %{_sharedstatedir}/taskd/ /usr/bin/sh
EOF

%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_sharedstatedir}/taskd/
mkdir -p %{buildroot}%{_sysconfdir}/pki/taskd/
cp -a pki/generate* %{buildroot}%{_sysconfdir}/pki/taskd/.
cp -a pki/vars %{buildroot}%{_sysconfdir}/pki/taskd/.
cp -a pki/README %{buildroot}%{_sysconfdir}/pki/taskd/.
mkdir -p %{buildroot}%{_localstatedir}/log/taskd/
mkdir -p %{buildroot}%{_unitdir}/
cp -a %{SOURCE1} %{buildroot}%{_unitdir}/taskd.service
mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services
cp -a %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/taskd.xml
mkdir -p %{buildroot}%{_sharedstatedir}/taskd/orgs/
cp -a %{SOURCE2} %{buildroot}%{_sharedstatedir}/taskd/config
rm -r %{buildroot}%{_datadir}/doc/taskd/
install -m0644 -D taskd.sysusers.conf %{buildroot}%{_sysusersdir}/taskd.conf
%oreon_autofiles main

%pre

%post

%systemd_post taskd.service
%preun

%systemd_preun taskd.service
%postun

%systemd_postun_with_restart taskd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
