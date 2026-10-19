%global source0_hash cd90fdd26c1aa9450f6acad23b8d3cd6442a01da28d5298b7d6c74e6785c3b1d
Name:           python-virtualbmc
Version:        3.3.0
Release:        1%{?dist}
Summary:        Create virtual BMCs for controlling virtual instances via IPMI
License:        ...
URL:            https://docs.openstack.org/virtualbmc/latest/
Source0:        https://files.pythonhosted.org/packages/source/v/virtualbmc/virtualbmc-%{version}.tar.gz
BuildArch:      noarch
Patch0: %{name}-3.2.0_multiprocess_fork.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-virtualbmc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-virtualbmc
Summary:        Create virtual BMCs for controlling virtual instances via IPMI
%description -n python3-virtualbmc

%prep
%global oreon_srcdir virtualbmc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-virtualbmc usr/lib/python3*/site-packages/virtualbmc* usr/lib64/python3*/site-packages/virtualbmc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/virtualbmc* usr/lib64/python3*/site-packages/virtualbmc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-virtualbmc -f %{oreon_filedir}/python3-virtualbmc.list

%changelog

%autochangelog
