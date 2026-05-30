%global source0_hash f3f90b7672698e66583e86e676771fd339bd84a51514e818a064a6defa903bf1

%bcond_with bootstrap
%global upstream_version 2.0.0-M1

Name:           maven-verifier
Version:        2.0.0~M1
Release:        %autorelease
Summary:        Apache Maven Verifier Component
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-verifier
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/maven-verifier/2.0.0-M1/maven-verifier-2.0.0-M1-source-release.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-http)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-embedder)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0.0~M1-18

%description
Provides a test harness for Maven integration tests.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# This test attempts to write outside the build directory
rm src/test/java/org/apache/maven/shared/verifier/ForkedLauncherTest.java
# Depends on ForkedLauncherTest
rm src/test/java/org/apache/maven/shared/verifier/VerifierTest.java
# This test attepmts to connect to the Internet
rm src/test/java/org/apache/maven/shared/verifier/Embedded3xLauncherTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0~M1-1
- Import
