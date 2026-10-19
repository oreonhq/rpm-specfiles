%global source0_hash 1a118823550e5db0ec239bee2f61a55545eb1643035082e5d4919aa5390cc847
Name:           python-xbout
Version:        0.4.0
Release:        1%{?dist}
Summary:        Collect data from BOUT++ runs in python using xarray
License:        Apache-2.0
URL:            https://github.com/boutproject/xBOUT
Source0:        https://files.pythonhosted.org/packages/source/x/xbout/xbout-%{version}.tar.gz
BuildArch:      noarch
Patch:          sphinx-theme.patch
Patch:          engine-h5netcdf.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7
BuildRequires:  python3dist(wheel) >= 0.29.0
Requires:       python3-xbout = %{version}-%{release}
# /oreon:deps
%package -n       python3-xbout+adios2
Summary:        Metapackage for python3-xbout adios2 extras
Requires:       python3-xbout = %{version}-%{release}
Provides:       python3dist(xbout[adios2]) = %{version}-%{release}

%description -n python3-xbout+adios2
Metapackage for python3-xbout adios2 extras.

%package -n       python3-xbout+calc
Summary:        Metapackage for python3-xbout calc extras
Requires:       python3-xbout = %{version}-%{release}
Requires:       python3dist(numpy) >= 1.18.0
Requires:       python3dist(scipy) >= 1.3.0
Requires:       python3dist(dask) >= 2.2.0
Requires:       python3dist(statsmodels) >= 0.10.1
Provides:       python3dist(xbout[calc]) = %{version}-%{release}

%description -n python3-xbout+calc
Metapackage for python3-xbout calc extras.

%package -n       python3-xbout+cherab
Summary:        Metapackage for python3-xbout cherab extras
Requires:       python3-xbout = %{version}-%{release}
Provides:       python3dist(xbout[cherab]) = %{version}-%{release}

%description -n python3-xbout+cherab
Metapackage for python3-xbout cherab extras.

%package -n       python3-xbout+docs
Summary:        Metapackage for python3-xbout docs extras
Requires:       python3-xbout = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5.3
Requires:       python3dist(sphinx-book-theme) >= 0.4.0rc1
Requires:       python3dist(sphinx-autodoc-typehints) >= 1.19
Provides:       python3dist(xbout[docs]) = %{version}-%{release}

%description -n python3-xbout+docs
Metapackage for python3-xbout docs extras.

%package -n       python3-xbout+3d_plot
Summary:        Metapackage for python3-xbout 3d_plot extras
Requires:       python3-xbout = %{version}-%{release}
Requires:       python3dist(k3d) >= 2.8.0
Requires:       python3dist(mayavi) >= 4.7.2
Provides:       python3dist(xbout[3d_plot]) = %{version}-%{release}

%description -n python3-xbout+3d_plot
Metapackage for python3-xbout 3d_plot extras.

%package -n       python3-xbout+tests
Summary:        Metapackage for python3-xbout tests extras
Requires:       python3-xbout = %{version}-%{release}
Requires:       python3dist(pytest) >= 3.3.0
Provides:       python3dist(xbout[tests]) = %{version}-%{release}

%description -n python3-xbout+tests
Metapackage for python3-xbout tests extras.

%description

%package -n     python3-xbout
Summary:        Collect data from BOUT++ runs in python using xarray
# oreon:reqs
Requires:       python3dist(animatplot-ng) >= 0.4.2
Requires:       python3dist(boutdata) >= 0.1.4
Requires:       python3dist(dask[array]) >= 2.10.0
Requires:       python3dist(gelidum) >= 0.5.3
Requires:       python3dist(matplotlib) >= 3.1.1
Requires:       python3dist(natsort) >= 5.5.0
Requires:       python3dist(pillow) >= 6.1.0
Requires:       python3dist(xarray) >= 2023.01.0
# /oreon:reqs
%description -n python3-xbout

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir xbout-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xbout usr/lib/python3*/site-packages/xbout* usr/lib64/python3*/site-packages/xbout* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xbout* usr/lib64/python3*/site-packages/xbout* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xbout -f %{oreon_filedir}/python3-xbout.list

%changelog

%autochangelog
