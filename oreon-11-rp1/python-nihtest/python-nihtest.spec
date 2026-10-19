%global source0_hash 9307197235c107f24a569a2847ee02ebd771a395d8d081dac9aab0f7b9139a75
Name:           python-nihtest
Version:        1.11.1
Release:        1%{?dist}
Summary:        A testing tool for command line utilities.
License:        BSD-3-Clause
URL:            https://github.com/nih-at/nihtest
Source0:        https://files.pythonhosted.org/packages/source/n/nihtest/nihtest-%{version}.tar.gz
BuildArch:      noarch
Patch:          run_tests_using_cmake_and_ctest.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nihtest = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-nihtest
Summary:        A testing tool for command line utilities.
%description -n python3-nihtest

%prep
%global oreon_srcdir nihtest-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nihtest usr/lib/python3*/site-packages/nihtest* usr/lib64/python3*/site-packages/nihtest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nihtest* usr/lib64/python3*/site-packages/nihtest* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nihtest -f %{oreon_filedir}/python3-nihtest.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.1-1
- Prepare for Oreon 11 (RP1)
