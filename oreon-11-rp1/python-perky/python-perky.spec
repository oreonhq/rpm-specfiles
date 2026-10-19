%global source0_hash b25c9aa590848a8c5a0ec70846280e9939df9102c25ed82c8e8d62ac38dac091
Name:           python-perky
Version:        0.10
Release:        1%{?dist}
Summary:        A simple, Pythonic file format.  Provides load, loads, dump, and
License:        MIT
URL:            https://github.com/larryhastings/perky/
Source0:        https://files.pythonhosted.org/packages/source/p/perky/perky-%{version}.tar.gz
BuildArch:      noarch
Patch:          use-flit_core-instead-of-flit-to-build-wheel.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-perky = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-perky
Summary:        A simple, Pythonic file format.  Provides load, loads, dump, and
%description -n python3-perky

%prep
%global oreon_srcdir perky-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-perky usr/lib/python3*/site-packages/perky* usr/lib64/python3*/site-packages/perky* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/perky* usr/lib64/python3*/site-packages/perky* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-perky -f %{oreon_filedir}/python3-perky.list

%changelog

%autochangelog
