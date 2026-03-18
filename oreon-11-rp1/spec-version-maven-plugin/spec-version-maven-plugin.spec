%global giturl  https://github.com/eclipse-ee4j/glassfish-%{name}

Name:           spec-version-maven-plugin
Version:        2.2
Release:        8%{?dist}
Summary:        Spec Version Maven Plugin
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0

URL:            https://projects.eclipse.org/projects/ee4j.glassfish
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Maven Plugin to configure APIs version and specs in a MANIFEST.MF file.

%{?javadoc_package}

%prep
%autosetup -n glassfish-%{name}-%{version}

%conf
sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

# remove spurious executable bits
find -O3 . -type f -perm /0111 -exec chmod a-x {} +
chmod a+x src/main/resources/checkVersion.sh

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2-8
- Prepare for Oreon 11 (RP1)
