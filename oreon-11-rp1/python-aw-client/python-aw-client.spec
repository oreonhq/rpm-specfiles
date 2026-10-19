%global source0_hash d6b0aeae82ded2dc0469b29109068d01ddf9e4195a5b7b8055849173b5edff7e
Name:           python-aw-client
Version:        0.5.15
Release:        1%{?dist}
Summary:        Client library for ActivityWatch
License:        MPL-2.0
URL:            https://github.com/ActivityWatch/aw-client/
Source0:        https://files.pythonhosted.org/packages/source/a/aw_client/aw_client-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aw-client = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aw-client
Summary:        Client library for ActivityWatch
%description -n python3-aw-client

%prep
%global oreon_srcdir aw_client-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aw-client usr/lib/python3*/site-packages/aw_client* usr/lib64/python3*/site-packages/aw_client* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aw_client* usr/lib64/python3*/site-packages/aw_client* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aw-client -f %{oreon_filedir}/python3-aw-client.list

%changelog

%autochangelog
