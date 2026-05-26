%global pypi_name funcsigs

# when bootstrapping Python 3, funcsigs needs to be rebuilt before sphinx
%bcond_without doc

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        42%{?dist}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/testing-cabal/funcsigs?
Source0:        https://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         no-unittest2.patch
# oreon url source checksums begin
%global source0_sha256 a7bb0f2cf3a3fd1ab2732cb49eba4252c2af4240442415b4abce3b87022a8f50
%global source0_file funcsigs-1.0.2.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%description
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.


%package -n     python3-%{pypi_name}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with doc}
BuildRequires:  python3-sphinx
%endif

%description -n python3-%{pypi_name}
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.

%if %{with doc}
%package -n python-%{pypi_name}-doc
Summary:        funcsigs documentation
%description -n python-%{pypi_name}-doc
Documentation for funcsigs
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/funcsigs-1.0.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a7bb0f2cf3a3fd1ab2732cb49eba4252c2af4240442415b4abce3b87022a8f50" || { echo "oreon: Source0 SHA256 mismatch for funcsigs-1.0.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?rhel} && 0%{?rhel} == 7
sed -i '/extras_require/,+3d' setup.py
%endif

%build
%py3_build

%if %{with doc}
# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install


%check
%{__python3} -m unittest tests.test_formatannotation
%{__python3} -m unittest tests.test_funcsigs
%{__python3} -m unittest tests.test_inspect

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.*.egg-info/

%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.2-42
- Prepare for Oreon 11 (RP1)
