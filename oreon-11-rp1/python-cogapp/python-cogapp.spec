%global source0_hash ec2a9170bfa644bf0d91996fdb5576c13d7e5e848bb2378a6f92727b48f92604
Name:           python-cogapp
Version:        3.6.0
Release:        1%{?dist}
Summary:        Cog: A content generator for executing Python snippets in source files.
License:        MIT
URL:            https://cog.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/c/cogapp/cogapp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
Requires:       python3-cogapp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cogapp
Summary:        Cog: A content generator for executing Python snippets in source files.
%description -n python3-cogapp

%prep
%global oreon_srcdir cogapp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cogapp usr/lib/python3*/site-packages/cogapp* usr/lib64/python3*/site-packages/cogapp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cogapp* usr/lib64/python3*/site-packages/cogapp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cogapp -f %{oreon_filedir}/python3-cogapp.list

%changelog

%autochangelog
