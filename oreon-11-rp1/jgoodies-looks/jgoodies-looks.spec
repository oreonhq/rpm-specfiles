%global source0_hash 9379737818c1d655b503d0a363f3cd30174517539075b861df959bd081ec7141

%global shortname looks

Name:           jgoodies-looks
Version:        2.7.0
Release:        17%{?dist}
Summary:        Free high-fidelity Windows and multi-platform appearance

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.jgoodies.com/freeware/libraries/looks/
# Upstream no longer distributes the library under an Open Source license. Latest
# Open Source release is taken from Maven Central
Source0:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}.pom
# Fix build with JDK 11
Patch0:         %{name}-2.7.0-jdk11.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.jgoodies:jgoodies-common)
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
The JGoodies look&feels make your Swing applications and applets look better.
They have been optimized for readability, precise micro-design and usability.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p0
mkdir -p src/main/java/
mv com/ src/main/java/

cp %{SOURCE1} pom.xml

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove useless dependency on JUnit (no test available)
%pom_remove_dep junit:junit

%mvn_file :%{name} %{name} %{name}

# Drop Windows L&F support files (unsupported on JDK 11)
rm -r src/main/java/com/jgoodies/looks/windows/

# Fix source/target version for JDK 17
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
