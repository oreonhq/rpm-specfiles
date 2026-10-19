%global source0_hash 041ee6da5af6b0f1eb327a8b5d73930eddc5d9d8b3daf7fbe00301564abd9510
Name:           python-biscuits
Version:        0.3.2
Release:        1%{?dist}
Summary:        Fast and tasty cookies handling.
License:        MIT
URL:            https://github.com/pyrates/biscuits
Source0:        https://files.pythonhosted.org/packages/source/b/biscuits/biscuits-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-biscuits = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-biscuits
Summary:        Fast and tasty cookies handling.
%description -n python3-biscuits

%prep
%global oreon_srcdir biscuits-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-biscuits usr/lib/python3*/site-packages/biscuits* usr/lib64/python3*/site-packages/biscuits* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/biscuits* usr/lib64/python3*/site-packages/biscuits* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-biscuits -f %{oreon_filedir}/python3-biscuits.list

%changelog

%autochangelog
