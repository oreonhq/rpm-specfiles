%global source0_hash 1bbde36eae57a5a289cd05081c6405618a5899814940752064ce351cd0204f71
Name:           python-pint
Version:        0.26.1
Release:        1%{?dist}
Summary:        Physical quantities module
License:        ...
URL:            https://github.com/hgrecco/pint
Source0:        https://files.pythonhosted.org/packages/source/p/pint/pint-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pint = %{version}-%{release}
# /oreon:deps
%package -n       python3-pint+test
Summary:        Metapackage for python3-pint test extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[test]) = %{version}-%{release}

%description -n python3-pint+test
Metapackage for python3-pint test extras.

%package -n       python3-pint+test-mpl
Summary:        Metapackage for python3-pint test-mpl extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[test-mpl]) = %{version}-%{release}

%description -n python3-pint+test-mpl
Metapackage for python3-pint test-mpl extras.

%package -n       python3-pint+test-all
Summary:        Metapackage for python3-pint test-all extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[test-all]) = %{version}-%{release}

%description -n python3-pint+test-all
Metapackage for python3-pint test-all extras.

%package -n       python3-pint+codspeed
Summary:        Metapackage for python3-pint codspeed extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[codspeed]) = %{version}-%{release}

%description -n python3-pint+codspeed
Metapackage for python3-pint codspeed extras.

%package -n       python3-pint+numpy
Summary:        Metapackage for python3-pint numpy extras
Requires:       python3-pint = %{version}-%{release}
Requires:       python3dist(numpy) >= 2.0.0
Provides:       python3dist(pint[numpy]) = %{version}-%{release}

%description -n python3-pint+numpy
Metapackage for python3-pint numpy extras.

%package -n       python3-pint+optype
Summary:        Metapackage for python3-pint optype extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[optype]) = %{version}-%{release}

%description -n python3-pint+optype
Metapackage for python3-pint optype extras.

%package -n       python3-pint+uncertainties
Summary:        Metapackage for python3-pint uncertainties extras
Requires:       python3-pint = %{version}-%{release}
Requires:       python3dist(uncertainties) >= 3.1.6
Provides:       python3dist(pint[uncertainties]) = %{version}-%{release}

%description -n python3-pint+uncertainties
Metapackage for python3-pint uncertainties extras.

%package -n       python3-pint+babel
Summary:        Metapackage for python3-pint babel extras
Requires:       python3-pint = %{version}-%{release}
Requires:       python3dist(babel) <= 2.8
Provides:       python3dist(pint[babel]) = %{version}-%{release}

%description -n python3-pint+babel
Metapackage for python3-pint babel extras.

%package -n       python3-pint+pandas
Summary:        Metapackage for python3-pint pandas extras
Requires:       python3-pint = %{version}-%{release}
Requires:       python3dist(pint-pandas) >= 0.3
Provides:       python3dist(pint[pandas]) = %{version}-%{release}

%description -n python3-pint+pandas
Metapackage for python3-pint pandas extras.

%package -n       python3-pint+xarray
Summary:        Metapackage for python3-pint xarray extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[xarray]) = %{version}-%{release}

%description -n python3-pint+xarray
Metapackage for python3-pint xarray extras.

%package -n       python3-pint+dask
Summary:        Metapackage for python3-pint dask extras
Requires:       python3-pint = %{version}-%{release}
Requires:       python3dist(dask) < 2025.3.0
Provides:       python3dist(pint[dask]) = %{version}-%{release}

%description -n python3-pint+dask
Metapackage for python3-pint dask extras.

%package -n       python3-pint+scipy
Summary:        Metapackage for python3-pint scipy extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[scipy]) = %{version}-%{release}

%description -n python3-pint+scipy
Metapackage for python3-pint scipy extras.

%package -n       python3-pint+matplotlib
Summary:        Metapackage for python3-pint matplotlib extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[matplotlib]) = %{version}-%{release}

%description -n python3-pint+matplotlib
Metapackage for python3-pint matplotlib extras.

%package -n       python3-pint+all
Summary:        Metapackage for python3-pint all extras
Requires:       python3-pint = %{version}-%{release}
Provides:       python3dist(pint[all]) = %{version}-%{release}

%description -n python3-pint+all
Metapackage for python3-pint all extras.

%package -n       python3-pint+docs
Summary:        Metapackage for python3-pint docs extras
Requires:       python3-pint = %{version}-%{release}
Requires:       python3dist(sphinx) >= 6
Requires:       python3dist(sphinx) < 8.2
Requires:       python3dist(ipython) <= 8.12
Requires:       python3dist(numba) >= 0.59
Requires:       python3dist(pygments) >= 2.4
Requires:       python3dist(sphinx-book-theme) >= 1.1.0
Requires:       python3dist(commonmark) == 0.8.1
Requires:       python3dist(recommonmark) == 0.5.0
Requires:       python3dist(numpy) < 2.5
Requires:       python3dist(dask[complete]) < 2025.3.0
Requires:       python3dist(jupyterlite-sphinx) >= 0.20
Requires:       python3dist(jupyterlite-pyodide-kernel) >= 0.4
Provides:       python3dist(pint[docs]) = %{version}-%{release}

%description -n python3-pint+docs
Metapackage for python3-pint docs extras.

%description

%package -n     python3-pint
Summary:        Physical quantities module
# oreon:reqs
Requires:       python3dist(flexcache) >= 0.3
Requires:       python3dist(flexparser) >= 0.4
Requires:       python3dist(platformdirs) >= 2.1.0
Requires:       python3dist(typing-extensions) >= 4.0.0
# /oreon:reqs
%description -n python3-pint

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pint-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pint usr/lib/python3*/site-packages/pint* usr/lib64/python3*/site-packages/pint* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pint* usr/lib64/python3*/site-packages/pint* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pint -f %{oreon_filedir}/python3-pint.list

%changelog

%autochangelog
