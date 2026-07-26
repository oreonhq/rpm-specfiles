%global source0_hash 05c08bf638cdd1ed66eb01738a1647c3c714737c3ec3abe009d2c1f793b4bb59

%global srcname pytest-remotedata
%global sum Pytest plugin for controlling remote data access

Name:           python-%{srcname}
Version:        0.4.1
Release:        11%{?dist}
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-remotedata
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a plugin for the pytest framework that allows developers
to control unit tests that require access to data from the internet. 

Many software packages provide features that require access to data from the
internet. These features need to be tested, but unit tests that access the
internet can dominate the overall runtime of a test suite. The pytest-remotedata
plugin allows developers to indicate which unit tests require access to the
internet, and to control when and whether such tests should execute as part of
any given run of the test suite.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_remotedata

%check
# Deselect tests that require internet
%pytest \
--deselect "test_strict_with_decorator.py::test_internet_access" \
--deselect "tests/test_strict_check.py::test_default_behavior" \
--deselect "tests/test_strict_check.py::test_strict_with_decorator[any]"

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
