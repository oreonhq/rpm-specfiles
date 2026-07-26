%global source0_hash 4733e202a1e860d9284408c7718915c0393eb9e70241e23da5826744b5394942

%global project     clojure
%global artifactId  spec.alpha
%global archivename %{artifactId}-%{artifactId}
%global full_version %{version}
%define add_determinism_options --handler=-jar

Name:           clojure-spec-alpha
Epoch:          1
Version:        0.6.249
Release:        1%{?dist}
Summary:        Spec is a Clojure library to describe the structure of data and functions

Group:          Development/Languages
License:        EPL-1.0
URL:            https://github.com/%{project}/%{artifactId}/
Source0:        https://github.com/%{project}/%{artifactId}/archive/refs/tags/v%{full_version}.zip

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)

%description 
Spec is a Clojure library to describe the structure of data and functions.
Specs can be used to validate data, conform (destructure) data, explain
invalid data, generate examples that conform to the specs, and automatically
use generative testing to test functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{artifactId}-%{version}
# Remove unpackaged parent pom and add the required groupId
%pom_remove_parent pom.xml
%pom_xpath_inject pom:project "<groupId>org.clojure</groupId>"
%pom_xpath_inject pom:project/pom:properties "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"
%pom_xpath_inject pom:project/pom:properties "<clojure.source.dir>src/main/clojure</clojure.source.dir>"
%pom_xpath_inject pom:project/pom:properties "<clojure.testSource.dir>src/test/clojure</clojure.testSource.dir>"
 
# Hook clojure-maven-plugin to maven phases
%pom_xpath_inject "pom:execution[pom:id='clojure-compile']" "<goals><goal>compile</goal></goals>"
%pom_xpath_inject "pom:execution[pom:id='clojure-test']" "<goals><goal>test</goal></goals>"

# Add builder helper to copy clojure source files so that
# compiler finds them.
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
%doc CHANGES.md README.md CONTRIBUTING.md
%changelog
%autochangelog
