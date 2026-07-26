%global source0_hash 235f0378671b1c41885a4b95229255f5cf3b9982820719653ee853badd234105

%bcond_without tests

%global pypi_name tcxreader
%global fullversion 0.4.11

%global _description %{expand:
This is a simple TCX parser / reader which can read Garmin TCX file
extension files. The following data is currently parsed:
longitude, latitude, elevation, time, distance, hr_value, cadence,
watts, TPX_speed (extension). It also works well with missing data!}

Name:           python-%{pypi_name}
Version:        %{?fullversion}
Release:        6%{?dist}
Summary:        tcxreader is a parser/reader for Garmin's TCX file format

# SPDX
License:        MIT
URL:            https://github.com/alenrajsp/tcxreader
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%endif

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc examples/ example_data/

%changelog
%autochangelog
