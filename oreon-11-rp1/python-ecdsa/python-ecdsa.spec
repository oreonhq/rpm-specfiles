%global source0_hash 62635b0ac1ca2e027f82122b5b81cb706edc38cd91c63dda28e4f3455a2bf930
Name:           python-ecdsa
Version:        0.19.2
Release:        1%{?dist}
Summary:        ECDSA cryptographic signature library _pure python_
License:        MIT
URL:            http://github.com/tlsfuzzer/python-ecdsa
Source0:        https://files.pythonhosted.org/packages/source/e/ecdsa/ecdsa-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ecdsa = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ecdsa
Summary:        ECDSA cryptographic signature library _pure python_
%description -n python3-ecdsa

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ecdsa-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ecdsa usr/lib/python3*/site-packages/ecdsa* usr/lib64/python3*/site-packages/ecdsa* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ecdsa* usr/lib64/python3*/site-packages/ecdsa* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ecdsa -f %{oreon_filedir}/python3-ecdsa.list

%changelog

%autochangelog
