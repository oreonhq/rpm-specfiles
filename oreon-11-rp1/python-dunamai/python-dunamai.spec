%global source0_hash 84ea45eddf9bb4b40df7610b1b22a03137365e6257dbf9d7b72128fdccca564c
Name:           python-dunamai
Version:        1.26.2
Release:        1%{?dist}
Summary:        Dynamic version generation
License:        MIT
URL:            https://github.com/mtkennerly/dunamai
Source0:        https://files.pythonhosted.org/packages/source/d/dunamai/dunamai-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-dunamai = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dunamai
Summary:        Dynamic version generation
%description -n python3-dunamai

%prep
%global oreon_srcdir dunamai-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dunamai usr/lib/python3*/site-packages/dunamai* usr/lib64/python3*/site-packages/dunamai* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dunamai* usr/lib64/python3*/site-packages/dunamai* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dunamai -f %{oreon_filedir}/python3-dunamai.list

%changelog

%autochangelog
