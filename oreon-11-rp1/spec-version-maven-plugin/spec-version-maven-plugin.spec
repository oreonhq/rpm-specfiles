# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 53c9a72d4e4e792d72dc39195783094eb92e9558d550958ffc68f9a91bcd0430
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global giturl  https://github.com/eclipse-ee4j/glassfish-%{name}

Name:           spec-version-maven-plugin
Version:        2.2
Release:        8%{?dist}
Summary:        Spec Version Maven Plugin
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0

URL:            https://projects.eclipse.org/projects/ee4j.glassfish
VCS:            git:%{giturl}.git
Source:        https://github.com/eclipse-ee4j/glassfish-spec-version-maven-plugin/archive/2.2/spec-version-maven-plugin-2.2.tar.gz

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
%oreon_verify_sources
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2-8
- Import
