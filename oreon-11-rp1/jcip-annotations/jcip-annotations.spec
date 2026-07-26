%global source0_hash 57d47e633507ce6e039dd52752720fdc96262093d58e1f43a117a995e312cf09

%global github_version 1.0-1
%global fedora_version %(echo -n %{github_version} | sed 's/-/./')

Name:           jcip-annotations
Version:        %{fedora_version}
Release:        5%{?dist}
Summary:        A clean room implementation of the JCIP Annotations

License:        Apache-2.0
URL:            https://github.com/stephenc/jcip-annotations
Source0:        https://github.com/stephenc/jcip-annotations/archive/refs/tags/jcip-annotations-%{github_version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25

%description
A clean room implementation of the JCIP Annotations based entirely on the
specification provided by the javadocs.

%package javadoc
Summary:        Javadoc for jcip-annotations

%description javadoc
Javadoc documentation for the jcip-annotations package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{github_version}

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove unnecessary dependency on JUnit
%pom_remove_dep junit:junit

# Compile for Java 8
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.8

# Install JAR directly in /usr/share/java
%mvn_file :jcip-annotations %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
