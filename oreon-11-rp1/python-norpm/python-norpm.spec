%global source0_hash a556e65415706a64b25b0d483ddfc8aa7ae0e9530135bd94f6656d0720a2614a
Name:           python-norpm
Version:        1.11
Release:        1%{?dist}
Summary:        RPM Macro Expansion in Python
License:        LGPL-2.1-or-later
URL:            https://github.com/praiskup/norpm
Source0:        https://files.pythonhosted.org/packages/source/n/norpm/norpm-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-norpm = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-norpm
Summary:        RPM Macro Expansion in Python
%description -n python3-norpm

%prep
%global oreon_srcdir norpm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-norpm usr/lib/python3*/site-packages/norpm* usr/lib64/python3*/site-packages/norpm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/norpm* usr/lib64/python3*/site-packages/norpm* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-norpm -f %{oreon_filedir}/python3-norpm.list

%changelog

%autochangelog
