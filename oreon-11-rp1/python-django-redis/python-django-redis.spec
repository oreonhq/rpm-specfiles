%global source0_hash e48491c862f4350b0747ceb1016700686fb93c4f4e0fb9c490fe6c6658ffd933
Name:           python-django-redis
Version:        7.0.0
Release:        1%{?dist}
Summary:        Full featured redis cache backend for Django.
License:        BSD-3-Clause
URL:            https://github.com/jazzband/django-redis
Source0:        https://files.pythonhosted.org/packages/source/d/django_redis/django_redis-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-django-redis = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-redis+hiredis
Summary:        Metapackage for python3-django-redis hiredis extras
Requires:       python3-django-redis = %{version}-%{release}
Requires:       python3dist(redis[hiredis]) >= 4.0.2
Provides:       python3dist(django-redis[hiredis]) = %{version}-%{release}

%description -n python3-django-redis+hiredis
Metapackage for python3-django-redis hiredis extras.

%package -n       python3-django-redis+lz4
Summary:        Metapackage for python3-django-redis lz4 extras
Requires:       python3-django-redis = %{version}-%{release}
Requires:       python3dist(lz4) >= 0.15
Provides:       python3dist(django-redis[lz4]) = %{version}-%{release}

%description -n python3-django-redis+lz4
Metapackage for python3-django-redis lz4 extras.

%package -n       python3-django-redis+msgpack
Summary:        Metapackage for python3-django-redis msgpack extras
Requires:       python3-django-redis = %{version}-%{release}
Requires:       python3dist(msgpack) >= 0.6.0
Provides:       python3dist(django-redis[msgpack]) = %{version}-%{release}

%description -n python3-django-redis+msgpack
Metapackage for python3-django-redis msgpack extras.

%package -n       python3-django-redis+pyzstd
Summary:        Metapackage for python3-django-redis pyzstd extras
Requires:       python3-django-redis = %{version}-%{release}
Requires:       python3dist(pyzstd) >= 0.15
Provides:       python3dist(django-redis[pyzstd]) = %{version}-%{release}

%description -n python3-django-redis+pyzstd
Metapackage for python3-django-redis pyzstd extras.

%description

%package -n     python3-django-redis
Summary:        Full featured redis cache backend for Django.
# oreon:reqs
Requires:       python3dist(django) < 7.0
Requires:       python3dist(django) >= 5.2
Requires:       python3dist(redis) >= 4.0.2
Requires:       python3dist(typing-extensions) >= 4.12
# /oreon:reqs
%description -n python3-django-redis

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_redis-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-redis usr/lib/python3*/site-packages/django_redis* usr/lib64/python3*/site-packages/django_redis* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_redis* usr/lib64/python3*/site-packages/django_redis* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-redis -f %{oreon_filedir}/python3-django-redis.list

%changelog

%autochangelog
