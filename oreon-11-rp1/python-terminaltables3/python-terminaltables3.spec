%global source0_hash 44df92e82b45fadf4e6af8e3a77214cce455a4e1ee66c3f8c871988e1f58f776
%bcond tests 0
Name:           python-terminaltables3
Version:        4.0.0
Release:        1%{?dist}
Summary:        Generate simple tables in terminals from a nested list of strings. Fork of terminaltables.
License:        MIT
URL:            https://github.com/matthewdeanmartin/terminaltables3
Source0:        https://github.com/matthewdeanmartin/terminaltables3/archive/v%{version}/terminaltables3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-terminaltables3 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-terminaltables3
Summary:        Generate simple tables in terminals from a nested list of strings. Fork of terminaltables.
%description -n python3-terminaltables3

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir terminaltables3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-terminaltables3 usr/lib/python3*/site-packages/terminaltables3* usr/lib64/python3*/site-packages/terminaltables3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/terminaltables3* usr/lib64/python3*/site-packages/terminaltables3* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%pytest
%endif
%files
%files -n python3-terminaltables3 -f %{oreon_filedir}/python3-terminaltables3.list

%changelog

%autochangelog
