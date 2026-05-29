%global source0_hash 2ae2fa6da45d91d495f647ed955f8af7bfc94ad8e7788169c423a516b84eea0f

Name: libloader
Version: 1.1.3
Release: 49%{?dist}
Summary: Resource Loading Framework
License: LGPL-2.1-only
#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant-openjdk25 , java-25-devel, jpackage-utils
BuildRequires: libbase >= 1.1.3
Requires: java-25-headless, jpackage-utils, libbase >= 1.1.3
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libloader-1.1.2.build.patch
Patch1: libloader-1.1.2.java11.patch
Patch2: libloader-1.1.3-remove-antcontrib-support.patch
Patch3: libloader-1.1.3-remove-commons-logging.patch

%description
LibLoader is a general purpose resource loading framework. It has been
designed to allow to load resources from any physical location and to
allow the processing of that content data in a generic way, totally
transparent to the user of that library.

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c
%patch -P0 -p1 -b .build
%patch -P1 -p1 -b .java11
%patch -P2 -p1 -b .no_antcontrib
%patch -P3 -p1 -b .no_commons_logging

find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase
cd lib
ln -s /usr/share/java/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-49
- Import
