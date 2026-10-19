%global source0_hash 94edc256424af38762eb31306eed28beb9f0efc50a8837492c9d6fd6004aed79
Name:           python-packaging
Version:        26.3
Release:        1%{?dist}
Summary:        Core utilities for Python packages
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://github.com/pypa/packaging
Source0:        https://files.pythonhosted.org/packages/source/p/packaging/packaging-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-packaging = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-packaging
Summary:        Core utilities for Python packages
%description -n python3-packaging

%prep
%global oreon_srcdir packaging-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-packaging usr/lib/python3*/site-packages/packaging* usr/lib64/python3*/site-packages/packaging* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/packaging* usr/lib64/python3*/site-packages/packaging* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-packaging -f %{oreon_filedir}/python3-packaging.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.0-1
- Prepare for Oreon 11 (RP1)
