%global source0_hash dc601ebe4a3c0368a8a25f9a104e9b41e3c0e77bc256832d20e9b9efcdcd6c5e

%global pypi_name pytest-datafiles

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        4%{?dist}
Summary:        A pytest plugin to create a 'tmpdir' containing predefined content

License:        MIT
URL:            https://github.com/omarkohl/pytest-datafiles
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This plugin allows you to specify one or several files/directories that are
copied to a temporary directory (tmpdir) before the execution of the test.
This means the original files are not modified and every test runs on its
own version of the same files.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This plugin allows you to specify one or several files/directories that are
copied to a temporary directory (tmpdir) before the execution of the test.
This means the original files are not modified and every test runs on its
own version of the same files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_datafiles.py
%{python3_sitelib}/*.dist-info/

%changelog
%autochangelog
