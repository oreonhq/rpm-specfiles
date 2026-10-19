%global source0_hash 03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7
Name:           python-yarl
Version:        1.25.1
Release:        1%{?dist}
Summary:        Yet another URL library
License:        Apache-2.0
URL:            https://matrix.to/#/#aio-libs:matrix.org
Source0:        https://files.pythonhosted.org/packages/source/y/yarl/yarl-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 47
Requires:       python3-yarl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-yarl
Summary:        Yet another URL library
%description -n python3-yarl

%prep
%global oreon_srcdir yarl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-yarl usr/lib/python3*/site-packages/yarl* usr/lib64/python3*/site-packages/yarl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/yarl* usr/lib64/python3*/site-packages/yarl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-yarl -f %{oreon_filedir}/python3-yarl.list

%changelog

%autochangelog
