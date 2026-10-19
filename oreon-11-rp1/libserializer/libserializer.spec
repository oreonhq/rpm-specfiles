Name: libserializer
Version: 1.1.2
Release:        1%{?dist}
Summary:        JFreeReport General Serialization Framework
License: LGPL-2.1-or-later
Source0:        libserializer-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org
Requires: java-25-headless, jpackage-utils, libbase >= 1.1.2
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libserializer-1.1.2.build.patch
Patch1: libserializer-1.1.2.java11.patch
Patch2:	libserializer-1.1.2-remove-antcontrib-support.patch
Patch3:	libserializer-1.1.2-remove-commons-logging.patch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase
# /oreon:deps
%description
Libserializer contains a general serialization framework that simplifies the
task of writing custom java serialization handlers.

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
%description javadoc
Javadoc for %{name}.

%prep

%setup -q -c
%patch -P0 -p1 -b .build
%patch -P1 -p1 -b .java11
%patch -P2 -p1 -b .no_antcontrib
%patch -P3 -p1 -b .no_commons_logging

find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase

%build

ant jar javadoc
%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/libserializer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libserializer-javadoc -f %{oreon_filedir}/libserializer-javadoc.list

%changelog

%autochangelog
