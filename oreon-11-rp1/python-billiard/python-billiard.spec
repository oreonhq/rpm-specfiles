%global source0_hash 3ddeaf82c0373e076c7b450c2fdc7ded6d73981bcfd931da1cdd0c0a03468dc5
Name:           python-billiard
Version:        4.3.0
Release:        1%{?dist}
Summary:        Python multiprocessing fork with improvements and bugfixes
License:        ...
URL:            https://github.com/celery/billiard
Source0:        https://files.pythonhosted.org/packages/source/b/billiard/billiard-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-billiard = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-billiard
Summary:        Python multiprocessing fork with improvements and bugfixes
%description -n python3-billiard

%prep
%global oreon_srcdir billiard-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-billiard usr/lib/python3*/site-packages/billiard* usr/lib64/python3*/site-packages/billiard* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/billiard* usr/lib64/python3*/site-packages/billiard* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-billiard -f %{oreon_filedir}/python3-billiard.list

%changelog

%autochangelog
