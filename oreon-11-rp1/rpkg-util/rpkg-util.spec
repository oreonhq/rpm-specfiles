%global source0_hash d18d6ff744a8317f7ce4710359a0543d59e570a5a2c6b4cd0fef2c48d7ba2dbf

# vim: syntax=spec

%if 0%{?fedora} || 0%{?rhel} > 7
%global python          /usr/bin/python3
%global python_build    %py3_build
%global python_install  %py3_install
%global python_sitelib  %python3_sitelib
%else
%global python          /usr/bin/python2
%global python_build    %py2_build
%global python_install  %py2_install
%global python_sitelib  %python2_sitelib
%endif

Name: rpkg-util
Version: 3.3
Release: 8%{?dist}
Summary: RPM packaging utility
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#55d05bb00449c2816114732e70911b53bbf97c42:
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util
# git checkout rpkg-util-3.3-1
# ./rpkg spec --sources
Source0: rpkg-util-55d05bb0.tar.gz
# upstream is deprecated, probably not worth forwarding
Patch0:  rpkg-util-rm-python-mock-usage.diff

BuildArch: noarch

%description
This package contains the rpkg utility. We are putting
the actual 'rpkg' package into a subpackage because there already
exists package https://src.fedoraproject.org/rpms/rpkg. That package,
however, does not actually produce rpkg rpm whereas rpkg-util does.

%package -n rpkg
Summary: RPM packaging utility
BuildArch: noarch

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-munch
BuildRequires: python3-rpm-macros
BuildRequires: python3-cached_property
BuildRequires: python3-rpm
BuildRequires: python3-pycurl
Requires: python3-cached_property
Requires: python3-munch
Requires: python3-rpm
Requires: python3-pycurl
# https://bugzilla.redhat.com/show_bug.cgi?id=2035475
Requires: python3-setuptools
%else
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
%endif

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

%files -n rpkg
%{!?_licensedir:%global license %doc}
%license LICENSE
%{python_sitelib}/*

%config(noreplace) %{_sysconfdir}/rpkg.conf
%{_datadir}/bash-completion/completions/rpkg.bash

%{_bindir}/rpkg
%{_mandir}/*/*

%changelog
%autochangelog
