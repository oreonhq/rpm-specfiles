%global source0_hash 60b2fc5dea92375de13b8cbe08d5fa0553a6585bcd136bb4b1efa5872ca4ea88

%bcond_without bootstrap

Name:           apache-parent
Version:        35
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 35-3
- bump release (retry failed build)

* Wed Apr 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 35-2
- %%autosetup -n apache-%%{version} for Maven apache-VERSION-source-release.zip layout

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 35-1
- Prepare for Oreon 11 (RP1)
