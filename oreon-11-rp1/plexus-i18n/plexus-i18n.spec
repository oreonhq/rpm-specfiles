%global source0_hash none

Name:           plexus-i18n
Version:        1.0
Release:        0.37.b10.4%{?dist}
Summary:        Plexus I18N Component
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-i18n
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10/
# tar cjf plexus-i18n-1.0-beta-10-src.tar.bz2 plexus-i18n-1.0-beta-10/
Source0:        https://deb.debian.org/debian/pool/main/p/plexus-i18n/plexus-i18n_1.0-beta-10.orig.tar.gz#/plexus-i18n-1.0-beta-10-src.tar.bz2
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
The Plexus project seeks to create end-to-end developer tools for 
writing applications. At the core is the container, which can be 
embedded or for a full scale application server. There are many 
reusable components for hibernate, form processing, jndi, i18n, 
velocity, etc. Plexus also includes an application server which 
is like a J2EE application server, without all the baggage.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }# -n: base directory name
%autosetup -n plexus-i18n-1.0-beta-10
# plexus maven plugin is deprecated
# switched it to plexus-component-metadata
%pom_xpath_set 'pom:plugin[pom:artifactId = "plexus-maven-plugin"]/pom:artifactId' plexus-component-metadata
# set goal to generate-metadata
%pom_xpath_set 'pom:goals[pom:goal = "descriptor"]/pom:goal' generate-metadata
# add missing dependencies
%pom_add_dep org.codehaus.plexus:plexus-container-default::provided
%pom_add_dep com.google.inject:guice::test
%pom_add_dep junit:junit::test
# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.37.b10.4
- Import
