%global source0_hash b1d6546f9f5446987dcc1146b5f9bd7c4343ad38551f984aefa8e331309b5364
Name:           python-django-rq
Version:        4.2.0
Release:        1%{?dist}
Summary:        An app that provides django integration for RQ _Redis Queue_
License:        MIT
URL:            https://python-rq.org/patterns/django/
Source0:        https://files.pythonhosted.org/packages/source/d/django_rq/django_rq-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-rq = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-rq+prometheus
Summary:        Metapackage for python3-django-rq prometheus extras
Requires:       python3-django-rq = %{version}-%{release}
Requires:       python3dist(prometheus-client) >= 0.4.0
Provides:       python3dist(django-rq[prometheus]) = %{version}-%{release}

%description -n python3-django-rq+prometheus
Metapackage for python3-django-rq prometheus extras.

%package -n       python3-django-rq+testing
Summary:        Metapackage for python3-django-rq testing extras
Requires:       python3-django-rq = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(pytest-django) >= 4.5
Provides:       python3dist(django-rq[testing]) = %{version}-%{release}

%description -n python3-django-rq+testing
Metapackage for python3-django-rq testing extras.

%description

%package -n     python3-django-rq
Summary:        An app that provides django integration for RQ _Redis Queue_
# oreon:reqs
Requires:       python3dist(django) >= 4.2
Requires:       python3dist(redis) >= 3.5
Requires:       python3dist(rq) >= 2.6.1
# /oreon:reqs
%description -n python3-django-rq

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_rq-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-rq usr/lib/python3*/site-packages/django_rq* usr/lib64/python3*/site-packages/django_rq* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_rq* usr/lib64/python3*/site-packages/django_rq* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-rq -f %{oreon_filedir}/python3-django-rq.list

%changelog

%autochangelog
