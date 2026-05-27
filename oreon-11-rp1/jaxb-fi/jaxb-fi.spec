%global source0_hash e4a3c86648681e58bb84313c2e97eb199498ec6b354eb60cd46ec4dc4806f0b3

Name:           jaxb-fi
Version:        2.1.1
Release:        %autorelease
Summary:        Implementation of the Fast Infoset Standard for Binary XML
# jaxb-fi is licensed Apache-2.0 and EDL-1.0 (BSD-3-Clause)
# bundled org.apache.xerces.util.XMLChar.java is licensed ASL 1.1
License:        Apache-2.0 AND BSD-3-Clause AND Apache-1.1
URL:            https://github.com/eclipse-ee4j/jaxb-fi
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/jaxb-fi/archive/2.1.1/jaxb-fi-2.1.1.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.1.1-17

%description
Fast Infoset Project, an Open Source implementation of the Fast Infoset
Standard for Binary XML.

The Fast Infoset specification (ITU-T Rec. X.891 | ISO/IEC 24824-1)
describes an open, standards-based "binary XML" format that is based on
the XML Information Set.

%package tests
Summary:        FastInfoset Roundtrip Tests
License:        Apache-2.0 AND BSD-3-Clause

%description tests
%{summary}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%pom_remove_parent

%pom_disable_module samples
%pom_disable_module utilities

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%mvn_package :FastInfosetRoundTripTests tests

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE.md
%doc README.md

%files tests -f .mfiles-tests
%license LICENSE NOTICE.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-1
- Prepare for Oreon 11 (RP1)
