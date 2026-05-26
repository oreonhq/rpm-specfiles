%bcond_with bootstrap

Name:           fusesource-pom
Version:        1.12
Release:        %autorelease
Summary:        Parent POM for FuseSource Maven projects
License:        Apache-2.0
URL:            https://fusesource.com/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/fusesource/mvnplugins/archive/refs/tags/fusesource-pom-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 c2ec07429085cdb2f4cb7b89a8c84a99f0921059a42e4cdac0084411df067b00
%global source0_file fusesource-pom-1.12.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
%endif

%description
This is a shared POM parent for FuseSource Maven projects.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/fusesource-pom-1.12.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c2ec07429085cdb2f4cb7b89a8c84a99f0921059a42e4cdac0084411df067b00" || { echo "oreon: Source0 SHA256 mismatch for fusesource-pom-1.12.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C
mv fusesource-pom/pom.xml .

%pom_remove_plugin :maven-scm-plugin

# WebDAV wagon is not available in Fedora.
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license license.txt notice.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12-1
- Import
