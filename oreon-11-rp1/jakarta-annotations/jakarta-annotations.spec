%global source0_hash d076d0b1990fc63fc7ad09cdad7cde8cd0c3b0c217c029f322b9af7527c2e06b

%bcond_with bootstrap

Name:           jakarta-annotations
Version:        3.0.0
Release:        %autorelease
Summary:        Jakarta Annotations
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://jakarta.ee/specifications/annotations/1.3/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jakartaee/common-annotations-api/archive/%{version}/common-annotations-api-%{version}.tar.gz#/jakarta-annotations-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.0.0-41
Provides:       glassfish-annotation-api = %{version}-%{release}

%description
Jakarta Annotations defines a collection of annotations representing
common semantic concepts that enable a declarative style of
programming that applies across a variety of Java technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n common-annotations-api-%{version}

# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent api

# 3.x has no aggregator POM; only the api module is built

# remove plugins not needed for RPM builds
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# Remove use of spec-version-maven-plugin
%pom_remove_plugin :spec-version-maven-plugin api
%pom_xpath_set pom:Bundle-Version '${project.version}' api
%pom_xpath_set pom:Bundle-SymbolicName '${project.artifactId}' api
%pom_xpath_set pom:Extension-Name '${extension.name}' api
%pom_xpath_set pom:Implementation-Version '${project.version}' api
%pom_xpath_set pom:Specification-Version '${spec.version}' api

# provide aliases for the old artifact coordinates
%mvn_alias jakarta.annotation:jakarta.annotation-api \
  javax.annotation:javax.annotation-api \
  javax.annotation:jsr250-api

%build
pushd api
%mvn_build -j
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
%autochangelog
