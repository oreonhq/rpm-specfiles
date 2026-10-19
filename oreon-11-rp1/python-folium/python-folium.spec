%global source0_hash a0d78b9d5a36ba7589ca9aedbd433e84e9fcab79cd6ac213adbcff922e454cb9
Name:           python-folium
Version:        0.20.0
Release:        1%{?dist}
Summary:        Make beautiful maps with Leaflet.js _ Python
License:        MIT
URL:            https://github.com/python-visualization/folium
Source0:        https://files.pythonhosted.org/packages/source/f/folium/folium-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 41.2
Requires:       python3-folium = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-folium
Summary:        Make beautiful maps with Leaflet.js _ Python
%description -n python3-folium

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir folium-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-folium usr/lib/python3*/site-packages/folium* usr/lib64/python3*/site-packages/folium* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/folium* usr/lib64/python3*/site-packages/folium* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-folium -f %{oreon_filedir}/python3-folium.list

%changelog

%autochangelog
