%global source0_hash c2b2726bd7aa9217b6c50b621fef5b2ae5def4d55b779c9e0694c15e0a8517ba

Name:           python-pyproject-api
Version:        1.10.1
Release:        %autorelease
Summary:        API to interact with the python pyproject.toml based projects

License:        MIT
URL:            https://pyproject-api.readthedocs.org
Source:         %{pypi_source pyproject_api}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
API to interact with the python pyproject.toml based projects.}

%description %_description

%package -n     python3-pyproject-api
Summary:        %{summary}

%description -n python3-pyproject-api %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pyproject_api-%{version}
# Remove unneeded testing deps
sed -i "/covdefaults/d;/pytest-cov/d" pyproject.toml
# Remove version constraints
sed -i 's/"setuptools>=.*"/"setuptools"/' pyproject.toml
sed -i 's/"pytest>=.*"/"pytest"/' pyproject.toml
sed -i 's/"pytest-mock>=.*"/"pytest-mock"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -g test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyproject_api

%check
# Skip test_setuptools_prepare_metadata_for_build_wheel
# see https://github.com/tox-dev/pyproject-api/issues/153
%pytest -k "not test_setuptools_prepare_metadata_for_build_wheel"

%files -n python3-pyproject-api -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
