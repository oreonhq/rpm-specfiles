%global source0_hash 5a8b51b6c18ce5ec4edd4d0f23c55a8b15590854168b2e5c734118ee369dcbfd
Name:           python-django-tables2
Version:        3.0.1
Release:        1%{?dist}
Summary:        Table/data-grid framework for Django
License:        ...
URL:            https://github.com/jieter/django-tables2/
Source0:        https://files.pythonhosted.org/packages/source/d/django_tables2/django_tables2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-tables2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-tables2+tablib
Summary:        Metapackage for python3-django-tables2 tablib extras
Requires:       python3-django-tables2 = %{version}-%{release}
Provides:       python3dist(django-tables2[tablib]) = %{version}-%{release}

%description -n python3-django-tables2+tablib
Metapackage for python3-django-tables2 tablib extras.

%description

%package -n     python3-django-tables2
Summary:        Table/data-grid framework for Django
# oreon:reqs
Requires:       python3dist(django) >= 4.2
# /oreon:reqs
%description -n python3-django-tables2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_tables2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-tables2 usr/lib/python3*/site-packages/django_tables2* usr/lib64/python3*/site-packages/django_tables2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_tables2* usr/lib64/python3*/site-packages/django_tables2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-tables2 -f %{oreon_filedir}/python3-django-tables2.list

%changelog

%autochangelog
