%bcond_without bootstrap

Name:           mojo-parent
Version:        85
Release:        %autorelease
Summary:        Codehaus MOJO parent project pom file
License:        Apache-2.0
URL:            https://www.mojohaus.org/mojo-parent/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/mojo-parent/%{version}/mojo-parent-%{version}-source-release.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
# oreon url source checksums begin
%global source0_sha256 fb2504cc93149d3dbe8ee9ddbf3136414a062c42bcfcf5fc65f12ccc1d16f589
%global source0_file mojo-parent-85-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
%endif

%description
Codehaus MOJO parent project pom file

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mojo-parent-85-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fb2504cc93149d3dbe8ee9ddbf3136414a062c42bcfcf5fc65f12ccc1d16f589" || { echo "oreon: Source0 SHA256 mismatch for mojo-parent-85-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
# Not needed in Fedora.
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_dep :junit-bom

cp %SOURCE1 .

%build
%mvn_alias : org.codehaus.mojo:mojo
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 85-1
- Prepare for Oreon 11 (RP1)
