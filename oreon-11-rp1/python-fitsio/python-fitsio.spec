%global source0_hash e2394fb0dca62f46feaaf61a48ad89fad6d2428a5a96a78ebfb4299a084b9260

%global srcname fitsio
%global sum A full featured python library to read from and write to FITS files

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        %{sum}

License:        GPL-2.0-only
URL:            https://github.com/esheldon/fitsio
Source0:        %{pypi_source}

# General
BuildRequires:  cfitsio-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc
# Python 3
BuildRequires:  python3-devel

%global _description %{expand:
This is a python extension written in c and python. Data are read 
into numerical python arrays.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires: %{py3_dist pytest}
Requires: %{py3_dist pytest}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

FITSIO_USE_SYSTEM_FITSIO=""
export FITSIO_USE_SYSTEM_FITSIO
FITSIO_SYSTEM_FITSIO_INCLUDEDIR="%{_includedir}/cfitsio"
export FITSIO_SYSTEM_FITSIO_INCLUDEDIR
FITSIO_SYSTEM_FITSIO_LIBDIR="%{_libdir}"
export FITSIO_SYSTEM_FITSIO_LIBDIR
%autosetup -p1 -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{srcname}.egg-info
# Remove bundled cfitsio, to be sure we are not using it
rm -rf cfitsio-*

%generate_buildrequires
%pyproject_buildrequires

%build
FITSIO_USE_SYSTEM_FITSIO=""
export FITSIO_USE_SYSTEM_FITSIO
FITSIO_SYSTEM_FITSIO_INCLUDEDIR="%{_includedir}/cfitsio"
export FITSIO_SYSTEM_FITSIO_INCLUDEDIR
FITSIO_SYSTEM_FITSIO_LIBDIR="%{_libdir}"
export FITSIO_SYSTEM_FITSIO_LIBDIR
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fitsio

%check
pushd %{buildroot}/%{python3_sitearch}
  %pytest fitsio
  rm -rf .pytest_cache
popd

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
