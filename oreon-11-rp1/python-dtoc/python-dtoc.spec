%global source0_hash 340f7a0b39c8c63aa9c36224f0026926427f7a2fa4413094131c0582cb15f823
Name:           python-dtoc
Version:        0.0.7
Release:        1%{?dist}
Summary:        Devicetree-to-C generator
License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/driver-model/of-plat.html
Source0:        https://files.pythonhosted.org/packages/source/d/dtoc/dtoc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-dtoc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dtoc
Summary:        Devicetree-to-C generator
# oreon:reqs
Requires:       python3dist(u-boot-pylib) >= 0.0.6
# /oreon:reqs
%description -n python3-dtoc

%prep
%global oreon_srcdir dtoc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dtoc usr/lib/python3*/site-packages/dtoc* usr/lib64/python3*/site-packages/dtoc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dtoc* usr/lib64/python3*/site-packages/dtoc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dtoc -f %{oreon_filedir}/python3-dtoc.list

%changelog

%autochangelog
