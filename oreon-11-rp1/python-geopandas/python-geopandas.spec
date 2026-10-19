%global source0_hash 06f2890a07e1a239047daa14b486a7c6ae5ce82dcf7405e13c46bf31f5d0dd66
Name:           python-geopandas
Version:        1.1.4
Release:        1%{?dist}
Summary:        Geographic pandas extensions
License:        BSD-3-Clause
URL:            https://github.com/geopandas/geopandas
Source0:        https://files.pythonhosted.org/packages/source/g/geopandas/geopandas-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-geopandas = %{version}-%{release}
# /oreon:deps
%package -n       python3-geopandas+all
Summary:        Metapackage for python3-geopandas all extras
Requires:       python3-geopandas = %{version}-%{release}
Requires:       python3dist(psycopg[binary]) >= 3.1.0
Requires:       python3dist(sqlalchemy) >= 2.0
Requires:       python3dist(matplotlib) >= 3.7
Requires:       python3dist(mapclassify) >= 2.5
Requires:       python3dist(pyarrow) >= 10.0.0
Requires:       python3dist(pointpats) >= 2.5.3
Provides:       python3dist(geopandas[all]) = %{version}-%{release}

%description -n python3-geopandas+all
Metapackage for python3-geopandas all extras.

%package -n       python3-geopandas+dev
Summary:        Metapackage for python3-geopandas dev extras
Requires:       python3-geopandas = %{version}-%{release}
Requires:       python3dist(pytest) >= 3.1.0
Provides:       python3dist(geopandas[dev]) = %{version}-%{release}

%description -n python3-geopandas+dev
Metapackage for python3-geopandas dev extras.

%description

%package -n     python3-geopandas
Summary:        Geographic pandas extensions
# oreon:reqs
Requires:       python3dist(numpy) >= 1.24
Requires:       python3dist(pandas) >= 2.0.0
Requires:       python3dist(pyogrio) >= 0.7.2
Requires:       python3dist(pyproj) >= 3.5.0
Requires:       python3dist(shapely) >= 2.0.0
# /oreon:reqs
%description -n python3-geopandas

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir geopandas-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-geopandas usr/lib/python3*/site-packages/geopandas* usr/lib64/python3*/site-packages/geopandas* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/geopandas* usr/lib64/python3*/site-packages/geopandas* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-geopandas -f %{oreon_filedir}/python3-geopandas.list

%changelog

%autochangelog
