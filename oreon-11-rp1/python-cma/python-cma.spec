%global source0_hash 5e6774388d4a3798116bf9aff7684cf44d59f966d868f375e61811f74e132934
Name:           python-cma
Version:        4.5.0
Release:        1%{?dist}
Summary:        CMA-ES, Covariance Matrix Adaptation Evolution Strategy for non-linear numerical optimization in Python
License:        BSD-3-Clause
URL:            https://github.com/CMA-ES/pycma
Source0:        https://files.pythonhosted.org/packages/source/c/cma/cma-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 79
Requires:       python3-cma = %{version}-%{release}
# /oreon:deps
%package -n       python3-cma+plotting
Summary:        Metapackage for python3-cma plotting extras
Requires:       python3-cma = %{version}-%{release}
Provides:       python3dist(cma[plotting]) = %{version}-%{release}

%description -n python3-cma+plotting
Metapackage for python3-cma plotting extras.

%package -n       python3-cma+constrained-solution-tracking
Summary:        Metapackage for python3-cma constrained-solution-tracking extras
Requires:       python3-cma = %{version}-%{release}
Provides:       python3dist(cma[constrained-solution-tracking]) = %{version}-%{release}

%description -n python3-cma+constrained-solution-tracking
Metapackage for python3-cma constrained-solution-tracking extras.

%package -n       python3-cma+statistical-tests
Summary:        Metapackage for python3-cma statistical-tests extras
Requires:       python3-cma = %{version}-%{release}
Provides:       python3dist(cma[statistical-tests]) = %{version}-%{release}

%description -n python3-cma+statistical-tests
Metapackage for python3-cma statistical-tests extras.

%description

%package -n     python3-cma
Summary:        CMA-ES, Covariance Matrix Adaptation Evolution Strategy for non-linear numerical optimization in Python
%description -n python3-cma

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cma-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cma usr/lib/python3*/site-packages/cma* usr/lib64/python3*/site-packages/cma* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cma* usr/lib64/python3*/site-packages/cma* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cma -f %{oreon_filedir}/python3-cma.list

%changelog

%autochangelog
