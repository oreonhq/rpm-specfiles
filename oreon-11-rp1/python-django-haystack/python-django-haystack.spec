%global source0_hash 1226a7c9ce13e1e7ead8ac83f6e87bfef4996f146ed24971fde7896115b1c530
Name:           python-django-haystack
Version:        3.4.0
Release:        1%{?dist}
Summary:        Pluggable search for Django.
License:        BSD-3-Clause
URL:            http://haystacksearch.org/
Source0:        https://files.pythonhosted.org/packages/source/d/django_haystack/django_haystack-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4
Requires:       python3-django-haystack = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-haystack+elasticsearch
Summary:        Metapackage for python3-django-haystack elasticsearch extras
Requires:       python3-django-haystack = %{version}-%{release}
Requires:       python3dist(elasticsearch) < 8
Requires:       python3dist(elasticsearch) >= 5
Provides:       python3dist(django-haystack[elasticsearch]) = %{version}-%{release}

%description -n python3-django-haystack+elasticsearch
Metapackage for python3-django-haystack elasticsearch extras.

%package -n       python3-django-haystack+testing
Summary:        Metapackage for python3-django-haystack testing extras
Requires:       python3-django-haystack = %{version}-%{release}
Requires:       python3dist(geopy) == 2
Requires:       python3dist(pysolr) >= 3.7
Requires:       python3dist(whoosh) < 3.0
Requires:       python3dist(whoosh) >= 2.5.4
Provides:       python3dist(django-haystack[testing]) = %{version}-%{release}

%description -n python3-django-haystack+testing
Metapackage for python3-django-haystack testing extras.

%description

%package -n     python3-django-haystack
Summary:        Pluggable search for Django.
# oreon:reqs
Requires:       python3dist(django) >= 4.2
# /oreon:reqs
%description -n python3-django-haystack

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_haystack-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-haystack usr/lib/python3*/site-packages/django_haystack* usr/lib64/python3*/site-packages/django_haystack* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_haystack* usr/lib64/python3*/site-packages/django_haystack* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-haystack -f %{oreon_filedir}/python3-django-haystack.list

%changelog

%autochangelog
