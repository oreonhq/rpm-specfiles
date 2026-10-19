%global source0_hash e16a260f2fd500af14f157b9b7b7d69292ce83b0f8a461ec68ce6a8a42967cbd
Name:           python-os-client-config
Version:        2.3.0
Release:        1%{?dist}
Summary:        OpenStack Client Configuation Library
License:        ...
URL:            https://docs.openstack.org/os-client-config/latest
Source0:        https://files.pythonhosted.org/packages/source/o/os_client_config/os_client_config-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-os-client-config = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-os-client-config
Summary:        OpenStack Client Configuation Library
%description -n python3-os-client-config

%prep
%global oreon_srcdir os_client_config-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-os-client-config usr/lib/python3*/site-packages/os_client_config* usr/lib64/python3*/site-packages/os_client_config* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/os_client_config* usr/lib64/python3*/site-packages/os_client_config* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-os-client-config -f %{oreon_filedir}/python3-os-client-config.list

%changelog

%autochangelog
