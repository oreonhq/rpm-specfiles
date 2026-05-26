Name:       directory-maven-plugin
Version:    1.0
Release:    8%{?dist}
Summary:    Establish locations for files in multi-module builds

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:    Apache-2.0
URL:        https://github.com/jdcasey/directory-maven-plugin

Source0:    https://github.com/jdcasey/directory-maven-plugin/archive/directory-maven-plugin-%{version}.tar.gz
# Fixes bz 2261062 - no mojo definition build error
# https://github.com/knight-of-ni/directory-maven-plugin/commit/ce51a6ea81b583c7b7b75e859bb1a508eb713fbe.patch
Patch0:     directory-maven-plugin-fix-no-mojo-definition.patch
# oreon url source checksums begin
%global source0_sha256 89936bd705abf6a70828d743374c3f716802699852c1d03361394d690850c964
%global source0_file directory-maven-plugin-1.0.tar.gz
# oreon url source checksums end

BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(junit:junit)

%description
The Directory Plugin for Maven is used to discover various project-related 
paths, such as the execution root directory, the directory for a specific 
project in the current build session, or the highest project base directory 
(closest to the filesystem root directory) available in the projects loaded 
from disk (not resolved from a remote repository). The plugin will then reflect
this value to the console, and also inject it into each project's properties 
using the value of the property plugin parameter.

%package javadoc
Summary:  Javadoc for %{name}

%description javadoc
%{summary}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/directory-maven-plugin-1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "89936bd705abf6a70828d743374c3f716802699852c1d03361394d690850c964" || { echo "oreon: Source0 SHA256 mismatch for directory-maven-plugin-1.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n directory-maven-plugin-directory-maven-plugin-%{version}

%pom_remove_parent

# Bump Java source option
sed -i 's/1.7/1.8/g' pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-8
- Prepare for Oreon 11 (RP1)
