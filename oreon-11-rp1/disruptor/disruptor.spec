%bcond_without bootstrap

Name:           disruptor
Version:        3.4.4
Release:        %autorelease
Summary:        Concurrent Programming Framework
License:        Apache-2.0
URL:            https://lmax-exchange.github.io/disruptor/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/LMAX-Exchange/disruptor/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/lmax/%{name}/%{version}/%{name}-%{version}.pom
# oreon url source checksums begin
%global source0_sha256 7fe7df10ea6d0f0b87442aafe2420a28250835e975a542b8c490a72a0e205b5c
%global source0_file disruptor-3.4.4.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.4.4-29

%description
A High Performance Inter-Thread Messaging Library.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/disruptor-3.4.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7fe7df10ea6d0f0b87442aafe2420a28250835e975a542b8c490a72a0e205b5c" || { echo "oreon: Source0 SHA256 mismatch for disruptor-3.4.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
# Cleanup
find . -name "*.class" -print -delete
find . -name "*.jar" -type f -print -delete

cp -p %{SOURCE1} pom.xml

# Add OSGi support
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-DocURL>%{url}</Bundle-DocURL>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-Vendor>LMAX Disruptor Development Team</Bundle-Vendor>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

# fail to compile cause: incompatible hamcrest apis
rm -r src/test/java/com/lmax/disruptor/RingBufferTest.java \
 src/test/java/com/lmax/disruptor/RingBufferEventMatcher.java
# Failed to stop thread: Thread[com.lmax.disruptor.BatchEventProcessor@1d057a39,5,main]
rm -r src/test/java/com/lmax/disruptor/dsl/DisruptorTest.java
# Test fails due to incompatible jmock version
#rm -f src/test/java/com/lmax/disruptor/EventPollerTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build -j -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENCE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.4-1
- Prepare for Oreon 11 (RP1)
