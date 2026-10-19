%global source0_hash d27d95c0a7d2d29ecf097b257e3cc06f0303e140d51103a24e82c81af0784615
%define Uname MgaRepo
Name: mgarepo
Version: 1.13.2
Release:        1%{?dist}
Summary:        Tools for Mageia repository access and management
Source0:        %{name}-%{version}.tar.xz
Patch0500: 0001-Fix-iterating-on-log-entries-with-Python-3.9.patch
Patch1000: 0001-buildrpm-Always-use-DNF.patch
License: GPL-2.0-or-later
URL: http://gitweb.mageia.org/software/build-system/mgarepo/
Requires: subversion
Requires: openssh-clients
Requires: python3-rpm
Requires: python3-PyGithub >= 1.27.1
Requires: python3-httplib2
Requires: wget
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Tools for Mageia repository access and management.

It is a fork of repsys :
<http://wiki.mandriva.com/en/Development/Packaging/Tools/repsys>

%package ldap
Summary: Plugin for retrieving maintainer information from LDAP for mgarepo
Requires: %{name} = %{version}-%{release}
Requires: python3-ldap3
%description ldap
A mgarepo plugin that allows retrieving maintainer information shown in
changelogs from a LDAP server.

See mgarepo --help-plugin ldapusers for more information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix requires for RPM Python bindings
sed -e "s/rpm-python/rpm/" -i setup.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mgarepo-ldap -f %{oreon_filedir}/mgarepo-ldap.list

%changelog

%autochangelog
