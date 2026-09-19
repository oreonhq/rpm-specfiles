%global source0_hash 09c39af89b4ffb2cdd50bbfc6d89472efc985538ab1762f4d1e4f7725010bc56

Name:           system-rules
Version:        1.19.0
Release:        14%{?dist}
Summary:        A collection of JUnit rules for testing code which uses java.lang.System
# Automatically converted from old format: CPL - review is highly recommended.
License:        CPL-1.0
URL:            https://stefanbirkner.github.io/system-rules
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/stefanbirkner/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:         sm.patch
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.github.stefanbirkner:fishbowl)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.mockito:mockito-core)

%description
System Rules is a collection of JUnit rules for testing code which uses
java.lang.System.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# -n: base directory name
%autosetup -n %{name}-%{name}-%{version}
echo "I was unable to make autosetup to apply that patch... `basename %{SOURCE1}`"
patch -p0 < %{SOURCE1}
rm src/test/java/org/junit/contrib/java/lang/system/internal/NoExitSecurityManagerTest.java

# delete precompiled jar and class files
find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete
# remove parent dep
%pom_remove_parent
# add groupId as consequences of removing parent
# see: https://maven.apache.org/guides/introduction/introduction-to-the-pom.html#the-solution
%pom_xpath_inject pom:project '<groupId>com.github.stefanbirkner</groupId>'
# add version to remove warning about unversioned plugin
%pom_xpath_inject 'pom:plugin[pom:artifactId = "maven-surefire-plugin"]' '<version>3.0.0-M5</version>'
# remove forkMode (deprecated)
%pom_xpath_remove 'pom:plugin[pom:artifactId = "maven-surefire-plugin"]/pom:configuration/pom:forkMode'
# alias for junit
# this PR will solve this in the future: https://src.fedoraproject.org/rpms/junit/pull-request/4
%pom_change_dep junit:junit-dep junit:junit
# add surefire deps
# see: https://bugzilla.redhat.com/show_bug.cgi?id=2007791#c15
%pom_add_dep org.apache.commons:commons-lang3:3.8.1:test
# remove unnecessary plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
%autochangelog
