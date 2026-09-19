%global source0_hash d27d95c0a7d2d29ecf097b257e3cc06f0303e140d51103a24e82c81af0784615

%define Uname MgaRepo

Name: mgarepo
Version: 1.13.2
Release: 37%{?dist}
Summary: Tools for Mageia repository access and management
# tarball needs to be created manually, since tags don't generate releases
# git clone git://git.mageia.org/software/build-system/mgarepo; cd mgarepo; git reset --hard %{version} && make dist
Source:  %{name}-%{version}.tar.xz

# Local fixes to upstream
Patch0500: 0001-Fix-iterating-on-log-entries-with-Python-3.9.patch

# Fedora-specific patches
# Mageia's urpmi is not available in Fedora, so we force DNF for buildrpm command
Patch1000: 0001-buildrpm-Always-use-DNF.patch

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://gitweb.mageia.org/software/build-system/mgarepo/
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: subversion
Requires: openssh-clients
Requires: python3-rpm
Requires: python3-PyGithub >= 1.27.1
Requires: python3-httplib2
Requires: wget
BuildArch: noarch

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

%files
%doc README.BINREPO CHANGES %{name}-example.conf
%attr(0644,-,-) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-ssh
%{_datadir}/%{name}
%{_mandir}/*/*
%{python3_sitelib}/%{Uname}
%exclude %{python3_sitelib}/%{Uname}/plugins/ldapusers.py*
%exclude %{python3_sitelib}/%{Uname}/plugins/__pycache__/__init__*
%exclude %{python3_sitelib}/%{Uname}/plugins/__pycache__/ldapusers*
%{python3_sitelib}/*.egg-info
%{_datadir}/bash-completion/completions/%{name}

%files ldap
%doc README.LDAP
%{python3_sitelib}/%{Uname}/plugins/ldapusers.py*
%{python3_sitelib}/%{Uname}/plugins/__pycache__/__init__*
%{python3_sitelib}/%{Uname}/plugins/__pycache__/ldapusers*

%changelog
%autochangelog
