%global source0_hash 6e1a19beef9225c83efd689c7e6b7da2d5215b1f42cd13b7fc3714d0a09c7b25
Name:           python-redis
Version:        8.1.0
Release:        1%{?dist}
Summary:        Python client for Redis database and key-value store
License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
BuildArch:      noarch
Patch:          Avoid-the-multiprocessing-forkserver-method.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-redis = %{version}-%{release}
# /oreon:deps
%package -n       python3-redis+hiredis
Summary:        Metapackage for python3-redis hiredis extras
Requires:       python3-redis = %{version}-%{release}
Requires:       python3dist(hiredis) >= 3.2.0
Provides:       python3dist(redis[hiredis]) = %{version}-%{release}

%description -n python3-redis+hiredis
Metapackage for python3-redis hiredis extras.

%package -n       python3-redis+xxhash
Summary:        Metapackage for python3-redis xxhash extras
Requires:       python3-redis = %{version}-%{release}
Requires:       python3dist(xxhash) >= 3.6.0
Provides:       python3dist(redis[xxhash]) = %{version}-%{release}

%description -n python3-redis+xxhash
Metapackage for python3-redis xxhash extras.

%package -n       python3-redis+ocsp
Summary:        Metapackage for python3-redis ocsp extras
Requires:       python3-redis = %{version}-%{release}
Requires:       python3dist(cryptography) >= 36.0.1
Requires:       python3dist(pyopenssl) >= 20.0.1
Requires:       python3dist(requests) >= 2.31.0
Provides:       python3dist(redis[ocsp]) = %{version}-%{release}

%description -n python3-redis+ocsp
Metapackage for python3-redis ocsp extras.

%package -n       python3-redis+jwt
Summary:        Metapackage for python3-redis jwt extras
Requires:       python3-redis = %{version}-%{release}
Requires:       python3dist(pyjwt) >= 2.13.0
Provides:       python3dist(redis[jwt]) = %{version}-%{release}

%description -n python3-redis+jwt
Metapackage for python3-redis jwt extras.

%package -n       python3-redis+circuit_breaker
Summary:        Metapackage for python3-redis circuit_breaker extras
Requires:       python3-redis = %{version}-%{release}
Requires:       python3dist(pybreaker) >= 1.4.0
Provides:       python3dist(redis[circuit_breaker]) = %{version}-%{release}

%description -n python3-redis+circuit_breaker
Metapackage for python3-redis circuit_breaker extras.

%package -n       python3-redis+otel
Summary:        Metapackage for python3-redis otel extras
Requires:       python3-redis = %{version}-%{release}
Requires:       python3dist(opentelemetry-api) >= 1.39.1
Requires:       python3dist(opentelemetry-sdk) >= 1.39.1
Requires:       python3dist(opentelemetry-exporter-otlp-proto-http) >= 1.39.1
Provides:       python3dist(redis[otel]) = %{version}-%{release}

%description -n python3-redis+otel
Metapackage for python3-redis otel extras.

%description

%package -n     python3-redis
Summary:        Python client for Redis database and key-value store
# oreon:reqs
Requires:       python3dist(async-timeout) >= 4.0.3
# /oreon:reqs
%description -n python3-redis

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir redis-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-redis usr/lib/python3*/site-packages/redis* usr/lib64/python3*/site-packages/redis* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/redis* usr/lib64/python3*/site-packages/redis* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-redis -f %{oreon_filedir}/python3-redis.list

%changelog

%autochangelog
