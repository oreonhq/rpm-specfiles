%global source0_hash c4a564d4dfb4472d931d145c43d1cf1ad78c24592142e7755b8866179eeac012
Name:           python-rstr
Version:        3.2.2
Release:        1%{?dist}
Summary:        Generate random strings in Python
License:        ...
URL:            https://github.com/leapfrogonline/rstr
Source0:        https://files.pythonhosted.org/packages/source/r/rstr/rstr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-rstr = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rstr
Summary:        Generate random strings in Python
%description -n python3-rstr

%prep
%global oreon_srcdir rstr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rstr usr/lib/python3*/site-packages/rstr* usr/lib64/python3*/site-packages/rstr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rstr* usr/lib64/python3*/site-packages/rstr* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rstr -f %{oreon_filedir}/python3-rstr.list

%changelog

%autochangelog
