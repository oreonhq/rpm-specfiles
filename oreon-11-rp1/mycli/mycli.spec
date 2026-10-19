%global source0_hash 343470fae15ee3ec4ef1a0ac6f4ca30dfad69df814c2b681403d7d0ab2a77792
%global         pypi_name mycli
Summary:        Interactive CLI for MySQL Database with auto-completion and syntax highlighting
Name:           mycli
Version:        2.25.2
Release:        1%{?dist}
License:        LicenseRef-Callaway-BSD
URL:            https://mycli.net
Source0:        https://files.pythonhosted.org/packages/source/m/mycli/mycli-%{version}.tar.gz
Patch:          0001-Revert-to-older-toml-format.patch
Patch:          0002-Fix-tox-config-and-some-test-fixes.patch
Patch:          0003-Disable-more-test-which-requires-db-server.patch
Patch:          0004-Revert-to-sqlglot-5.1.3.patch
Patch:          0005-Relax-various-reqs.patch
BuildArch:      noarch
%{?server_tests:BuildRequires:  mysql-server}
Suggests:       python3-mycli+ssh
%py_provides    python3-%{pypi_name}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-mycli = %{version}-%{release}
# /oreon:deps
%package -n       python3-mycli+llm
Summary:        Metapackage for python3-mycli llm extras
Requires:       python3-mycli = %{version}-%{release}
Requires:       python3dist(llm) >= 0.33
Requires:       python3dist(setuptools) == 83.*
Requires:       python3dist(pip) >= 26.2.1
Provides:       python3dist(mycli[llm]) = %{version}-%{release}

%description -n python3-mycli+llm
Metapackage for python3-mycli llm extras.

%package -n       python3-mycli+dataframe
Summary:        Metapackage for python3-mycli dataframe extras
Requires:       python3-mycli = %{version}-%{release}
Requires:       python3dist(polars) >= 1.44.1
Requires:       python3dist(altair) >= 6.2.2
Requires:       python3dist(vl-convert-python) >= 1.9.0
Provides:       python3dist(mycli[dataframe]) = %{version}-%{release}

%description -n python3-mycli+dataframe
Metapackage for python3-mycli dataframe extras.

%package -n       python3-mycli+all
Summary:        Metapackage for python3-mycli all extras
Requires:       python3-mycli = %{version}-%{release}
Provides:       python3dist(mycli[all]) = %{version}-%{release}

%description -n python3-mycli+all
Metapackage for python3-mycli all extras.

%package -n       python3-mycli+dev
Summary:        Metapackage for python3-mycli dev extras
Requires:       python3-mycli = %{version}-%{release}
Requires:       python3dist(behave) >= 1.3.3
Requires:       python3dist(coverage) >= 7.15.4
Requires:       python3dist(mypy) >= 2.3.1
Requires:       python3dist(pexpect) >= 4.9.0
Requires:       python3dist(pytest) >= 9.1.1
Requires:       python3dist(pytest-cov) >= 7.1.0
Requires:       python3dist(pytest-random-order) >= 1.2.0
Requires:       python3dist(tox) >= 4.35.0
Requires:       python3dist(pdbpp) >= 0.11.7
Requires:       python3dist(ruff) >= 0.16.5
Provides:       python3dist(mycli[dev]) = %{version}-%{release}

%description -n python3-mycli+dev
Metapackage for python3-mycli dev extras.

%description
Nice interactive shell for MySQL Database with auto-completion and
syntax highlighting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

db_env () {
    export PYTEST_HOST=127.0.0.1
    export PYTEST_USER=root
    export PYTEST_PASSWORD=root
    export PYTEST_PORT=3333
    export DATADIR=$(mktemp -d /tmp/myclitest.XXXXXX)
}
db_setup () {
    mysqld --no-defaults --datadir=$DATADIR --initialize-insecure
    mysqld --no-defaults --datadir=$DATADIR --socket=$DATADIR/my.sock --port=$PYTEST_PORT -D
    mysql -uroot --password='' --socket=$DATADIR/my.sock --port=$PYTEST_PORT -e 'CREATE DATABASE mycli_test_db;'
    mysql -uroot --password='' --socket=$DATADIR/my.sock --port=$PYTEST_PORT -e 'CREATE DATABASE test;'
    mysql -uroot --password='' --socket=$DATADIR/my.sock --port=$PYTEST_PORT -e "set password='"$PYTEST_PASSWORD"';"
}
db_teardown () {
    mysql -uroot --password=$PYTEST_PASSWORD --socket=$DATADIR/my.sock --port=$PYTEST_PORT -e 'SHUTDOWN;'
    count=0
    while [ $count -lt 15 ] ; do
	sleep 1
	grep -q 'Shutdown complete' $DATADIR/*.err && break
	((count+=1))
    done
    rm -rf $DATADIR/*
    rm -r  $DATADIR
}
%if 0%{?server_tests}
db_env
db_setup
echo :$PYTEST_USER:$PYTEST_PASSWORD:$PYTEST_PORT:
mysql -uroot --password=$PYTEST_PASSWORD --socket=$DATADIR/my.sock --port=3333 -e 'SELECT version();'
%endif
%pytest --ignore=test/test_parseutils.py
%{?server_tests:db_teardown}
%files

%changelog

%autochangelog
