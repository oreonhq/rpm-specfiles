%global source0_hash 741e2c3b351ddf169a738da9f2c048608ff7f2c5cc02f1ebc6b118bb090d5d55
Name:           python-certifi
Version:        2026.7.22
Release:        1%{?dist}
Summary:        Python package for providing Mozilla_s CA Bundle.
License:        MPL-2.0
URL:            https://github.com/certifi/python-certifi
Source0:        https://files.pythonhosted.org/packages/source/c/certifi/certifi-%{version}.tar.gz
BuildArch:      noarch
Patch:          certifi-2025.07.09-use-system-cert.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42.0.0
Requires:       python3-certifi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-certifi
Summary:        Python package for providing Mozilla_s CA Bundle.
%description -n python3-certifi

%prep
%global oreon_srcdir certifi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-certifi usr/lib/python3*/site-packages/certifi* usr/lib64/python3*/site-packages/certifi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/certifi* usr/lib64/python3*/site-packages/certifi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-certifi -f %{oreon_filedir}/python3-certifi.list

%changelog

%autochangelog
