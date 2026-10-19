%global source0_hash 5d257fe58d0772bc46a557880ca78e2a8e07fec7bfd9d11074aef8e33e1aecbc
Name:           python-statsmodels
Version:        0.15.0
Release:        1%{?dist}
Summary:        Statistical computations and models for Python
License:        BSD-3-Clause
URL:            https://www.statsmodels.org
Source0:        https://files.pythonhosted.org/packages/source/s/statsmodels/statsmodels-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 4
BuildRequires:  python3dist(cython) >= 3.0.13
BuildRequires:  python3dist(numpy) < 3
BuildRequires:  python3dist(numpy) >= 2.0.0
BuildRequires:  python3dist(scipy) < 2
BuildRequires:  python3dist(scipy) >= 1.13
BuildRequires:  python3dist(setuptools-scm) < 10
BuildRequires:  python3dist(setuptools-scm) >= 9.2.0
Requires:       python3-statsmodels = %{version}-%{release}
# /oreon:deps
%package -n       python3-statsmodels+test
Summary:        Metapackage for python3-statsmodels test extras
Requires:       python3-statsmodels = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.4.1
Requires:       python3dist(pytest) < 10
Provides:       python3dist(statsmodels[test]) = %{version}-%{release}

%description -n python3-statsmodels+test
Metapackage for python3-statsmodels test extras.

%package -n       python3-statsmodels+doc
Summary:        Metapackage for python3-statsmodels doc extras
Requires:       python3-statsmodels = %{version}-%{release}
Requires:       python3dist(pandas) >= 2.2.2
Requires:       python3dist(pytest) >= 8.4.1
Requires:       python3dist(pytest) < 10
Provides:       python3dist(statsmodels[doc]) = %{version}-%{release}

%description -n python3-statsmodels+doc
Metapackage for python3-statsmodels doc extras.

%package -n       python3-statsmodels+dev
Summary:        Metapackage for python3-statsmodels dev extras
Requires:       python3-statsmodels = %{version}-%{release}
Requires:       python3dist(cython) >= 3.0.10
Requires:       python3dist(cython) < 4
Requires:       python3dist(setuptools-scm) >= 9.0
Requires:       python3dist(meson-python) >= 0.18.0
Requires:       python3dist(matplotlib) >= 3
Provides:       python3dist(statsmodels[dev]) = %{version}-%{release}

%description -n python3-statsmodels+dev
Metapackage for python3-statsmodels dev extras.

%package -n       python3-statsmodels+polars
Summary:        Metapackage for python3-statsmodels polars extras
Requires:       python3-statsmodels = %{version}-%{release}
Requires:       python3dist(polars) >= 1.0.0
Provides:       python3dist(statsmodels[polars]) = %{version}-%{release}

%description -n python3-statsmodels+polars
Metapackage for python3-statsmodels polars extras.

%description

%package -n     python3-statsmodels
Summary:        Statistical computations and models for Python
# oreon:reqs
Requires:       python3dist(formulaic) >= 1.1.0
Requires:       python3dist(numpy) < 3
Requires:       python3dist(numpy) >= 1.23.5
Requires:       python3dist(packaging) >= 21.3
Requires:       python3dist(pandas) >= 1.4
Requires:       python3dist(patsy) >= 0.5.6
Requires:       python3dist(scipy) >= 1.8
# /oreon:reqs
%description -n python3-statsmodels

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir statsmodels-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-statsmodels usr/lib/python3*/site-packages/statsmodels* usr/lib64/python3*/site-packages/statsmodels* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/statsmodels* usr/lib64/python3*/site-packages/statsmodels* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-statsmodels -f %{oreon_filedir}/python3-statsmodels.list

%changelog

%autochangelog
