%global source0_hash 69383f2c2a72b68dff0ec564358280bed8e2a5e9971e9871b8ff4d7c978ec9f5

%bcond tests 1
%global forgeurl https://github.com/repo-helper/hatch-requirements-txt

Name:           python-hatch-requirements-txt
Version:        0.4.1
%forgemeta
Release:        9%{?dist}
Summary:        Hatchling plugin to read project dependencies from requirements.txt

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Update tests for latest hatchling [i.e., 1.22.x]
# %%{forgeurl}/commit/1aa21b86db3503ed46683fa7af748d7aa1e853e1
# Cherry-picked to 0.4.1; changes to files in .github/ managed by repo_helper
# omitted.
Patch:          0001-Update-tests-for-latest-hatchling.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist coincidence}
BuildRequires:  %{py3_dist pkginfo}
BuildRequires:  %{py3_dist pytest}
%endif

%description
%{summary}.

%package -n python3-hatch-requirements-txt
Summary:        %{summary}

%description -n python3-hatch-requirements-txt
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{forgesetupargs}
# pytest-timeout is not needed to run tests in the RPM build environment
sed -i '/^timeout =/d' tox.ini
# Remove unnecessary shebangs
find hatch_requirements_txt/ -type f ! -executable -name '*.py' -print \
    -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hatch_requirements_txt

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-hatch-requirements-txt -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
