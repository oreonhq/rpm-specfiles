%global source0_hash 680e969cae18c30adbddd6a087ed09f6a296b4937b4c8bc69be813bdbbfa9847
Name:           python-openidc-client
Version:        0.6.0
Release:        1%{?dist}
Summary:        OpenID Connect Client with caching and token management
License:        MIT
URL:            https://github.com/puiterwijk/python-openidc-client
Source0:        https://files.pythonhosted.org/packages/source/o/openidc-client/openidc-client-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-feat-really-support-not-receiving-refresh-token.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-openidc-client = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-openidc-client
Summary:        OpenID Connect Client with caching and token management
%description -n python3-openidc-client

%prep
%global oreon_srcdir openidc-client-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openidc-client usr/lib/python3*/site-packages/openidc_client* usr/lib64/python3*/site-packages/openidc_client* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openidc_client* usr/lib64/python3*/site-packages/openidc_client* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-openidc-client -f %{oreon_filedir}/python3-openidc-client.list

%changelog

%autochangelog
