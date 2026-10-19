%global source0_hash 1eef4f583c4f8ef4fc57d8b57753fe6e8935501eb36497bb574064e80e3d0b15
Name:           python-klein
Version:        24.8.0
Release:        1%{?dist}
Summary:        werkzeug + twisted.web
License:        MIT
URL:            https://github.com/twisted/klein
Source0:        https://files.pythonhosted.org/packages/source/k/klein/klein-%{version}.tar.gz
BuildArch:      noarch
Patch0:         imp-removal.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-klein = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-klein
Summary:        werkzeug + twisted.web
%description -n python3-klein

%prep
%global oreon_srcdir klein-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-klein usr/lib/python3*/site-packages/klein* usr/lib64/python3*/site-packages/klein* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/klein* usr/lib64/python3*/site-packages/klein* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-klein -f %{oreon_filedir}/python3-klein.list

%changelog

%autochangelog
