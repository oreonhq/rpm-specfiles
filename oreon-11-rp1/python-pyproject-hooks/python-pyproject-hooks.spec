%global source0_hash 1e859bd5c40fae9448642dd871adf459e5e2084186e8d2c2a79a824c970da1f8

# Needed for Python bootstrap
%bcond_without tests

Name:           python-pyproject-hooks
Version:        1.2.0
Release:        %autorelease
Summary:        Wrappers to call pyproject.toml-based build backend hooks

# SPDX
License:        MIT
URL:            https://pypi.org/project/pyproject_hooks/
Source:         %{pypi_source pyproject_hooks}

# Upstream fix for compatibility with Python 3.15
Patch:          f230da76.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a low-level library for calling build-backends in
pyproject.toml-based project. It provides the basic functionality
to help write tooling that generates distribution files from
Python projects.}


%description %_description

%package -n     python3-pyproject-hooks
Summary:        %{summary}

%description -n python3-pyproject-hooks %_description


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n pyproject_hooks-%{version}
sed -i "/flake8/d" dev-requirements.txt


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:dev-requirements.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyproject_hooks


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-pyproject-hooks -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-1
- Prepare for Oreon 11 (RP1)
