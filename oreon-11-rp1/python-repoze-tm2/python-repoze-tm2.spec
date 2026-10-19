%global source0_hash 662fb67900910a6cac6e0f437245a244af09f19ea0e3ba49446a2f98861e1e01
Name:           python-repoze-tm2
Version:        2.3
Release:        1%{?dist}
Summary:        Per-request transactions via WSGI middleware
License:        LicenseRef-Repoze-BSD-derived
URL:            https://github.com/repoze/repoze.tm2
Source0:        https://files.pythonhosted.org/packages/source/r/repoze_tm2/repoze_tm2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-repoze-tm2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-repoze-tm2
Summary:        Per-request transactions via WSGI middleware
%description -n python3-repoze-tm2

%prep
%global oreon_srcdir repoze_tm2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-repoze-tm2 usr/lib/python3*/site-packages/repoze_tm2* usr/lib64/python3*/site-packages/repoze_tm2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/repoze_tm2* usr/lib64/python3*/site-packages/repoze_tm2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-repoze-tm2 -f %{oreon_filedir}/python3-repoze-tm2.list

%changelog

%autochangelog
