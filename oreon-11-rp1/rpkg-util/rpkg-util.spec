%global source0_hash d18d6ff744a8317f7ce4710359a0543d59e570a5a2c6b4cd0fef2c48d7ba2dbf
%global python          /usr/bin/python2
%global python_build    %py2_build
%global python_install  %py2_install
%global python_sitelib  %python2_sitelib
Name: rpkg-util
Version: 3.3
Release:        1%{?dist}
Summary:        RPM packaging utility
License: GPL-2.0-or-later
URL: https://pagure.io/rpkg-util.git
Source0:        rpkg-util-55d05bb0.tar.gz
Patch0:  rpkg-util-rm-python-mock-usage.diff
BuildArch: noarch
# oreon:deps
BuildRequires:  preproc
BuildRequires:  python-munch
BuildRequires:  python-pycurl
BuildRequires:  python2
BuildRequires:  python2-cached_property
BuildRequires:  python2-configparser
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-rpm-macros
BuildRequires:  python2-setuptools
BuildRequires:  rpkg-macros
BuildRequires:  rpm-python
# /oreon:deps
%description
This package contains the rpkg utility. We are putting
the actual 'rpkg' package into a subpackage because there already
exists package https://src.fedoraproject.org/rpms/rpkg. That package,
however, does not actually produce rpkg rpm whereas rpkg-util does.

%package -n rpkg
Summary: RPM packaging utility
BuildArch: noarch
BuildRequires: python2
BuildRequires: python2-setuptools
BuildRequires: python2-devel
BuildRequires: python2-mock
BuildRequires: python2-pytest
BuildRequires: python2-configparser
BuildRequires: python-munch
BuildRequires: python2-rpm-macros
BuildRequires: python2-cached_property
BuildRequires: rpm-python
BuildRequires: python-pycurl
Requires: python2-configparser
Requires: python2-cached_property
Requires: python-munch
Requires: rpm-python
Requires: python-pycurl
BuildRequires: preproc
BuildRequires: rpkg-macros
Requires: preproc
Requires: rpkg-macros
Requires: rpm-build
Requires: cpio
%description -n rpkg
This is an RPM packaging utility that can work with both DistGit
and standard Git repositories and handles packed directory content
as well as unpacked one.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -T -b 0 -q -n rpkg-util
%patch 0 -p1  

version=%version
version=${version//.${version#*.*.}/}
sed -i 's/version=.*/version="'$version'",/' setup.py

%check

PYTHON=%{python} ./unittests
%build

%python_build
%{python} man/rpkg_man_page.py > rpkg.1
%install
%{python_install}
sed -i '1 s|#.*|#!%{python}|' %{buildroot}%{_bindir}/rpkg
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 rpkg.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_datarootdir}/bash-completion/completions
cp -a rpkg.conf %{buildroot}%{_sysconfdir}/
cp -a rpkg.bash %{buildroot}%{_datarootdir}/bash-completion/completions/
%oreon_autofiles rpkg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rpkg -f %{oreon_filedir}/rpkg.list

%changelog

%autochangelog
