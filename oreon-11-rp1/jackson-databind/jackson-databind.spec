Name:           jackson-databind
Version:        2.18.2
Release:        6%{?dist}
Summary:        General data-binding package for Jackson (2.x)
License:        Apache-2.0 and LGPL-2.0-or-later

URL:            https://github.com/FasterXML/jackson-databind
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
Buildrequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} >= 10
ExclusiveArch:  %{java_arches} noarch
%endif

%description
The general-purpose data-binding functionality and tree-model for Jackson Data
Processor. It builds on core streaming parser/generator package, and uses
Jackson Annotations for configuration.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin "org.jacoco:jacoco-maven-plugin"
%pom_remove_plugin "org.moditect:moditect-maven-plugin"
%pom_remove_plugin "de.jjohannes:gradle-module-metadata-maven-plugin"
%pom_xpath_set "//pom:javac.src.version" "11"
%pom_xpath_set "//pom:javac.target.version" "11"
%pom_xpath_inject "//pom:properties" " <maven.compiler.source>11</maven.compiler.source>"
%pom_xpath_inject "//pom:properties" " <maven.compiler.target>11</maven.compiler.target>"

cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

# unavailable test deps
%pom_remove_dep javax.measure:jsr-275
rm src/test/java/com/fasterxml/jackson/databind/introspect/NoClassDefFoundWorkaroundTest.java
%pom_xpath_remove pom:classpathDependencyExcludes

# TestTypeFactoryWithClassLoader fails to compile
# - mockito is only transitively pulled in by powermock, so add it back
%pom_add_dep org.mockito:mockito-core::test

%mvn_file : %{name}

%build
%mvn_build -f -j -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.2-6
- Prepare for Oreon 11 (RP1)
