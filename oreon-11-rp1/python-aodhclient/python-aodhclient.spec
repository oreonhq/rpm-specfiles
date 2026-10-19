%global source0_hash 1956f73b6b99a85544de0abf56ae02f23e7f349a9b83698f0e8e6890c0aad6a4
Name:           python-aodhclient
Version:        3.12.0
Release:        1%{?dist}
Summary:        Python client library for Aodh
License:        Apache-2.0
URL:            https://docs.openstack.org/python-aodhclient
Source0:        https://files.pythonhosted.org/packages/source/a/aodhclient/aodhclient-%{version}.tar.gz
BuildArch:      noarch
Patch0:           0001-Revert-Add-OSprofiler-support-for-Aodh-client.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.0.0
BuildRequires:  python3dist(setuptools) >= 64.0.0
Requires:       python3-aodhclient = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aodhclient
Summary:        Python client library for Aodh
%description -n python3-aodhclient

%prep
%global oreon_srcdir aodhclient-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aodhclient usr/lib/python3*/site-packages/aodhclient* usr/lib64/python3*/site-packages/aodhclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aodhclient* usr/lib64/python3*/site-packages/aodhclient* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aodhclient -f %{oreon_filedir}/python3-aodhclient.list

%changelog

%autochangelog
