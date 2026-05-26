%bcond_with bootstrap

Name:           plexus-classworlds
Version:        2.8.0
Release:        %autorelease
Summary:        Plexus Classworlds Classloader Framework
License:        Apache-2.0 AND Plexus
URL:            https://github.com/codehaus-plexus/plexus-classworlds
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-classworlds/archive/plexus-classworlds-2.8.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 6c85f80a054e91b4bc59fc6fc7e26f95645699ecef913ec3489a260a8e82324a
%global source0_file plexus-classworlds-2.8.0.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.8.0-12

%description
Classworlds is a framework for container developers who require complex
manipulation of Java's ClassLoaders. Java's native ClassLoader mechanisms and
classes can cause much headache and confusion for certain types of application
developers. Projects which involve dynamic loading of components or otherwise
represent a 'container' can benefit from the classloading control provided by
classworlds.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-classworlds-2.8.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6c85f80a054e91b4bc59fc6fc7e26f95645699ecef913ec3489a260a8e82324a" || { echo "oreon: Source0 SHA256 mismatch for plexus-classworlds-2.8.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C
%mvn_file : %{name} plexus/classworlds
%mvn_alias : classworlds:classworlds

%pom_remove_plugin :maven-dependency-plugin

# These tests depend on artifacts that are not packaged
sed -i /testConfigure_Valid/s/./@org.junit.jupiter.api.Disabled/ src/test/java/org/codehaus/plexus/classworlds/launcher/ConfiguratorTest.java
sed -i /testConfigure_Optionally_Existent/s/./@org.junit.jupiter.api.Disabled/ src/test/java/org/codehaus/plexus/classworlds/launcher/ConfiguratorTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt LICENSE-Codehaus.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.0-1
- Import
