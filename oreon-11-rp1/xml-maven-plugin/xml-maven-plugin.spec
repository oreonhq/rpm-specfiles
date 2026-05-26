Name:           xml-maven-plugin
Summary:        Maven XML Plugin
Version:        1.1.0
Release:        %autorelease
License:        Apache-2.0

URL:            https://www.mojohaus.org/xml-maven-plugin/
Source0:        https://github.com/mojohaus/xml-maven-plugin/archive/%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 d3e57f6952ec4a9f241d9ed24ca2a0a168d5ed0a1462beb7c339cabe855d1dd1
%global source0_file xml-maven-plugin-1.1.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(xml-resolver:xml-resolver)

%description
A plugin for various XML related tasks like validation and transformation.


%package javadoc
Summary:       Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xml-maven-plugin-1.1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d3e57f6952ec4a9f241d9ed24ca2a0a168d5ed0a1462beb7c339cabe855d1dd1" || { echo "oreon: Source0 SHA256 mismatch for xml-maven-plugin-1.1.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

# Add the version
sed -i 's|stylesheet |stylesheet version="1.0" |'  src/it/it8/src/main/xsl/it8.xsl

%pom_xpath_set pom:mojo.java.target 8


%build
%mvn_build -f


%install
%mvn_install


%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-1
- Prepare for Oreon 11 (RP1)
