%global source0_hash 55e95b788ec4e72a57e704c2eccdf44163ef23bcb4fce883c71936e1ed8ad8f8
Name:           python-etcd3gw
Version:        2.7.0
Release:        1%{?dist}
Summary:        A Python client for etcd3 grpc-gateway v3 API
License:        Apache-2.0
URL:            https://docs.openstack.org/etcd3gw
Source0:        https://files.pythonhosted.org/packages/source/e/etcd3gw/etcd3gw-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-etcd3gw = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-etcd3gw
Summary:        A Python client for etcd3 grpc-gateway v3 API
%description -n python3-etcd3gw

%prep
%global oreon_srcdir etcd3gw-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-etcd3gw usr/lib/python3*/site-packages/etcd3gw* usr/lib64/python3*/site-packages/etcd3gw* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/etcd3gw* usr/lib64/python3*/site-packages/etcd3gw* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-etcd3gw -f %{oreon_filedir}/python3-etcd3gw.list

%changelog

%autochangelog
