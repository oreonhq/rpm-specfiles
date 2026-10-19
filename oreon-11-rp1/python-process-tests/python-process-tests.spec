%global source0_hash e5d57dea7161251e91cadb84bf3ecc85275fb121fd478e579f800777b1d424bd
%global srcname process-tests
Name:           python-%{srcname}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Tools for testing processes
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ionelmc/python-process-tests
Source0:        https://pypi.python.org/packages/source/p/process-tests/process-tests-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 30.3.0
Requires:       python3-process-tests = %{version}-%{release}
# /oreon:deps
%description
Tools for testing processes.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Tools for testing processes
BuildRequires:  python%{python3_pkgversion}-devel
%description -n python%{python3_pkgversion}-%{srcname}
Tools for testing processes for Python 3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/process_tests* usr/lib64/python3*/site-packages/process_tests* usr/bin/*

%files
%files -n python3-process-tests -f %{oreon_filedir}/python3-process-tests.list

%changelog

%autochangelog
