%global source0_hash 7a48db711a89c04937647093ce97e13d75d5350cb3e087e9058cdd5228b52873

%global srcname resalloc-openstack
%global pkgname resalloc_openstack

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with python2
%global default_sitelib %python3_sitelib
%global python python3
%global pythonpfx python3
%else
%bcond_without python2
%global default_sitelib %python2_sitelib
%global python python2
%global pythonpfx python
%endif

Name:       %srcname
Summary:    Resource allocator scripts for OpenStack
Version:    9.8
Release:    10%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://github.com/praiskup/resalloc-openstack
BuildArch:  noarch

BuildRequires: %pythonpfx-devel
BuildRequires: %pythonpfx-setuptools
BuildRequires: %python-argparse-manpage

Requires: %pythonpfx-cinderclient
Requires: %pythonpfx-glanceclient
Requires: %pythonpfx-keystoneauth1
Requires: %pythonpfx-neutronclient
Requires: %pythonpfx-novaclient

Source0: https://github.com/praiskup/%name/releases/download/v%version/%name-%version.tar.gz

%description
Resource allocator spawner/terminator scripts for OpenStack virtual machines,
designed so they either allocate all the sub-resources, or nothing (in case of
some failure).  This is especially useful if working with older OpenStack
deployments which all the time keep orphaned servers, floating IPs, volumes,
etc. dangling around.

These scripts are primarily designed to be used with resalloc-server.rpm, but in
general might be used separately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%if %{with python2}
%py2_build
%else
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%else
%py3_install
%endif

%check

%files
%license COPYING
%doc README
%{_bindir}/%{name}-*
%_mandir/man1/%{name}-*.1*
%{default_sitelib}/%{pkgname}
%{default_sitelib}/%{pkgname}-*.egg-info

%changelog
%autochangelog
