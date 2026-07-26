%global source0_hash e67ddec4a2967c0fe24fb33e6647429dafd21ea9853997249c610a8a5adc7635

%global hash      8b3bdb6f0dc656b3e5e2f913dbb90cc44b05ae97
%global hashShort 8b3bdb6

Name:           maven-archetype
Version:        3.2.1.0.%{hashShort}
Release:        21%{?dist}
Summary:        Maven project templating toolkit

# Most of the code is under ASL 2.0, but some bundled jdom sources are
# under ASL 1.1
# Automatically converted from old format: ASL 2.0 and ASL 1.1 - review is highly recommended.
License:        Apache-2.0 AND Apache-1.1
URL:            https://maven.apache.org/archetype/
Source0:       https://github.com/apache/maven-archetype/archive/%{hash}.zip

# We only use groovy for running a post generation script,
# removing this continues the old behaviour of ignoring it
Patch1: 0001-Avoid-reliance-on-groovy.patch

# Taken from https://github.com/apache/maven-archetype/commit/e4eed30d1c0c6eabf45c49194ff6f0d8a4e4d5a7
Patch2: 0002-declare-dependencies.patch

# Port to commons-lang3
Patch3: 0003-Port-to-commons-lang3.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(net.sourceforge.jchardet:jchardet)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.jdom:jdom)
BuildRequires:  icu4j
BuildRequires:  apache-commons-collections

%description
Archetype is a Maven project templating toolkit. An archetype is
defined as an original pattern or model from which all other things of
the same kind are made. The names fits as we are trying to provide a
system that provides a consistent means of generating Maven
projects. Archetype will help authors create Maven project templates
for users, and provides users with the means to generate parameterized
versions of those project templates.

Using archetypes provides a great way to enable developers quickly in
a way consistent with best practices employed by your project or
organization. Within the Maven project we use archetypes to try and
get our users up and running as quickly as possible by providing a
sample project that demonstrates many of the features of Maven while
introducing new users to the best practices employed by Maven. In a
matter of seconds a new user can have a working Maven project to use
as a jumping board for investigating more of the features in Maven. We
have also tried to make the Archetype mechanism additive and by that
we mean allowing portions of a project to be captured in an archetype
so that pieces or aspects of a project can be added to existing
projects. A good example of this is the Maven site archetype. If, for
example, you have used the quick start archetype to generate a working
project you can then quickly create a site for that project by using
the site archetype within that existing project. You can do anything
like this with archetypes.

You may want to standardize J2EE development within your organization
so you may want to provide archetypes for EJBs, or WARs, or for your
web services. Once these archetypes are created and deployed in your
organization's repository they are available for use by all developers
within your organization.

%package javadoc
Summary: API documentation for %{name}

%description    javadoc
%{summary}.

%package catalog
Summary: Maven Archetype Catalog model

%description catalog
%{summary}.

%package descriptor
Summary: Maven Archetype Descriptor model

%description descriptor
%{summary}.

%package common
Summary: Maven Archetype common classes
# Registry module was obsoleted and removed by upstream F31
Obsoletes: %{name}-registry <= 3.1.1-1

%description common
%{summary}.

%package packaging
Summary: Maven Archetype packaging configuration for archetypes

%description packaging
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{hash}
%patch -P1 -p1
#%patch2 -p1
%patch -P3 -p1

# Not needed for RPM builds
%pom_remove_plugin -r :apache-rat-plugin
#%%pom_remove_plugin -r :maven-enforcer-plugin

# Add OSGI info to catalog and descriptor jars
pushd archetype-models/archetype-catalog
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.catalog.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd
pushd archetype-models/archetype-descriptor
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.metadata.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd

# Remove ivy as a runtime dep
%pom_remove_dep org.apache.ivy:ivy archetype-common

%pom_remove_dep  org.sonatype.aether:
pushd archetype-common
%pom_remove_dep  org.sonatype.aether:
popd

# Disable processing of test resources using ant
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin archetype-common

# Don't build the maven-plugin
%pom_disable_module maven-archetype-plugin

%build
%mvn_package :archetype-models maven-archetype
# Tests are skipped due to missing test dependencies
%mvn_build -f -s -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8 -Dsource=8 -DdetectJavaApiLink=false

%install
%mvn_install

%files -f .mfiles-maven-archetype
%license NOTICE.txt

%files catalog -f .mfiles-archetype-catalog

%files descriptor -f .mfiles-archetype-descriptor

%files common -f .mfiles-archetype-common
%license NOTICE.txt

%files packaging -f .mfiles-archetype-packaging

%files javadoc -f .mfiles-javadoc
%license NOTICE.txt

%changelog
%autochangelog
