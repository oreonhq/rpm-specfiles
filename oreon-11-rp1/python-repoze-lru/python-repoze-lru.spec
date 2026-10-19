%global source0_hash a252408cd93fe670c88d6665b96fe5d42e071dba2507a1f21a1e609ae4fa891a
Name:           python-repoze-lru
Version:        0.8
Release:        1%{?dist}
Summary:        A tiny LRU cache implementation and decorator
License:        LicenseRef-Repoze-BSD-derived
URL:            https://github.com/repoze/repoze.lru
Source0:        https://files.pythonhosted.org/packages/source/r/repoze_lru/repoze_lru-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-repoze-lru = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-repoze-lru
Summary:        A tiny LRU cache implementation and decorator
%description -n python3-repoze-lru

%prep
%global oreon_srcdir repoze_lru-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-repoze-lru usr/lib/python3*/site-packages/repoze_lru* usr/lib64/python3*/site-packages/repoze_lru* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/repoze_lru* usr/lib64/python3*/site-packages/repoze_lru* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-repoze-lru -f %{oreon_filedir}/python3-repoze-lru.list

%changelog

%autochangelog
