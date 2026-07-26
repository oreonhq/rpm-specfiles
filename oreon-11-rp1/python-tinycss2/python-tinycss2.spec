%global source0_hash d339d2b616ba90ccce58da8495a78f46e55d4d25f9fd71dfd526f07e7d53f957

%global srcname tinycss2

Name:           python-%{srcname}
Version:        1.5.1
Release:        2%{?dist}
Summary:        Low-level CSS parser for Python

License:        BSD-3-Clause
URL:            https://www.courtbouillon.org/tinycss2/
Source0:        %{pypi_source tinycss2}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# The test extra contains linters, we cherry-pick only what we need:
BuildRequires:  python3-pytest

%description
tinycss2 is a modern, low-level CSS parser for Python. tinycss2 is a rewrite of
tinycss with a simpler API, based on the more recent CSS Syntax Level 3
specification.

%package     -n python3-%{srcname}
Summary:        Low-level CSS parser for Python 3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
tinycss2 is a modern, low-level CSS parser for Python. tinycss2 is a rewrite of
tinycss with a simpler API, based on the more recent CSS Syntax Level 3
specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{pytest}
# remove files which are only required for unit tests (including test.pyc/.pyo)
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/css-parsing-tests
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/test.py
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/__pycache__/test.*.py?

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
%autochangelog
