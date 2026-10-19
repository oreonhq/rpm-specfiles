%global source0_hash 017c852d3df6b8492666b5e3544bb4f283a49ca357fac28af465b8cb8017f1e4
Name:           python-flask-session
Version:        0.8.0
Release:        2%{?dist}
Summary:        Server side session extension for Flask
License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/flask-session
Source0:        https://github.com/pallets-eco/flask-session/archive/%{version}/flask-session-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-flask-session = %{version}-%{release}
# /oreon:deps
%package -n       python3-flask-session+cachelib
Summary:        Metapackage for python3-flask-session cachelib extras
Requires:       python3-flask-session = %{version}-%{release}
Requires:       python3dist(cachelib) >= 0.10.2
Provides:       python3dist(flask-session[cachelib]) = %{version}-%{release}

%description -n python3-flask-session+cachelib
Metapackage for python3-flask-session cachelib extras.

%package -n       python3-flask-session+memcached
Summary:        Metapackage for python3-flask-session memcached extras
Requires:       python3-flask-session = %{version}-%{release}
Provides:       python3dist(flask-session[memcached]) = %{version}-%{release}

%description -n python3-flask-session+memcached
Metapackage for python3-flask-session memcached extras.

%package -n       python3-flask-session+mongodb
Summary:        Metapackage for python3-flask-session mongodb extras
Requires:       python3-flask-session = %{version}-%{release}
Requires:       python3dist(pymongo) >= 4.6.2
Provides:       python3dist(flask-session[mongodb]) = %{version}-%{release}

%description -n python3-flask-session+mongodb
Metapackage for python3-flask-session mongodb extras.

%package -n       python3-flask-session+redis
Summary:        Metapackage for python3-flask-session redis extras
Requires:       python3-flask-session = %{version}-%{release}
Requires:       python3dist(redis) >= 5.0.3
Provides:       python3dist(flask-session[redis]) = %{version}-%{release}

%description -n python3-flask-session+redis
Metapackage for python3-flask-session redis extras.

%package -n       python3-flask-session+sqlalchemy
Summary:        Metapackage for python3-flask-session sqlalchemy extras
Requires:       python3-flask-session = %{version}-%{release}
Requires:       python3dist(flask-sqlalchemy) >= 3.0.5
Provides:       python3dist(flask-session[sqlalchemy]) = %{version}-%{release}

%description -n python3-flask-session+sqlalchemy
Metapackage for python3-flask-session sqlalchemy extras.

%package -n       python3-flask-session+all
Summary:        Metapackage for python3-flask-session all extras
Requires:       python3-flask-session = %{version}-%{release}
Provides:       python3dist(flask-session[all]) = %{version}-%{release}

%description -n python3-flask-session+all
Metapackage for python3-flask-session all extras.

%description

%package -n python3-flask-session
Summary:        Server side session extension for Flask
# oreon:reqs
Requires:       python3dist(flask) >= 2.2
Requires:       python3dist(msgspec) >= 0.18.6
# /oreon:reqs
%description -n python3-flask-session

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir flask-session-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-session usr/lib/python3*/site-packages/flask_session* usr/lib64/python3*/site-packages/flask_session* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_session* usr/lib64/python3*/site-packages/flask_session* usr/bin/*

%check

redis-server &
%pytest -v tests/test_basic.py tests/test_cachelib.py tests/test_filesystem.py tests/test_redis.py
kill %1
memcached -vv &
%pytest -v tests/test_memcached.py
kill %1
%files
%files -n python3-flask-session -f %{oreon_filedir}/python3-flask-session.list

%changelog

%autochangelog
