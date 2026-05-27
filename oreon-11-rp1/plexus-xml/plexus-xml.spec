%global source0_hash 82359f0a2e638a7cd30f46888dc892b262915a7145a57303b0256d01fac2c9d8

%bcond bootstrap 0

Name:           plexus-xml
Version:        4.0.4
Release:        %autorelease
Summary:        Plexus XML Utilities
# Licensing breakdown:
# Apache-1.1: src/main/java/org/codehaus/plexus/util/xml/StringUtils.java
# xpp: src/main/java/org/codehaus/plexus/util/xml/pull/MXParser.java
# Everything else is Apache-2.0
License:        Apache-1.1 AND Apache-2.0 AND xpp
URL:            https://codehaus-plexus.github.io/plexus-xml/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz

# https://github.com/codehaus-plexus/plexus-xml/pull/53
Patch:          0001-Upgrade-to-Maven-4.0.0-rc-2.patch
# https://github.com/codehaus-plexus/plexus-xml/pull/65
Patch:          0002-Bump-org.apache.maven-maven-xml-from-4.0.0-rc-3-to-4.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven:maven-xml:4.0.0-rc-4)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.0.4-5

%description
A collection of various utility classes to ease working with XML.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
# Test dependencies are not packaged
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license NOTICE.txt LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.4-1
- Prepare for Oreon 11 (RP1)
