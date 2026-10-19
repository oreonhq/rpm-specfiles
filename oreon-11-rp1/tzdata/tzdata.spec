%global source0_hash e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4
%global source1_hash b1cffc3ace4c4c7cd0efba2f7add86ec3d0b79da48bcf03582671fd3c8feace8
%global source3_hash 4809b438f61e404dec1c857d56c8d60724312c19bd8b8cf720a1fbedf4f0766f
Summary:        Timezone data
Name: tzdata
Version: 2026c
%define tzdata_version 2026c
%define tzcode_version 2026c
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain AND (GPL-2.0-only WITH ClassPath-exception-2.0)
URL: https://www.iana.org/time-zones
Source0:        https://data.iana.org/time-zones/releases/%{name}%{version}.tar.gz
Source1:        https://data.iana.org/time-zones/releases/tzcode%{tzcode_version}.tar.gz
Patch002: 0002-Fix-have-snprintf-error.patch
Patch003: 0003-continue-to-ship-posixrules.patch
Conflicts: glibc-common <= 2.3.2-63
BuildArchitectures: noarch
ExcludeArch: i686
%bcond_with vanguard
# oreon:deps
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  glibc
BuildRequires:  glibc-common
BuildRequires:  java-25-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package contains data files with rules for various timezones around
the world.

%package java
Summary: Timezone data for Java
Source3: javazic-1.8-37392f2f5d59.tar.xz
Source4: ZoneTest.java
Patch100: 8051641.patch
Patch101: javazic-harden-links.patch
%description java
This package contains timezone information for use by Java runtimes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
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

rm tzdata.zi
%if %{with vanguard}
make VERSION=%{version} ZFLAGS="-b fat" DATAFORM=vanguard tzdata.zi
%elif 0%{?rhel}
make VERSION=%{version} ZFLAGS="-b fat" DATAFORM=rearguard tzdata.zi
%else
make tzdata.zi
%endif
FILES="africa antarctica asia australasia europe northamerica southamerica
       etcetera backward factory"
mkdir zoneinfo/{,posix,right}
zic -b fat -y ./yearistype -d zoneinfo -L /dev/null -p America/New_York $FILES
zic -b fat -y ./yearistype -d zoneinfo/posix -L /dev/null $FILES
zic -b fat -y ./yearistype -d zoneinfo/right -L leapseconds $FILES
JAVA_FILES="rearguard/africa rearguard/antarctica rearguard/asia \
      rearguard/australasia rearguard/europe rearguard/northamerica \
      rearguard/southamerica rearguard/etcetera \
      rearguard/backward"
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

echo ============TESTING===============
/usr/bin/env LANG=C make -k VALIDATE=':' check && true
system_java_home=$(dirname $(readlink -f $(which java)))/..
mkdir -p java_home
cp -Lr $system_java_home/* java_home/.
for tzdb in $(find java_home -name tzdb.dat) ; do
    rm $tzdb
    cp $RPM_BUILD_ROOT%{_datadir}/javazi-1.8/tzdb.dat $tzdb
done
cp %{SOURCE4} .
javac ZoneTest.java
java_home/bin/java ZoneTest
echo ============END TESTING===========
%files -f %{oreon_filedir}/main.list
%files -n tzdata-java -f %{oreon_filedir}/tzdata-java.list

%changelog

%autochangelog
