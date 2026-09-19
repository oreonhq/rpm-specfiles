%global source0_hash 4b26ff4e7110db76eeb6f5a7b64a82623839d595c2038eeda662f2a2db78e97c

%global pkgname linecache2

# For bootstrapping Python
%bcond_without tests

Name:           python-%{pkgname}
Version:        1.0.0
Release:        48%{?dist}
Summary:        Backport of the linecache module

# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            https://github.com/testing-cabal/linecache2
Source0:        http://pypi.python.org/packages/source/l/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# Test dependencies
%if %{with tests}
BuildRequires:  python3-fixtures
%endif

%global _description\
A backport of linecache to older supported Pythons.\

%description %_description

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

%if %{with tests}
%check
mv tests %{pkgname}/
%{__python3} -m unittest -v
mv %{pkgname}/tests .
%endif

%files -n python3-%{pkgname}
%doc AUTHORS ChangeLog README.rst
%{python3_sitelib}/*

%changelog
%autochangelog
