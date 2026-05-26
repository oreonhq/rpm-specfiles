%bcond_without bootstrap

Name:           maven-shared-io
Epoch:          1
Version:        3.0.0
Release:        %autorelease
Summary:        API for I/O support like logging, download or file scanning
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-shared-io
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Rejected upstream: https://issues.apache.org/jira/browse/MSHARED-490
Patch:          0001-Fix-running-tests-with-Maven-3.3.9.patch
# From upstream commit: https://github.com/apache/maven-shared-io/commit/5e37cfb2f0fa79e77a9cd627278e28b4d45aa5f8
Patch:          0002-Fix-incorrect-parent-relativePath.patch
# oreon url source checksums begin
%global source0_sha256 4908e8bc610bad4a74ea4b09e0cf77f53af41b648a68d805400195f710a55e43
%global source0_file maven-shared-io-3.0.0-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.easymock:easymock)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:3.0.0-47

%description
API for I/O support like logging, download or file scanning.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-shared-io-3.0.0-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4908e8bc610bad4a74ea4b09e0cf77f53af41b648a68d805400195f710a55e43" || { echo "oreon: Source0 SHA256 mismatch for maven-shared-io-3.0.0-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%mvn_build -j -- -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-1
- Prepare for Oreon 11 (RP1)
