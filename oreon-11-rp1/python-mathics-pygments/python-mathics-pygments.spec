%global source0_hash 694a2fdaf61eb60068f3dc83385a5eedb2ce9c0444b73603e8d20387586c4fc5
Name:           python-mathics-pygments
Version:        1.0.4
Release:        1%{?dist}
Summary:        Mathematica/Wolfram Language Lexer for Pygments
License:        MIT
URL:            http://github.com/Mathics3/mathics-pygments/
Source0:        https://files.pythonhosted.org/packages/source/m/mathics_pygments/mathics_pygments-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/Mathics3/mathics-pygments/pull/5.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mathics-pygments = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mathics-pygments
Summary:        Mathematica/Wolfram Language Lexer for Pygments
%description -n python3-mathics-pygments

%prep
%global oreon_srcdir mathics_pygments-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mathics-pygments usr/lib/python3*/site-packages/mathics_pygments* usr/lib64/python3*/site-packages/mathics_pygments* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mathics_pygments* usr/lib64/python3*/site-packages/mathics_pygments* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mathics-pygments -f %{oreon_filedir}/python3-mathics-pygments.list

%changelog

%autochangelog
