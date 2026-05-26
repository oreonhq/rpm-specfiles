%bcond_without bootstrap

Name:           apache-commons-io
Epoch:          1
Version:        2.20.0
Release:        %autorelease
Summary:        Utilities to assist with developing IO functionality
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-io/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz
# oreon url source checksums begin
%global source0_sha256 301f655a687bc7cbc0c43b69fef807aba00e6c3bea4a4f7512c957faa379a33c
%global source0_file commons-io-2.20.0-src.tar.gz
# oreon url source checksums end

BuildRequires:  jurand
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:2.16.1-13

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/commons-io-2.20.0-src.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "301f655a687bc7cbc0c43b69fef807aba00e6c3bea4a4f7512c957faa379a33c" || { echo "oreon: Source0 SHA256 mismatch for commons-io-2.20.0-src.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n commons-io-%{version}-src

sed -i 's/\r//' *.txt

# Run tests in multiple reusable forks to improve test performance
sed -i -e /reuseForks/d -e /forkCount/d pom.xml
sed -i '/<argLine>/d' pom.xml

%mvn_file : commons-io %{name}
%mvn_alias : org.apache.commons:

%pom_remove_dep org.junit-pioneer:junit-pioneer
jurand -i -s -a src -n DefaultLocale

%pom_remove_dep com.google.jimfs:jimfs
rm src/test/java/org/apache/commons/io/input/ReversedLinesFileReaderParamFileTest.java
rm src/test/java/org/apache/commons/io/file/PathUtilsContentEqualsTest.java

%build
# See "-DcommonsIoVersion" in maven-surefire for the tested version

# The following tests fail on tmpfs/nfs:
#  * PathUtilsDeleteDirectoryTest.testDeleteDirectory1FileSize0OverrideReadOnly:80->testDeleteDirectory1FileSize0:68 » FileSystem
#  * PathUtilsDeleteFileTest.testDeleteReadOnlyFileDirectory1FileSize1:114 » FileSystem
#  * PathUtilsDeleteFileTest.testSetReadOnlyFileDirectory1FileSize1:134 » FileSystem
#  * PathUtilsDeleteTest.testDeleteDirectory1FileSize0OverrideReadonly:97->testDeleteDirectory1FileSize0:69 » FileSystem
#  * PathUtilsDeleteTest.testDeleteDirectory1FileSize1OverrideReadOnly:145->testDeleteDirectory1FileSize1:117 » FileSystem

# moditect profile generates module-info.class
%mvn_build -j -f -- -Dcommons.osgi.symbolicName=org.apache.commons.io

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%changelog
* Wed Apr 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20.0-2
- %%autosetup -n commons-io-%%{version}-src for upstream source tarball layout

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20.0-1
- Prepare for Oreon 11 (RP1)
