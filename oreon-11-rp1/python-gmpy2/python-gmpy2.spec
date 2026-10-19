%global source0_hash 313f35e9fe6b9ddf72759b14dac25166fe5757c970403e4bbf87a70ab2be07df
Name:           python-gmpy2
Version:        2.3.1
Release:        1%{?dist}
Summary:        gmpy2 interface to GMP, MPFR, and MPC for Python
License:        LGPL-3.0-or-later
URL:            https://github.com/gmpy2/gmpy2
Source0:        https://files.pythonhosted.org/packages/source/g/gmpy2/gmpy2-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 80
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.0
Requires:       python3-gmpy2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-gmpy2+docs
Summary:        Metapackage for python3-gmpy2 docs extras
Requires:       python3-gmpy2 = %{version}-%{release}
Requires:       python3dist(sphinx) >= 4
Requires:       python3dist(sphinx-rtd-theme) >= 1
Provides:       python3dist(gmpy2[docs]) = %{version}-%{release}

%description -n python3-gmpy2+docs
Metapackage for python3-gmpy2 docs extras.

%package -n       python3-gmpy2+tests
Summary:        Metapackage for python3-gmpy2 tests extras
Requires:       python3-gmpy2 = %{version}-%{release}
Provides:       python3dist(gmpy2[tests]) = %{version}-%{release}

%description -n python3-gmpy2+tests
Metapackage for python3-gmpy2 tests extras.

%description

%package -n     python3-gmpy2
Summary:        gmpy2 interface to GMP, MPFR, and MPC for Python
%description -n python3-gmpy2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir gmpy2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gmpy2 usr/lib/python3*/site-packages/gmpy2* usr/lib64/python3*/site-packages/gmpy2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gmpy2* usr/lib64/python3*/site-packages/gmpy2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gmpy2 -f %{oreon_filedir}/python3-gmpy2.list

%changelog

%autochangelog
