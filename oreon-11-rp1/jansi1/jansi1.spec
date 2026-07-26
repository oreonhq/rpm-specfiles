%global source0_hash 73cd47ecf370a33c6e76afb5d9a8abf99489361d7bd191781dbd9b7efd082aa5

Name:           jansi1
Version:        1.18
Release:        26%{?dist}
Summary:        Generate and interpret ANSI escape sequences in Java
License:        Apache-2.0
URL:            https://fusesource.github.io/jansi/

Source0:        https://github.com/fusesource/jansi/archive/jansi-project-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi-native)

%description
Jansi is a small Java library that allows you to use ANSI escape
sequences in your Java console applications.  It implements ANSI support
on platforms which don't support it like Windows and provides graceful
degradation when output is sent to output devices which cannot support
ANSI sequences.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jansi-jansi-project-%{version}

%pom_disable_module example
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-site-plugin

# No maven-uberize-plugin
%pom_remove_plugin -r :maven-uberize-plugin

# Remove unnecessary deps for jansi-native builds
cd jansi
%pom_remove_dep :jansi-windows32
%pom_remove_dep :jansi-windows64
%pom_remove_dep :jansi-osx
%pom_remove_dep :jansi-freebsd32
%pom_remove_dep :jansi-freebsd64
# it's there only to be bundled in uberjar and we disable uberjar generation
%pom_remove_dep :jansi-linux32
%pom_remove_dep :jansi-linux64
cd -

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin -r :maven-javadoc-plugin

# Build for JDK 1.8 at a minimum for JDK 17 compatibility
%pom_xpath_set //pom:source 1.8
%pom_xpath_set //pom:target 1.8

%build
%mvn_compat_version org.fusesource.jansi:jansi %{version} 1
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license license.txt
%doc readme.md changelog.md

%changelog
%autochangelog
