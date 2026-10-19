%global source0_hash 437b6a622223824380bfb4e64f612711a6b648c795f565efc8625af66fb57f0c
Name:           python-invoke
Version:        3.0.3
Release:        1%{?dist}
Summary:        Pythonic task execution
License:        BSD-2-Clause
URL:            https://github.com/pyinvoke/invoke
Source0:        https://files.pythonhosted.org/packages/source/i/invoke/invoke-%{version}.tar.gz
BuildArch:      noarch
Patch1:         0001-Fix-requirements.patch
Patch2:         %{name}-SystemError.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-invoke = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-invoke
Summary:        Pythonic task execution
%description -n python3-invoke

%prep
%global oreon_srcdir invoke-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-invoke usr/lib/python3*/site-packages/invoke* usr/lib64/python3*/site-packages/invoke* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/invoke* usr/lib64/python3*/site-packages/invoke* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-invoke -f %{oreon_filedir}/python3-invoke.list

%changelog

%autochangelog
