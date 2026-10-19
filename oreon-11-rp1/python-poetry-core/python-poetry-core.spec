%global source0_hash e5a6fa94749ba460c56898d2b9649e3779b9f20f225d75be2fdff0ec43a3449d
%bcond tests %{undefined rhel}
Name:           python-poetry-core
Version:        2.5.0
Release:        1%{?dist}
Summary:        Poetry PEP 517 Build Backend
License:        MIT
URL:            https://github.com/python-poetry/poetry-core
Source0:        https://github.com/python-poetry/poetry-core/archive/%{version}/poetry-core-%{version}.tar.gz
Patch:          poetry-core-2.2.1-devendor.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-poetry-core = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-poetry-core
Summary:        Poetry PEP 517 Build Backend
Conflicts:      python%{python3_version}dist(poetry) < 1.1
%description -n python3-poetry-core

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n poetry-core-%{version}

# Assert the tomli dependency from the devendor patch is conditional
%{python3} -c "import tomllib; t = tomllib.load(open('pyproject.toml', 'rb')); assert t['tool']['poetry']['dependencies']['tomli']['python'] == '<3.11'"

%build

rm -r src/poetry/core/_vendor
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-poetry-core usr/lib/python3*/site-packages/poetry_core* usr/lib64/python3*/site-packages/poetry_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/poetry_core* usr/lib64/python3*/site-packages/poetry_core* usr/bin/*

%check

%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif
%files
%files -n python3-poetry-core -f %{oreon_filedir}/python3-poetry-core.list

%changelog

%autochangelog
