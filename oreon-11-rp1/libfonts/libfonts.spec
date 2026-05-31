%global source0_hash 6cbedbfaef3c62610243e446c93d0a97c15d89e13902e757958ca8ca06876b58

Name: libfonts
Version: 1.1.3
Release: 51%{?dist}
Summary: TrueType Font Layouting
License: LGPL-2.1-only AND Unicode-DFS-2016
#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip
#a) to simplify the licensing
#unzip, find . -name "*.jar" -exec rm {} \;, rm -r patches
#b) to update data files to clearer license
#cd encodings
#wget -e robots=off --no-host-directories --recursive --no-parent --reject "index.html*" --cut-dirs=2 https://unicode.org/Public/MAPPINGS/
#rm -rf OBSOLETE
Source: %{name}-%{version}-jars-itextpatch_deleted-encodings_updated.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant-openjdk25 , java-25-devel, jpackage-utils, libloader >= 1.1.3
Requires: java-25-headless, jpackage-utils, libloader >= 1.1.3
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libfonts-1.1.2.build.patch
Patch1: libfonts-1.1.2.java11.patch
Patch2: libfonts-1.1.3-remove-antcontrib-support.patch
Patch3: libfonts-1.1.3-remove-commons-logging.patch
%description
LibFonts is a library developed to support advanced layouting in JFreeReport.
This library allows to read TrueType-Font files to extract layouting specific
informations.

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
%patch -P0 -p1 -b .build
%patch -P1 -p1 -b .java11
%patch -P2 -p1 -b .no_antcontrib
%patch -P3 -p1 -b .no_commons_logging
find . -name "*.jar" -exec rm -f {} \;
rm -r source/org/pentaho/reporting/libraries/fonts/itext
mkdir -p lib
build-jar-repository -s -p lib libbase libloader

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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-51
- Import
