%global source0_hash c4d1199e6df34125dd36db5eb0efe545b254dec3980ce5dd80e6bab3e78757c3
Name:           python-django-taggit
Version:        6.1.0
Release:        1%{?dist}
Summary:        django-taggit is a reusable Django application for simple tagging.
License:        ...
URL:            https://github.com/jazzband/django-taggit
Source0:        https://files.pythonhosted.org/packages/source/d/django_taggit/django_taggit-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-taggit = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-taggit
Summary:        django-taggit is a reusable Django application for simple tagging.
%description -n python3-django-taggit

%prep
%global oreon_srcdir django_taggit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-taggit usr/lib/python3*/site-packages/django_taggit* usr/lib64/python3*/site-packages/django_taggit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_taggit* usr/lib64/python3*/site-packages/django_taggit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-taggit -f %{oreon_filedir}/python3-django-taggit.list

%changelog

%autochangelog
