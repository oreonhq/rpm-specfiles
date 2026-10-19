%global source0_hash 49af9c18aac4caa90e0e1e8437e2160cd8b3f126053dae6453d65b393590fcf9
Name:           python-types-mock
Version:        5.2.0.20260518
Release:        1%{?dist}
Summary:        Typing stubs for mock
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        https://files.pythonhosted.org/packages/source/t/types_mock/types_mock-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82.0.1
Requires:       python3-types-mock = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-types-mock
Summary:        Typing stubs for mock
%description -n python3-types-mock

%prep
%global oreon_srcdir types_mock-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-types-mock usr/lib/python3*/site-packages/types_mock* usr/lib64/python3*/site-packages/types_mock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/types_mock* usr/lib64/python3*/site-packages/types_mock* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-types-mock -f %{oreon_filedir}/python3-types-mock.list

%changelog

%autochangelog
