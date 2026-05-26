%bcond_without bootstrap

Name:           felix-parent
Version:        9
Release:        %autorelease
Summary:        Parent POM file for Apache Felix Specs
License:        Apache-2.0
URL:            https://felix.apache.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/felix/felix-parent/%{version}/%{name}-%{version}-source-release.tar.gz
# oreon url source checksums begin
%global source0_sha256 6c361e7803911061b24dd24adbfc23de960cf3933fa71feb4a689f5683aa5d55
%global source0_file felix-parent-9-source-release.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache:apache:pom:)
%endif

%description
Parent POM file for Apache Felix Specs.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/felix-parent-9-source-release.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6c361e7803911061b24dd24adbfc23de960cf3933fa71feb4a689f5683aa5d55" || { echo "oreon: Source0 SHA256 mismatch for felix-parent-9-source-release.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
%mvn_alias : :felix
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin org.apache.geronimo.genesis.plugins:tools-maven-plugin

# wagon ssh dependency unneeded
%pom_xpath_remove pom:extensions

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9-1
- Prepare for Oreon 11 (RP1)
