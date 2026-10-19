%global source0_hash babfb13c2771f6da9caef28a88192c17c9fe407aa6a785dc20b567ddc1ddcb86
%global debug_package %{nil}
%global with_javadoc 1
Name:       fernflower
Version:    211.7442.40
Release:        1%{?dist}
Summary:        JIdea's java decompiler
License:    Apache-2.0 
URL:        https://github.com/JetBrains/intellij-community/tree/master/plugins/java-decompiler/engine
Source0:        %{name}-%{version}.tar.gz
Source1:    %{name}
Source2:    create-sources.sh
Patch0:     remove_main.patch
Patch1:     port_to_java_8.patch
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
Requires:      java-25-headless
Requires:      javapackages-tools
Provides:      %{name}-decompiler
# oreon:deps
BuildRequires:  java-25-devel
BuildRequires:  javapackages-tools
BuildRequires:  zip
# /oreon:deps
%description
JIdea's decompiler is the first actually working analytical decompiler for Java and probably
for a high-level programming language in general. Naturally it is still under development,
please send your bug reports and improvement suggestions to the issue tracker.

%package javadoc
Summary: %{name} API documentation
Requires: javapackages-filesystem
BuildArch: noarch
Provides:  %{name}-decompiler-javadoc
%description javadoc
The %{name} 100% empty API documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup
# removing test classes and jars, tests are not run in rpm build anyway (but can be run out of it)
# maybe to pack them as demos?
find | grep "\\.class$"
find | grep "\\.jar$"
rm -rvf test
rm -rvf testData
rm  -vf gradle/wrapper/gradle-wrapper.jar
find | grep "\\.class$" && exit 1
find | grep "\\.jar$"   && exit 1
#removing main method from entry point jar
%patch -P0
%patch -P1 -p1

%build

mkdir build
javac -source 8 -target 8 -d build `find src -type f`
cd build
jar -cf ../%{name}.jar  org
cd ..
mkdir build/libs
mv %{name}.jar build/libs/
mkdir fernflower-javadoc 
cd fernflower-javadoc 
javadoc `find ../src -type f`
cd ..
zip -r %{name}.zip fernflower-javadoc
%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE1}  $RPM_BUILD_ROOT/%{_bindir}/ # cusotm launcher for main method in main jar
mkdir -p $RPM_BUILD_ROOT/%{_javadir}/
cp  build/libs/%{name}.jar $RPM_BUILD_ROOT/%{_javadir}
mkdir -p $RPM_BUILD_ROOT/%{_javadocdir}/%{name}
cp %{name}.zip $RPM_BUILD_ROOT/%{_javadocdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n fernflower-javadoc -f %{oreon_filedir}/fernflower-javadoc.list

%changelog

%autochangelog
