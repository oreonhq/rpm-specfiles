# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b26882805f26aac59d5b222978e6580484b834ccdc98be89df2f05a6dc53a652
%global source1_hash cc3d27ca2a0d8399504551b920970d80af83bfb9c216e8082a15491921935d54
%global source3_hash 4809b438f61e404dec1c857d56c8d60724312c19bd8b8cf720a1fbedf4f0766f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: Timezone data
Name: tzdata
Version:        2026e
%define tzdata_version 2026e
%define tzcode_version 2026e
Release:        1%{?dist}
License: LicenseRef-Oreon-Public-Domain AND (GPL-2.0-only WITH ClassPath-exception-2.0)
URL: https://www.iana.org/time-zones
Source0:        https://data.iana.org/time-zones/releases/tzdata%{version}.tar.gz
Source1:        https://data.iana.org/time-zones/releases/tzcode%{version}.tar.gz

Patch002:        0002-Fix-have-snprintf-error.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: gawk, glibc, perl-interpreter
BuildRequires: java-25-devel
BuildRequires: glibc-common >= 2.5.90-7
BuildRequires:  oreon-rpm-macros
Conflicts: glibc-common <= 2.3.2-63
BuildArchitectures: noarch
ExcludeArch: i686

# Using '--with vanguard' will change the data format to the new vanguard form.
%bcond_with vanguard

%description
This package contains data files with rules for various timezones around
the world.

%package java
Summary: Timezone data for Java
Source3: javazic-1.8-37392f2f5d59.tar.xz
Source4: ZoneTest.java
Patch100:        8051641.patch
Patch101:        javazic-harden-links.patch

%description java
This package contains timezone information for use by Java runtimes.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -

%setup -q -c -a 1

%patch -p1 -P 2

# zic now defaults to "-b slim" to control data bloat.
# This can cause build issues for some packages.
# For now, build with ZFLAGS="-b fat" for backward compatibitliy.

# tzdata-2018g introduced 25:00 transition times.  This breaks OpenJDK.
# Use rearguard for java
mkdir rearguard
make VERSION=%{version} ZFLAGS="-b fat" tzdata%{version}-rearguard.tar.gz.t
mv tzdata%{version}-rearguard.tar.gz rearguard
pushd rearguard
tar zxf tzdata%{version}-rearguard.tar.gz
popd


tar xf %{SOURCE3}
%patch -P 100
%patch -p1 -P 101

echo "%{name}%{tzdata_version}" >> VERSION

%build
# Run make to create the tzdata.zi file
rm tzdata.zi
%if %{with vanguard}
make VERSION=%{version} ZFLAGS="-b fat" DATAFORM=vanguard tzdata.zi
%else
make tzdata.zi
%endif

FILES="africa antarctica asia australasia europe northamerica southamerica
       etcetera backward factory"

mkdir zoneinfo/{,posix,right}
zic -b fat -y ./yearistype -d zoneinfo -L /dev/null -p America/New_York $FILES
zic -b fat -y ./yearistype -d zoneinfo/posix -L /dev/null $FILES
zic -b fat -y ./yearistype -d zoneinfo/right -L leapseconds $FILES

# grep -v tz-art.htm tz-link.htm > tz-link.html

# tzdata-2018g introduced 25:00 which breaks java - use the rearguard files for java
JAVA_FILES="rearguard/africa rearguard/antarctica rearguard/asia \
      rearguard/australasia rearguard/europe rearguard/northamerica \
      rearguard/southamerica rearguard/etcetera \
      rearguard/backward"

# Java 8 tzdata
pushd javazic-1.8
javac -source 1.8 -target 1.8 -classpath . `find . -name \*.java`
popd

java -classpath javazic-1.8 build.tools.tzdb.TzdbZoneRulesCompiler \
    -srcdir . -dstfile tzdb.dat \
    -verbose \
    $JAVA_FILES javazic-1.8/tzdata_jdk/gmt javazic-1.8/tzdata_jdk/jdk11_backward

%install
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -prd zoneinfo $RPM_BUILD_ROOT%{_datadir}
install -p -m 644 zone.tab zone1970.tab iso3166.tab leap-seconds.list leapseconds tzdata.zi $RPM_BUILD_ROOT%{_datadir}/zoneinfo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/javazi-1.8
install -p -m 644 tzdb.dat $RPM_BUILD_ROOT%{_datadir}/javazi-1.8/

%check
echo ============TESTING===============
# Use the glibc provided versions of date, zdump, and zic
for p in date zdump zic ; do cp /usr/bin/$p . ; done
make -k CC=: CHECK_WEB_PAGES="" check && true

# Create a custom JAVA_HOME, where we can replace tzdb.dat with the
# one just built, for testing.
system_java_home=$(dirname $(readlink -f $(which java)))/..
mkdir -p java_home
cp -Lr $system_java_home/* java_home/.
for tzdb in $(find java_home -name tzdb.dat) ; do
    rm $tzdb
    cp $RPM_BUILD_ROOT%{_datadir}/javazi-1.8/tzdb.dat $tzdb
done
# Compile the smoke test and run it.
cp %{SOURCE4} .
javac ZoneTest.java
java_home/bin/java ZoneTest
echo ============END TESTING===========

%files
%{_datadir}/zoneinfo
%license LICENSE
%doc README
%doc theory.html
%doc tz-link.html
%doc tz-art.html

%files java
%{_datadir}/javazi-1.8

