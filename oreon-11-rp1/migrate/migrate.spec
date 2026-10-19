%global source0_hash 677bf03c19d684dc5bef47e981ec1b4564482cbf5f9b190cb48e110183fd6d25
%bcond check 0
%global _gobuildtags cassandra cockroachdb mongodb mysql postgres redshift \
                     sqlite3 sqlite github gitlab go_bindata godoc_vfs \
                     google_cloud_storage iofs pkger aws_s3 filesystem
%global _remove_drivers database/clickhouse \\\
                        database/firebird \\\
                        database/neo4j \\\
                        database/pgx \\\
                        database/ql \\\
                        database/rqlite \\\
                        database/snowflake \\\
                        database/spanner \\\
                        database/sqlcipher \\\
                        database/sqlserver \\\
                        database/yugabytedb \\\
                        source/bitbucket
%global goipath         github.com/golang-migrate/migrate/v4
Version:                4.19.1
%global tag             v%{version}
%gometa -L -f
%global goname migrate
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go database migrations library and program
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC0-1.0 AND ISC AND LicenseRef-Fedora-Public-Domain AND LicenseRef-scancode-protobuf AND MIT AND MPL-2.0 AND NCSA AND NTP AND OpenSSL AND PostgreSQL AND ZPL-2.1 AND Zlib AND blessing
URL:            %{gourl}
Source0:        https://github.com/golang-%{name}/%{name}/archive/%{tag}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Go database migrations library and program.

This package is built with the following databases backends:
* cassandra
* cockroachdb
* mongodb
* mysql
* postgres
* redshift
* sqlite3
* sqlite

This package is built with the following source backends:
* github
* gitlab
* go-bindata
* godoc-vfs
* gcs
* iofs
* pkger
* s3}

%global golicenses     LICENSE
%global godocs         CONTRIBUTING.md FAQ.md GETTING_STARTED.md \
                       MIGRATIONS.md README.md SECURITY.md migrate-README.md \\\
                       cassandra-README.md \\\
                       cockroachdb-README.md \\\
                       mongodb-README.md \\\
                       mysql-README.md \\\
                       redshift-README.md \\\
                       postgres-README.md \\\
                       sqlite3-README.md \\\
                       sqlite-README.md \\\
                       file-README.md \\\
                       github-README.md \\\
                       gitlab-README.md \\\
                       go-bindata-README.md \\\
                       gcs-README.md \\\
                       iofs-README.md \\\
                       pkger-README.md \\\
                       s3-README.md

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
rm -rf %_remove_drivers
# remove zero length README files
rm database/crate/README.md
rm database/shell/README.md
# remove test files that require dktest
rm $(grep -lr '"github.com/dhui/dktest"')
# remove test files that require docker https://bugzilla.redhat.com/show_bug.cgi?id=2348699
rm $(grep -lr '"github.com/docker/docker')

%build

export BUILDTAGS="%{_gobuildtags}"
export LDFLAGS="-X main.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/migrate %{goipath}/cmd/migrate
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
mv cmd/migrate/README.md                 migrate-README.md
mv database/cassandra/README.md          cassandra-README.md
mv database/cockroachdb/README.md        cockroachdb-README.md
mv database/mongodb/README.md            mongodb-README.md
mv database/mysql/README.md              mysql-README.md
mv database/postgres/README.md           postgres-README.md
mv database/redshift/README.md           redshift-README.md
mv database/sqlite3/README.md            sqlite3-README.md
mv database/sqlite/README.md             sqlite-README.md
mv source/aws_s3/README.md               s3-README.md
mv source/file/README.md                 file-README.md
mv source/github/README.md               github-README.md
mv source/gitlab/README.md               gitlab-README.md
mv source/go_bindata/README.md           go-bindata-README.md
mv source/google_cloud_storage/README.md gcs-README.md
mv source/iofs/README.md                 iofs-README.md
mv source/pkger/README.md                pkger-README.md
%oreon_autofiles main
%if %{with check}
%check

%go_vendor_license_check -c %{S:2}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
