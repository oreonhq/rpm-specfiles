%global source0_hash c1149011a3bec662d4dd92427197bd5d02546f380b3568eb6217efb743614309

%global pypi_name pytest-ordering

Name:           python-%{pypi_name}
Version:        0.6
Release:        23%{?dist}
Summary:        Plugin to run your pytest tests in a specific order

License:        MIT
URL:            https://github.com/ftobia/pytest-ordering
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Adapt tests to work with pytest 6.2+
Patch1:         %{url}/pull/76.patch

BuildArch:      noarch

%description
pytest-ordering is a pytest plugin to run your tests in any order that you
specify. It provides custom markers that say when your tests should run in
relation to each other. They can be absolute (i.e. first, or second-to-last)
or relative (i.e. run this test before this other test).

%dnl --------------------------------------------------------------------------

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
pytest-ordering is a pytest plugin to run your tests in any order that you
specify. It provides custom markers that say when your tests should run in
relation to each other. They can be absolute (i.e. first, or second-to-last)
or relative (i.e. run this test before this other test).

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%dnl --------------------------------------------------------------------------

%package -n     %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-alabaster

%description -n %{name}-doc
Documentation for %{name}.

%files -n %{name}-doc
%doc html
%license LICENSE

%dnl --------------------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs/source/ html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l pytest_ordering

%check
%pytest -k "not test_run_marker_registered"

%changelog
%autochangelog
