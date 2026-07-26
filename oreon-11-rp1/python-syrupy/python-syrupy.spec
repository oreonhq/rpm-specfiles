%global source0_hash bb013e1b375e8a3e51fad1055d22e9faf116d2e054934dded2462ef495b7ca90

Name:           python-syrupy
Version:        4.9.1
Release:        6%{?dist}
Summary:        Pytest snapshot plugin

License:        Apache-2.0
URL:            https://syrupy-project.github.io/syrupy/
Source:         https://github.com/syrupy-project/syrupy/archive/v%{version}/syrupy-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# for tests
BuildRequires:  python3-pytest-xdist

%global _description %{expand:
Syrupy is a pytest snapshot plugin. It enables developers
to write tests which assert immutability of computed results.}

%description %_description

%package -n python3-syrupy
Summary:        %{summary}

%description -n python3-syrupy %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n syrupy-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files syrupy

%check
%pytest

%files -n python3-syrupy -f %{pyproject_files}
%doc README.* CHANGELOG.md

%changelog
%autochangelog
