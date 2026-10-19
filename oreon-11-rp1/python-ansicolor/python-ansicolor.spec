%global source0_hash 6de60837fb322b9fb8c8863061504688520bd0aa62defab43dbf4f2c011dafda
Name:           python-ansicolor
Version:        0.3.3
Release:        1%{?dist}
Summary:        A library to produce ansi color output and colored highlighting and diffing
License:        ...
URL:            https://github.com/numerodix/ansicolor
Source0:        https://files.pythonhosted.org/packages/source/a/ansicolor/ansicolor-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ansicolor = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ansicolor
Summary:        A library to produce ansi color output and colored highlighting and diffing
%description -n python3-ansicolor

%prep
%global oreon_srcdir ansicolor-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ansicolor usr/lib/python3*/site-packages/ansicolor* usr/lib64/python3*/site-packages/ansicolor* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ansicolor* usr/lib64/python3*/site-packages/ansicolor* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ansicolor -f %{oreon_filedir}/python3-ansicolor.list

%changelog

%autochangelog
