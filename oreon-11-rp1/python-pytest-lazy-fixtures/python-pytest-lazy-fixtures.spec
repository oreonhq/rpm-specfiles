%global source0_hash 8684abfd4914ea01f1e2f7b24524739344421d8f3f12286fb3100fb5681e1181

%global pypi_name pytest-lazy-fixtures
%global package_dir_name pytest_lazy_fixtures

Name:           python-%{pypi_name}
Version:        1.4.1
Release:        %autorelease
Summary:        Library to use fixtures in @pytest.mark.parametrize

License:        MIT
URL:            https://github.com/dev-petrov/pytest-lazy-fixtures
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-lazy-fixtures/pytest_lazy_fixtures-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-poetry-core
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Use your fixtures in @pytest.mark.parametrize

This project was inspired by pytest-lazy-fixture.

Improvements that have been made in this project:

    You can use fixtures in any data structures
    You can access the attributes of fixtures
    You can use functions in fixtures}

%description %_description

%package -n python3-%{pypi_name}
Summary: Library to use fixtures in @pytest.mark.parametrize

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{package_dir_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_lazy_fixtures

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
