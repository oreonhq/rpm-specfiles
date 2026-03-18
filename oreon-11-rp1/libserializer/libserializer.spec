Name: libserializer
Version: 1.1.2
Release: 48%{?dist}
Summary: JFreeReport General Serialization Framework
License: LGPL-2.1-or-later
#Original source: http://downloads.sourceforge.net/jfreereport/libserializer-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: libserializer-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org
BuildRequires: ant-openjdk25 , java-25-devel, jpackage-utils, libbase >= 1.1.2
Requires: java-25-headless, jpackage-utils, libbase >= 1.1.2
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libserializer-1.1.2.build.patch
Patch1: libserializer-1.1.2.java11.patch
Patch2:	libserializer-1.1.2-remove-antcontrib-support.patch
Patch3:	libserializer-1.1.2-remove-commons-logging.patch

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

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-48
- Prepare for Oreon 11 (RP1)
