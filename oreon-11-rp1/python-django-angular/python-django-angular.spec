%global source0_hash b9c97de2b4658d30f6e3a4f9d5515a479914ac5976a3cb46a609faae0bd95852
Name:           python-django-angular
Version:        2.3.1
Release:        1%{?dist}
Summary:        Let Django play well with AngularJS
License:        MIT
URL:            https://github.com/jrief/django-angular
Source0:        https://files.pythonhosted.org/packages/source/d/django-angular/django-angular-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-angular = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-angular
Summary:        Let Django play well with AngularJS
%description -n python3-django-angular

%prep
%global oreon_srcdir django-angular-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-angular usr/lib/python3*/site-packages/django_angular* usr/lib64/python3*/site-packages/django_angular* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_angular* usr/lib64/python3*/site-packages/django_angular* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-angular -f %{oreon_filedir}/python3-django-angular.list

%changelog

%autochangelog
