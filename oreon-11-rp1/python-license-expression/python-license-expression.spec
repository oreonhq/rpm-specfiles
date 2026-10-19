%global source0_hash d4c3c31c8f891829e81132ffdd1b935b41ab11b090ac40eaff78b7d2cf7c4892
Name:           python-license-expression
Version:        30.4.4
Release:        1%{?dist}
Summary:        Library to parse, compare, simplify and normalize license expressions
License:        Apache-2.0
URL:            https://github.com/nexB/license-expression
Source0:        https://github.com/nexB/license-expression/archive/v%{version}/license-expression-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This module defines a mini language to parse, validate, simplify, normalize and
compare license expressions using a boolean logic engine.
This supports SPDX license expressions and also accepts other license naming
conventions and license identifiers aliases to resolve and normalize licenses.
Using boolean logic, license expressions can be tested for equality,
containment, equivalence and can be normalized or simplified.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 50
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6
Requires:       python3-license-expression = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-license-expression
Summary:        Library to parse, compare, simplify and normalize license expressions
%description -n python3-license-expression %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n license-expression-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -i 's|setuptools_scm\[toml\]|setuptools_scm|' pyproject.toml
sed -i 's|setuptools_scm\[toml\]|setuptools_scm|' setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-license-expression usr/lib/python3*/site-packages/license_expression* usr/lib64/python3*/site-packages/license_expression* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/license_expression* usr/lib64/python3*/site-packages/license_expression* usr/bin/*

%check

%pytest
%files
%files -n python3-license-expression -f %{oreon_filedir}/python3-license-expression.list

%changelog

%autochangelog
