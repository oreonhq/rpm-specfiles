%global source0_hash 3104d4db450096c91f625320773d2d7314c7ef0c086cbf9202cd4a5f720c9aec
%global srcname fields
Name:           python-%{srcname}
Version:        5.0.0
Release:        28%{?dist}
Summary:        Container class boilerplate killer
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/%{name}
Source0:        https://github.com/ionelmc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-5.0.0-sphinx-1.3.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-py3doc-enhanced
# /oreon:deps
%description
Container class boilerplate killer.

Features:
- Human-readable __repr__
- Complete set of comparison methods
- Keyword and positional argument support. Works like a normal class - you can
  override just about anything in the subclass (eg: a custom __init__). In
  contrast, hynek/characteristic forces different call schematics and calls
  your __init__ with different arguments.

%package doc
Summary:        Documentation for '%{name}'
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx-theme-py3doc-enhanced
%description doc
HTML API documentation for the '%{srcname}' Python module.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Container class boilerplate killer
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-benchmark
Recommends:     %{name}-doc = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{srcname}
Container class boilerplate killer.

Features:
- Human-readable __repr__
- Complete set of comparison methods
- Keyword and positional argument support. Works like a normal class - you can
  override just about anything in the subclass (eg: a custom __init__). In
  contrast, hynek/characteristic forces different call schematics and calls
  your __init__ with different arguments.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/\[pytest\]/\[tool:pytest\]/' setup.cfg

%build

%py3_build
PYTHONPATH=$PWD/src sphinx-build -b html docs docs/_build/html
rm -rf docs/_build/html/.buildinfo docs/_build/html/.doctrees
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} \
  --ignore=tests/test_perf.py \
  tests
%files -f %{oreon_filedir}/main.list
%files -n python-fields-doc -f %{oreon_filedir}/python-fields-doc.list
%files -n python3-fields -f %{oreon_filedir}/python3-fields.list

%changelog

%autochangelog
