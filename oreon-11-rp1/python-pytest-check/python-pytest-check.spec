%global source0_hash 33d87e28d5e49217f413277e1e0d267cd66c90a85a208944c44312c9c8e4ff74

Name:           python-pytest-check
Version:        2.5.4
Release:        %autorelease
Summary:        A pytest plugin that allows multiple failures per test 

License:        MIT
URL:            https://github.com/okken/pytest-check
Source:         %{pypi_source pytest_check}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A pytest plugin that allows multiple failures per test.}

%description %_description

%package -n python3-pytest-check
Summary:        %{summary}
%description -n python3-pytest-check %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest_check-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_check

%check
%pytest

%files -n python3-pytest-check -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
