%global source0_hash 93abf22cf9a62b915f724e433bde702995ac274865425fd4a76d1d9b5828da1a
Name:           python-types-psutil
Version:        7.2.2.20260906
Release:        1%{?dist}
Summary:        Typing stubs for psutil
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        https://files.pythonhosted.org/packages/source/t/types_psutil/types_psutil-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82.0.1
Requires:       python3-types-psutil = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-types-psutil
Summary:        Typing stubs for psutil
%description -n python3-types-psutil

%prep
%global oreon_srcdir types_psutil-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-types-psutil usr/lib/python3*/site-packages/types_psutil* usr/lib64/python3*/site-packages/types_psutil* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/types_psutil* usr/lib64/python3*/site-packages/types_psutil* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-types-psutil -f %{oreon_filedir}/python3-types-psutil.list

%changelog

%autochangelog
