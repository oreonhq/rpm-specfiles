%global source0_hash c41c51f733b0bfdae6718dca4b94fb0bdf72fab70f35fc68d62bf8ac60d6442d
Name:           python-filecheck
Version:        1.0.6
Release:        1%{?dist}
Summary:        A Python-native clone of LLVMs FileCheck tool
License:        Apache-2.0
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/f/filecheck/filecheck-%{version}.tar.gz
BuildArch:      noarch
Patch0: %{name}-tests-x86_64.patch
Patch1: %{name}-no-coverage.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-filecheck = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-filecheck
Summary:        A Python-native clone of LLVMs FileCheck tool
%description -n python3-filecheck

%prep
%global oreon_srcdir filecheck-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-filecheck usr/lib/python3*/site-packages/filecheck* usr/lib64/python3*/site-packages/filecheck* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/filecheck* usr/lib64/python3*/site-packages/filecheck* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-filecheck -f %{oreon_filedir}/python3-filecheck.list

%changelog

%autochangelog
