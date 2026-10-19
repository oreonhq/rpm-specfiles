%global source0_hash 8cdaf5b7f3f4f39557ae05ed8b0852136b43a04ab686db7d39255b206233677a
Name:           python-astroid
Version:        4.3.2
Release:        1%{?dist}
Summary:        An abstract syntax tree for Python with inference support.
License:        LGPL-2.1-or-later
URL:            https://github.com/pylint-dev/astroid
Source0:        https://files.pythonhosted.org/packages/source/a/astroid/astroid-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-astroid = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-astroid
Summary:        An abstract syntax tree for Python with inference support.
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4
# /oreon:reqs
%description -n python3-astroid

%prep
%global oreon_srcdir astroid-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-astroid usr/lib/python3*/site-packages/astroid* usr/lib64/python3*/site-packages/astroid* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/astroid* usr/lib64/python3*/site-packages/astroid* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-astroid -f %{oreon_filedir}/python3-astroid.list

%changelog

%autochangelog
