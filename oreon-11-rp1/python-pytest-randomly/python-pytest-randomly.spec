%global source0_hash 1ca0b4bb6772ef8499459cf34a4e39910d157e49f49f0fa57e6dbe15143d7f9a

%bcond_without check

Name:           python-pytest-randomly
Version:        5.0.0
Release:        1%{?dist}
Summary:        Pytest plugin to randomly order tests and control random.seed
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source0:        https://github.com/pytest-dev/pytest-randomly/archive/%{version}/pytest-randomly-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Pytest plugin to randomly order tests and control random.seed.

%package -n     python3-pytest-randomly
Summary:        %{summary}

%description -n python3-pytest-randomly
Pytest plugin to randomly order tests and control random.seed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n pytest-randomly-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_randomly

%if %{with check}
%check
%pyproject_check_import
%pytest -p no:randomly -k 'not test_it_runs_before_stepwise and not test_model_bakery and not test_factory_boy and not test_faker and not test_numpy and not test_xdist'
%endif

%files -n python3-pytest-randomly -f %{pyproject_files}
%doc README.rst HISTORY.rst
%license LICENSE

%changelog
%autochangelog
