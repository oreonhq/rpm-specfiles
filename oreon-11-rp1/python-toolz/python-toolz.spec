%global source0_hash 72a3dcb7f8308e2074e915f81ebfae24d68f5efa19e798ce80f9c524b6d9a4da

%global srcname toolz
%global desc Toolz provides a set of utility functions for iterators, functions, and\
dictionaries. These functions interoperate well and form the building blocks\
of common data analytic operations. They extend the standard libraries\
itertools and functools and borrow heavily from the standard libraries of\
contemporary functional languages.\
\
Toolz provides a suite of functions which have the following functional\
virtues:\
\
    Composable: They interoperate due to their use of core data structures.\
    Pure: They don’t change their inputs or rely on external state.\
    Lazy: They don’t run until absolutely necessary, allowing them to support\
          large streaming data sets.\
\
Toolz functions are pragmatic. They understand that most programmers have\
deadlines.\
\
    Low Tech: They’re just functions, no syntax or magic tricks to learn\
    Tuned: They’re profiled and optimized\
    Serializable: They support common solutions for parallel computing\
\
This gives developers the power to write powerful programs to solve complex\
problems with relatively simple code. This code can be easy to understand\
without sacrificing performance. Toolz enables this approach, commonly\
associated with functional programming, within a natural Pythonic style\
suitable for most developers.

Name:           python-%{srcname}
Version:        1.0.0
Release:        7%{?dist}
Summary:        A functional standard library for Python

# The project is released under the BSD-3-Clause license.
# The _version.py file created by versioneer is licensed CC0-1.0; this will
# change to Unlicense when versioneer is updated to a newer version.
License:        BSD-3-Clause AND CC0-1.0
URL:            https://github.com/pytoolz/%{srcname}/
Source0:        https://github.com/pytoolz/toolz/archive/%{version}/%{srcname}-%{version}.tar.gz
# Add python 3.14 support
Patch:          %{url}/pull/592.patch
BuildArch:      noarch

%description
%{desc}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A functional standard library for Python %{python3_version}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l toolz tlz

%check
# shakespeare test downloads a file
%pytest -v -k 'not test_shakespeare'

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE.txt

%changelog
%autochangelog
