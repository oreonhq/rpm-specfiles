%global source0_hash 4b26ff4e7110db76eeb6f5a7b64a82623839d595c2038eeda662f2a2db78e97c
%global pkgname linecache2
%bcond_without tests
Name:           python-%{pkgname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Backport of the linecache module
License:        LicenseRef-Callaway-Python
URL:            https://github.com/testing-cabal/linecache2
Source0:        http://pypi.python.org/packages/source/l/%{pkgname}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-pbr
# /oreon:deps
%description

%package     -n python3-%{pkgname}
Summary:        Backport of the linecache module
%description -n python3-%{pkgname}
A backport of linecache to older supported Pythons.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}
# tests shouldn't be installed
mv %{pkgname}/tests .

# use the standard library unittest module
sed -i 's/import unittest2 as unittest/import unittest/' tests/*.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

mv tests %{pkgname}/
%{__python3} -m unittest -v
mv %{pkgname}/tests .
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-linecache2 -f %{oreon_filedir}/python3-linecache2.list

%changelog

%autochangelog
