%global source0_hash 6d9e3a3f690db54a42eb9e98591ec5e9731779d3650c39668a220982f587a699

# Whether to build extension modules with mypyc:
%bcond          mypyc 1

Name:           python-tomli
Version:        2.4.0
Release:        %autorelease
Summary:        A little TOML parser for Python

License:        MIT
URL:            https://pypi.org/project/tomli/
Source0:        https://github.com/hukkin/tomli/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%if %{with mypyc}
BuildRequires:  gcc
# scripts/use_setuptools.py uses tomli-w.
BuildRequires:  python3-tomli-w
%else
BuildArch:      noarch
%endif

# The test suite uses the stdlib's unittest framework, but we use %%pytest
# as the test runner.
BuildRequires:  python3-pytest

%global _description %{expand:
Tomli is a Python library for parsing TOML.
Tomli is fully compatible with TOML v1.0.0.}


%description %_description

%package -n python3-tomli
Summary:        %{summary}

%description -n python3-tomli %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n tomli-%{version}
%if %{with mypyc}
# Taken from .github/workflows/tests.yaml, uses tomli-w, required for mypyc.
%{python3} scripts/use_setuptools.py
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%if %{with mypyc}
export TOMLI_USE_MYPYC=1
%endif
%pyproject_wheel


%install
%pyproject_install
# There is a top-level <hash>_mypyc module:
# https://github.com/hukkin/tomli/issues/268
%pyproject_save_files tomli %{?with_mypyc:'*_mypyc'}


%check
%pyproject_check_import
%pytest


%files -n python3-tomli -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.0-1
- Prepare for Oreon 11 (RP1)
