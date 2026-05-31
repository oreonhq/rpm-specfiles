%global source0_hash 59655868b2f301868ae85745d3e003e17f7d75608f9d5dac8879c3f5d0e970ec

%bcond_with bootstrap

Name:           apiguardian
Version:        1.1.2
Release:        %autorelease
Summary:        API Guardian Java annotation
License:        Apache-2.0
URL:            https://github.com/apiguardian-team/apiguardian
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/apiguardian-team/apiguardian/archive/r%{version}.tar.gz
Source100:        https://repo1.maven.org/maven2/org/apiguardian/apiguardian-api/%{version}/apiguardian-api-%{version}.pom

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.1.2-28

%description
API Guardian indicates the status of an API element and therefore its
level of stability as well.  It is used to annotate public types,
methods, constructors, and fields within a framework or application in
order to publish their API status and level of stability and to
indicate how they are intended to be used by consumers of the API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
find -name \*.jar -delete
cp -p %{SOURCE100} pom.xml

mv src/module/java/* src/main/java

# Inject OSGi manifest required by Eclipse
%pom_xpath_inject pom:project "
  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <configuration>
            <archive>
              <manifestEntries>
                <Implementation-Title>apiguardian-api</Implementation-Title>
                <Implementation-Vendor>apiguardian.org</Implementation-Vendor>
                <Implementation-Version>%{version}</Implementation-Version>
                <Specification-Title>apiguardian-api</Specification-Title>
                <Specification-Vendor>apiguardian.org</Specification-Vendor>
                <Specification-Version>%{version}</Specification-Version>
                <!-- OSGi metadata required by Eclipse -->
                <Bundle-ManifestVersion>2</Bundle-ManifestVersion>
                <Bundle-SymbolicName>org.apiguardian</Bundle-SymbolicName>
                <Bundle-Version>%{version}</Bundle-Version>
                <Export-Package>org.apiguardian.api;version=\"%{version}\"</Export-Package>
              </manifestEntries>
            </archive>
          </configuration>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-compiler-plugin</artifactId>
          <executions>
            <execution>
              <id>default-compile</id>
              <goals>
                <goal>compile</goal>
              </goals>
              <configuration>
                <release>8</release>
                <excludes>
                  <exclude>**/module-info.java</exclude>
                </excludes>
              </configuration>
            </execution>
            <execution>
              <id>module-info</id>
              <goals>
                <goal>compile</goal>
              </goals>
              <configuration>
                <release>9</release>
                <includes>
                  <include>**/module-info.java</include>
                </includes>
              </configuration>
            </execution>
          </executions>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>"

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-1
- Import
