%global source0_hash 12574ec97dfc768a09711894a535ab07485549d0063e1ded5b6008fb355b2f4b

%bcond tests 1
%global forgeurl https://github.com/python-coincidence/coincidence

Name:           python-coincidence
Version:        0.6.6
%forgemeta
Release:        7%{?dist}
Summary:        Helper functions for pytest

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          Use-setuptools-instead-of-whey-as-build-backend.patch
Patch:          test_regressions-use-tomllib-instead-of-toml.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description
%{summary}.

%package -n python3-coincidence
Summary:        %{summary}

%description -n python3-coincidence
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{forgesetupargs}
# pytest-timeout is not needed to run tests in the RPM build environment
sed -i '/^timeout =/d' tox.ini
# Remove unnecessary shebangs
find coincidence/ -type f ! -executable -name '*.py' -print \
    -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files coincidence

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-coincidence -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
