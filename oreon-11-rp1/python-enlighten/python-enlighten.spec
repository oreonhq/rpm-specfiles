%global source0_hash 85c35412a9a4f3886b3337d41f813441fab9a30d9f5b5f0c015bd078a4411473
Name:           python-enlighten
Version:        1.14.1
Release:        1%{?dist}
Summary:        Enlighten Progress Bar
License:        MPL-2.0
URL:            https://python-enlighten.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/e/enlighten/enlighten-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-enlighten = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-enlighten
Summary:        Enlighten Progress Bar
%description -n python3-enlighten

%prep
%global oreon_srcdir enlighten-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-enlighten usr/lib/python3*/site-packages/enlighten* usr/lib64/python3*/site-packages/enlighten* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/enlighten* usr/lib64/python3*/site-packages/enlighten* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-enlighten -f %{oreon_filedir}/python3-enlighten.list

%changelog

%autochangelog
