%global source0_hash 43b695c90d888fee2e66365a01d508aa5792727d7968892d790cebc0dd79afc9

%bcond tests 1

Name:           python-pytest-split
Summary:        Pytest plugin to split the test suite into sub-suites
Version:        0.11.0
Release:        %autorelease

License:         MIT
URL:             https://github.com/jerry-git/pytest-split
Source:          %{url}/archive/refs/tags/%{version}/pytest-split-%{version}.tar.gz
BuildArch:       noarch

BuildRequires:   python3-devel
BuildRequires:   help2man
BuildRequires:   tomcli
BuildRequires:   python3dist(poetry-core)
BuildRequires:   python3dist(pytest)

%global _description %{expand:
Pytest plugin which splits the test suite to equally sized
sub suites based on test execution time.}

%description %_description

%package -n python3-pytest-split
Summary:        %{summary}

%description -n python3-pytest-split %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest-split-%{version}
# Remove pytest configuration to avoid dependency on coverage (pytest-cov)
tomcli set pyproject.toml del 'tool.pytest.ini_options'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pytest_split
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH="%{buildroot}%{python3_sitelib}" help2man \
    --version-string %{version} \
    %{buildroot}%{_bindir}/slowest-tests | \
    gzip > %{buildroot}%{_mandir}/man1/slowest-tests.1.gz

%check
%pyproject_check_import

%if %{with tests}
%pytest tests
%endif

%files -n python3-pytest-split -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{_bindir}/slowest-tests
%{_mandir}/man1/slowest-tests.1.*

%changelog
%autochangelog
