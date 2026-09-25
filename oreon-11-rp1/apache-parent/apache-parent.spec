%global source0_hash 182ad0954e4a60bc73cafcaab595d39d65b8156f7085f0b87505907eb03fe608

%bcond_without bootstrap

Name:           apache-parent
Version:        40
Release:        %autorelease
Summary:        Parent POM file for Apache projects
License:        Apache-2.0
URL:            https://apache.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/apache/%{version}/apache-%{version}-source-release.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
%endif
%if %{without bootstrap}
# Not generated automatically
BuildRequires:  mvn(org.apache.apache.resources:apache-jar-resource-bundle)
%endif
Requires:       mvn(org.apache.apache.resources:apache-jar-resource-bundle)

%description
This package contains the parent pom file for apache projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n apache-%{version}

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-site-plugin docs
%pom_remove_plugin :maven-scm-publish-plugin docs

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
%autochangelog
