%global source0_hash 47bc10e5df23bb1f0d3ee493a26cb8d1d99e179884aabff62d3e51033b6a73ce

%global pypi_name DateTimeRange
%global module_name datetimerange

Name:           python-%{module_name}
Version:        1.2.0
Release:        14%{?dist}
Summary:        Python module DateTimeRange

License:        MIT
URL:            https://github.com/thombashi/DateTimeRange
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-typepy

#test requirements
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz

%global _description %{expand:
DateTimeRange is a Python library to handle a time range. e.g. check whether
a time is within the time range, get the intersection of time ranges,
truncating a time range, iterate through a time range, and so forth.}

%description %_description

%package -n     python3-%{module_name}
Summary:        %{summary}
 
%description -n python3-%{module_name}
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module_name}

%check
%pytest -v

%files -n python3-%{module_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog
%autochangelog
