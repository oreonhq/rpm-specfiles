%global source0_hash 3f582add0700d4141e279625252e7a0655f9ad81feab3b8ab9077966668a2c99
Name:           python-exrex
Version:        0.12.0
Release:        1%{?dist}
Summary:        Irregular methods for regular expressions
License:        ...
URL:            https://github.com/asciimoo/exrex
Source0:        https://files.pythonhosted.org/packages/source/e/exrex/exrex-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://patch-diff.githubusercontent.com/raw/asciimoo/exrex/pull/69.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-exrex = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-exrex
Summary:        Irregular methods for regular expressions
%description -n python3-exrex

%prep
%global oreon_srcdir exrex-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-exrex usr/lib/python3*/site-packages/exrex* usr/lib64/python3*/site-packages/exrex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/exrex* usr/lib64/python3*/site-packages/exrex* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-exrex -f %{oreon_filedir}/python3-exrex.list

%changelog

%autochangelog
