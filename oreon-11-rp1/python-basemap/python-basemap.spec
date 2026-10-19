%global source0_hash 192ee1c63291d7d1af98fab798c45239ea27e6ca31041afa8c42c8b697e44596
%global debug_package %{nil}
Name:           python-basemap
Version:        2.0.0
Release:        1%{?dist}
Summary:        Plots data on map projections (with continental and political boundaries)
License:        LGPL-2.1-or-later
URL:            https://matplotlib.org/basemap/
Source0:        https://github.com/matplotlib/basemap/archive/v%{version}/basemap-%{version}.tar.gz
Patch0:         pyver.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 3.2
BuildRequires:  python3dist(cython) >= 3.0
BuildRequires:  python3dist(numpy) == 2.0.0
BuildRequires:  python3dist(numpy) == 2.1.0
BuildRequires:  python3dist(setuptools) < 81.0
BuildRequires:  python3dist(setuptools) >= 67.0
BuildRequires:  python3dist(wheel) < 0.46
BuildRequires:  python3dist(wheel) >= 0.40
Requires:       python3-basemap = %{version}-%{release}
# /oreon:deps
%description

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
%global oreon_srcdir basemap-%{version}
%oreon_prep
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
%oreon_autofiles python-basemap-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-basemap usr/lib/python3*/site-packages/basemap* usr/lib64/python3*/site-packages/basemap* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/basemap* usr/lib64/python3*/site-packages/basemap* usr/bin/*

%check

PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} \
    %python3 -c 'from mpl_toolkits.basemap import Basemap'
%files
%files -n python-basemap-examples -f %{oreon_filedir}/python-basemap-examples.list
%files -n python3-basemap -f %{oreon_filedir}/python3-basemap.list

%changelog

%autochangelog
