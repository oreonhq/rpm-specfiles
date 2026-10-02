%global source0_hash ea6b464eb6c720362c4cc9887739108f392dde5bb7805111a892f00a921c3fa1
%global source1_hash cdab929a3b95211f43d2090c5e2d0dfe8465960e378bc32b35841dab324433a6

Name:           jspecify
Version:        1.0.0
Release:        %autorelease
Summary:        Standard Java annotations for nullness
License:        Apache-2.0
URL:            https://jspecify.dev/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jspecify/jspecify/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/jspecify/jspecify/%{version}/jspecify-%{version}.pom

BuildRequires:  javapackages-local-openjdk25

%description
JSpecify provides standard Java annotations (@Nullable, @NonNull,
@NullMarked, @NullUnmarked) for static analysis of nullness.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -C
find -name '*.jar' -delete

%build
mkdir -p classes
javac --release 9 -d classes $(find src/main/java src/java9/java -name '*.java')
jar --create --file %{name}.jar -C classes .

%install
%mvn_artifact %{SOURCE1} %{name}.jar
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
%autochangelog
