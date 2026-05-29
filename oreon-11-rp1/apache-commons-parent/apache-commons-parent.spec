%global source0_hash 18ea71fef1ecef690c9d86f4ffdfd83ee68a6ff41b6bc7e7b7a6be0b8f5ae000

%bcond_with bootstrap

Name:           apache-commons-parent
Version:        89
Release:        %autorelease
Summary:        Apache Commons Parent Pom
License:        Apache-2.0
URL:            https://commons.apache.org/commons-parent-pom.html
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/apache/commons-parent/archive/rel/commons-parent-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
# Not generated automatically
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
%endif
Requires:       mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:       mvn(org.moditect:moditect-maven-plugin)

%description
The Project Object Model files for the apache-commons packages.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# Plugin is not in fedora
%pom_remove_plugin org.apache.commons:commons-build-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin

# Plugins useless in package builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :versions-maven-plugin
%pom_remove_plugin :maven-artifact-plugin
%pom_remove_plugin :maven-changes-plugin

%pom_remove_dep org.junit:junit-bom

# Remove profiles for plugins that are useless in package builds
for profile in animal-sniffer japicmp jacoco; do
    %pom_xpath_remove "pom:profile[pom:id='${profile}']"
done

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 89-1
- Import
