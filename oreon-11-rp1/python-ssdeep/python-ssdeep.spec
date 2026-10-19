%global source0_hash 6f984a1248ee6b434bab0e2b274621f1888d81b8241858d30f981214263b17fa
%global pypi_name ssdeep
%global pypi_description A straightforward Python module for ssdeep by Jesse Kornblum, \
which is a library for computing context triggered piecewise hashes (CTPH). \
Also called fuzzy hashes, CTPH can match inputs that have homologies. \
Such inputs have sequences of identical bytes in the same order, although \
bytes in between these sequences may be different in both content and length.
Name: python-%{pypi_name}
Summary:        Python wrapper for the ssdeep library
License: LGPL-3.0-or-later
Version: 3.4.1
Release:        7%{?dist}
URL: https://github.com/DinoTools/python-ssdeep/
Source0:        https://github.com/DinoTools/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
Patch: 0001-Remove-pytest-runner-from-setup_requires.patch
Patch: 0002-Replace-tests_require-with-a-test-extra.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.4.1
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-ssdeep = %{version}-%{release}
# /oreon:deps
%description
%{pypi_description}

%package -n python3-%{pypi_name}
Summary:        Python wrapper for the ssdeep library
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

%build

%pyproject_wheel
pushd docs/
make man
make html
%install
%pyproject_install
install -d -m 755 %{buildroot}%{_mandir}/man5/
install -m 644 docs/build/man/pythonssdeep.1 %{buildroot}%{_mandir}/man5/python3-%{pypi_name}.5
%oreon_autofiles main usr/lib/python3*/site-packages/ssdeep* usr/lib64/python3*/site-packages/ssdeep* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-ssdeep -f %{oreon_filedir}/python3-ssdeep.list
%files -n python3-ssdeep-doc -f %{oreon_filedir}/python3-ssdeep-doc.list

%changelog

%autochangelog
