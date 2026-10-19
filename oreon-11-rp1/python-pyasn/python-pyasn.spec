%global source0_hash a2d55fb3ee47947609f50211ca5b0bac411a86f3c935fb92ca4b0b8ab7c668ff
Name:           python-pyasn
Version:        1.6.2
Release:        1%{?dist}
Summary:        Offline IP address to Autonomous System Number lookup module.
License:        MIT
URL:            https://github.com/hadiasghari/pyasn
Source0:        https://files.pythonhosted.org/packages/source/p/pyasn/pyasn-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/commit/1d64d6d2f20e0353b46fbf5b94f8bdea8f41e9ce.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyasn = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyasn
Summary:        Offline IP address to Autonomous System Number lookup module.
%description -n python3-pyasn

%prep
%global oreon_srcdir pyasn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyasn usr/lib/python3*/site-packages/pyasn* usr/lib64/python3*/site-packages/pyasn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyasn* usr/lib64/python3*/site-packages/pyasn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyasn -f %{oreon_filedir}/python3-pyasn.list

%changelog

%autochangelog
