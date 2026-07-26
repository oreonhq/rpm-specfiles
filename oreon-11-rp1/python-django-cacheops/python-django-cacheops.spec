%global source0_hash a3c521788190074de00116e599c1948d3eccd24429b0d09366bcb7038cd4c4e1

%global srcname django-cacheops
%global desc %{expand: \
A slick app that supports automatic or manual queryset caching
and automatic granular event-driven invalidation.

It uses redis as backend for ORM cache and redis or filesystem
for simple time-invalidated one.

And there is more to it:

  * decorators to cache any user function or view as a queryset or by time
  * extensions for django and jinja2 templates
  * transparent transaction support
  * dog-pile prevention mechanism
  * a couple of hacks to make django faster}

Name:           python-%{srcname}
Version:        7.2
Release:        3%{?dist}
Summary:        ORM cache with automatic granular event-driven invalidation for Django

License:        BSD-3-Clause
URL:            https://github.com/Suor/%{srcname}
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-jinja2
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-django
BuildRequires:	valkey-compat-redis

%description %{desc}

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cacheops

%check
# Launching a redis server for the tests
mkdir -p data
pidfile=$PWD/redis.pid
%{_bindir}/redis-server \
    --bind 127.0.0.1 \
    --port 6379	\
    --daemonize yes \
    --logfile $PWD/redis.log \
    --dir $PWD/data \
    --pidfile $pidfile

# skipping LockingTests because before_after is too old and not in Fedora
# skipping test_385 because off pickling error
%pytest -v -k "not LockingTests and not test_385"

# shutting down the server
if [ -f $pidfile ]; then
    %{_bindir}/redis-cli -p 6379 shutdown
fi
cat $PWD/redis.log

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG

%changelog
%autochangelog
