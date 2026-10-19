%global source0_hash ba09ede515a0ae8a7192040a1b778c0fb0f025fa5877e9be895cd325fa5e9d7b
%global source1_hash 8a70979ec650c3399891e6c05f2e65ada7a4b1da7ba14aeba14ab8317c5b506b
%bcond_without tests
%global gem_name mysql2
Name: rubygem-%{gem_name}
Version: 0.5.7
Release:        1%{?dist}
Summary:        A simple, fast Mysql library for Ruby, binding to libmysql
License: MIT
URL: https://github.com/brianmario/mysql2
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/brianmario/mysql2/archive/refs/tags/%{version}.tar.gz#/%{gem_name}-%{version}-tests.tar.gz
Requires: rubygem(bigdecimal)
%if %{with tests}
%if !0%{?rhel} || (0%{?oreon} >= 11)
%endif
%endif
# oreon:deps
BuildRequires:  /usr/bin/hostname
BuildRequires:  /usr/bin/openssl
BuildRequires:  gcc
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mariadb-server
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(eventmachine)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The Mysql2 gem is meant to serve the extremely common use-case of
connecting, querying and iterating on results. Some database libraries
out there serve as direct 1:1 mappings of the already complex C API\'s
available. This one is not.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
CONFIGURE_ARGS="--without-mysql-rpath $CONFIGURE_ARGS"
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}
rm -rf %{buildroot}%{gem_instdir}/ext
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

pushd .%{gem_instdir}
ln -s %{_builddir}/%{gem_name}-%{version}/spec spec
TOP_DIR=$(pwd)
export TEST_RUBY_MYSQL2_SSL_CERT_DIR="${TOP_DIR}/spec/ssl"
export TEST_RUBY_MYSQL2_SSL_CERT_HOST=localhost
pushd spec/ssl
bash gen_certs.sh
popd
echo "
[mysqld]
ssl-ca=${TOP_DIR}/spec/ssl/ca-cert.pem
ssl-cert=${TOP_DIR}/spec/ssl/server-cert.pem
ssl-key=${TOP_DIR}/spec/ssl/server-key.pem
" > ~/.my.cnf
MYSQL_TEST_PORT="$((13306 + ${RANDOM} % 1000))"
MYSQL_TEST_USER=$(id -un)
MYSQL_TEST_DATA_DIR="${TOP_DIR}/data"
MYSQL_TEST_SOCKET="${TOP_DIR}/mysql.sock"
MYSQL_TEST_LOG="${TOP_DIR}/mysql.log"
MYSQL_TEST_PID_FILE="${TOP_DIR}/mysql.pid"
mkdir "${MYSQL_TEST_DATA_DIR}"
mysql_install_db \
  --auth-root-authentication-method=normal \
  --datadir="${MYSQL_TEST_DATA_DIR}" \
  --log-error="${MYSQL_TEST_LOG}"
%{_libexecdir}/mysqld \
  --datadir="${MYSQL_TEST_DATA_DIR}" \
  --log-error="${MYSQL_TEST_LOG}" \
  --socket="${MYSQL_TEST_SOCKET}" \
  --pid-file="${MYSQL_TEST_PID_FILE}" \
  --port="${MYSQL_TEST_PORT}" \
  --ssl &
conn_found=false
for i in $(seq 10); do
  echo "Waiting for the DB server to accept connections... ${i}"
  sleep 1
  if grep -q 'ready for connections' "${MYSQL_TEST_LOG}"; then
    conn_found=true
    break
  fi
done
if ! "${conn_found}"; then
  echo "ERROR: Failed to connect the DB server."
  cat "${MYSQL_TEST_LOG}"
  exit 1
fi
mysql -u root \
  -e 'CREATE DATABASE /*M!50701 IF NOT EXISTS */ test' \
  -S "${MYSQL_TEST_SOCKET}" \
  -P "${MYSQL_TEST_PORT}"
cat <<EOF > spec/configuration.yml
root:
  host: localhost
  username: root
  password:
  database: test
  port: ${MYSQL_TEST_PORT}
  socket: ${MYSQL_TEST_SOCKET}
user:
  host: localhost
  username: ${MYSQL_TEST_USER}
  password:
  database: mysql2_test
  port: ${MYSQL_TEST_PORT}
  socket: ${MYSQL_TEST_SOCKET}
EOF
rspec -Ilib:%{buildroot}%{gem_extdir_mri} -f d spec
popd
kill "$(cat "${MYSQL_TEST_PID_FILE}")"
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mysql2-doc -f %{oreon_filedir}/rubygem-mysql2-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.7-3
- Import
