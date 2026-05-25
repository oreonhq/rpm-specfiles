# build with tests?
%bcond_without tests

# Generated from mysql2-0.3.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mysql2

Name: rubygem-%{gem_name}
Version: 0.5.7
Release: 3%{?dist}
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
License: MIT
URL: https://github.com/brianmario/mysql2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/brianmario/mysql2.git
# cd mysql2 && git archive -v -o mysql2-0.5.7-tests.tar.gz 0.5.7 spec/
Source1: %{gem_name}-%{version}-tests.tar.gz

# Required in lib/mysql2.rb
Requires: rubygem(bigdecimal)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: gcc
BuildRequires: mariadb-connector-c-devel
%if %{with tests}
BuildRequires: mariadb-server
BuildRequires: rubygem(rspec)
# Used in mysql_install_db
BuildRequires: %{_bindir}/hostname
BuildRequires: rubygem(bigdecimal)
%if !0%{?rhel} || 0%{?oreon}
# Used in spec/em/em_spec.rb as optional dependency.
# If rubygem-eventmachine is not present, the tests in the file are skipped.
BuildRequires: rubygem(eventmachine)
%endif
# Used in spec/ssl/gen_certs.sh
BuildRequires: %{_bindir}/openssl
%endif

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
%setup -q -n %{gem_name}-%{version} -b 1

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

# Prevent dangling symlink in -debuginfo.
rm -rf %{buildroot}%{gem_instdir}/ext


%if %{with tests}
%check
pushd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/spec spec

TOP_DIR=$(pwd)

# Added in https://github.com/brianmario/mysql2/pull/1293
export TEST_RUBY_MYSQL2_SSL_CERT_DIR="${TOP_DIR}/spec/ssl"
# Added in https://github.com/brianmario/mysql2/pull/1310
export TEST_RUBY_MYSQL2_SSL_CERT_HOST=localhost

pushd spec/ssl
bash gen_certs.sh
popd

# See https://github.com/brianmario/mysql2/blob/master/ci/ssl.sh
echo "
[mysqld]
ssl-ca=${TOP_DIR}/spec/ssl/ca-cert.pem
ssl-cert=${TOP_DIR}/spec/ssl/server-cert.pem
ssl-key=${TOP_DIR}/spec/ssl/server-key.pem
" > ~/.my.cnf

# Use testing port because the standard mysqld port 3306 is occupied.
# Assign a random port to consider a case of multi builds in parallel in a host.
# https://src.fedoraproject.org/rpms/rubygem-pg/pull-request/3
MYSQL_TEST_PORT="$((13306 + ${RANDOM} % 1000))"
MYSQL_TEST_USER=$(id -un)
MYSQL_TEST_DATA_DIR="${TOP_DIR}/data"
MYSQL_TEST_SOCKET="${TOP_DIR}/mysql.sock"
MYSQL_TEST_LOG="${TOP_DIR}/mysql.log"
MYSQL_TEST_PID_FILE="${TOP_DIR}/mysql.pid"

mkdir "${MYSQL_TEST_DATA_DIR}"
# See https://mariadb.com/kb/en/authentication-from-mariadb-10-4/#configuring-mariadb-install-db-to-revert-to-the-previous-authentication-method
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

# See https://github.com/brianmario/mysql2/blob/master/ci/setup.sh
mysql -u root \
  -e 'CREATE DATABASE /*M!50701 IF NOT EXISTS */ test' \
  -S "${MYSQL_TEST_SOCKET}" \
  -P "${MYSQL_TEST_PORT}"

# See https://github.com/brianmario/mysql2/blob/master/tasks/rspec.rake
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

# Clean up
kill "$(cat "${MYSQL_TEST_PID_FILE}")"

%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/support
%license %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.7-3
- Import
