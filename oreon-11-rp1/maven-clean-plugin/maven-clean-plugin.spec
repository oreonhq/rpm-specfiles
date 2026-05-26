Name:           maven-clean-plugin
Version:        3.3.2
Release:        9%{?dist}
Summary:        Maven Clean Plugin
License:        Apache-2.0
URL:            http://maven.apache.org/plugins/maven-clean-plugin/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 fbdbe1121da3397c6a50892346c3239c8b1c3c78df2fe3e57a4d1609782cbab6
%global source0_file maven-clean-plugin-3.3.2-source-release.zip
# oreon url source checksums end

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)

%description
The Maven Clean Plugin is a plugin that removes files generated
at build-time in a project's directory.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-clean-plugin-3.3.2-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fbdbe1121da3397c6a50892346c3239c8b1c3c78df2fe3e57a4d1609782cbab6" || { echo "oreon: Source0 SHA256 mismatch for maven-clean-plugin-3.3.2-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

# junit dependency was removed in Plexus 1.6
%pom_add_dep junit:junit::test

%pom_remove_dep org.codehaus.plexus:plexus-xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.2-9
- Prepare for Oreon 11 (RP1)
