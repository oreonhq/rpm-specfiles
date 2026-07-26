%global source0_hash 07b7d2490ee5fbdcb8c153b58cb0adfd9d72fbc5f94f43d71c67b52e35d9f07c

%global giturl  https://github.com/JetBrains/java-annotations

Name:           jetbrains-annotations
Version:        26.1.0
Release:        %autorelease
Summary:        Annotations for JVM-based languages

License:        Apache-2.0
URL:            https://www.jetbrains.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/java-annotations-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/jetbrains/annotations/%{version}/annotations-%{version}.pom

BuildArch:      noarch
ExclusiveArch:  noarch %{java_arches}

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)

%description
This package contains a set of Java annotations which can be used in JVM-based
languages.  They serve as additional documentation and can be interpreted by
IDEs and static analysis tools to improve code analysis.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n java-annotations-%{version}

%conf
cp -p %{SOURCE1} pom.xml

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.10.1 . '<configuration><source>1.8</source><target>1.8</target></configuration>'

%mvn_file org.jetbrains:annotations %{name}
%mvn_alias org.jetbrains:annotations com.intellij:

# Assemble the sources to build
mv src/jvmMain src/main

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
%autochangelog
