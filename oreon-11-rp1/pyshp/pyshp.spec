%global source0_hash 2f48423ff717240740e17b9c1f900fc3a41c80a0579a4a0eabeea81ccf563bdc
Name:           pyshp
Version:        3.1.6
Release:        1%{?dist}
Summary:        Pure Python read/write support for ESRI Shapefile format
License:        MIT
SourceLicense:  %{license} AND LicenseRef-Fedora-Public-Domain AND ODbl-1.0
URL:            https://github.com/GeospatialPython/pyshp
Source0:        https://github.com/GeospatialPython/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%global ne_url https://github.com/nvkelso/natural-earth-vector
%global ne_commit ca96624a56bd078437bca8184e78163e5039ad19
Source10:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.cpg
Source11:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.dbf
Source12:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.prj
Source13:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.shp
Source14:       %{ne_url}/raw/%{ne_commit}/10m_cultural/ne_10m_admin_1_states_provinces.shx
Source20:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.cpg
Source21:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.dbf
Source22:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.prj
Source23:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.shp
Source24:       %{ne_url}/raw/%{ne_commit}/110m_cultural/ne_110m_admin_0_tiny_countries.shx
%global data_url https://github.com/JamesParrott/PyShp_test_shapefile
%global data_commit 2583dba70d0892fc787e1a837df07c3ea8e69950
Source25:       %{data_url}/raw/%{data_commit}/gis_osm_natural_a_free_1.zip
BuildArch:      noarch
%global common_description %{expand:
The Python Shapefile Library (PyShp) provides read and write support for the
Esri Shapefile format. The Shapefile format is a popular Geographic Information
System vector data format created by Esri. For more information about this
format please read the well-written “ESRI Shapefile Technical Description –
July 1998” located at
http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf. The Esri document
describes the shp and shx file formats.  However a third file format called dbf
is also required. This format is documented on the web as the “XBase File
Format Description” and is a simple file-based database format created in the
1960’s. For more on this specification see:
http://www.clicketyclick.dk/databases/xbase/format/index.html
Both the Esri and XBase file-formats are very simple in design and memory
efficient which is part of the reason the shapefile format remains popular
despite the numerous ways to store and exchange GIS data available today.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyshp = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyshp+stubs
Summary:        Metapackage for python3-pyshp stubs extras
Requires:       python3-pyshp = %{version}-%{release}
Provides:       python3dist(pyshp[stubs]) = %{version}-%{release}

%description -n python3-pyshp+stubs
Metapackage for python3-pyshp stubs extras.

%description %{common_description}

%package -n python3-pyshp
Summary:        Pure Python read/write support for ESRI Shapefile format
%py_provides python3-shapefile
%description -n python3-pyshp %{common_description}

%prep

%autosetup -p1
mkdir -p _testdata
ln '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE20}' '%{SOURCE21}' '%{SOURCE22}' '%{SOURCE23}' '%{SOURCE24}' \
    '%{SOURCE25}' _testdata/

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyshp usr/lib/python3*/site-packages/pyshp* usr/lib64/python3*/site-packages/pyshp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyshp* usr/lib64/python3*/site-packages/pyshp* usr/bin/*

%check

pushd _testdata
%{python3} -m http.server 8000 &
SERVER_PID="$!"
trap "kill '${SERVER_PID}'" INT TERM EXIT
popd
export REPLACE_REMOTE_URLS_WITH_LOCALHOST='yes'
%pytest -v
%{py3_test_envvars} %{python3} test_shapefile.py
%files
%files -n python3-pyshp -f %{oreon_filedir}/python3-pyshp.list

%changelog

%autochangelog
