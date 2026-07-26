%global source0_hash 147de8cb164f3fc9d7196967f109ab3c0b93ea3463ab50631e56438eab7b5adc

# Enable tests by default.
%bcond_without tests

%global pypi_name pytest-aiohttp

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        6%{?dist}
Summary:        Pytest plugin for aiohttp support

License:        Apache-2.0
URL:            https://github.com/aio-libs/pytest-aiohttp/
Source0:        %{pypi_source pytest_aiohttp}
BuildArch:      noarch

%description
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest_aiohttp-%{version} -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files pytest_aiohttp

%if %{with tests}
%check
%pytest -W ignore::DeprecationWarning
%endif

%files -n python3-%{pypi_name}  -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license LICENSE

%changelog
%autochangelog
