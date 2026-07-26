%global source0_hash 6f984a1248ee6b434bab0e2b274621f1888d81b8241858d30f981214263b17fa

%global pypi_name ssdeep

%global pypi_description A straightforward Python module for ssdeep by Jesse Kornblum, \
which is a library for computing context triggered piecewise hashes (CTPH). \
Also called fuzzy hashes, CTPH can match inputs that have homologies. \
Such inputs have sequences of identical bytes in the same order, although \
bytes in between these sequences may be different in both content and length.

Name: python-%{pypi_name}
Summary: Python wrapper for the ssdeep library
License: LGPL-3.0-or-later

Version: 3.4.1
Release: 7%{?dist}

URL: https://github.com/DinoTools/python-ssdeep/
# v3.4.1 is not available on PyPi, so we fetch from GitHub
Source0: %{URL}/archive/%{version}/python-%{pypi_name}-%{version}.tar.gz

# Remove pytest-runner from setup_requires
# https://github.com/DinoTools/python-ssdeep/pull/69
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
# Rebased on 3.4.1.
Patch: 0001-Remove-pytest-runner-from-setup_requires.patch
Patch: 0002-Replace-tests_require-with-a-test-extra.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: ssdeep-devel
BuildRequires: python3-sphinx

%description
%{pypi_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{pypi_description}

%package -n python3-%{pypi_name}-doc
Summary: Documentation for python3-%{pypi_name}
BuildArch: noarch

%description -n python3-%{pypi_name}-doc
This package contains documentation (in HTML and man page format)
for the ssdeep Python3 module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python-%{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

pushd docs/
make man
make html

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

install -d -m 755 %{buildroot}%{_mandir}/man5/
install -m 644 docs/build/man/pythonssdeep.1 %{buildroot}%{_mandir}/man5/python3-%{pypi_name}.5

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst CONTRIBUTING.rst

%files -n python3-%{pypi_name}-doc
%license LICENSE
%doc docs/build/html/*
%{_mandir}/man5/python3-%{pypi_name}.5*

%changelog
%autochangelog
