%global source0_hash b55ffaf0449790242feb4c56ab799ea7af92801a0a43f9e2f4f8af2ab24dfc4a
%bcond tests 1
Name:           python-immutables
Version:        0.21
Release:        1%{?dist}
Summary:        Immutable Collections
License:        Apache-2.0 AND 0BSD
URL:            https://github.com/MagicStack/immutables
Source0:        https://files.pythonhosted.org/packages/source/i/immutables/immutables-%{version}.tar.gz
%global common_description %{expand:
An immutable mapping type for Python.
The underlying datastructure is a Hash Array Mapped Trie (HAMT) used in
Clojure, Scala, Haskell, and other functional languages. This implementation is
used in CPython 3.7 in the contextvars module (see PEP 550 and PEP 567 for more
details).
Immutable mappings based on HAMT have O(log N) performance for both set() and
get() operations, which is essentially O(1) for relatively small mappings.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-immutables = %{version}-%{release}
# /oreon:deps
%package -n       python3-immutables+test
Summary:        Metapackage for python3-immutables test extras
Requires:       python3-immutables = %{version}-%{release}
Requires:       python3dist(flake8) >= 5.0
Requires:       python3dist(pycodestyle) >= 2.9
Requires:       python3dist(mypy) >= 1.4
Requires:       python3dist(pytest) >= 7.4
Provides:       python3dist(immutables[test]) = %{version}-%{release}

%description -n python3-immutables+test
Metapackage for python3-immutables test extras.

%description %{common_description}

%package -n python3-immutables
Summary:        Immutable Collections
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif
BuildRequires:  pythoncapi-compat-static
%description -n python3-immutables %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n immutables-%{version} -p 1

# don't install source files
sed -e '/include_package_data=/ s/True/False/' -i setup.py

# delete mypy tests to avoid that dependency
rm tests/conftest.py tests/test_mypy.py

# remove bundled pythoncapi-compat
rm -vf immutables/pythoncapi_compat.h

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-immutables usr/lib/python3*/site-packages/immutables* usr/lib64/python3*/site-packages/immutables* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/immutables* usr/lib64/python3*/site-packages/immutables* usr/bin/*

%check

%if %{with tests}
%pytest --verbose
%else
%pyproject_check_import
%endif
%files
%files -n python3-immutables -f %{oreon_filedir}/python3-immutables.list

%changelog

%autochangelog
