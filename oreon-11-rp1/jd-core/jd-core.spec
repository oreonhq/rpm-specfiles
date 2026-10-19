%global source0_hash 98dfdbef1e6ac1814bf5fe4b58027eb655d85b92abf266e957982dd09f7899ba
Name:          jd-core
Version:       1.1.3
Release:        1%{?dist}
Summary:        JD java decompiler library
License:       GPL-3.0-or-later
URL:           https://github.com/java-decompiler/jd-core/
Source0:        https://github.com/java-decompiler/jd-core/archive/refs/tags/v%{version}.tar.gz
BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch
Requires:      javapackages-tools
# oreon:deps
BuildRequires:  java-25-devel
BuildRequires:  javapackages-tools
# /oreon:deps
%description 
JD-Core is a standalone JAVA library containing the JAVA decompiler of
"Java Decompiler project". It support Java 1.8 to Java 21.0, including Lambda
expressions, method references and default methods. JD-Core is the engine
for jd-GUI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
rm $(find | grep "\\.class$") || echo no class found
rm $(find | grep "\\.jar$")   || echo no jar found
rm $(find | grep "\\.zip$")   || echo no zip found

%build

sourceVersion="-source 8 -target 8 -g "
jdName=%{name}
jdVersion=%{version}
mkdir build
javac ${sourceVersion} $(find src/main/java/ -type f ) -d build
jar -cf ${jdName}-${jdVersion}.jar -C build org
%install
mkdir -p %{buildroot}/%{_javadir}/%{name}/
cp %{name}-%{version}.jar %{buildroot}/%{_javadir}/%{name}/
pushd %{buildroot}/%{_javadir}/%{name}/
  ln -s %{name}-%{version}.jar %{name}.jar
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
