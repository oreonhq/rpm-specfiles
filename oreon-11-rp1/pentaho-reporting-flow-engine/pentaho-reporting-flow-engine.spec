%global source0_hash 233f66e8d25c5dd971716d4200203a612a407649686ef3b52075d04b4c9df0dd

Name: pentaho-reporting-flow-engine
Version: 0.9.4
Release: 40%{?dist}
Summary: Pentaho Flow Reporting Engine
License: LGPL-2.1-or-later
Epoch: 1
Source:        https://downloads.sourceforge.net/jfreereport/flow-engine-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant-openjdk25 , java-25-devel, jpackage-utils, libbase, libserializer
BuildRequires: libloader, libfonts, pentaho-libxml, xml-commons-apis
BuildRequires: librepository, sac, flute, liblayout, libformula
Requires: java-25-headless, jpackage-utils, libbase >= 1.1.3, libfonts >= 1.1.3
Requires: pentaho-libxml, libformula >= 1.1.3, librepository >= 1.1.3
Requires: sac, flute, liblayout >= 0.2.10, libserializer
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: pentaho-reporting-flow-engine-0.9.4-remove-commons-logging.patch

%description
Pentaho Reporting Flow Engine is a free Java report library, formerly
known as 'JFreeReport'

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = 1:%{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
%patch -P0 -p1 -b .no_commons_logging
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib libbase libloader \
    libfonts libxml jaxp libformula librepository sac flute liblayout \
    libserializer

%build
ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/flow-engine.jar $RPM_BUILD_ROOT%{_javadir}/flow-engine.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.4-40
- Prepare for Oreon 11 (RP1)
