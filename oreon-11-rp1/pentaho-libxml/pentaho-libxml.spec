%define origname libxml
Name: pentaho-libxml
Version: 1.1.3
Release:        1%{?dist}
Summary:        Namespace aware SAX-Parser utility library
License: LGPL-2.1-only
Source0:        %{origname}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
Requires: java-25-headless, jpackage-utils, libbase >= 1.1.2, libloader >= 1.1.2
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libxml-1.1.2-build.patch
Patch1: libxml-1.1.2-java11.patch
Patch2: libxml-1.1.3-remove-commons-logging.patch
Patch3: libxml-1.1.3-remove-antcontrib-support.patch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase
BuildRequires:  libloader
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pentaho-libxml-javadoc -f %{oreon_filedir}/pentaho-libxml-javadoc.list

%changelog

%autochangelog
