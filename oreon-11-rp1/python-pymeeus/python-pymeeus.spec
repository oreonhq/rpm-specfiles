%global source0_hash 548f7186bd8b96cbc069cf649a8e8e377dce49ac74486709849fe63a99cad684
Name:           python-pymeeus
Version:        0.5.12
Release:        1%{?dist}
Summary:        Python implementation of Jean Meeus astronomical routines
License:        ...
URL:            https://github.com/architest/pymeeus
Source0:        https://files.pythonhosted.org/packages/source/P/PyMeeus/PyMeeus-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-Fix-documentation-build-with-sphinx-8.patch
Patch1:         0002-fix-pytest-7-2-compatibility.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pymeeus = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pymeeus
Summary:        Python implementation of Jean Meeus astronomical routines
%description -n python3-pymeeus

%prep
%global oreon_srcdir PyMeeus-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pymeeus usr/lib/python3*/site-packages/pymeeus* usr/lib64/python3*/site-packages/pymeeus* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymeeus* usr/lib64/python3*/site-packages/pymeeus* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pymeeus -f %{oreon_filedir}/python3-pymeeus.list

%changelog

%autochangelog
