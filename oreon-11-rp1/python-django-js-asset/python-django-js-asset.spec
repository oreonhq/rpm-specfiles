%global source0_hash 8442924298430402edc6620d6383545c81610db08859e0162665309e68262270
Name:           python-django-js-asset
Version:        4.1.0
Release:        1%{?dist}
Summary:        script tag with additional attributes for django.forms.Media
License:        BSD-3-Clause
URL:            https://github.com/feincms/django-js-asset/
Source0:        https://files.pythonhosted.org/packages/source/d/django_js_asset/django_js_asset-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-js-asset = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-js-asset+tests
Summary:        Metapackage for python3-django-js-asset tests extras
Requires:       python3-django-js-asset = %{version}-%{release}
Provides:       python3dist(django-js-asset[tests]) = %{version}-%{release}

%description -n python3-django-js-asset+tests
Metapackage for python3-django-js-asset tests extras.

%description

%package -n     python3-django-js-asset
Summary:        script tag with additional attributes for django.forms.Media
# oreon:reqs
Requires:       python3dist(django) >= 4.2
# /oreon:reqs
%description -n python3-django-js-asset

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_js_asset-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-js-asset usr/lib/python3*/site-packages/django_js_asset* usr/lib64/python3*/site-packages/django_js_asset* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_js_asset* usr/lib64/python3*/site-packages/django_js_asset* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-js-asset -f %{oreon_filedir}/python3-django-js-asset.list

%changelog

%autochangelog
