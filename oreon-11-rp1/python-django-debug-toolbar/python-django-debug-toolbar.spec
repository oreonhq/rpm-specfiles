%global source0_hash cae32d3e441e608f39f3f1ca6b3f028c38d5d04d74c98d8ab96d46022dee3163
Name:           python-django-debug-toolbar
Version:        8.0.0
Release:        1%{?dist}
Summary:        A configurable set of panels that display various debug information about the current request/response.
License:        BSD-3-Clause
URL:            https://github.com/django-commons/django-debug-toolbar
Source0:        https://files.pythonhosted.org/packages/source/d/django_debug_toolbar/django_debug_toolbar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-debug-toolbar = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-debug-toolbar
Summary:        A configurable set of panels that display various debug information about the current request/response.
# oreon:reqs
Requires:       python3dist(django) >= 5.2
Requires:       python3dist(sqlparse) >= 0.2
# /oreon:reqs
%description -n python3-django-debug-toolbar

%prep
%global oreon_srcdir django_debug_toolbar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-debug-toolbar usr/lib/python3*/site-packages/django_debug_toolbar* usr/lib64/python3*/site-packages/django_debug_toolbar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_debug_toolbar* usr/lib64/python3*/site-packages/django_debug_toolbar* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-debug-toolbar -f %{oreon_filedir}/python3-django-debug-toolbar.list

%changelog

%autochangelog
