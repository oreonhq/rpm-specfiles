%global source0_hash 3a116c73ea381d12d08bdc39a6204cbde86e138a2b2b614c54259f0e20e8043f
Name:           python-xkbregistry
Version:        1.5
Release:        1%{?dist}
Summary:        Bindings for libxkbregistry using cffi
License:        MIT
URL:            https://github.com/sde1000/python-xkbregistry
Source0:        https://files.pythonhosted.org/packages/source/x/xkbregistry/xkbregistry-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45.0
Requires:       python3-xkbregistry = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xkbregistry
Summary:        Bindings for libxkbregistry using cffi
%description -n python3-xkbregistry

%prep
%global oreon_srcdir xkbregistry-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xkbregistry usr/lib/python3*/site-packages/xkbregistry* usr/lib64/python3*/site-packages/xkbregistry* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xkbregistry* usr/lib64/python3*/site-packages/xkbregistry* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xkbregistry -f %{oreon_filedir}/python3-xkbregistry.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-1
- Prepare for Oreon 11 (RP1)
