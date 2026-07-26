%global source0_hash 017c852d3df6b8492666b5e3544bb4f283a49ca357fac28af465b8cb8017f1e4

Name:           python-flask-session
Version:        0.8.0
Release:        2%{?dist}
Summary:        Server side session extension for Flask

License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/flask-session
Source:         %{url}/archive/%{version}/flask-session-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

# Extra testing deps
BuildRequires: redis
BuildRequires: python3-redis
BuildRequires: python3-pymemcache
BuildRequires: memcached

# These are for the remaining tests that aren't working properly at the moment
# See the check section
#BuildRequires: python3-pymongo
#BuildRequires: python3-boto3
#BuildRequires: python3-flask-sqlalchemy

%global _description %{expand:
Flask-Session is an extension for Flask that adds support for server-side
sessions to your application.}

%description %_description

%package -n python3-flask-session
Summary:        %{summary}

%description -n python3-flask-session %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flask-session-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files flask_session

%check
# Enable only working backends tests:
#   Mongo test: no mongodb in Fedora anymore due to licensing
#   Sqlalchemy test expects a pre-created DB
#   DynamoDB: missing mypy_boto3 dependencies in Fedora
# Note: pytest will try to import so will fail if
#       we run on whole directory, so we have to run on files
redis-server &
%pytest -v tests/test_basic.py tests/test_cachelib.py tests/test_filesystem.py tests/test_redis.py
kill %1

memcached -vv &
%pytest -v tests/test_memcached.py
kill %1

%files -n python3-flask-session -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
