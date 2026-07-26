%global source0_hash 7b8488e687971ae56729ff4e2e5209ff8806cf8cd57718bfd7e521be130621b4

Name:           taskd
Version:        1.1.0
Release:        28%{?dist}
Summary:        Secure server providing multi-user, multi-client access to task data
License:        MIT
URL:            https://github.com/goldenHairDafo/taskd/
Source0:        http://taskwarrior.org/download/%{name}-%{version}.tar.gz
Source1:        taskd.service
Source2:        taskd-config
Source3:        taskd.xml
Source4:        README.Fedora

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libuuid-devel
BuildRequires:  gnutls-devel
BuildRequires:  shadow-utils

%if 0%{?rhel} && 0%{?rhel} <= 6
# On rhel, we don't need systemd to build.  but we do on fedora.
# ...just to define some macros
%else
BuildRequires:  systemd
%endif

# For certificate generation
Requires:       gnutls-utils

# Systemd requires
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

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

# Users will keep their keys here, but we copy some helpful scripts too.
mkdir -p %{buildroot}%{_sysconfdir}/pki/taskd/
cp -a pki/generate* %{buildroot}%{_sysconfdir}/pki/taskd/.
cp -a pki/vars %{buildroot}%{_sysconfdir}/pki/taskd/.
cp -a pki/README %{buildroot}%{_sysconfdir}/pki/taskd/.

mkdir -p %{buildroot}%{_localstatedir}/log/taskd/

%if 0%{?rhel} && 0%{?rhel} <= 6
# EL6 and earlier needs a sysvinit script
# Also, no firewalld on old EL
%else
mkdir -p %{buildroot}%{_unitdir}/
cp -a %{SOURCE1} %{buildroot}%{_unitdir}/taskd.service

mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services
cp -a %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/taskd.xml
%endif

mkdir -p %{buildroot}%{_sharedstatedir}/taskd/orgs/
cp -a %{SOURCE2} %{buildroot}%{_sharedstatedir}/taskd/config

rm -r %{buildroot}%{_datadir}/doc/taskd/

install -m0644 -D taskd.sysusers.conf %{buildroot}%{_sysusersdir}/taskd.conf

%pre
# Systemd scriptlets
%if 0%{?rhel} && 0%{?rhel} <= 6
# No systemd for el6
%else

%post
%systemd_post taskd.service

%preun
%systemd_preun taskd.service

%postun
%systemd_postun_with_restart taskd.service

%endif

%files
%doc AUTHORS COPYING ChangeLog NEWS README README.Fedora
%{_bindir}/taskd
%{_bindir}/taskdctl
%{_mandir}/man1/taskd.1.*
%{_mandir}/man1/taskdctl.1.*
%{_mandir}/man5/taskdrc.5.*

%{_sysconfdir}/pki/taskd/generate*
%{_sysconfdir}/pki/taskd/vars
%{_sysconfdir}/pki/taskd/README

%dir %attr(0750, taskd, taskd) %{_sysconfdir}/pki/taskd/
%dir %attr(0750, taskd, taskd) %{_localstatedir}/log/taskd/

%dir %attr(0750, taskd, taskd) %{_sharedstatedir}/taskd/
%config(noreplace) %attr(0644, taskd, taskd) %{_sharedstatedir}/taskd/config
%dir %attr(0750, taskd, taskd) %{_sharedstatedir}/taskd/orgs/

%if 0%{?rhel} && 0%{?rhel} <= 6
# No sysvinit files for el6
%else
%{_unitdir}/taskd.service
%{_prefix}/lib/firewalld/services/taskd.xml
%endif
%{_sysusersdir}/taskd.conf

%changelog
%autochangelog
