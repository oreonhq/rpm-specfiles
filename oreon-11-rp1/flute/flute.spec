%global source0_hash 1732d6fc1f78b24f6a2820c4fee0ee33a9938748cac6629b814e94b94d7dbd05
Name: flute
Version: 1.3.0
Release:        1%{?dist}
Summary:        Java CSS parser using SAC
License: W3C AND LGPL-2.1-or-later
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
URL: http://www.w3.org/Style/CSS/SAC/
Requires: java-25-headless, jpackage-utils sac
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  sac
# /oreon:deps
%description
A Cascading Style Sheets parser using the Simple API for CSS, for Java.

%package javadoc
Summary: Javadoc for %{name}
%description javadoc
Javadoc for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib sac

%build

ant jar javadoc
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n flute-javadoc -f %{oreon_filedir}/flute-javadoc.list

%changelog

%autochangelog
