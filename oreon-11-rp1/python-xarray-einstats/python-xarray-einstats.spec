%global source0_hash 45283e8b471ac54ac2957bc14e311f681b84dabc50c85959b9931e6f5cc60bcb

%bcond check 0

%global srcname xarray-einstats

Name: python-%{srcname}
Version: 0.5.1
Release: 9%{?dist}
Summary: Stats, linear algebra and einops for xarray 
License: Apache-2.0

URL: https://github.com/arviz-devs/xarray-einstats
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires:  python3-devel

%global _description %{expand:
xarray-einstats is an open source Python library part of the ArviZ project. 
It acts as a bridge between the xarray library for labelled arrays and 
libraries for raw arrays such as NumPy or SciPy.}     

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname}
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files xarray_einstats

%check
# Tests are not included in the tarball
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md 

%changelog
%autochangelog
