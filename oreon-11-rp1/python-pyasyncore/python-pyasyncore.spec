%global source0_hash dd483d5103a6d59b66b86e0ca2334ad43dca732ff23a0ac5d63c88c52510542e
Name:           python-pyasyncore
Version:        1.0.5
Release:        1%{?dist}
Summary:        Make asyncore available for Python 3.12 onwards
License:        PSF-2.0
URL:            https://github.com/simonrob/pyasyncore
Source0:        https://files.pythonhosted.org/packages/source/p/pyasyncore/pyasyncore-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyasyncore = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyasyncore
Summary:        Make asyncore available for Python 3.12 onwards
%description -n python3-pyasyncore

%prep
%global oreon_srcdir pyasyncore-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyasyncore usr/lib/python3*/site-packages/pyasyncore* usr/lib64/python3*/site-packages/pyasyncore* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyasyncore* usr/lib64/python3*/site-packages/pyasyncore* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyasyncore -f %{oreon_filedir}/python3-pyasyncore.list

%changelog

%autochangelog
