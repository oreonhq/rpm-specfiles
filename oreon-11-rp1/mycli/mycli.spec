%global source0_hash adf59bfe9a8ba61d5b9587564fc2c4182613841e44fee373678e26dbc7e026ee

#global         server_tests   1

%global         pypi_name mycli
Summary:        Interactive CLI for MySQL Database with auto-completion and syntax highlighting
Name:           mycli
Version:        1.51.1
Release:        1%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://mycli.net
Source0:        %{pypi_source}
Patch:          0001-Revert-to-older-toml-format.patch
Patch:          0002-Fix-tox-config-and-some-test-fixes.patch
Patch:          0003-Disable-more-test-which-requires-db-server.patch
Patch:          0004-Revert-to-sqlglot-5.1.3.patch
Patch:          0005-Relax-various-reqs.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest) >= 2.7.0
BuildRequires:  python3dist(behave) >= 1.2.4
BuildRequires:  python3dist(pexpect) >= 3.3
BuildRequires:  python3dist(paramiko) >= 2.7.2
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(prompt-toolkit) >= 3.0.5
BuildRequires:  python3dist(cli-helpers) >= 2.0.1
BuildRequires:  python3dist(cli-helpers[styles]) >= 2.0.1
BuildRequires:  python3dist(configobj) >= 5.0.5
BuildRequires:  python3dist(pycryptodomex)
BuildRequires:  python3dist(pymysql) >= 0.9.2
BuildRequires:  python3dist(pyperclip)
BuildRequires:  python3dist(sshtunnel)
# Test infra:
%{?server_tests:BuildRequires:  mysql-server}
Suggests:       python3-mycli+ssh
%py_provides    python3-%{pypi_name}

%description
Nice interactive shell for MySQL Database with auto-completion and
syntax highlighting.

%pyproject_extras_subpkg -n python3-%{pypi_name} ssh

%pyproject_extras_subpkg -n python3-%{pypi_name} llm

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%pyproject_wheel

%generate_buildrequires
%pyproject_buildrequires -x ssh -x llm

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

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

%files -f %{pyproject_files}
%license LICENSE.txt
%doc mycli/AUTHORS README.md mycli/SPONSORS
%{_bindir}/%{pypi_name}

%changelog
%autochangelog
