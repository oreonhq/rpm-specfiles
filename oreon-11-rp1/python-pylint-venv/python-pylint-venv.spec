%global source0_hash 3b05ed629731744ba4a8cf8dbe33db0d578416131143a43e9ee85c5004c977ab

Name:           python-pylint-venv
Version:        3.0.4
Release:        %autorelease
Summary:        Make pylint respect virtualenvs

%global forgeurl https://github.com/jgosmann/pylint-venv/
%global tag v%{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pylint

%global _description %{expand:
Pylint does not respect the currently activated virtualenv if it is not
installed in every virtual environment individually. This module provides a
Pylint init-hook to use the same Pylint installation with different virtual
environments.}

%description %_description

%package -n python3-pylint-venv
Summary:        %{summary}
%description -n python3-pylint-venv %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pylint_venv

%check
%{py3_test_envvars} test/test.sh
%pyproject_check_import

%files -n python3-pylint-venv -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGES.md

%changelog
%autochangelog
