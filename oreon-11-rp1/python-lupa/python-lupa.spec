%global source0_hash d8022641b9ec8ecf2c5ecbe9f47e5a70e0b87c4b5ae921b92cb02a638e0acd08
Name:           python-lupa
Version:        2.8
Release:        1%{?dist}
Summary:        Python wrapper around Lua and LuaJIT
License:        ...
URL:            https://github.com/scoder/lupa
Source0:        https://files.pythonhosted.org/packages/source/l/lupa/lupa-%{version}.tar.gz
Patch:          lupa-default-to-no-bundle.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.2.4
Requires:       python3-lupa = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-lupa
Summary:        Python wrapper around Lua and LuaJIT
%description -n python3-lupa

%prep
%global oreon_srcdir lupa-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lupa usr/lib/python3*/site-packages/lupa* usr/lib64/python3*/site-packages/lupa* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lupa* usr/lib64/python3*/site-packages/lupa* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lupa -f %{oreon_filedir}/python3-lupa.list

%changelog

%autochangelog
