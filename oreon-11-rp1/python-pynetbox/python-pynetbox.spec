%global source0_hash c359e9b9ed599d145a987c755dbe786da967caf236e3afe1e94a154cf5aeab5c
Name:           python-pynetbox
Version:        7.8.0
Release:        1%{?dist}
Summary:        NetBox API client library
License:        ...
URL:            https://github.com/netbox-community/pynetbox
Source0:        https://files.pythonhosted.org/packages/source/p/pynetbox/pynetbox-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pynetbox = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pynetbox
Summary:        NetBox API client library
%description -n python3-pynetbox

%prep
%global oreon_srcdir pynetbox-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pynetbox usr/lib/python3*/site-packages/pynetbox* usr/lib64/python3*/site-packages/pynetbox* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pynetbox* usr/lib64/python3*/site-packages/pynetbox* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pynetbox -f %{oreon_filedir}/python3-pynetbox.list

%changelog

%autochangelog
