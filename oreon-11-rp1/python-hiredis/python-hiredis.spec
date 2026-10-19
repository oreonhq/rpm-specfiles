%global source0_hash 2bbb55435506e481d270df8d0b29dd94acb85d11d71df4b8efce23849a4d0bb7
Name:           python-hiredis
Version:        3.4.1
Release:        1%{?dist}
Summary:        Python wrapper for hiredis
License:        MIT
URL:            https://github.com/redis/hiredis-py/releases
Source0:        https://files.pythonhosted.org/packages/source/h/hiredis/hiredis-%{version}.tar.gz
Patch0:         use-system-hiredis.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hiredis = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-hiredis
Summary:        Python wrapper for hiredis
%description -n python3-hiredis

%prep
%global oreon_srcdir hiredis-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hiredis usr/lib/python3*/site-packages/hiredis* usr/lib64/python3*/site-packages/hiredis* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hiredis* usr/lib64/python3*/site-packages/hiredis* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-hiredis -f %{oreon_filedir}/python3-hiredis.list

%changelog

%autochangelog
