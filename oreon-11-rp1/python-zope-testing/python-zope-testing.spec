%global source0_hash 7b34133a8f4a7135f3732fa5ba31d9968e9b9029881157d2a24493356d7fd54a

%global _without_tests 1
%global modname zope.testing

# The upstream tarball got renamed with an underscore
# but the package name still has a dot in it.

# Break circular dependency on python-zope-testrunner
%bcond tests 1

Name:           python-zope-testing
Version:        6.0
Release:        %autorelease
Summary:        Zope Testing Framework
License:        ZPL-2.1
URL:            https://pypi.io/project/%{modname}
Source0:        https://pypi.io/packages/source/z/%{modname}/zope_testing-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%package -n python%{python3_pkgversion}-zope-testing
Summary:        Zope Testing Framework
%{?python_provide:%python_provide python%{python3_pkgversion}-zope-testing}

%description -n python%{python3_pkgversion}-zope-testing
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n zope_testing-%{version}

rm -rf %{modname}.egg-info

# Allow newer version of setuptools
sed -i 's/"setuptools [<=]= .*"/"setuptools"/' pyproject.toml
sed -i 's/setuptools [<=]= .*/setuptools/' tox.ini

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zope
# __init__.py* are not needed since .pth file is used
rm -f %{buildroot}%{python3_sitelib}/zope/__init__.py*

%check
%py3_check_import zope.testing
%if %{with tests}
%tox
%endif

%files -n python%{python3_pkgversion}-zope-testing -f %{pyproject_files}
%doc CHANGES.rst README.rst src/zope/testing/*.txt
%license COPYRIGHT.txt LICENSE.txt
%exclude %{python3_sitelib}/zope/testing/*.txt

%changelog
%autochangelog
