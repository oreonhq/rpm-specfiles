%global source0_hash db9eee1579678a2eec6974c831dc93abf612a4df5a3c45e9d7ed35ea5f9e2497
Name:           python-libpysal
Version:        4.15.0
Release:        1%{?dist}
Summary:        Core components of PySAL - A library of spatial analysis functions
License:        ...
URL:            https://github.com/pysal/libpysal
Source0:        https://files.pythonhosted.org/packages/source/l/libpysal/libpysal-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Remove-unused-build-requirements.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-libpysal = %{version}-%{release}
# /oreon:deps
%package -n       python3-libpysal+plus
Summary:        Metapackage for python3-libpysal plus extras
Requires:       python3-libpysal = %{version}-%{release}
Requires:       python3dist(joblib) >= 1.5.0
Requires:       python3dist(networkx) >= 3.4
Requires:       python3dist(numba) >= 0.60
Requires:       python3dist(pandarm) >= 0.0
Requires:       python3dist(pulp) < 4
Requires:       python3dist(pyarrow) >= 16.1
Requires:       python3dist(sqlalchemy) >= 2.0
Requires:       python3dist(xarray) >= 2024.5
Provides:       python3dist(libpysal[plus]) = %{version}-%{release}

%description -n python3-libpysal+plus
Metapackage for python3-libpysal plus extras.

%package -n       python3-libpysal+dev
Summary:        Metapackage for python3-libpysal dev extras
Requires:       python3-libpysal = %{version}-%{release}
Provides:       python3dist(libpysal[dev]) = %{version}-%{release}

%description -n python3-libpysal+dev
Metapackage for python3-libpysal dev extras.

%package -n       python3-libpysal+docs
Summary:        Metapackage for python3-libpysal docs extras
Requires:       python3-libpysal = %{version}-%{release}
Provides:       python3dist(libpysal[docs]) = %{version}-%{release}

%description -n python3-libpysal+docs
Metapackage for python3-libpysal docs extras.

%package -n       python3-libpysal+tests
Summary:        Metapackage for python3-libpysal tests extras
Requires:       python3-libpysal = %{version}-%{release}
Requires:       python3dist(geodatasets) >= 2024.7.0
Requires:       python3dist(matplotlib) >= 3.10
Provides:       python3dist(libpysal[tests]) = %{version}-%{release}

%description -n python3-libpysal+tests
Metapackage for python3-libpysal tests extras.

%description

%package -n     python3-libpysal
Summary:        Core components of PySAL - A library of spatial analysis functions
# oreon:reqs
Requires:       python3dist(beautifulsoup4) >= 4.13.0
Requires:       python3dist(geopandas) >= 1.1.0
Requires:       python3dist(numpy) >= 2.0.0
Requires:       python3dist(packaging) >= 24.1
Requires:       python3dist(pandas) >= 2.3.0
Requires:       python3dist(platformdirs) >= 4.3
Requires:       python3dist(requests) >= 2.32.0
Requires:       python3dist(scikit-learn) >= 1.5.0
Requires:       python3dist(scipy) >= 1.14.0
Requires:       python3dist(shapely) >= 2.1
# /oreon:reqs
%description -n python3-libpysal

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir libpysal-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-libpysal usr/lib/python3*/site-packages/libpysal* usr/lib64/python3*/site-packages/libpysal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/libpysal* usr/lib64/python3*/site-packages/libpysal* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-libpysal -f %{oreon_filedir}/python3-libpysal.list

%changelog

%autochangelog
