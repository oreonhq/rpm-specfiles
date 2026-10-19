%global source0_hash 3d20a8d748add9b1c68efc6c592a99b4b0937c9dcddd140fdae352bf2513aea5
Name:           python-bitstruct
Version:        8.23.0
Release:        1%{?dist}
Summary:        This module performs conversions between Python values and C bit field structs represented as Python byte strings.
License:        MIT
URL:            https://github.com/eerimoq/bitstruct
Source0:        https://files.pythonhosted.org/packages/source/b/bitstruct/bitstruct-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 68.0
Requires:       python3-bitstruct = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bitstruct
Summary:        This module performs conversions between Python values and C bit field structs represented as Python byte strings.
%description -n python3-bitstruct

%prep
%global oreon_srcdir bitstruct-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bitstruct usr/lib/python3*/site-packages/bitstruct* usr/lib64/python3*/site-packages/bitstruct* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bitstruct* usr/lib64/python3*/site-packages/bitstruct* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bitstruct -f %{oreon_filedir}/python3-bitstruct.list

%changelog

%autochangelog
