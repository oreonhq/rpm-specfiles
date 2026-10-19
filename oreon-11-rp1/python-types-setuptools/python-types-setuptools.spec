%global source0_hash 0f123655f44390a15ec62c9fa30b57f6dafe53014524d28b62cab1edbc303059
Name:           python-types-setuptools
Version:        84.0.0.20261006
Release:        1%{?dist}
Summary:        Typing stubs for setuptools
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        https://files.pythonhosted.org/packages/source/t/types_setuptools/types_setuptools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82.0.1
Requires:       python3-types-setuptools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-types-setuptools
Summary:        Typing stubs for setuptools
%description -n python3-types-setuptools

%prep
%global oreon_srcdir types_setuptools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-types-setuptools usr/lib/python3*/site-packages/types_setuptools* usr/lib64/python3*/site-packages/types_setuptools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/types_setuptools* usr/lib64/python3*/site-packages/types_setuptools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-types-setuptools -f %{oreon_filedir}/python3-types-setuptools.list

%changelog

%autochangelog
