%global source0_hash 80f94bbe85be8f5adccd51330c26d07e6efdf6e154657cf107f7e65ce510d886
Name:           python-token-bucket
Version:        0.4.0
Release:        1%{?dist}
Summary:        Very fast implementation of the token bucket algorithm.
License:        Apache-2.0
URL:            https://github.com/falconry/token-bucket
Source0:        https://files.pythonhosted.org/packages/source/t/token_bucket/token_bucket-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0000-py312-imp.patch
Patch1:         0001-Drop-pytest-runner-and-setup.py-test-support.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-token-bucket = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-token-bucket
Summary:        Very fast implementation of the token bucket algorithm.
%description -n python3-token-bucket

%prep
%global oreon_srcdir token_bucket-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-token-bucket usr/lib/python3*/site-packages/token_bucket* usr/lib64/python3*/site-packages/token_bucket* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/token_bucket* usr/lib64/python3*/site-packages/token_bucket* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-token-bucket -f %{oreon_filedir}/python3-token-bucket.list

%changelog

%autochangelog
