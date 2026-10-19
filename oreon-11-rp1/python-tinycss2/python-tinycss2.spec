%global source0_hash d339d2b616ba90ccce58da8495a78f46e55d4d25f9fd71dfd526f07e7d53f957
%global srcname tinycss2
Name:           python-%{srcname}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Low-level CSS parser for Python
License:        BSD-3-Clause
URL:            https://www.courtbouillon.org/tinycss2/
Source0:        https://files.pythonhosted.org/packages/source/t/tinycss2/tinycss2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-tinycss2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-tinycss2+doc
Summary:        Metapackage for python3-tinycss2 doc extras
Requires:       python3-tinycss2 = %{version}-%{release}
Provides:       python3dist(tinycss2[doc]) = %{version}-%{release}

%description -n python3-tinycss2+doc
Metapackage for python3-tinycss2 doc extras.

%package -n       python3-tinycss2+test
Summary:        Metapackage for python3-tinycss2 test extras
Requires:       python3-tinycss2 = %{version}-%{release}
Provides:       python3dist(tinycss2[test]) = %{version}-%{release}

%description -n python3-tinycss2+test
Metapackage for python3-tinycss2 test extras.

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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/tinycss2* usr/lib64/python3*/site-packages/tinycss2* usr/bin/*

%check

%{pytest}
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/css-parsing-tests
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/test.py
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/__pycache__/test.*.py?
%files
%files -n python3-tinycss2 -f %{oreon_filedir}/python3-tinycss2.list

%changelog

%autochangelog
