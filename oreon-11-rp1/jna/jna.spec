%global source0_hash 33a9e27b5a6eaa024bb117325392d1ccba7ca63f95d201230ad7c33d60f54c23
%if %{defined rhel} || (0%{?oreon} >= 11)
%bcond_with reflections
%else
%bcond_without reflections
%endif
Name:           jna
Version:        5.19.1
Release:        1%{?dist}
Summary:        Pure Java access to native libraries
License:        Apache-2.0 OR LGPL-2.1-or-later
URL:            https://github.com/java-native-access/jna/
Source0:        https://github.com/java-native-access/jna/archive/refs/tags/%{version}.tar.gz#/jna-%{version}.tar.gz
Source1:        package-list
Patch0:        0001-Adapt-build.patch
Patch1:        0002-Load-system-library.patch
Patch2:        0003-Tests-headless.patch
Patch3:        0004-Fix-javadoc-build.patch
Patch4:        0005-Fix-duplicate-manifest-entry.patch
Patch5:        0006-Remove-Werror.patch
Patch6:        0007-Support-openjdk-17.patch
ExclusiveArch:  %{java_arches}
Requires:       libffi
%if %{with reflections}
%endif
Obsoletes:      %{name}-javadoc < 5.15.0-4
# oreon:deps
BuildRequires:  ant-junit
BuildRequires:  ant-openjdk25
BuildRequires:  gcc
BuildRequires:  hamcrest
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  junit
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libffi-devel
BuildRequires:  make
BuildRequires:  objectweb-asm
BuildRequires:  reflections
# /oreon:deps
%description
JNA provides Java programs easy access to native shared libraries
(DLLs on Windows) without writing anything but Java code. JNA's
design aims to provide native access in a natural way with a
minimum of effort. No boilerplate or generated code is required.
While some attention is paid to performance, correctness and ease
of use take priority.

%package        contrib
Summary:        Contrib for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    contrib
This package contains the contributed examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
cp %{SOURCE1} .

chmod -Rf a+rX,u+w,g-w,o-w .
sed -i 's|@LIBDIR@|%{_libdir}/%{name}|' src/com/sun/jna/Native.java

# TEMPLATE has to be changed to %%version in the pom files
# in order to generate correct provides
sed -i 's/TEMPLATE/%{version}/' \
 pom-jna-jpms.xml \
 pom-jna-platform.xml \
 pom-jna.xml \
 pom-jna-platform-jpms.xml \
;

# clean LICENSE.txt
sed -i 's/\r//' LICENSE

chmod -c 0644 LICENSE OTHERS CHANGES.md

%if %{with reflections}
sed s,'<include name="junit.jar"/>,&<include name="reflections.jar"/>,' -i build.xml
build-jar-repository -s -p lib junit reflections
%else
build-jar-repository -s -p lib junit
rm test/com/sun/jna/StructureFieldOrderInspector.java
rm test/com/sun/jna/StructureFieldOrderInspectorTest.java
%endif
ln -s $(xmvn-resolve ant:ant:1.10.5) lib/ant.jar
ln -s $(xmvn-resolve org.ow2.asm:asm) lib/asm-8.0.1.jar
ln -s $(xmvn-resolve org.hamcrest:hamcrest-all) lib/hamcrest-core-1.3.jar
ln -s $(xmvn-resolve org.reflections:reflections) lib/test/reflections.jar

cp lib/native/aix-ppc64.jar lib/clover.jar

%build

ant -Drelease -Dcompatibility=1.8 -Dplatform.compatibility=1.8\
 -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true -DCC=%{__cc} native dist
find contrib -name build -exec rm -rf {} \; || :
%install
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -m 755 build/native*/libjnidispatch*.so %{buildroot}%{_libdir}/%{name}/
%mvn_file :jna jna jna/jna %{_javadir}/jna
%mvn_package :jna-platform contrib
%mvn_alias :jna-platform :platform
%mvn_artifact pom-jna.xml build/jna-min.jar
%mvn_artifact pom-jna-platform.xml contrib/platform/dist/jna-platform.jar
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jna-contrib -f %{oreon_filedir}/jna-contrib.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.17.0-1
- Import
