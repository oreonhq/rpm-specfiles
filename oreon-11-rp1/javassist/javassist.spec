%global source0_hash 7a89cadb3334c797845452ff155e8dff95f48b2a69d8e8c7608f4aad03a249a1
Name:           javassist
Version:        3.33.0
Release:        1%{?dist}
Summary:        Java Programming Assistant for Java bytecode manipulation
License:        MPL-1.1 OR LGPL-2.1-or-later OR Apache-2.0
%global upstream_version rel_%(sed s/\\\\./_/g <<<"%{version}")_ga
URL:            https://www.javassist.org/
Source0:        https://github.com/jboss-%{name}/%{name}/archive/refs/tags/rel_3_33_0_ga.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Obsoletes:      %{name}-javadoc < 3.33.0-10
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)
# /oreon:deps
%description
Javassist enables Java programs to define a new class at runtime and to
modify a class file when the JVM loads it. Unlike other similar
bytecode editors, Javassist provides two levels of API: source level
and bytecode level. If the users use the source-level API, they can
edit a class file without knowledge of the specifications of the Java
bytecode. The whole API is designed with only the vocabulary of the
Java language. You can even specify inserted bytecode in the form of
source text; Javassist compiles it on the fly. On the other hand, the
bytecode-level API allows the users to directly edit a class file as
other editors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n javassist-rel_3_33_0_ga

# remove unnecessary maven plugins
%pom_remove_plugin :maven-source-plugin

# disable profiles that only add com.sun:tools dependency
%pom_xpath_remove "pom:profiles"

# add compatibility alias for old maven artifact coordinates
%mvn_alias : %{name}:%{name}

# add compatibility symlink for old classpath
%mvn_file : %{name}

%build

%mvn_build -j
rm javassist.jar src/test/resources/*.jar
find src/test -name "*.class" -print -delete
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
