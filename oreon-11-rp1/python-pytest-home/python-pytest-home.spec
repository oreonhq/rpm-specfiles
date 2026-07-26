%global source0_hash 602151ce28186322507c7bbf1688acd567ecc00ccde37ead8946ed4ff70fd55b

Name:           python-pytest-home
Version:        0.6.0
Release:        %autorelease
Summary:        A temporary home directory fixture

License:        MIT
URL:            https://github.com/jaraco/pytest-home
Source:         %{pypi_source pytest_home}

BuildArch:      noarch
BuildRequires:  python3-devel
# for tests
BuildRequires:  git-core

%global _description %{expand:
Configures the home directory to a temporary directory,
hiding the user's dotfiles and other home-bound state.

Before the fixture is enacted, home resolves to the user's
usual home dir.}

%description %_description

%package -n python3-pytest-home
Summary:        %{summary}

%description -n python3-pytest-home %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest_home-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_home

%check
mv pytest_home _pytest_home
%pytest

%files -n python3-pytest-home -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
