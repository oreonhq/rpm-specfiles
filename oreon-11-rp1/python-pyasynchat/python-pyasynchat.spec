%global source0_hash 36665473ae730dac51e6d7dad70f8295962120c830ab692f0a31efba32687e24
Name:           python-pyasynchat
Version:        1.0.5
Release:        1%{?dist}
Summary:        Make asynchat available for Python 3.12 onwards
License:        PSF-2.0
URL:            https://github.com/simonrob/pyasynchat
Source0:        https://files.pythonhosted.org/packages/source/p/pyasynchat/pyasynchat-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyasynchat = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyasynchat
Summary:        Make asynchat available for Python 3.12 onwards
%description -n python3-pyasynchat

%prep
%global oreon_srcdir pyasynchat-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyasynchat usr/lib/python3*/site-packages/pyasynchat* usr/lib64/python3*/site-packages/pyasynchat* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyasynchat* usr/lib64/python3*/site-packages/pyasynchat* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyasynchat -f %{oreon_filedir}/python3-pyasynchat.list

%changelog

%autochangelog
