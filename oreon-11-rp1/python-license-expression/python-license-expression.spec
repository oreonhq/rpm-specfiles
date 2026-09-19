%global source0_hash d4c3c31c8f891829e81132ffdd1b935b41ab11b090ac40eaff78b7d2cf7c4892

Name:           python-license-expression
Version:        30.4.4
Release:        %autorelease
Summary:        Library to parse, compare, simplify and normalize license expressions

License:        Apache-2.0
URL:            https://github.com/nexB/license-expression
Source0:        %{url}/archive/v%{version}/license-expression-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
This module defines a mini language to parse, validate, simplify, normalize and
compare license expressions using a boolean logic engine.

This supports SPDX license expressions and also accepts other license naming
conventions and license identifiers aliases to resolve and normalize licenses.

Using boolean logic, license expressions can be tested for equality,
containment, equivalence and can be normalized or simplified.}

%description %{common_description}

%package -n python3-license-expression
Summary:        %{summary}

%description -n python3-license-expression %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n license-expression-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -i 's|setuptools_scm\[toml\]|setuptools_scm|' pyproject.toml
sed -i 's|setuptools_scm\[toml\]|setuptools_scm|' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files license_expression

%check
%pytest

%files -n python3-license-expression -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst

%changelog
%autochangelog
