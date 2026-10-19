%global source0_hash 759c0bdad4c135d5e4cb43b0b98612e8d1cbd81c3ed1ce6698298ff0740bac44
Name:           python-django-health-check
Version:        4.5.1
Release:        1%{?dist}
Summary:        Monitor the health of your Django app and its connected services.
License:        MIT
URL:            https://github.com/codingjoe/django-health-check
Source0:        https://files.pythonhosted.org/packages/source/d/django_health_check/django_health_check-%{version}.tar.gz
BuildArch:      noarch
Patch:          django-health-check-3.20.8-pytest-no-coverage.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-django-health-check = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-health-check+psutil
Summary:        Metapackage for python3-django-health-check psutil extras
Requires:       python3-django-health-check = %{version}-%{release}
Requires:       python3dist(psutil) >= 7.2.0
Provides:       python3dist(django-health-check[psutil]) = %{version}-%{release}

%description -n python3-django-health-check+psutil
Metapackage for python3-django-health-check psutil extras.

%package -n       python3-django-health-check+celery
Summary:        Metapackage for python3-django-health-check celery extras
Requires:       python3-django-health-check = %{version}-%{release}
Requires:       python3dist(celery) >= 5.0.0
Provides:       python3dist(django-health-check[celery]) = %{version}-%{release}

%description -n python3-django-health-check+celery
Metapackage for python3-django-health-check celery extras.

%package -n       python3-django-health-check+kafka
Summary:        Metapackage for python3-django-health-check kafka extras
Requires:       python3-django-health-check = %{version}-%{release}
Requires:       python3dist(confluent-kafka) >= 2.0.0
Provides:       python3dist(django-health-check[kafka]) = %{version}-%{release}

%description -n python3-django-health-check+kafka
Metapackage for python3-django-health-check kafka extras.

%package -n       python3-django-health-check+rabbitmq
Summary:        Metapackage for python3-django-health-check rabbitmq extras
Requires:       python3-django-health-check = %{version}-%{release}
Requires:       python3dist(aio-pika) >= 9.0.0
Provides:       python3dist(django-health-check[rabbitmq]) = %{version}-%{release}

%description -n python3-django-health-check+rabbitmq
Metapackage for python3-django-health-check rabbitmq extras.

%package -n       python3-django-health-check+redis
Summary:        Metapackage for python3-django-health-check redis extras
Requires:       python3-django-health-check = %{version}-%{release}
Requires:       python3dist(redis) >= 4.2.0
Provides:       python3dist(django-health-check[redis]) = %{version}-%{release}

%description -n python3-django-health-check+redis
Metapackage for python3-django-health-check redis extras.

%package -n       python3-django-health-check+rss
Summary:        Metapackage for python3-django-health-check rss extras
Requires:       python3-django-health-check = %{version}-%{release}
Requires:       python3dist(httpx) >= 0.27.0
Requires:       python3dist(feedparser) >= 6.0.0
Provides:       python3dist(django-health-check[rss]) = %{version}-%{release}

%description -n python3-django-health-check+rss
Metapackage for python3-django-health-check rss extras.

%package -n       python3-django-health-check+atlassian
Summary:        Metapackage for python3-django-health-check atlassian extras
Requires:       python3-django-health-check = %{version}-%{release}
Requires:       python3dist(httpx) >= 0.27.0
Provides:       python3dist(django-health-check[atlassian]) = %{version}-%{release}

%description -n python3-django-health-check+atlassian
Metapackage for python3-django-health-check atlassian extras.

%description

%package -n     python3-django-health-check
Summary:        Monitor the health of your Django app and its connected services.
# oreon:reqs
Requires:       python3dist(django) >= 5.2
Requires:       python3dist(dnspython) >= 2.0.0
# /oreon:reqs
%description -n python3-django-health-check

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_health_check-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-health-check usr/lib/python3*/site-packages/django_health_check* usr/lib64/python3*/site-packages/django_health_check* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_health_check* usr/lib64/python3*/site-packages/django_health_check* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-health-check -f %{oreon_filedir}/python3-django-health-check.list

%changelog

%autochangelog
