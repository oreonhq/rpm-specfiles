%global source0_hash 3caad75fa61565ed5ca49f5b4a082e007090664625ca521832e666aa3e9156b1

%global shortname common

Name:           jgoodies-common
Version:        1.8.1
Release:        27%{?dist}
Summary:        Common library shared by JGoodies libraries and applications

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.jgoodies.com/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

# fontconfig and DejaVu fonts needed for tests
BuildRequires:  dejavu-sans-fonts
BuildRequires:  fontconfig
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
The JGoodies Common library provides convenience code for other JGoodies
libraries and applications.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Unzip source and test files from provided JARs
mkdir -p src/main/java/ src/test/java/
pushd src/main/java/
jar -xf ../../../%{name}-%{version}-sources.jar
popd
pushd src/test/java/
jar -xf ../../../%{name}-%{version}-tests.jar
popd

# Delete prebuild JARs
find -name "*.jar" -exec rm {} \;

# Remove DOS line endings
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed 's|\r||g' $file > $file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done

# remove unnecessary dependency on parent POM
%pom_remove_parent

%mvn_file :%{name} %{name} %{name}

# Fix source/target version for JDK 17
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.html RELEASE-NOTES.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
