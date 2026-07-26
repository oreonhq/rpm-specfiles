%global source0_hash 5f9e8a29b4a8e55ddd740216ddb0a8a5e97f1c9c7f6bfdac91863473a8c60f9c

Name:           python-pytest-gitconfig
Version:        0.9.0
Release:        %autorelease
Summary:        Provide a Git config sandbox for testing

License:        MIT
URL:            https://github.com/noirbizarre/pytest-gitconfig
VCS:            git:%{url}.git
Source:         %{pypi_source pytest_gitconfig}

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  git-core

%global _description %{expand:
Provide a Git config sandbox for testing.}

%description %_description

%package -n     python3-pytest-gitconfig
Summary:        %{summary}

%description -n python3-pytest-gitconfig %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest_gitconfig-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pytest_gitconfig

%check
%pyproject_check_import
%pytest

%files -n python3-pytest-gitconfig -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
