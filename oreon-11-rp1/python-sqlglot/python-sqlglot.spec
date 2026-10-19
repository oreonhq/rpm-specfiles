%global source0_hash f4b3f6f7ea52810815f71655c1d52d7da147c019010d7699e243be474be7f090
Name:           python-sqlglot
Version:        9.0.6
Release:        1%{?dist}
Summary:        An easily customizable SQL parser and transpiler
License:        MIT
URL:            https://github.com/tobymao/sqlglot
Source0:        https://files.pythonhosted.org/packages/source/s/sqlglot/sqlglot-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sqlglot = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sqlglot
Summary:        An easily customizable SQL parser and transpiler
%description -n python3-sqlglot

%prep
%global oreon_srcdir sqlglot-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlglot usr/lib/python3*/site-packages/sqlglot* usr/lib64/python3*/site-packages/sqlglot* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlglot* usr/lib64/python3*/site-packages/sqlglot* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlglot -f %{oreon_filedir}/python3-sqlglot.list

%changelog

%autochangelog
