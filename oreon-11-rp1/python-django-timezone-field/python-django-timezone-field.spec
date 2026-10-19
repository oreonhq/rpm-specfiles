%global source0_hash a004d0b19fe10bf5964cb21a65b36324b16a61879e4711c0dafdf8d6253e8ebc
Name:           python-django-timezone-field
Version:        7.2.2
Release:        1%{?dist}
Summary:        A Django app providing DB, form, and REST framework fields for zoneinfo and pytz timezone objects.
License:        BSD-2-Clause
URL:            https://github.com/mfogel/django-timezone-field/
Source0:        https://files.pythonhosted.org/packages/source/d/django_timezone_field/django_timezone_field-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-django-timezone-field = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-timezone-field
Summary:        A Django app providing DB, form, and REST framework fields for zoneinfo and pytz timezone objects.
%description -n python3-django-timezone-field

%prep
%global oreon_srcdir django_timezone_field-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-timezone-field usr/lib/python3*/site-packages/django_timezone_field* usr/lib64/python3*/site-packages/django_timezone_field* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_timezone_field* usr/lib64/python3*/site-packages/django_timezone_field* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-timezone-field -f %{oreon_filedir}/python3-django-timezone-field.list

%changelog

%autochangelog
