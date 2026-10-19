%global source0_hash 0b2c880b5d13660a7ea651001fb4acb527696c01f15c9ee650f377aa543fd523
Name:           python-cleo
Version:        2.1.0
Release:        1%{?dist}
Summary:        Cleo allows you to create beautiful and testable command-line interfaces.
License:        MIT
URL:            https://github.com/python-poetry/cleo
Source0:        https://files.pythonhosted.org/packages/source/c/cleo/cleo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.1.0
Requires:       python3-cleo = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cleo
Summary:        Cleo allows you to create beautiful and testable command-line interfaces.
%description -n python3-cleo

%prep
%global oreon_srcdir cleo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cleo usr/lib/python3*/site-packages/cleo* usr/lib64/python3*/site-packages/cleo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cleo* usr/lib64/python3*/site-packages/cleo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cleo -f %{oreon_filedir}/python3-cleo.list

%changelog

%autochangelog
