%global source0_hash 063c821c32859ae8bdce2cc9e74156645c074218a464f8262e29a3b8de839737
Name:           python-queuelib
Version:        1.10.0
Release:        1%{?dist}
Summary:        Collection of persistent _disk-based_ and non-persistent _memory-based_ queues
License:        BSD-3-Clause
URL:            https://github.com/scrapy/queuelib
Source0:        https://files.pythonhosted.org/packages/source/q/queuelib/queuelib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-queuelib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-queuelib
Summary:        Collection of persistent _disk-based_ and non-persistent _memory-based_ queues
%description -n python3-queuelib

%prep
%global oreon_srcdir queuelib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-queuelib usr/lib/python3*/site-packages/queuelib* usr/lib64/python3*/site-packages/queuelib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/queuelib* usr/lib64/python3*/site-packages/queuelib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-queuelib -f %{oreon_filedir}/python3-queuelib.list

%changelog

%autochangelog
