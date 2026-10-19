%global source0_hash 57e7e6f69295c8f922511488eeb79680729e14bb8eb382d5cad83aa11345c36c
Name:           python-kazoo
Version:        2.11.0
Release:        1%{?dist}
Summary:        _Higher Level Zookeeper Client_
License:        ...
URL:            https://github.com/python-zk/kazoo
Source0:        https://files.pythonhosted.org/packages/source/k/kazoo/kazoo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 46.4.0
Requires:       python3-kazoo = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-kazoo
Summary:        _Higher Level Zookeeper Client_
%description -n python3-kazoo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir kazoo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-kazoo usr/lib/python3*/site-packages/kazoo* usr/lib64/python3*/site-packages/kazoo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/kazoo* usr/lib64/python3*/site-packages/kazoo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-kazoo -f %{oreon_filedir}/python3-kazoo.list

%changelog

%autochangelog
