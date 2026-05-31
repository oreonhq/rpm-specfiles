%global source0_hash a75230ed063a49f2cab97463f0f312f143ff83b56c986b521392094ee3574d48

%bcond_without bootstrap

Name:           maven-bundle-plugin
Version:        5.1.9
Release:        %autorelease
Summary:        Maven Bundle Plugin
License:        Apache-2.0
URL:            https://felix.apache.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/felix/maven-bundle-plugin/%{version}/maven-bundle-plugin-%{version}-source-release.tar.gz

Patch:          0001-Fix-incorrect-parent-relativePath.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 5.1.9-20

%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

find -name '*.jar' -delete

# There is forked version of maven-osgi in
# src/{main,test}/java/org/apache/maven

rm -rf src/main/java/org/apache/felix/obrplugin/
%pom_remove_dep :org.apache.felix.bundlerepository

rm -f src/main/java/org/apache/felix/bundleplugin/baseline/BaselineReport.java
%pom_remove_dep :doxia-sink-api
%pom_remove_dep :doxia-site-renderer
%pom_remove_dep :maven-reporting-api

%pom_remove_dep :org.osgi.core
%pom_remove_dep :jdom

%pom_remove_plugin :maven-invoker-plugin

%build
# Tests depend on bundled JARs
# source and target set explicitly for xmvn-javadoc-plugin
%mvn_build -j -f -- -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.9-1
- Prepare for Oreon 11 (RP1)
