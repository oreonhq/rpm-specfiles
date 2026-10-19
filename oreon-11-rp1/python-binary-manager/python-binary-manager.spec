%global source0_hash 9651010615285b98d31107a86930a364df32e8a8fe3c6354481ddc2a9803d3ac
Name:           python-binary-manager
Version:        0.0.7
Release:        1%{?dist}
Summary:        Binman firmware-packaging tool
License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/package/index.html
Source0:        https://files.pythonhosted.org/packages/source/b/binary_manager/binary_manager-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-binary-manager = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-binary-manager
Summary:        Binman firmware-packaging tool
# oreon:reqs
Requires:       python3dist(dtoc) >= 0.0.6
Requires:       python3dist(u-boot-pylib) >= 0.0.6
# /oreon:reqs
%description -n python3-binary-manager

%prep
%global oreon_srcdir binary_manager-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-binary-manager usr/lib/python3*/site-packages/binary_manager* usr/lib64/python3*/site-packages/binary_manager* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/binary_manager* usr/lib64/python3*/site-packages/binary_manager* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-binary-manager -f %{oreon_filedir}/python3-binary-manager.list

%changelog

%autochangelog
