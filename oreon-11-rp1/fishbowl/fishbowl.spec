%global source0_hash ea6e368aa16e71861e9a9ea62fa7f9c4131c54ee2ab3994f17669161e36f8392

Name:           fishbowl
Version:        1.4.1
Release:        14%{?dist}
Summary:        A collection of helper methods for dealing with exceptions in Java 8
License:        MIT
URL:            https://stefanbirkner.github.io/fishbowl
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/stefanbirkner/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.testng:testng)

%description
Fishbowl provides helper methods for dealing with exceptions.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

%pom_remove_parent

# add groupId as consequences of removing parent
# see: http://maven.apache.org/guides/introduction/introduction-to-the-pom.html#the-solution
%pom_xpath_inject pom:project '<groupId>com.github.stefanbirkner</groupId>'

# remove test deps not available in repo
%pom_remove_dep com.google.truth:truth
%pom_remove_dep de.bechte.junit:junit-hierarchicalcontextrunner
%pom_remove_dep org.easytesting:fest-assert

# remove junit-hierarchicalcontextrunner annotations as consequences of removing deps
find -name '*.java' | xargs sed -ri 's/^import .*\.HierarchicalContextRunner;//;s/@.*\(HierarchicalContextRunner.*\)//g'

# remove tests since truth and fest-assert is unavailable
rm ./src/test/java8/com/github/stefanbirkner/fishbowl/FishbowlJUnitReadmeTest.java
rm ./src/test/java8/com/github/stefanbirkner/fishbowl/FishbowlTestNgReadmeTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%changelog
%autochangelog
