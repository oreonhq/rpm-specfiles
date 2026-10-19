%global source0_hash 9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a
Name:           python-biopython
Version:        1.88
Release:        1%{?dist}
Summary:        Freely available tools for computational molecular biology.
License:        LicenseRef-Biopython-License-Agreement
URL:            https://biopython.org/
Source0:        https://files.pythonhosted.org/packages/source/b/biopython/biopython-%{version}.tar.gz
Patch0:           %{pypi_name}-CVE_2025_68463_1.patch
Patch1:           %{pypi_name}-fix_numpy-2.4_compatibility.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 74.1
Requires:       python3-biopython = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-biopython
Summary:        Freely available tools for computational molecular biology.
%description -n python3-biopython

%prep
%global oreon_srcdir biopython-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-biopython usr/lib/python3*/site-packages/biopython* usr/lib64/python3*/site-packages/biopython* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/biopython* usr/lib64/python3*/site-packages/biopython* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-biopython -f %{oreon_filedir}/python3-biopython.list

%changelog

%autochangelog
