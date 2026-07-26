%global source0_hash f62a0e77d1e2a6cd8b9d8120d5b62b6a015dc7c6185768a01e983c77c0b794e3

%bcond check 0

%global srcname h5netcdf

Name: python-%{srcname}
Version: 1.7.3
Release: %autorelease
Summary: Python interface for the netCDF4 file-format in HDF5 files
License: BSD-3-Clause

URL: https://h5netcdf.org/
Source: %{pypi_source %{srcname}}

BuildArch: noarch
BuildRequires:  python3-devel

%global _description %{expand:
A Python interface for the netCDF4 file-format that reads and writes 
local or remote HDF5 files directly via h5py or h5pyd, without relying 
on the Unidata netCDF library.}     

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname}
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-x test}

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l h5netcdf

%check
%if %{with check}
%pytest
%else
%pyproject_check_import -e '*.test*'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS.txt

%changelog
%autochangelog
