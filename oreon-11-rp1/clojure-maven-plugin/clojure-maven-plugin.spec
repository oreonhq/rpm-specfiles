%global source0_hash 8e09fc6b1d8d9f7d1bee5c34f7e3eef50c986512830953ffb0dd69321f540eba
%global upstream    talios
%global groupId     com.theoryinpractise
%global artifactId  clojure-maven-plugin
Name:           %{artifactId}
Version:        1.9.4
Release:        1%{?dist}
Summary:        Clojure plugin for Maven
License:        EPL-1.0
URL:            https://github.com/%{upstream}/%{name}
Source0:        https://github.com/%{upstream}/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
# /oreon:deps
%description
This plugin has been designed to make working with clojure as easy as
possible, when working in a mixed language, enterprise project.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{artifactId}-%{artifactId}-%{version}

# release plugin is not required for RPM builds
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :ossindex-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin

%build

export LANG=en_US.utf8
%mvn_build -f -j
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
