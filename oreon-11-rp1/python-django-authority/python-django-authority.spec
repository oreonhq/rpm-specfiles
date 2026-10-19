%global source0_hash f2e0b2adfa98cc5f0b4766f35d2666c7d040452d91e93fc47401e85f85bbecbd
Name:           python-django-authority
Version:        0.14
Release:        1%{?dist}
Summary:        A Django app that provides generic per-object-permissions for Django_s auth app.
License:        ...
URL:            https://github.com/jazzband/django-authority/
Source0:        https://files.pythonhosted.org/packages/source/d/django-authority/django-authority-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-authority = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-authority
Summary:        A Django app that provides generic per-object-permissions for Django_s auth app.
%description -n python3-django-authority

%prep
%global oreon_srcdir django-authority-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-authority usr/lib/python3*/site-packages/django_authority* usr/lib64/python3*/site-packages/django_authority* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_authority* usr/lib64/python3*/site-packages/django_authority* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-authority -f %{oreon_filedir}/python3-django-authority.list

%changelog

%autochangelog
