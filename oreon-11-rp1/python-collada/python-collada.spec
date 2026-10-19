%global source0_hash c34d6dcf0fe2eba5896f71c96d37a1c0fe1a61f08440fa0cfcec3dc2895d3302
Name:           python-pycollada
Version:        0.9.3
Release:        1%{?dist}
Summary:        python library for reading and writing collada documents
License:        ...
URL:            http://pycollada.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pycollada/pycollada-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-pycollada = %{version}-%{release}
# /oreon:deps
%package -n       python3-pycollada+prettyprint
Summary:        Metapackage for python3-pycollada prettyprint extras
Requires:       python3-pycollada = %{version}-%{release}
Provides:       python3dist(pycollada[prettyprint]) = %{version}-%{release}

%description -n python3-pycollada+prettyprint
Metapackage for python3-pycollada prettyprint extras.

%package -n       python3-pycollada+validation
Summary:        Metapackage for python3-pycollada validation extras
Requires:       python3-pycollada = %{version}-%{release}
Provides:       python3dist(pycollada[validation]) = %{version}-%{release}

%description -n python3-pycollada+validation
Metapackage for python3-pycollada validation extras.

%description

%package -n     python3-pycollada
Summary:        python library for reading and writing collada documents
%description -n python3-pycollada

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pycollada-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pycollada usr/lib/python3*/site-packages/pycollada* usr/lib64/python3*/site-packages/pycollada* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pycollada* usr/lib64/python3*/site-packages/pycollada* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pycollada -f %{oreon_filedir}/python3-pycollada.list

%changelog

%autochangelog
