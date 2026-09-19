%global source0_hash none

Name:           codehaus-parent
Version:        4
Release:        37%{?dist}
Summary:        Parent pom file for codehaus projects
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://codehaus.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/%{version}/codehaus-parent-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-enforcer.patch

BuildRequires:  maven-local-openjdk25

%description
This package contains the parent pom file for codehaus projects.

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
%patch -P0

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
%autochangelog
