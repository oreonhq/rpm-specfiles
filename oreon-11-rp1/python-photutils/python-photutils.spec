%global source0_hash 947527f77794469f960d51e6fd7add2fd531b16f2369d4541b1441eb81b3d9f7

%bcond check 0

%global srcname photutils

Name: python-%{srcname}
Version: 2.3.0
Release: %autorelease
Summary: Astropy affiliated package for image photometry tasks
License: BSD-3-Clause

URL: http://photutils.readthedocs.org/en/latest/index.html
Source0: %{pypi_source}

ExcludeArch: %{ix86}
BuildRequires: gcc

%global _description %{expand:
Photutils contains functions for:
 * estimating the background and background rms in astronomical images
 * detecting sources in astronomical images
 * estimating morphological parameters of those sources (e.g., 
    centroid and shape parameters)
 * performing aperture and PSF photometry}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

BuildRequires: python3-devel

Recommends: %{py3_dist scipy}  >= 1.7.2
Recommends: %{py3_dist scikit-image} >= 0.19   
Recommends: %{py3_dist scikit-learn} >= 1.0
Recommends: %{py3_dist matplotlib} >= 3.7

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t -e %{toxenv}-test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files photutils

%if %{with check}
%check
%{tox} 
%endif 

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
