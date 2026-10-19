%global source0_hash 37a708bfceba5b7b0b544456bb3857f708c83734dfb3f3f1ababcc602b923e85
Name:           cortado
Version:        0.6.0
Release:        1%{?dist}
Summary:        Java media framework
URL:            http://www.theora.org/cortado/
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
Source0:        http://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         cortado-0.6.0-javadoc-fix.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25 jpackage-utils jorbis
# oreon:deps
BuildRequires:  java-25-devel
BuildRequires:  jorbis
BuildRequires:  jpackage-utils
# /oreon:deps
%description
Cortado is a Java media framework based on GStreamer's design.

%package javadoc
Summary:        Java docs for %{name}
Requires:       jpackage-utils
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
# Remove included jorbis copy
rm -fr src/com/jcraft
# We don't want to include the examples in the jar we build
mv src/com/fluendo/examples .
# javac does not like the UTF-8 x, ∗, − and ’ symbols used in the comments
sed -i "s/×/x/g" src/com/fluendo/jheora/Quant.java
sed -i "s/∗/*/g" src/com/fluendo/jheora/Quant.java
sed -i "s/−/-/g" src/com/fluendo/jheora/Quant.java
sed -i "s/’/'/g" src/com/fluendo/jheora/Quant.java

%build

javac -source 1.8 -target 1.8 `find stubs -name "*.java"`
export CLASSPATH=stubs:%{_javadir}/jogg.jar:%{_javadir}/jorbis.jar:.
javac -source 1.8 -target 1.8 `find src -name "*.java"`
pushd src
jar cf %{name}.jar `find -name "*.class"`
popd
javadoc -source 1.8 -d doc -public `find src -name "*.java"`
%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a src/%{name}.jar $RPM_BUILD_ROOT%{_javadir}
cp -a doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles cortado-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cortado-javadoc -f %{oreon_filedir}/cortado-javadoc.list

%changelog

%autochangelog
