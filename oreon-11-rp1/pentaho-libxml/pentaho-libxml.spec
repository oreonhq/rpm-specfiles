%define origname libxml

Name: pentaho-libxml
Version: 1.1.3
Release: 47%{?dist}
Summary: Namespace aware SAX-Parser utility library
License: LGPL-2.1-only
#Original source: http://downloads.sourceforge.net/jfreereport/%%{origname}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{origname}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant-openjdk25 , java-25-devel, jpackage-utils, libbase, libloader
Requires: java-25-headless, jpackage-utils, libbase >= 1.1.2, libloader >= 1.1.2
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libxml-1.1.2-build.patch
Patch1: libxml-1.1.2-java11.patch
Patch2: libxml-1.1.3-remove-commons-logging.patch
Patch3: libxml-1.1.3-remove-antcontrib-support.patch

%description
Pentaho LibXML is a namespace aware SAX-Parser utility library. It eases the
pain of implementing non-trivial SAX input handlers.

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
%patch -P2 -p1 -b .no_commons_logging
%patch -P3 -p1 -b .remove-antcontrib-support
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase libloader
cd lib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{origname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{origname}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{origname}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{origname}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{origname}.jar

%files javadoc
%{_javadocdir}/%{origname}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-47
- Import
