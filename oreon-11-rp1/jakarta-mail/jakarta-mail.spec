%bcond_with bootstrap

Name:           jakarta-mail
Version:        2.1.5
Release:        %autorelease
Summary:        Jakarta Mail API
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://jakarta.ee/specifications/mail/2.1/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jakartaee/mail-api/archive/%{version}/mail-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 3f3eb57cb6c9bc1a8714bf5f0eaa780a1201bc183f95f1ba18f9cfc09be8a809
%global source0_file mail-2.1.5.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.1.5-2

%description
Jakarta Mail defines a platform-independent and protocol-independent
framework to build mail and messaging applications.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mail-2.1.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3f3eb57cb6c9bc1a8714bf5f0eaa780a1201bc183f95f1ba18f9cfc09be8a809" || { echo "oreon: Source0 SHA256 mismatch for mail-2.1.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C

pushd api
# Remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin

# Missing dependency
%pom_remove_dep :angus-activation
rm src/test/java/jakarta/mail/internet/NonAsciiFileNamesTest.java
popd

%build
pushd api
%mvn_build -j
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.5-1
- Import
