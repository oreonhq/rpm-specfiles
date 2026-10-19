%global source0_hash d9425bc516390c54743a1045b2c1c97f02d245a913a241dd499f958adb2df998
Name:           python-unidiff
Version:        1.0.1
Release:        1%{?dist}
Summary:        Unified diff parsing/metadata extraction library.
License:        MIT
URL:            https://github.com/matiasb/python-unidiff
Source0:        https://files.pythonhosted.org/packages/source/u/unidiff/unidiff-%{version}.tar.gz
BuildArch:      noarch
Patch1: 0001-use-setuptools-console_scripts-for-usr-bin-unidiff.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-unidiff = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-unidiff
Summary:        Unified diff parsing/metadata extraction library.
%description -n python3-unidiff

%prep
%global oreon_srcdir unidiff-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-unidiff usr/lib/python3*/site-packages/unidiff* usr/lib64/python3*/site-packages/unidiff* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/unidiff* usr/lib64/python3*/site-packages/unidiff* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-unidiff -f %{oreon_filedir}/python3-unidiff.list

%changelog

%autochangelog
