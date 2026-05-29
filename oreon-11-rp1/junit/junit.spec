%global source0_hash 1b6d700fc374c82951d247f6d80238951d87c61661ceb151f9fbf40f65413561

%bcond_without bootstrap

Name:           junit
Epoch:          1
Version:        4.13.2
Release:        %autorelease
Summary:        Java regression test package
License:        EPL-1.0
URL:            https://junit.org/junit4/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/junit-team/junit4/archive/refs/tags/r4.13.2.tar.gz

Patch:          0001-Port-to-hamcrest-2.2.patch
Patch:          0002-Port-to-OpenJDK-21.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
%endif
%if %{without bootstrap}
# For other packages, surefire-junit4 is normally pulled as transitive
# runtime dependency of junit, but junit doesn't build-depend on
# itself, so explicit BR on surefire-junit4 is needed.
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit4)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:4.13.2-20

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck. 
It is used by the developer who implements unit tests in Java. JUnit is Open
Source Software, released under the Common Public License Version 1.0 and 
hosted on GitHub.

%package manual
Summary:        Manual for %{name}

%description manual
Documentation for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n junit4-r%{version}
find . -name '*.jar' -delete
find . -name '*.class' -delete
rm -rf src/site

# InaccessibleBaseClassTest fails with Java 8
sed -i /InaccessibleBaseClassTest/d src/test/java/org/junit/tests/AllTests.java

%pom_remove_plugin :replacer
sed s/@version@/%{version}/ src/main/java/junit/runner/Version.java.template >src/main/java/junit/runner/Version.java

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

# Removing hamcrest source jar references (not available and/or necessary)
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file : %{name}

%mvn_alias junit:junit junit:junit-dep

%build
%mvn_build -j -- -DjdkVersion=1.8 -P\!restrict-doclint

%install
%mvn_install

%files -f .mfiles
%license LICENSE-junit.txt
%doc README.md

%files manual
%license LICENSE-junit.txt
%doc doc/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.13.2-1
- oreon 11 rp1
