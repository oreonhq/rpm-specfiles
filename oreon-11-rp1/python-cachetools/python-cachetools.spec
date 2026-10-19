%global source0_hash bcac1a1b8da6909994a2957238a57b8140dab7c5c5c69a43669654fe87a33c1d
Name:           python-cachetools
Version:        7.2.0
Release:        1%{?dist}
Summary:        Extensible memoizing collections and decorators
License:        MIT
URL:            https://github.com/tkem/cachetools/
Source0:        https://files.pythonhosted.org/packages/source/c/cachetools/cachetools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm) >= 8.2
Requires:       python3-cachetools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cachetools
Summary:        Extensible memoizing collections and decorators
%description -n python3-cachetools

%prep
%global oreon_srcdir cachetools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cachetools usr/lib/python3*/site-packages/cachetools* usr/lib64/python3*/site-packages/cachetools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cachetools* usr/lib64/python3*/site-packages/cachetools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cachetools -f %{oreon_filedir}/python3-cachetools.list

%changelog

%autochangelog
