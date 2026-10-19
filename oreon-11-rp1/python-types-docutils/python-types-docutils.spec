%global source0_hash 6f77b72baeed83d34d01303a3a6c87f0e215d37dd9847c91e876bf018a2efdf5
Name:           python-types-docutils
Version:        0.23.0.20260917
Release:        1%{?dist}
Summary:        Typing stubs for docutils
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        https://files.pythonhosted.org/packages/source/t/types_docutils/types_docutils-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82.0.1
Requires:       python3-types-docutils = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-types-docutils
Summary:        Typing stubs for docutils
%description -n python3-types-docutils

%prep
%global oreon_srcdir types_docutils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-types-docutils usr/lib/python3*/site-packages/types_docutils* usr/lib64/python3*/site-packages/types_docutils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/types_docutils* usr/lib64/python3*/site-packages/types_docutils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-types-docutils -f %{oreon_filedir}/python3-types-docutils.list

%changelog

%autochangelog
