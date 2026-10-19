%global source0_hash cf5661357ff22bc64e20d3341c26e538aa54583aea0763cfe6aaec0ab8e3a8ee
Name:           python-django-mptt
Version:        0.18.0
Release:        1%{?dist}
Summary:        Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.
License:        MIT
URL:            https://github.com/django-mptt/django-mptt/
Source0:        https://files.pythonhosted.org/packages/source/d/django_mptt/django_mptt-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-mptt = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-mptt+tests
Summary:        Metapackage for python3-django-mptt tests extras
Requires:       python3-django-mptt = %{version}-%{release}
Provides:       python3dist(django-mptt[tests]) = %{version}-%{release}

%description -n python3-django-mptt+tests
Metapackage for python3-django-mptt tests extras.

%description

%package -n     python3-django-mptt
Summary:        Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.
%description -n python3-django-mptt

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_mptt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-mptt usr/lib/python3*/site-packages/django_mptt* usr/lib64/python3*/site-packages/django_mptt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_mptt* usr/lib64/python3*/site-packages/django_mptt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-mptt -f %{oreon_filedir}/python3-django-mptt.list

%changelog

%autochangelog
