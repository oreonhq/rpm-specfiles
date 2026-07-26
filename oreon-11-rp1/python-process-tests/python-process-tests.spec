%global source0_hash e5d57dea7161251e91cadb84bf3ecc85275fb121fd478e579f800777b1d424bd

%global srcname process-tests

Name:           python-%{srcname}
Version:        3.0.0
Release:        %autorelease
Summary:        Tools for testing processes

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ionelmc/python-process-tests
Source0:        https://pypi.python.org/packages/source/p/process-tests/process-tests-%{version}.tar.gz

BuildArch:      noarch

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l process_tests

%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.rst

%changelog
%autochangelog
