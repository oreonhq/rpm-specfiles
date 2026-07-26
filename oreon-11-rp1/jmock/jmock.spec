%global source0_hash 9a93b325a59e776a157316e194b97090047e22ac120be8d37f347c4034564bc2

Name:           jmock
Version:        2.12.0
Release:        22%{?dist}
Summary:        Java library for testing code with mock objects
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.jmock.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jmock-developers/jmock-library/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Port-to-jakarta.xml.ws-4.0.0.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(com.google.auto.service:auto-service)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(jakarta.xml.ws:jakarta.xml.ws-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apache-extras.beanshell:bsh)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm)

# required for some unit tests
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)

%description
Mock objects help you design and test the interactions between the objects in
your programs.
The jMock library:
  * makes it quick and easy to define mock objects, so you don't break the
    rhythm of programming.
  * lets you precisely specify the interactions between your objects, reducing
    the brittleness of your tests.
  * works well with the auto-completion and re-factoring features of your IDE
  * plugs into your favorite test framework
  * is easy to extend.

%package example
Summary:        jMock Examples
%description example
jMock Examples.

%package imposters
Summary:        jMock imposters
%description imposters
jMock imposters.

%package junit3
Summary:        jMock JUnit 3 Integration
%description junit3
jMock JUnit 3 Integration.

%package junit4
Summary:        jMock JUnit 4 Integration
%description junit4
jMock JUnit 4 Integration.

%package junit5
Summary:        jMock JUnit 5 Integration
%description junit5
jMock JUnit 5 Integration.

%package legacy
Summary:        jMock Legacy Plugins
%description legacy
Plugins that make it easier to use jMock with legacy code.

%package testjar
Summary:        jMock Test Jar
%description testjar
Source for JAR files used in jMock Core tests.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# -p1: strip one level directory in patch
# -n: base directory name
%autosetup -p1 -n %{name}-library-%{version}
# remove unnecessary dependency on parent POM
%pom_remove_parent
# remove maven plugins that are not required for RPM builds
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin -r :versions-maven-plugin
%pom_remove_plugin :maven-gpg-plugin testjar
# change dep artifact
%pom_change_dep :jaxws-api jakarta.xml.ws:jakarta.xml.ws-api jmock
# use correct maven artifact for @javax.annotations.Nullable
%pom_change_dep com.google.code.findbugs:annotations com.google.code.findbugs:jsr305 testjar
# don't install imposters-tests and parent package
%mvn_package :jmock-imposters-tests __noinstall
%mvn_package :jmock-parent __noinstall

%build
%mvn_build -s -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files           -f .mfiles-%{name}
%doc README*
%license LICENSE.txt
%files example   -f .mfiles-%{name}-example
%files imposters -f .mfiles-%{name}-imposters
%files junit3    -f .mfiles-%{name}-junit3
%files junit4    -f .mfiles-%{name}-junit4
%files junit5    -f .mfiles-%{name}-junit5
%files legacy    -f .mfiles-%{name}-legacy
%files testjar   -f .mfiles-%{name}-testjar
%license LICENSE.txt

%changelog
%autochangelog
