%global source0_hash 244035963e4428530d9e3a6101a1ef97209c6825edab1567beac148ccc1db1b6
Name:           python-pyperclip
Version:        1.11.0
Release:        1%{?dist}
Summary:        A cross-platform clipboard module for Python. _Only handles plain text for now._
License:        ...
URL:            https://github.com/asweigart/pyperclip
Source0:        https://files.pythonhosted.org/packages/source/p/pyperclip/pyperclip-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-pyperclip = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyperclip
Summary:        A cross-platform clipboard module for Python. _Only handles plain text for now._
%description -n python3-pyperclip

%prep
%global oreon_srcdir pyperclip-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyperclip usr/lib/python3*/site-packages/pyperclip* usr/lib64/python3*/site-packages/pyperclip* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyperclip* usr/lib64/python3*/site-packages/pyperclip* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyperclip -f %{oreon_filedir}/python3-pyperclip.list

%changelog

%autochangelog
