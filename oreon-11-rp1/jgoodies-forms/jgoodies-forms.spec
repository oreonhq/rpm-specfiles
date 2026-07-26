%global source0_hash c3c68c47000becf8fb6ca498fda90b808c6a3edc6405dd332d771042c0f358d4

%define shortname forms

Name:           jgoodies-forms
Version:        1.9.0
Release:        17%{?dist}
Summary:        Framework to lay out and implement elegant Swing panels in Java

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://www.jgoodies.com/freeware/libraries/forms/
# Upstream no longer distributes the library under an Open Source license. Latest
# Open Source release is taken from Maven Central
Source0:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.jgoodies:jgoodies-common)
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
The JGoodies Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the hard stuff
possible, the good design easy and the bad difficult.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
mkdir -p src/main/java/
mv com/ src/main/java/

cp %{SOURCE1} pom.xml

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove useless dependency on JUnit (no test available)
%pom_remove_dep junit:junit

%mvn_file :%{name} %{name} %{name}

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
