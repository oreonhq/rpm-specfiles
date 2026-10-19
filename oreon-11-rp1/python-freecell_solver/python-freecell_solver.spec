%global source0_hash 354be418ab23ed2afa30228b30e6af7eb245c7a8c150e8d0c48a06816b3b0733
Name:           python-freecell-solver
Version:        0.6.0
Release:        1%{?dist}
Summary:        Freecell Solver bindings
License:        ...
URL:            https://github.com/shlomif/freecell_solver
Source0:        https://files.pythonhosted.org/packages/source/f/freecell_solver/freecell_solver-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-freecell-solver = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-freecell-solver
Summary:        Freecell Solver bindings
%description -n python3-freecell-solver

%prep
%global oreon_srcdir freecell_solver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-freecell-solver usr/lib/python3*/site-packages/freecell_solver* usr/lib64/python3*/site-packages/freecell_solver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/freecell_solver* usr/lib64/python3*/site-packages/freecell_solver* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-freecell-solver -f %{oreon_filedir}/python3-freecell-solver.list

%changelog

%autochangelog
