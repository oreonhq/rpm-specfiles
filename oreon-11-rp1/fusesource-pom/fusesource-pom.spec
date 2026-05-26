# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c2ec07429085cdb2f4cb7b89a8c84a99f0921059a42e4cdac0084411df067b00
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
%endif

%description
This is a shared POM parent for FuseSource Maven projects.

%prep
%oreon_verify_sources
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
