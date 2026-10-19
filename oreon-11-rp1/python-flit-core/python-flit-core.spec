%global source0_hash 62e12b63ead8335b37f59fabb977c7167fe476dafb5e41785dfa8c9aff843bc6
Name:           python-flit-core
Version:        4.1.0
Release:        1%{?dist}
Summary:        Distribution-building parts of Flit. See flit package for more information
License:        BSD-3-Clause
URL:            https://github.com/pypa/flit
Source0:        https://files.pythonhosted.org/packages/source/f/flit_core/flit_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flit-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flit-core
Summary:        Distribution-building parts of Flit. See flit package for more information
%description -n python3-flit-core

%prep
%global oreon_srcdir flit_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flit-core usr/lib/python3*/site-packages/flit_core* usr/lib64/python3*/site-packages/flit_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flit_core* usr/lib64/python3*/site-packages/flit_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flit-core -f %{oreon_filedir}/python3-flit-core.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.0-1
- Prepare for Oreon 11 (RP1)
