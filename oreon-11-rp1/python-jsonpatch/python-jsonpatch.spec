%global pypi_name jsonpatch

Name:           python-%{pypi_name}
Version:        1.33
Release:        12%{?dist}
Summary:        Applying JSON Patches in Python

License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-patch
Source0:        https://pypi.io/packages/source/j/jsonpatch/%{pypi_name}-%{version}.tar.gz
# tarball from pypi does not include file tests.js required for a specific test.
# upstream issue https://github.com/stefankoegl/python-json-patch/issues/82
Patch0:         0001-Skip-unit-test-in-packaging.patch
# Avoid usage of unittest.makeSuite, removed from Python 3.13
Patch1:         https://github.com/stefankoegl/python-json-patch/pull/159.patch

BuildArch:      noarch

%description
Library to apply JSON Patches according to RFC 6902 - Python 2 build.

%package -n python3-%{pypi_name}
Summary:        Applying JSON Patches in Python 3

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-jsonpointer
Requires:       python3-jsonpointer

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Library to apply JSON Patches according to RFC 6902 - Python 3 build.

%prep
%setup -qn %{pypi_name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1


%build
%py3_build

%install
%py3_install
# remove jsondiff binary conflicting with python-jsondiff
# https://bugzilla.redhat.com/show_bug.cgi?id=2029805
rm %{buildroot}%{_bindir}/jsondiff
mv %{buildroot}%{_bindir}/jsonpatch %{buildroot}%{_bindir}/jsonpatch-%{python3_version}
ln -s ./jsonpatch-%{python3_version} %{buildroot}%{_bindir}/jsonpatch-3
ln -s ./jsonpatch-%{python3_version} %{buildroot}%{_bindir}/jsonpatch

%check
%{__python3} tests.py

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/jsonpatch
%{_bindir}/jsonpatch-3*
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.33-12
- Prepare for Oreon 11 (RP1)
