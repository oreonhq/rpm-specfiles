%global source0_hash 2d79c21660973acfe4cc8ef4dd18e44a863ae617c8e9c3ca431a2941fe5afb6b
Name:           python-multiregex
Version:        2.0.4
Release:        1%{?dist}
Summary:        Quickly match many regexes against a string. Provides 2-10x speedups over naïve regex matching.
License:        BSD-3-Clause
URL:            https://github.com/quantco/multiregex
Source0:        https://files.pythonhosted.org/packages/source/m/multiregex/multiregex-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/Quantco/multiregex/pull/100.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-multiregex = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-multiregex
Summary:        Quickly match many regexes against a string. Provides 2-10x speedups over naïve regex matching.
%description -n python3-multiregex

%prep
%global oreon_srcdir multiregex-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-multiregex usr/lib/python3*/site-packages/multiregex* usr/lib64/python3*/site-packages/multiregex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/multiregex* usr/lib64/python3*/site-packages/multiregex* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-multiregex -f %{oreon_filedir}/python3-multiregex.list

%changelog

%autochangelog
