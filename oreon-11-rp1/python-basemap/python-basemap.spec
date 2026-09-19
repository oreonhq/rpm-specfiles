%global source0_hash none

%global debug_package %{nil}

Name:           python-basemap
Version:        2.0.0
Release:        7%{?dist}
Summary:        Plots data on map projections (with continental and political boundaries) 
License:        LGPL-2.1-or-later
URL:            https://matplotlib.org/basemap/
Source0:        https://github.com/matplotlib/basemap/archive/v%{version}/basemap-%{version}.tar.gz
Patch0:         pyver.patch

BuildRequires:  gcc

%global _description\
Basemap is a matplotlib toolkit that allows you to plot data on map\
projections (with continental and political boundaries).

%description %_description

%package -n     python-basemap-examples
Summary:        Example programs and data for python3-basemap
License:        LicenseRef-Callaway-Copyright-only 
Requires:       python3-basemap

%description -n python-basemap-examples
%{summary}.

%package -n python3-basemap
Summary:        Plots data on map projections (with continental and political boundaries)
License:        LGPL-2.1-or-later
BuildRequires:  python3-devel, proj-devel, shapelib-devel, python3-numpy-f2py, geos-devel
BuildRequires:  python3-setuptools, python3-pip
BuildRequires:  chrpath
# Needed to regenerate Cython generated files.
BuildRequires:  python3-Cython
BuildRequires:  python3-httplib2
BuildRequires:  python3-matplotlib >= 0.98
BuildRequires:  python3-pyproj
Requires:       python3-matplotlib >= 0.98
Provides: python3-basemap-data = %{version}-%{release}
Obsoletes: python3-basemap-data < %{version}-%{release}

%description -n python3-basemap
Basemap is a matplotlib toolkit that allows you to plot data on map
projections (with continental and political boundaries).

%prep
%autosetup -n basemap-%{version} -p1

%build
export GEOS_LIB="/usr/"

%python3 setup.py config
%pyproject_wheel

pushd data/basemap_data
%pyproject_wheel
popd

%install
%pyproject_install

pushd data/basemap_data
%pyproject_install
popd
chrpath --delete %{buildroot}%{python3_sitearch}/_geoslib.cpython-3*.so

%check
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} \
    %python3 -c 'from mpl_toolkits.basemap import Basemap'

%files -n python-basemap-examples
%doc doc/examples/*

%files -n python3-basemap
%license LICENSE.*
%doc README.md
%{python3_sitearch}/mpl_toolkits/basemap
%{python3_sitearch}/basemap-*.dist-info
%{python3_sitearch}/_geoslib.cpython-3*.so
%{python3_sitelib}/mpl_toolkits/basemap_data
# It seems that they forgot to bump the version in basemap_data
%{python3_sitelib}/basemap_data-*.dist-info

%changelog
%autochangelog
