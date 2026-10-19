%global source0_hash 52b30c08571108023937e4b5d96a5cc35282ff0a2e51630aeea00e27d723d3ac
Name:           python-django-formtools
Version:        2.7
Release:        1%{?dist}
Summary:        A set of high-level abstractions for Django forms
License:        ...
URL:            https://django-formtools.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/d/django_formtools/django_formtools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-django-formtools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-formtools
Summary:        A set of high-level abstractions for Django forms
# oreon:reqs
Requires:       python3dist(django) >= 5.2
# /oreon:reqs
%description -n python3-django-formtools

%prep
%global oreon_srcdir django_formtools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-formtools usr/lib/python3*/site-packages/django_formtools* usr/lib64/python3*/site-packages/django_formtools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_formtools* usr/lib64/python3*/site-packages/django_formtools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-formtools -f %{oreon_filedir}/python3-django-formtools.list

%changelog

%autochangelog
