%bcond_without bootstrap

Name:           plexus-testing
Version:        1.3.0
Release:        %autorelease
Summary:        Plexus Testing
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-testing
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 4274def676a736ed8933f16fbc767f2a60e67948abc1c8d5e363008c3c5a78f9
%global source0_file plexus-testing-1.3.0.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.3.0-12

%description
The Plexus Testing contains the necessary classes to be able to test
Plexus components.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-testing-1.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4274def676a736ed8933f16fbc767f2a60e67948abc1c8d5e363008c3c5a78f9" || { echo "oreon: Source0 SHA256 mismatch for plexus-testing-1.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
%pom_add_dep org.codehaus.plexus:plexus-utils
%pom_add_dep org.codehaus.plexus:plexus-xml

# Some tests rely on Jakarta Injection API, which is not packaged
rm src/test/java/org/codehaus/plexus/testing/TestJakartaComponent.java
rm src/test/java/org/codehaus/plexus/testing/PlexusTestJakartaTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-1
- Prepare for Oreon 11 (RP1)
