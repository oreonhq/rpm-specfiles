%global source0_hash 5bb9acf524d3583985cf689f7643fb8cb380f20387b6f904b77b468bbaf982bf

%global srcname gatspy 
%global sum General tools for Astronomical Time Series in Python

Name:           python-%{srcname}
Version:        0.3
Release:        39%{?dist}
Summary:        %{sum}

License:        BSD-2-Clause
URL:            https://www.astroml.org/gatspy/
Source0:        https://pypi.python.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Gatspy contains efficient, well-documented implementations of several common
routines for Astronomical time series analysis, including the Lomb-Scargle
periodogram, the Supersmoother method, and others.

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
Requires:  python3-numpy
Requires:  python3-scipy
Requires:  python3-astroML
Requires:  python3-supersmoother
Recommends:python3-astroML-addons

%description -n python3-%{srcname}
Gatspy contains efficient, well-documented implementations of several common
routines for Astronomical time series analysis, including the Lomb-Scargle
periodogram, the Supersmoother method, and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files gatspy

%check
# Disabled for now as tests require online access
#nosetests-%{python3_version} %{srcname}
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.md README.md

%changelog
%autochangelog
