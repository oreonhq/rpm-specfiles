%global source0_hash 9983f1cbd391352b143226635df4164cfab285cf630963f7fe4a17bc183894f6
Name: libbase
Version: 1.1.3
Release:        47%{?dist}
Summary:        JFree Base Services
License: LGPL-2.1-only
Source0:        https://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
URL: http://reporting.pentaho.org/
%if 0%{?fedora} >= 43 || (0%{?oreon} >= 11)
Requires: java-25-headless, jpackage-utils
%else
Requires: java-headless, jpackage-utils
%endif
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Patch0: libbase-1.1.2.build.patch
Patch1: libbase-1.1.2.java11.patch
Patch2: libbase-1.1.3-remove-antcontrib-support.patch
Patch3: libbase-1.1.3-remove-commons-logging.patch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
# /oreon:deps
%description
LibBase is a library developed to provide base services like logging,
configuration and initialization to other libraries and applications. The
library is the root library for all Pentaho-Reporting projects.

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

%build

ant jar javadoc
%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libbase-javadoc -f %{oreon_filedir}/libbase-javadoc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-47
- Import
