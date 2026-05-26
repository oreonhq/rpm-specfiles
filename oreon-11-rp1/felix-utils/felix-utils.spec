%bcond_with bootstrap
%global bundle org.apache.felix.utils

Name:           felix-utils
Version:        1.11.8
Release:        %autorelease
Summary:        Utility classes for OSGi
License:        Apache-2.0
URL:            https://felix.apache.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/felix/%{bundle}/%{version}/%{bundle}-%{version}-source-release.tar.gz

# The module org.osgi.cmpn requires implementing methods which were not
# implemented in previous versions where org.osgi.compendium was used
Patch:          0000-Port-to-osgi-cmpn.patch
# oreon url source checksums begin
%global source0_sha256 c8c5a4716b0f18f70ef47f019b81967932f4487d0730aae81c595cb672dabae6
%global source0_file org.apache.felix.utils-1.11.8-source-release.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.11.8-24

%description
Utility classes for OSGi

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/org.apache.felix.utils-1.11.8-source-release.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c8c5a4716b0f18f70ef47f019b81967932f4487d0730aae81c595cb672dabae6" || { echo "oreon: Source0 SHA256 mismatch for org.apache.felix.utils-1.11.8-source-release.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.felix</groupId>"
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-compiler-plugin

%mvn_file :%{bundle} "felix/%{bundle}"

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc DEPENDENCIES

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11.8-1
- Import
