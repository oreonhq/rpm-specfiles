%global source0_hash e1fb87f3f7b980d33414473279615c4644027e013012d156efa538bc2b031772
Name: liblayout
Version: 0.2.10
Release:        1%{?dist}
Summary:        CSS based layouting framework
License: LGPL-2.1-or-later and Unicode-DFS-2016
Source0:        http://downloads.sourceforge.net/jfreereport/liblayout-%{version}.zip
URL: http://reporting.pentaho.org/
Requires: java-25-headless, jpackage-utils, flute, libloader >= 1.1.3
Requires: librepository >= 1.1.3, libfonts >= 1.1.3, sac
Requires: pentaho-libxml, libbase >= 1.0.0
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: liblayout-0.2.10-remove-commons-logging.patch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  flute
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase
BuildRequires:  libfonts
BuildRequires:  libloader
BuildRequires:  librepository
BuildRequires:  pentaho-libxml
BuildRequires:  sac
# /oreon:deps
%description
LibLayout is a layouting framework. It is based on the Cascading StyleSheets
standard. The layouting expects to receive its content as a DOM structure
(although it does not rely on the W3C-DOM API).

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
%description javadoc
Javadoc for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
%patch -P0 -p1 -b .no_commons_logging
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib flute libloader librepository libxml libfonts \
    sac libbase

%build

ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n liblayout-javadoc -f %{oreon_filedir}/liblayout-javadoc.list

%changelog

%autochangelog
