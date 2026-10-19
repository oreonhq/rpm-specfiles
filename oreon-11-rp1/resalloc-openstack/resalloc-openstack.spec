%global source0_hash 7a48db711a89c04937647093ce97e13d75d5350cb3e087e9058cdd5228b52873
%global srcname resalloc-openstack
%global pkgname resalloc_openstack
%bcond_without python2
%global default_sitelib %python2_sitelib
%global python python2
%global pythonpfx python
Name:       %srcname
Summary:        Resource allocator scripts for OpenStack
Version:    9.10
Release:        1%{?dist}
License:    GPL-2.0-or-later
URL:        https://github.com/praiskup/resalloc-openstack
BuildArch:  noarch
Requires: %pythonpfx-cinderclient
Requires: %pythonpfx-glanceclient
Requires: %pythonpfx-keystoneauth1
Requires: %pythonpfx-neutronclient
Requires: %pythonpfx-novaclient
Source0:        https://github.com/praiskup/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-argparse-manpage
# /oreon:deps
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
%oreon_autofiles main
%endif
%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
