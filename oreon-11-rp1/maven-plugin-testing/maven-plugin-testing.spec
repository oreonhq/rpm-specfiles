%bcond_without bootstrap

Name:           maven-plugin-testing
Version:        3.3.0
Release:        %autorelease
Summary:        Maven Plugin Testing
License:        Apache-2.0
URL:            https://maven.apache.org/plugin-testing/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch:          0001-Port-to-plexus-utils-3.0.21.patch
Patch:          0002-Port-to-current-maven-artifact.patch
Patch:          0003-Port-to-maven-3.8.1.patch
# From upstream commit 43b8eaaf
Patch:          0004-Stabilize-project.patch
# oreon url source checksums begin
%global source0_sha256 e59a7fc8179f0cd659875d94c396020a66f1c8c2b716c00ef9d39623b2926f97
%global source0_file maven-plugin-testing-3.3.0-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.3.0-55

%description
The Maven Plugin Testing contains the necessary modules
to be able to test Maven Plugins.

%package harness
Summary:        Maven Plugin Testing Mechanism

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-plugin-testing-3.3.0-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e59a7fc8179f0cd659875d94c396020a66f1c8c2b716c00ef9d39623b2926f97" || { echo "oreon: Source0 SHA256 mismatch for maven-plugin-testing-3.3.0-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin maven-plugin-testing-harness

%pom_disable_module maven-plugin-testing-tools
%pom_disable_module maven-test-tools

%mvn_alias : org.apache.maven.shared:

%build
%mvn_build -j -s -- -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles-%{name}
%license LICENSE NOTICE

%files harness -f .mfiles-%{name}-harness

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.0-1
- Prepare for Oreon 11 (RP1)
