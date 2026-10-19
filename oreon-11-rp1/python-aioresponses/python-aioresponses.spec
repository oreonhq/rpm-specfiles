%global source0_hash 1dcfa28938fc006f046a98383a7c07ac180be7a492c1ed557f5cd7b0805357d3
Name:           python-aioresponses
Version:        0.7.9
Release:        1%{?dist}
Summary:        Mock out requests made by ClientSession from aiohttp package
License:        MIT
URL:            https://github.com/pnuckowski/aioresponses
Source0:        https://files.pythonhosted.org/packages/source/a/aioresponses/aioresponses-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aioresponses = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aioresponses
Summary:        Mock out requests made by ClientSession from aiohttp package
%description -n python3-aioresponses

%prep
%global oreon_srcdir aioresponses-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aioresponses usr/lib/python3*/site-packages/aioresponses* usr/lib64/python3*/site-packages/aioresponses* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aioresponses* usr/lib64/python3*/site-packages/aioresponses* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aioresponses -f %{oreon_filedir}/python3-aioresponses.list

%changelog

%autochangelog
