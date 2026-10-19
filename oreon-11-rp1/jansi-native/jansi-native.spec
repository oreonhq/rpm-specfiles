%global source0_hash 1a000a9c42ef0a561aa5b797df745f072a48a9d87bd65ec24a107e9e782927e0
%global bits %{__isa_bits}
%global debug_package %{nil}
%global commit 5015ad023a55785dbe6ad19cc786c0533387feff
Name:           jansi-native
Version:        1.8
Release:        1%{?dist}
Summary:        Jansi Native implements the JNI Libraries used by the Jansi project
License:        Apache-2.0
URL:            http://jansi.fusesource.org/
Source0:        https://github.com/fusesource/%{name}/archive/refs/tags/%{commit}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  %{java_arches}
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
so_dir=target/generated-sources/hawtjni/lib/META-INF/native/linux%{bits}/
mkdir -p $so_dir
cp -a %{_prefix}/lib/jansi/libjansi.so $so_dir
%mvn_build -- -Dplatform=linux%{bits}
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jansi-native-javadoc -f %{oreon_filedir}/jansi-native-javadoc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8-24
- Prepare for Oreon 11 (RP1)
