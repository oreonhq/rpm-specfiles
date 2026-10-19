%global source0_hash 9e332c0a0da370cb1c00823678065e9b0462fbdf1efa0f38c37485cc78c8a576
Name:           python-arviz
Version:        1.3.0
Release:        1%{?dist}
Summary:        Expose features from _ArviZverse_ refactored packages together in the __arviz__ namespace.
License:        ...
URL:            https://github.com/arviz-devs/arviz
Source0:        https://files.pythonhosted.org/packages/source/a/arviz/arviz-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.4
Requires:       python3-arviz = %{version}-%{release}
# /oreon:deps
%package -n       python3-arviz+netcdf4
Summary:        Metapackage for python3-arviz netcdf4 extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[netcdf4]) = %{version}-%{release}

%description -n python3-arviz+netcdf4
Metapackage for python3-arviz netcdf4 extras.

%package -n       python3-arviz+h5netcdf
Summary:        Metapackage for python3-arviz h5netcdf extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[h5netcdf]) = %{version}-%{release}

%description -n python3-arviz+h5netcdf
Metapackage for python3-arviz h5netcdf extras.

%package -n       python3-arviz+zarr
Summary:        Metapackage for python3-arviz zarr extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[zarr]) = %{version}-%{release}

%description -n python3-arviz+zarr
Metapackage for python3-arviz zarr extras.

%package -n       python3-arviz+matplotlib
Summary:        Metapackage for python3-arviz matplotlib extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[matplotlib]) = %{version}-%{release}

%description -n python3-arviz+matplotlib
Metapackage for python3-arviz matplotlib extras.

%package -n       python3-arviz+bokeh
Summary:        Metapackage for python3-arviz bokeh extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[bokeh]) = %{version}-%{release}

%description -n python3-arviz+bokeh
Metapackage for python3-arviz bokeh extras.

%package -n       python3-arviz+plotly
Summary:        Metapackage for python3-arviz plotly extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[plotly]) = %{version}-%{release}

%description -n python3-arviz+plotly
Metapackage for python3-arviz plotly extras.

%package -n       python3-arviz+doc
Summary:        Metapackage for python3-arviz doc extras
Requires:       python3-arviz = %{version}-%{release}
Requires:       python3dist(pydata-sphinx-theme) >= 0.13
Requires:       python3dist(sphinx) >= 5
Provides:       python3dist(arviz[doc]) = %{version}-%{release}

%description -n python3-arviz+doc
Metapackage for python3-arviz doc extras.

%package -n       python3-arviz+test
Summary:        Metapackage for python3-arviz test extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[test]) = %{version}-%{release}

%description -n python3-arviz+test
Metapackage for python3-arviz test extras.

%package -n       python3-arviz+check
Summary:        Metapackage for python3-arviz check extras
Requires:       python3-arviz = %{version}-%{release}
Provides:       python3dist(arviz[check]) = %{version}-%{release}

%description -n python3-arviz+check
Metapackage for python3-arviz check extras.

%description

%package -n     python3-arviz
Summary:        Expose features from _ArviZverse_ refactored packages together in the __arviz__ namespace.
# oreon:reqs
Requires:       python3dist(arviz-base) < 1.4.0
Requires:       python3dist(arviz-base) >= 1.3.0
Requires:       python3dist(arviz-plots) < 1.4.0
Requires:       python3dist(arviz-plots) >= 1.3.0
Requires:       python3dist(arviz-stats[xarray]) < 1.4.0
Requires:       python3dist(arviz-stats[xarray]) >= 1.3.0
# /oreon:reqs
%description -n python3-arviz

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir arviz-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-arviz usr/lib/python3*/site-packages/arviz* usr/lib64/python3*/site-packages/arviz* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/arviz* usr/lib64/python3*/site-packages/arviz* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-arviz -f %{oreon_filedir}/python3-arviz.list

%changelog

%autochangelog
