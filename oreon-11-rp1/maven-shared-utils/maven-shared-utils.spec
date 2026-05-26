%bcond_without bootstrap

Name:           maven-shared-utils
Version:        3.4.2
Release:        %autorelease
Summary:        Maven shared utility classes
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-shared-utils
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch:          0001-Avoid-setting-POSIX-attributes-for-symbolic-links.patch
# oreon url source checksums begin
%global source0_sha256 0b72bbf60911e17398e9c0ce29866e4f13a26e8da4aa2e8304e73152ac4d4ef3
%global source0_file maven-shared-utils-3.4.2-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.4.2-22

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-shared-utils-3.4.2-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0b72bbf60911e17398e9c0ce29866e4f13a26e8da4aa2e8304e73152ac4d4ef3" || { echo "oreon: Source0 SHA256 mismatch for maven-shared-utils-3.4.2-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

find -name '*.java' -exec sed -i 's/\r//' {} +


%pom_remove_dep org.apache.commons:commons-text
rm src/test/java/org/apache/maven/shared/utils/CaseTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.2-1
- Prepare for Oreon 11 (RP1)
