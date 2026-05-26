%bcond_without bootstrap

Name:           maven-parent
Version:        43
Release:        %autorelease
Summary:        Apache Maven parent POM
License:        Apache-2.0
URL:            https://maven.apache.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 6eef96011f3674fc1720fa61c6d1d5b276e96bb8902f33b5e28df0ee7b6ea47e
%global source0_file maven-parent-43-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
%endif

%description
Apache Maven parent POM file used by other Maven projects.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-parent-43-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6eef96011f3674fc1720fa61c6d1d5b276e96bb8902f33b5e28df0ee7b6ea47e" || { echo "oreon: Source0 SHA256 mismatch for maven-parent-43-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-scm-publish-plugin
%pom_remove_dep :junit-bom

%pom_xpath_remove "pom:execution[pom:id='generate-helpmojo']" maven-plugins

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 43-1
- Prepare for Oreon 11 (RP1)
