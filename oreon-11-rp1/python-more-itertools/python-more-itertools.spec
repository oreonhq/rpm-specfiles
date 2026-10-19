%global source0_hash 48e8f4d9e7e5878571ecf6f2b4e57634f93cd474cc8cfbd2376f2d11b396e30d
Name:           python-more-itertools
Version:        11.1.0
Release:        1%{?dist}
Summary:        More routines for operating on iterables, beyond itertools
License:        MIT
URL:            https://github.com/more-itertools/more-itertools
Source0:        https://files.pythonhosted.org/packages/source/m/more_itertools/more_itertools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-more-itertools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-more-itertools
Summary:        More routines for operating on iterables, beyond itertools
%description -n python3-more-itertools

%prep
%global oreon_srcdir more_itertools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-more-itertools usr/lib/python3*/site-packages/more_itertools* usr/lib64/python3*/site-packages/more_itertools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/more_itertools* usr/lib64/python3*/site-packages/more_itertools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-more-itertools -f %{oreon_filedir}/python3-more-itertools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.5.0-1
- Prepare for Oreon 11 (RP1)
