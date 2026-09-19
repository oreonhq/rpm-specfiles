%global source0_hash dcfe3d203c5ebfec618300c23ebe317450e579a3659012ce57c577ff9045432b

Name:           jackson-annotations
Version:        2.19.4
Release:        1%{?dist}
Summary:        Core annotations for Jackson data processor
License:        Apache-2.0

URL:            https://github.com/FasterXML/jackson-annotations
Source0:        https://github.com/FasterXML/jackson-annotations/archive/refs/tags/jackson-annotations-2.18.2.tar.gz#/jackson-annotations-2.18.2.tar.gz

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:) >= 2.17
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} >= 10
ExclusiveArch:  %{java_arches} noarch
%endif

%description
Core annotations used for value types,
used by Jackson data-binding package.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin "org.moditect:moditect-maven-plugin"
%pom_remove_plugin "org.sonatype.plugins:nexus-staging-maven-plugin"
%pom_remove_plugin "de.jjohannes:gradle-module-metadata-maven-plugin"
%pom_remove_plugin "org.codehaus.mojo:build-helper-maven-plugin"
%pom_xpath_set "//pom:javac.src.version" "11"
%pom_xpath_set "//pom:javac.target.version" "11"
%pom_xpath_set "//pom:maven.compiler.source" "11"
%pom_xpath_set "//pom:maven.compiler.target" "11"

sed -i 's/\r//' LICENSE

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.2-6
- Prepare for Oreon 11 (RP1)
