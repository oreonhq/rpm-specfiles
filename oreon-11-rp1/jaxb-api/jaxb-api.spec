Name:           jaxb-api
Version:        4.0.5
Release:        %autorelease
Summary:        Jakarta XML Binding API
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/jaxb-api/archive/4.0.5/jaxb-api-4.0.5.tar.gz
# oreon url source checksums begin
%global source0_sha256 f917772a40db9dd025d3227b0e50614a667dd4ce26de0f3b712e7db1d5df1f44
%global source0_file jaxb-api-4.0.5.tar.gz
# oreon url source checksums end

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.0.2-13

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jaxb-api-4.0.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f917772a40db9dd025d3227b0e50614a667dd4ce26de0f3b712e7db1d5df1f44" || { echo "oreon: Source0 SHA256 mismatch for jaxb-api-4.0.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

# Remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.5-1
- Prepare for Oreon 11 (RP1)
