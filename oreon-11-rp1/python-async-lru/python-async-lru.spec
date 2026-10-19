%global source0_hash 89bdb258a0140d7313cf8f4031d816a042202faa61d0ab310a0a538baa1c24b6
Name:           python-async-lru
Version:        2.3.0
Release:        1%{?dist}
Summary:        Simple LRU cache for asyncio
License:        MIT
URL:            https://matrix.to/#/#aio-libs:matrix.org
Source0:        https://files.pythonhosted.org/packages/source/a/async_lru/async_lru-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-async-lru = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-async-lru
Summary:        Simple LRU cache for asyncio
%description -n python3-async-lru

%prep
%global oreon_srcdir async_lru-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-async-lru usr/lib/python3*/site-packages/async_lru* usr/lib64/python3*/site-packages/async_lru* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/async_lru* usr/lib64/python3*/site-packages/async_lru* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-async-lru -f %{oreon_filedir}/python3-async-lru.list

%changelog

%autochangelog
