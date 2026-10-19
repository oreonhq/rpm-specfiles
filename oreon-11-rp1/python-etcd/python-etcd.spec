%global source0_hash 58e4c4a1c94fdc29973e7ec714858f36356f105af4da136e7373ab734356976d
Name:           python-etcd
Version:        2.0.8
Release:        1%{?dist}
Summary:        A Python etcd client that just works.
License:        ...
URL:            https://github.com/dsoprea/PythonEtcdClient
Source0:        https://files.pythonhosted.org/packages/source/e/etcd/etcd-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/288.patch
Patch:          %{url}/pull/289.patch
Patch:          %{url}/pull/290.patch
Patch:          %{url}/pull/294.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-etcd = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-etcd
Summary:        A Python etcd client that just works.
%description -n python3-etcd

%prep
%global oreon_srcdir etcd-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-etcd usr/lib/python3*/site-packages/etcd* usr/lib64/python3*/site-packages/etcd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/etcd* usr/lib64/python3*/site-packages/etcd* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-etcd -f %{oreon_filedir}/python3-etcd.list

%changelog

%autochangelog
