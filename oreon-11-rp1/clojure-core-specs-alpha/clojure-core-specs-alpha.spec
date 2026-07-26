%global source0_hash 2ce6a405ed3dd016e2e401f9d2bf18b8303e75842349e3e0ff033d6e1dbfa1f5

%global project     clojure
%global artifactId  core.specs.alpha
%global archivename %{artifactId}-%{artifactId}
%global full_version %{version}
%define add_determinism_options --handler=-jar

Name:           clojure-core-specs-alpha
Epoch:          1
Version:        0.5.81
Release:        1%{?dist}
Summary:        Clojure library containing specs to describe Clojure core macros and functions

Group:          Development/Languages
License:        EPL-1.0
URL:            https://github.com/%{project}/%{artifactId}
Source0:        %{URL}/archive/refs/tags/v%{full_version}.zip

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)
BuildRequires:  mvn(org.clojure:spec.alpha)

%description 
Core.specs.alpha is a Clojure library containing specs to describe Clojure
core macros and functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{artifactId}-%{full_version}
# Remove unpackaged parent pom and add the required groupId
%pom_remove_parent pom.xml
%pom_xpath_inject pom:project "<groupId>org.clojure</groupId>"

# Hook clojure-maven-plugin to maven phases
%pom_xpath_inject pom:project/pom:properties "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"
%pom_xpath_inject pom:project/pom:properties "<clojure.source.dir>src/main/clojure</clojure.source.dir>"
%pom_xpath_inject pom:project/pom:properties "<clojure.testSource.dir>src/test/clojure</clojure.testSource.dir>"
 
%pom_xpath_inject "pom:execution[pom:id='clojure-compile']" "<goals><goal>compile</goal></goals>"
%pom_xpath_inject "pom:execution[pom:id='clojure-test']" "<goals><goal>test</goal></goals>"
# Copy clojure source files so they are included in the jar
%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin:1.12 . "
        <executions>
          <execution>
            <id>add-clojure-source-dirs</id>
            <phase>generate-sources</phase>
            <goals>
              <goal>add-source</goal>
              <goal>add-resource</goal>
            </goals>
            <configuration>
              <sources>
                <source>src/main/clojure</source>
              </sources>
              <resources>
                <resource>
                  <directory>src/main/clojure</directory>
                </resource>
              </resources>
            </configuration>
          </execution>
          <execution>
            <id>add-clojure-test-source-dirs</id>
            <phase>generate-sources</phase>
            <goals>
              <goal>add-test-source</goal>
              <goal>add-test-resource</goal>
            </goals>
            <configuration>
              <sources>
                <source>src/test/clojure</source>
              </sources>
              <resources>
                <resource>
                  <directory>src/test/clojure</directory>
                </resource>
              </resources>
            </configuration>
          </execution>
        </executions>"

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc epl-v10.html CHANGES.md README.md CONTRIBUTING.md

%changelog
%autochangelog
