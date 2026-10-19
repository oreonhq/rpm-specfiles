%global source1_hash d3acf88cdd1e879b2dcdc3427b1eaa53f201dffe160ef3ba74e99b1bd48b7184
%global source0_hash 6aca94c73672378711d767aa10dcf3ac2af0171a035e6d0f0f8a54d773491333
%global giturl  https://github.com/kevinbirch/%{name}
Name:           string-template-maven-plugin
Version:        1.1
Release:        1%{?dist}
Summary:        Execute StringTemplate files during a maven build
License:        MIT
URL:            https://kevinbirch.github.io/%{name}/
VCS:            git:%{giturl}.git
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        %{giturl}/archive/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/kevinbirch/%{name}/master/LICENSE
Patch:          %{name}-aether.patch
Patch:          %{name}-annotations.patch
Patch:          %{name}-descriptor.patch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.twdata.maven:mojo-executor-maven-plugin)
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n string-template-maven-plugin-javadoc -f %{oreon_filedir}/string-template-maven-plugin-javadoc.list

%changelog

%autochangelog
