%global source0_hash 934b0e6a39d95995062c193f7eaeed8a8ffa06ff1bcef4b62b0dc74a708bacc1

%global srcname pytest-dependency

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        Pytest plugin to manage dependencies of tests

License:        Apache-2.0
URL:            https://github.com/RKrahl/pytest-dependency
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This module is a plugin for the popular Python testing framework pytest.
It manages dependencies of tests: you may mark some tests as dependent from
other tests. These tests will then be skipped if any of the dependencies did
fail or has been skipped.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_dependency

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGES.rst

%changelog
%autochangelog
