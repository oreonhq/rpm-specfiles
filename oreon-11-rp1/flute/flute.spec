Name: flute
Version: 1.3.0
Release: 42.OOo31%{?dist}
Summary: Java CSS parser using SAC
# The entire source code is W3C except ParseException.java which is LGPL version 2.1 or later
License: W3C AND LGPL-2.1-or-later
Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
# oreon url source checksums begin
%global source0_sha256 1732d6fc1f78b24f6a2820c4fee0ee33a9938748cac6629b814e94b94d7dbd05
%global source0_file flute-1.3.0-OOo31.zip
# oreon url source checksums end
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant-openjdk25 , java-25-devel, jpackage-utils, sac
Requires: java-25-headless, jpackage-utils sac
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

%description
A Cascading Style Sheets parser using the Simple API for CSS, for Java.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/flute-1.3.0-OOo31.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1732d6fc1f78b24f6a2820c4fee0ee33a9938748cac6629b814e94b94d7dbd05" || { echo "oreon: Source0 SHA256 mismatch for flute-1.3.0-OOo31.zip" >&2; exit 1; })
# oreon verify url source checksums end
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

%files
%doc COPYRIGHT.html
%{_javadir}/*.jar

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-42.OOo31
- Prepare for Oreon 11 (RP1)
