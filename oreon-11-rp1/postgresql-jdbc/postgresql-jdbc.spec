%global source0_hash 4537ba157c6eab9022d0a48bb6e6ca5a736ced8cc7121e1276322fb104dd3718
%{!?runselftest:%global runselftest 1}
%global section devel
%global source_path pgjdbc/src/main/java/org/postgresql
Summary:        JDBC driver for PostgreSQL
Name:           postgresql-jdbc
Version:        42.7.13
Release:        1%{?dist}
License:        BSD-2-Clause
URL:            https://jdbc.postgresql.org/
Source0:        https://repo1.maven.org/maven2/org/postgresql/postgresql/%{version}/postgresql-%{version}-jdbc-src.tar.gz
Source1:        postgresql_jdbc_tests_init.sh
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Provides:       pgjdbc = %{version}-%{release}
%if %runselftest
%endif
Obsoletes:      %{name}-javadoc < 42.7.4-9
Provides:       bundled(mvn(com.ongres.scram:scram-client)) = 3.2
Provides:       bundled(mvn(com.ongres.scram:scram-common)) = 3.2
Provides:       bundled(mvn(com.ongres.stringprep:saslprep)) = 2.2
Provides:       bundled(mvn(com.ongres.stringprep:stringprep)) = 2.2
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.ongres.scram:scram-client)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
# /oreon:deps
%description
PostgreSQL is an advanced Object-Relational database management system. The
postgresql-jdbc package includes the .jar files needed for Java programs to
access a PostgreSQL database.

%package tests
Summary:        Tests for %{name}
%description tests
This package contains tests for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n postgresql-%{version}-jdbc-src

# remove any binary libs
find -type f \( -name "*.jar" -or -name "*.class" \) -delete

# compat symlink: requested by dtardon (libreoffice), reverts part of
# 0af97ce32de877 commit.
%mvn_file org.postgresql:postgresql %{name}/postgresql %{name} postgresql

# For compat reasons, make Maven artifact available under older coordinates.
%mvn_alias org.postgresql:postgresql postgresql:postgresql

# remove unmet dependency
%pom_remove_dep uk.org.webcompere:system-stubs-jupiter
# remove tests that depend on the system-stubs-jupiter
grep -l -r '^import uk\.org\.webcompere\.systemstubs' src/test | xargs rm -v

# Install -tests Jar as well
%pom_xpath_inject 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]' '
<executions>
  <execution>
    <goals>
      <goal>test-jar</goal>
    </goals>
  </execution>
</executions>'
%mvn_package org.postgresql:postgresql::tests: tests

%build

%if %runselftest
. %{SOURCE1}
setup_build_local_properties > build.local.properties
%postgresql_tests_start
%else
opts="-DskipTests=true"
%endif
%mvn_build -j -- $opts
xmvn --offline -Dmdep.outputFile=tests-classpath dependency:build-classpath
%install
%mvn_install
install -m 644 -D tests-classpath %{buildroot}%{_datadir}/%{name}-tests/classpath
install -m 644 -D -t %{buildroot}%{_datadir}/%{name}-tests build.properties ssltest.properties
cp -r -t %{buildroot}%{_datadir}/%{name}-tests certdir
install -m 755 -D -t %{buildroot}%{_libexecdir}/%{name}-tests %{SOURCE1}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n postgresql-jdbc-tests -f %{oreon_filedir}/postgresql-jdbc-tests.list

%changelog

%autochangelog
