%global source0_hash b92087bebcb3782984116ca3723c7abdb2ab5e76a75ea9397f4a4c35a544fe18

%global pypi_name pytest-venv

Name:           python-%{pypi_name}
Version:        0.3
Release:        %autorelease
Summary:        py.test fixture for creating a virtual environment

# SPDX
License:        MIT
URL:            https://github.com/mmerickel/pytest-venv
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
pytest-venv is a simple pytest plugin that exposes a venv fixture.
The fixture is used to create a new virtual environment which can be used to
install packages and run commands inside tests.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(pytest)

%description -n python3-%{pypi_name}
pytest-venv is a simple pytest plugin that exposes a venv fixture.
The fixture is used to create a new virtual environment which can be used to
install packages and run commands inside tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
sed -i '/pytest-cov/d' setup.py

%generate_buildrequires
%pyproject_buildrequires -r -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_venv

%check
%pytest -k "not test_it_installs and not test_it_upgrades_dep"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
