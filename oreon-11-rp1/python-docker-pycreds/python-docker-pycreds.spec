%global source0_hash 6ce3270bcaf404cc4c3e27e4b6c70d3521deae82fb508767870fdbf772d584d4

# Created by pyp2rpm-1.1.2 and rewrote manually afterwards
%global pypi_name docker-pycreds

%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
# Disable python2 build by default
%bcond_with python2
%else
%bcond_with python3
%bcond_without python2
%endif

# the test suite is diabled b/c it needs docker-credential-secretservice binary
# and we don't have that now (Sep 2016) in Fedora
%bcond_with tests

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        28%{?dist}
Summary:        Python bindings for the docker credentials store API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/shin-/dockerpy-creds/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python bindings for the docker credentials store API

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Python bindings for the docker credentials store API

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six

%if %{with tests}
BuildRequires:  python2-pytest
%endif # tests

%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:  python2-six

%description -n python2-%{pypi_name}
Python bindings for the docker credentials store API
%endif # with python2

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        Python bindings for the docker credentials store API

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%if %{with tests}
BuildRequires:  python3-pytest
%endif # tests

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:  python3-six

%description -n python3-%{pypi_name}
Python bindings for the docker credentials store API

%endif # python3

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif # with python2
%if %{with python3}
%py3_build
%endif # with python3

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with python2}
%py2_install
%endif # with python2
%if %{with python3}
%py3_install
%endif # with python3

# we are not using setup.py test here b/c the project pins to specific versions
%check
# sanity test
%if %{with python2}
%{__python2} -c "import dockerpycreds"
%if %{with tests}
PYTHONPATH="${PWD}" py.test-%{python2_version} -vv tests/
%endif # tests
%endif # with python2

%if %{with python3}
%{__python3} -c "import dockerpycreds"
%if %{with tests}
PYTHONPATH="${PWD}" py.test-%{python3_version} -vv tests/
%endif # tests
%endif # python3

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.md
%license LICENSE
%{python2_sitelib}/dockerpycreds
%{python2_sitelib}/docker_pycreds-%{version}-py?.?.egg-info
%endif # with python2

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/dockerpycreds
%{python3_sitelib}/docker_pycreds-%{version}-py%{python3_version}.egg-info
%endif # python3

%changelog
%autochangelog
