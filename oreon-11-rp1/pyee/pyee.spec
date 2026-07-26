%global source0_hash 0d09a47412dc50f52647a30499ec50e1c1248ca2d4d8d842fd3604fa76f083ad

# Tests don't currently pass
%bcond_with tests

Name:      pyee
Version:   13.0.0
Release:   5%{?dist}
Summary:   A port of node.js's EventEmitter to python
License:   MIT
URL:       https://pypi.python.org/pypi/pyee
Source0:   https://github.com/jfhbrook/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-sphinx
%if %{with tests}
BuildRequires: python3-flake8
BuildRequires: python3-pytest
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-pytest-runner
BuildRequires: python3-pytest-trio
%endif

%description
A port of node.js's EventEmitter to python.

%package -n python3-ee
Summary:       A port of node.js's EventEmitter to python
%{?python_provide:%python_provide python3-ee}

%description -n python3-ee
A port of node.js's EventEmitter to python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
# currently segfaults
# %%py3_check_import pyee
%if %{with tests}
%pytest -v
%endif

%files -n python3-ee -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
