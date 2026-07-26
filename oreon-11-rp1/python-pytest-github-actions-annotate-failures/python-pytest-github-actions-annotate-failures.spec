%global source0_hash a2fbf58e8b97932303eb0f17aab932ce1f053f205837b7be8e1b6afd4fffeaf9

%global pypi_name pytest-github-actions-annotate-failures

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        %{autorelease}
Summary:        Pytest plugin to annotate failed tests in GitHub Actions

%global forgeurl https://github.com/pytest-dev/pytest-github-actions-annotate-failures
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Pytest plugin to annotate failed tests with a workflow command for
GitHub Actions.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_github_actions_annotate_failures

%check
# Test fails with pytest >= 7.4 (F40+)
%if %{fedora} >= 40
k="${k-}${k+ and }not test_annotation_pytest_error"
%endif

%pytest -v ${k+-k }"${k-}"

# Additional smoke test
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
