%global source0_hash ce6c548e665759b6150cef4db9ab9d7bdd89857e90c513abd6b7340bdd7dbd6a
Name:           python-zeroconf
Version:        0.151.3
Release:        1%{?dist}
Summary:        A pure python implementation of multicast DNS service discovery
License:        LGPL-2.1-or-later
URL:            https://github.com/python-zeroconf/python-zeroconf
Source0:        https://files.pythonhosted.org/packages/source/z/zeroconf/zeroconf-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.0.8
BuildRequires:  python3dist(poetry-core) >= 2.1.0
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-zeroconf = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-zeroconf
Summary:        A pure python implementation of multicast DNS service discovery
%description -n python3-zeroconf

%prep
%global oreon_srcdir zeroconf-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zeroconf usr/lib/python3*/site-packages/zeroconf* usr/lib64/python3*/site-packages/zeroconf* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zeroconf* usr/lib64/python3*/site-packages/zeroconf* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zeroconf -f %{oreon_filedir}/python3-zeroconf.list

%changelog

%autochangelog
