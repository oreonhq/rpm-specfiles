%global source2_hash 1e53a10e6b65c64ae0f5a241c8ef289c7578f1109d8a78512dff7de2b29117b3
%global source1_hash 6e44e595cb55c08cb86cf2cb234b25b5f3ff9cfa31fc96811b8228581a011888
%global source0_hash 9ea9d0ba249723e7351ae5d7c66f6f9186213e0839c3a500c887037cf966acdd
Name:           maven-reporting-impl
Version:        4.0.0
Release:        6%{?dist}
Summary:        Abstract classes to manage report generation
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-reporting-impl/
VCS:            git:https://github.com/apache/maven-reporting-impl.git
Source0:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip
Source1:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip.asc
Source2:        https://downloads.apache.org/maven/KEYS
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
%{?javadoc_package}
# oreon:deps
BuildRequires:  gpgverify
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-integration-tools)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-apt)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xdoc)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit:junit-bom:pom:)
# /oreon:deps
%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1

# Fix end of line encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

# Unavailable plugins
%pom_remove_plugin :maven-install-plugin src/it/setup-reporting-plugin/pom.xml
%pom_remove_plugin :maven-site-plugin src/it/use-as-site-report/pom.xml

# integration tests try to download stuff from the internet
# and therefore they don't work in Koji
%pom_remove_plugin :maven-invoker-plugin

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.0-6
- Prepare for Oreon 11 (RP1)
