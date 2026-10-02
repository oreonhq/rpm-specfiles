%global source0_hash b2f2f90c5264d3f6518a197181bb0c8b722a13ea9cc5daf5666ead8f8c9d4d43
%global source1_hash cb8e8d950653a3c8acb71fd16a1e9a65167ce7ab179eb0717384b486cc0ba017

Name:           fastcsv
Version:        4.2.0
Release:        %autorelease
Summary:        Fast, lightweight and easy to use CSV library for Java
License:        MIT
URL:            https://fastcsv.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/osiegmar/FastCSV/archive/v%{version}/FastCSV-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/de/siegmar/fastcsv/%{version}/fastcsv-%{version}.pom

BuildRequires:  javapackages-local-openjdk25

%description
FastCSV is a high-performance CSV reader and writer library for Java
with no runtime dependencies (RFC 4180 compliant).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n FastCSV-%{version} -p1 -C
find -name '*.jar' -delete

%build
mkdir -p classes
javac --release 17 -d classes $(find lib/src/main/java -name '*.java')
jar --create --file %{name}.jar -C classes .

%install
%mvn_artifact %{SOURCE1} %{name}.jar
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
%autochangelog
