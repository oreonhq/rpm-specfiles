%global source0_hash 77891101c94b75a8ca305453b879b318ab6001b370df02be2c0b6d1bb322db10

%global srcname pytest-astropy-header

Name: python-%{srcname}
Version: 0.2.2
Release: %autorelease
Summary: pytest plugin to add diagnostic info to the header of output

License: BSD-3-Clause
URL: https://github.com/astropy/pytest-astropy-header
Source0: %{pypi_source}
BuildRequires:  python3-devel

BuildArch: noarch

%global _description %{expand:
This plugin package provides a way to include information about the system, 
Python installation, and select dependencies in the header of the output 
when running pytest. It can be used with packages that are not affiliated 
with the Astropy project, but is optimized for use with 
astropy-related projects.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist setuptools_scm}

%description -n python3-%{srcname} 
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pytest_astropy_header

%check
%pyproject_check_import 

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
