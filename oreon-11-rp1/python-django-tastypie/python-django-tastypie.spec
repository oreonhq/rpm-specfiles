%global source0_hash 1eb41318b08c0ebc9b8a386871b45401a623e6a5566bf32ae3e17be2c59318b7
Name:           python-django-tastypie
Version:        0.15.1
Release:        1%{?dist}
Summary:        A flexible _ capable API layer for Django.
License:        ...
URL:            https://github.com/django-tastypie/django-tastypie
Source0:        https://files.pythonhosted.org/packages/source/d/django_tastypie/django_tastypie-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-tastypie = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-tastypie
Summary:        A flexible _ capable API layer for Django.
%description -n python3-django-tastypie

%prep
%global oreon_srcdir django_tastypie-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-tastypie usr/lib/python3*/site-packages/django_tastypie* usr/lib64/python3*/site-packages/django_tastypie* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_tastypie* usr/lib64/python3*/site-packages/django_tastypie* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-tastypie -f %{oreon_filedir}/python3-django-tastypie.list

%changelog

%autochangelog
