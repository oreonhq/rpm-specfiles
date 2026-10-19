%global source0_hash fb733957396cb82301f3f79cd320aef262cd0592c93d6b4fd656771506999624
Name:           python-bytecode
Version:        0.19.0
Release:        1%{?dist}
Summary:        Python module to generate and modify bytecode
License:        MIT
URL:            https://github.com/MatthieuDartiailh/bytecode
Source0:        https://files.pythonhosted.org/packages/source/b/bytecode/bytecode-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-bytecode = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bytecode
Summary:        Python module to generate and modify bytecode
%description -n python3-bytecode

%prep
%global oreon_srcdir bytecode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bytecode usr/lib/python3*/site-packages/bytecode* usr/lib64/python3*/site-packages/bytecode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bytecode* usr/lib64/python3*/site-packages/bytecode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bytecode -f %{oreon_filedir}/python3-bytecode.list

%changelog

%autochangelog
