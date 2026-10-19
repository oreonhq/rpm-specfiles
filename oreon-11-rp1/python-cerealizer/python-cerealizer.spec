%global source0_hash 8ad33be5038f0987646be093d387e9976937cf2f1016884a05f9fa7cac1fb52e
Name:           python-cerealizer
Version:        0.8.4
Release:        1%{?dist}
Summary:        A secure pickle-like module
License:        PSF-2.0
URL:            http://www.lesfleursdunormal.fr/static/informatique/cerealizer/index_en.html
Source0:        https://files.pythonhosted.org/packages/source/C/Cerealizer/Cerealizer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cerealizer = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cerealizer
Summary:        A secure pickle-like module
%description -n python3-cerealizer

%prep
%global oreon_srcdir Cerealizer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cerealizer usr/lib/python3*/site-packages/cerealizer* usr/lib64/python3*/site-packages/cerealizer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cerealizer* usr/lib64/python3*/site-packages/cerealizer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cerealizer -f %{oreon_filedir}/python3-cerealizer.list

%changelog

%autochangelog
