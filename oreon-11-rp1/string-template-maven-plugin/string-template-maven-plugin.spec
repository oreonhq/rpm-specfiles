%global source0_hash 6aca94c73672378711d767aa10dcf3ac2af0171a035e6d0f0f8a54d773491333

%global giturl  https://github.com/kevinbirch/%{name}

Name:           string-template-maven-plugin
Version:        1.1
Release:        20%{?dist}
Summary:        Execute StringTemplate files during a maven build

License:        MIT
URL:            https://kevinbirch.github.io/%{name}/
VCS:            git:%{giturl}.git
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        %{giturl}/archive/%{name}-%{version}.tar.gz
# The license file was added to git after the last release
Source1:        https://raw.githubusercontent.com/kevinbirch/%{name}/master/LICENSE
# Update org.sonatype.aether to org.eclipse.aether
# https://github.com/kevinbirch/string-template-maven-plugin/pull/12
Patch:          %{name}-aether.patch
# Use maven plugin annotations instead of magic javadoc comments
Patch:          %{name}-annotations.patch
# Work around https://issues.apache.org/jira/browse/MNG-5346
Patch:          %{name}-descriptor.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.twdata.maven:mojo-executor-maven-plugin)

%description
This plugin allows you to execute StringTemplate template files during your
build.  The values for templates can come from static declarations or from a
Java class specified to be executed.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version} -p1
cp -p %{SOURCE1} .

%conf
# Updated name
%pom_change_dep :stringtemplate :ST4

# We do not need the versions reports
%pom_remove_plugin :versions-maven-plugin

# We do not have the secret key for signing jars
%pom_remove_plugin :maven-gpg-plugin

# We do not create any source JARs
%pom_remove_plugin :maven-source-plugin

# We use xmvn-javadoc instead of maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin

# This only enforces use of ancient maven and java versions
%pom_remove_plugin :maven-enforcer-plugin

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# Require JDK 8 at a minimum
sed -i 's/1\.6/1.8/g' pom.xml tests/pom.xml \
  src/main/java/com/webguys/maven/plugin/st/Controller.java

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
