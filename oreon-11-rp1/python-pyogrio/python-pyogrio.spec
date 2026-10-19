%global source0_hash 9614f27a1891113f80653e0b76b4233ea1fb3beeb1ac46d118ab22e1670f8f13
Name:           python-pyogrio
Version:        0.13.0
Release:        1%{?dist}
Summary:        Vectorized spatial vector file format I/O using GDAL/OGR
License:        MIT
URL:            https://github.com/geopandas/pyogrio
Source0:        https://files.pythonhosted.org/packages/source/p/pyogrio/pyogrio-%{version}.tar.gz
Patch:          0001-Drop-extra-dependencies.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(versioneer[toml]) == 0.28
Requires:       python3-pyogrio = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyogrio+dev
Summary:        Metapackage for python3-pyogrio dev extras
Requires:       python3-pyogrio = %{version}-%{release}
Requires:       python3dist(cython) >= 3.1
Provides:       python3dist(pyogrio[dev]) = %{version}-%{release}

%description -n python3-pyogrio+dev
Metapackage for python3-pyogrio dev extras.

%package -n       python3-pyogrio+test
Summary:        Metapackage for python3-pyogrio test extras
Requires:       python3-pyogrio = %{version}-%{release}
Provides:       python3dist(pyogrio[test]) = %{version}-%{release}

%description -n python3-pyogrio+test
Metapackage for python3-pyogrio test extras.

%package -n       python3-pyogrio+benchmark
Summary:        Metapackage for python3-pyogrio benchmark extras
Requires:       python3-pyogrio = %{version}-%{release}
Provides:       python3dist(pyogrio[benchmark]) = %{version}-%{release}

%description -n python3-pyogrio+benchmark
Metapackage for python3-pyogrio benchmark extras.

%package -n       python3-pyogrio+geopandas
Summary:        Metapackage for python3-pyogrio geopandas extras
Requires:       python3-pyogrio = %{version}-%{release}
Provides:       python3dist(pyogrio[geopandas]) = %{version}-%{release}

%description -n python3-pyogrio+geopandas
Metapackage for python3-pyogrio geopandas extras.

%description

%package -n     python3-pyogrio
Summary:        Vectorized spatial vector file format I/O using GDAL/OGR
%description -n python3-pyogrio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyogrio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyogrio usr/lib/python3*/site-packages/pyogrio* usr/lib64/python3*/site-packages/pyogrio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyogrio* usr/lib64/python3*/site-packages/pyogrio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyogrio -f %{oreon_filedir}/python3-pyogrio.list

%changelog

%autochangelog
