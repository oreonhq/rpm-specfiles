Name: libformula
Version: 1.1.3
Release:        1%{?dist}
Summary:        Formula Parser
License: LGPL-2.1-only
Source0:        %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
Requires: java-25-headless, jpackage-utils, libbase >= 1.1.3
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libformula-1.1.2.build.patch
Patch1: libformula-1.1.2.java11.patch
Patch2:	libformula-1.1.3-remove-ant-contrib-support.patch
Patch3:	libformula-1.1.3-remove-commons-logging.patch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase
# /oreon:deps
%description
LibFormula provides Excel-Style-Expressions. The implementation provided
here is very generic and can be used in any application that needs to
compute formulas.

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
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libformula-javadoc -f %{oreon_filedir}/libformula-javadoc.list

%changelog

%autochangelog
