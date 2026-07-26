%global source0_hash cc3dd31f9bf30f6ec11c5153da3c606df7545f3cd90bfb90ce6bd4c48e717aaf

%global pypi_name pytest-testmon

Name:           python-%{pypi_name}
Version:        2.1.4
Release:        %autorelease
Summary:        A py.test plug-in which executes only tests affected by recent changes
License:        MIT
URL:            http://testmon.org/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-coverage
#BuildRequires:  python3-unittest_mixins

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%package -n     python3-%{pypi_name}
Summary:        A py.test plug-in which executes only tests affected by recent changes
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pytest
Requires:       python3-coverage
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

This a Python 3 version of the package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest_testmon-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files testmon

%check
# This project doesn't appear to have tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
