%global source0_hash 4c59bed60417375cba26cebb2c67ab350b655934670270b1c89dbcd7e60f1b4c
Name:           python-django-crispy-forms
Version:        2.7
Release:        1%{?dist}
Summary:        Best way to have Django DRY forms
License:        MIT
URL:            https://github.com/django-crispy-forms/django-crispy-forms
Source0:        https://files.pythonhosted.org/packages/source/d/django_crispy_forms/django_crispy_forms-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-django-crispy-forms = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-crispy-forms
Summary:        Best way to have Django DRY forms
# oreon:reqs
Requires:       python3dist(django) >= 5.2
# /oreon:reqs
%description -n python3-django-crispy-forms

%prep
%global oreon_srcdir django_crispy_forms-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-crispy-forms usr/lib/python3*/site-packages/django_crispy_forms* usr/lib64/python3*/site-packages/django_crispy_forms* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_crispy_forms* usr/lib64/python3*/site-packages/django_crispy_forms* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-crispy-forms -f %{oreon_filedir}/python3-django-crispy-forms.list

%changelog

%autochangelog
