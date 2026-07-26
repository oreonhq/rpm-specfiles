%global source0_hash 0bf45d3c3cb17a033d4b6c177bad41bbccb77c4b057752a828e236a61394211c

%bcond bootstrap 0

Name:           maven-resolver2
Epoch:          1
Version:        2.0.9
Release:        %autorelease
Summary:        Apache Maven Artifact Resolver library
License:        Apache-2.0
URL:            https://maven.apache.org/resolver/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/maven/resolver/maven-resolver-%{version}-source-release.zip

Patch:          0001-Remove-use-of-deprecated-SHA-1-and-MD5-algorithms.patch
Patch:          0002-Make-I-O-errors-during-test-cleanup-non-fatal.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-model-builder:4.0.0-rc-4)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-resolver-provider:4.0.0-rc-4)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils:4.0.2)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j:2.0.17)
BuildRequires:  mvn(org.slf4j:slf4j-api:2.0.17)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:2.0.5-5

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

# Skip tests that equire internet connection
#rm maven-resolver-supplier/src/test/java/org/eclipse/aether/supplier/RepositorySystemSupplierTest.java
#rm maven-resolver-transport-http/src/test/java/org/eclipse/aether/transport/http/{HttpServer,HttpTransporterTest}.java
%pom_remove_dep :jetty-bom

#%pom_remove_plugin -r :bnd-maven-plugin
#%pom_remove_plugin -r org.codehaus.mojo:animal-sniffer-maven-plugin
#%pom_remove_plugin -r :japicmp-maven-plugin

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-redisson
#%pom_disable_module maven-resolver-transport-classpath
#%mvn_package :maven-resolver-test-util __noinstall
%pom_disable_module maven-resolver-test-http
%pom_disable_module maven-resolver-transport-jetty
%pom_disable_module maven-resolver-transport-minio
%pom_disable_module maven-resolver-generator-sigstore
%pom_disable_module maven-resolver-generator-gnupg
%pom_disable_module maven-resolver-tools
%pom_disable_module maven-resolver-supplier-mvn3

%pom_remove_plugin :bnd-maven-plugin
%pom_remove_plugin :maven-jar-plugin

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :japicmp-maven-plugin

%mvn_compat_version : 2.0.9

%build
%mvn_build -j -f -j -- -Dmaven4Version=4.0.0-rc-4

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
%autochangelog
