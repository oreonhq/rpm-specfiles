%global source0_hash 4e3a95b63175be8e10f0662de506a36d8cc6cb86ecc5b30ae880c8dafb34a0cd
Name:           python-wxpython
Version:        4.3.1
Release:        1%{?dist}
Summary:        Cross platform GUI toolkit for Python, _Phoenix_ version
License:        ...
URL:            https://wxPython.org/
Source0:        https://files.pythonhosted.org/packages/source/w/wxpython/wxpython-%{version}.tar.gz
Patch:          fix-ftbfs-doxygen-1.15.0.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.0.10
BuildRequires:  python3dist(requests) >= 2.26.0
BuildRequires:  python3dist(setuptools) >= 70.1
BuildRequires:  python3dist(sip) == 6.12.0
Requires:       python3-wxpython = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wxpython
Summary:        Cross platform GUI toolkit for Python, _Phoenix_ version
%description -n python3-wxpython

%prep
%global oreon_srcdir wxpython-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wxpython usr/lib/python3*/site-packages/wxpython* usr/lib64/python3*/site-packages/wxpython* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wxpython* usr/lib64/python3*/site-packages/wxpython* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wxpython -f %{oreon_filedir}/python3-wxpython.list

%changelog

%autochangelog
