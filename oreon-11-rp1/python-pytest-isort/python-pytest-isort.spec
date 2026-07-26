%global source0_hash 8f0cd0809ee36354ce613f95a59e63a0ee6f0e87a3030b93b6082856f2e7011f

%global pypi_name pytest-isort

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        4%{?dist}
Summary:        Pytest plugin to check import ordering using isort

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/moccu/pytest-isort/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
py.test plugin to check import ordering using isort.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-isort
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
py.test plugin to check import ordering using isort.

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
%{pytest} -v tests

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/pytest_isort/
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
