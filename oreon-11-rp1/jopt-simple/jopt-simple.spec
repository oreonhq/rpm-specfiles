%global source0_hash efb97daa0086a8c0d44877e9247a57cce3342dc5c1ed0f7ab0cf5e1a2b4b6a5b

Name:           jopt-simple
Version:        5.0.4
Release:        26%{?dist}
Summary:        A Java command line parser
License:        MIT
URL:            http://jopt-simple.github.io/jopt-simple
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jopt-simple/jopt-simple/archive/jopt-simple-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

%description
JOpt Simple is a Java library for parsing command line options, such as those
you might pass to an invocation of javac.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n jopt-simple-jopt-simple-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_dep org.infinitest:continuous-testing-toolkit
%pom_remove_plugin org.pitest:pitest-maven
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-compiler-plugin

%build
# Unit testing is disabled due to a missing dependency in Fedora of continuous-testing-toolkit
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
