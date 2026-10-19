%global source0_hash 0f2a4552174af98b621522eb36c8d1009a7f73d2bf591d973a34fc65cc740680
Name:           python-django-markdownx
Version:        4.0.11
Release:        1%{?dist}
Summary:        A comprehensive Markdown editor built for Django.
License:        ...
URL:            https://github.com/neutronX/django-markdownx
Source0:        https://files.pythonhosted.org/packages/source/d/django_markdownx/django_markdownx-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-markdownx = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-markdownx
Summary:        A comprehensive Markdown editor built for Django.
%description -n python3-django-markdownx

%prep
%global oreon_srcdir django_markdownx-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-markdownx usr/lib/python3*/site-packages/django_markdownx* usr/lib64/python3*/site-packages/django_markdownx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_markdownx* usr/lib64/python3*/site-packages/django_markdownx* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-markdownx -f %{oreon_filedir}/python3-django-markdownx.list

%changelog

%autochangelog
