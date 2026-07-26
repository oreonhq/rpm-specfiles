%global source0_hash c4e181f1b525c931a318d4812fa8de656c2c8fb77fccf1571ecf0cc5fe8e7f8f

Name:           python-pytest-cases
Version:        3.9.1
Release:        %autorelease
Summary:        Separate test code from test cases in pytest

License:        BSD-3-Clause
URL:            https://pypi.org/project/pytest-cases/
Source0:        %{pypi_source pytest_cases}

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(makefun) > 1.7
BuildRequires:  python3dist(decopatch)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-harvest) > 1.10
BuildRequires:  python3dist(pytest-asyncio)

%description
%{summary}.

%package -n python3-pytest-cases
Summary: %{summary}

%description -n python3-pytest-cases
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest_cases-%{version}
cat >pyproject.toml <<EOF
[build-system]
requires = [
    "decopatch",
    "pytest-steps",
    "setuptools_scm",
    "pypandoc",
    "six"]
build-backend = "setuptools.build_meta"
EOF

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
PYTHONPATH=build/lib %{python3} -m pytest -v

%files -n python3-pytest-cases
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_cases/
%{python3_sitelib}/pytest_cases-%{version}.dist-info/

%changelog
%autochangelog
