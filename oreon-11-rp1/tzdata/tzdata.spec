%global source0_hash 4aa79e4effee53fc4029ffe5f6ebe97937282ebcdf386d5d2da91ce84142f957
%global source1_hash 697ebe6625444aef5080f58e49d03424bbb52e08bf483d3ddb5acf10cbd15740
%global source3_hash 4809b438f61e404dec1c857d56c8d60724312c19bd8b8cf720a1fbedf4f0766f

Summary: Timezone data
Name: tzdata
Version: 2025c
%define tzdata_version 2025c
%define tzcode_version 2025c
Release: 3%{?dist}
License: LicenseRef-Fedora-Public-Domain AND (GPL-2.0-only WITH ClassPath-exception-2.0)
URL: https://www.iana.org/time-zones
Source0:        https://data.iana.org/time-zones/releases/tzdata%{tzdata_version}.tar.gz
Source1:        https://data.iana.org/time-zones/releases/tzcode%{tzcode_version}.tar.gz

Patch002: 0002-Fix-have-snprintf-error.patch
Patch003: 0003-continue-to-ship-posixrules.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: gawk, glibc, perl-interpreter
BuildRequires: java-25-devel
BuildRequires: glibc-common >= 2.5.90-7
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
%if 0%{?rhel}
%patch -p1 -P 3
%endif

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

%if 0%{?rhel}
# Use rearguard for rhel (overwrite default dataform)
tar zxf rearguard/tzdata%{version}-rearguard.tar.gz
%endif

tar xf %{SOURCE3}
%patch -P 100
%patch -p1 -P 101

echo "%{name}%{tzdata_version}" >> VERSION

%build
# Run make to create the tzdata.zi file
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
/usr/bin/env LANG=C make -k VALIDATE=':' check && true

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

%changelog
* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2025c-3
- Use HTTPS for IANA tzdata and tzcode tarballs (spectool has no FTP)
- Fetch javazic tarball from Fedora lookaside so spectool and CI can download it

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2025c-2
- Prepare for Oreon 11 (RP1)
