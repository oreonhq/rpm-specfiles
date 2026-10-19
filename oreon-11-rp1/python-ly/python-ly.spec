%global source0_hash 636e10bc0efba784a2c88c672334674da06be96039abf65744710860312b0a26
Name:           python-ly
Version:        1.2
Release:        1%{?dist}
Summary:        This is just a test module
License:        ...
URL:            https://pypi.org/project/ly/
Source0:        https://files.pythonhosted.org/packages/source/l/ly/ly-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ly = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ly
Summary:        This is just a test module
%description -n python3-ly

%prep
%global oreon_srcdir ly-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ly usr/lib/python3*/site-packages/ly* usr/lib64/python3*/site-packages/ly* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ly* usr/lib64/python3*/site-packages/ly* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ly -f %{oreon_filedir}/python3-ly.list

%changelog

%autochangelog
