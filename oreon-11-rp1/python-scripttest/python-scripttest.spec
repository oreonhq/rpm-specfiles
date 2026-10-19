%global source0_hash d40e8859d71b1d4918e1d918c667bce05928286f2cbd09cfb7a6cc1f3f308ad0
Name:           python-scripttest
Version:        3.0
Release:        1%{?dist}
Summary:        Helper to test command-line scripts
License:        MIT
URL:            https://github.com/pypa/scripttest/
Source0:        https://files.pythonhosted.org/packages/source/s/scripttest/scripttest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-scripttest = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-scripttest
Summary:        Helper to test command-line scripts
%description -n python3-scripttest

%prep
%global oreon_srcdir scripttest-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scripttest usr/lib/python3*/site-packages/scripttest* usr/lib64/python3*/site-packages/scripttest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scripttest* usr/lib64/python3*/site-packages/scripttest* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-scripttest -f %{oreon_filedir}/python3-scripttest.list

%changelog

%autochangelog
