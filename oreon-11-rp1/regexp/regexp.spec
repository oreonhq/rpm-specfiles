%global source0_hash none

Name:           regexp
Epoch:          1
Version:        1.5
Release:        %autorelease
Summary:        Simple regular expressions API
License:        Apache-2.0
URL:            https://jakarta.apache.org/regexp/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://archive.apache.org/dist/jakarta/%{name}/jakarta-%{name}-%{version}.tar.gz
Source2:        jakarta-%{name}-osgi-manifest.MF

Patch:          jakarta-%{name}-attach-osgi-manifest.patch

BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.5-57
Provides:       deprecated()

%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan Locke.
He originally wrote this software back in 1996 and it has stood up quite
well to the test of time.
It includes complete Javadoc documentation as well as a simple Applet
for visual debugging and testing suite for compatibility.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -C
cp -p %{SOURCE2} MANIFEST.MF
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

cat > pom.xml << EOF
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>jakarta-%{name}</groupId>
  <artifactId>jakarta-%{name}</artifactId>
  <version>%{version}</version>
</project>
EOF

%mvn_file : %{name}

%mvn_alias jakarta-%{name}:jakarta-%{name} %{name}:%{name}

%build
mkdir lib
%ant -Djakarta-site2.dir=. -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 jar

%mvn_artifact pom.xml build/*.jar

%install
%mvn_install

%check
%ant -Djakarta-site2.dir=. test

%files -f .mfiles
%license LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.5-1
- Import
