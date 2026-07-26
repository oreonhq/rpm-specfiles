%global source0_hash ff8d2b6855f660cd23cd5ec79bd10264d39f24f6235773331b48e7fcd637d6cc

%global modname chai

Name:               python-%{modname}
Version:            1.1.2
Release:            40%{?dist}
Summary:            Easy to use mocking/stub/spy framework

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/chai
Source0:            http://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

%description
Chai provides a very easy to use api for mocking/stubbing your python
objects, patterned after the `Mocha <http://mocha.rubyforge.org/>`_ library
for Ruby.

%package -n         python%{python3_pkgversion}-%{modname}
Summary:            Easy to use mocking/stub framework

BuildRequires:      python%{python3_pkgversion}-devel
# For testing
BuildRequires:      python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{modname}
Chai provides a very easy to use api for mocking/stubbing your python
objects, patterned after the `Mocha <http://mocha.rubyforge.org/>`_ library
for Ruby.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

# Remove py2-only files.  They make our tests fail on py3.
rm chai/python2.py

# Remove py2-only file for the py3 tests.
rm tests/comparator_py2.py

# Replace unittest aliases removed in Python 3.12
sed -i \
    -e 's|assertEquals(|assertEqual(|' \
    -e 's|assertNotEquals(|assertNotEqual(|' \
    -e 's|assert_true(|assertTrue(|' \
    -e 's|assert_equals(|assertEqual(|' \
$(find tests -type f)

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pytest

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
