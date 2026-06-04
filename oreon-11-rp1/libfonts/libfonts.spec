%global source0_hash none

Name: libfonts
Version: 1.1.3
Release: 51%{?dist}
Summary: TrueType Font Layouting
License: LGPL-2.1-only AND Unicode-DFS-2016
Source: https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/1.1.3-stable/libfonts-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant-openjdk25 , java-25-devel, jpackage-utils, libloader >= 1.1.3
Requires: java-25-headless, jpackage-utils, libloader >= 1.1.3
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0:        libfonts-1.1.2.build.patch
Patch1:        libfonts-1.1.2.java11.patch
Patch2:        libfonts-1.1.3-remove-antcontrib-support.patch
Patch3:        libfonts-1.1.3-remove-commons-logging.patch
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
_src="libfonts-%{version}.zip"
if test ! -f "$_src"; then
  curl -sfL -o "$_src" "https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/1.1.3-stable/libfonts-%{version}.zip"
fi
test "%{source0_hash}" = "none" || { f="$_src"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
rm -rf patches
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
