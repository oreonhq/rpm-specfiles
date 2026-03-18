%global bits %{__isa_bits}
%global debug_package %{nil}

# jansi-native-1.8 tag is missing from git
# https://github.com/fusesource/jansi-native/commit/5015ad0
%global commit 5015ad023a55785dbe6ad19cc786c0533387feff

Name:           jansi-native
Version:        1.8
Release:        24%{?dist}
Summary:        Jansi Native implements the JNI Libraries used by the Jansi project
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://jansi.fusesource.org/
Source0:        https://github.com/fusesource/jansi-native/archive/%{commit}/jansi-native-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
# jansi-native is embedded in jansi 2.x
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime) >= 1.9-2
# jansi-native provides JNI libraries for use by the JAVA Jansi project,
# so it is only necessary on java_arches
ExclusiveArch:  %{java_arches}

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

%package javadoc
Summary:          Javadocs for %{name}
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-native-%{commit}

%mvn_alias :jansi-linux%{bits} :jansi-linux
%mvn_file :jansi-linux%{bits} %{name}/jansi-linux%{bits} %{name}/jansi-linux

# use more modern source and target settings
%pom_xpath_set //pom:source 1.8
%pom_xpath_set //pom:target 1.8

# fix javadoc generation for java 11
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_inject pom:pluginManagement/pom:plugins "<plugin>
<artifactId>maven-javadoc-plugin</artifactId>
<configuration>
<source>1.8</source>
<detectJavaApiLink>false</detectJavaApiLink>
</configuration>
</plugin>"

%pom_xpath_remove "pom:plugin[pom:artifactId='hawtjni-maven-plugin']"

%build
%mvn_build

# copy libjansi.so
so_dir=target/generated-sources/hawtjni/lib/META-INF/native/linux%{bits}/
mkdir -p $so_dir
cp -a %{_prefix}/lib/jansi/libjansi.so $so_dir

%mvn_build -- -Dplatform=linux%{bits}

%install
%mvn_install

%files -f .mfiles
%doc readme.md changelog.md
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8-24
- Prepare for Oreon 11 (RP1)
