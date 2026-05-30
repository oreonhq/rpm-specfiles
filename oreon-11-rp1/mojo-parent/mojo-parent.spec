%global source0_hash fb2504cc93149d3dbe8ee9ddbf3136414a062c42bcfcf5fc65f12ccc1d16f589

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

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
%endif

%description
Codehaus MOJO parent project pom file

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
