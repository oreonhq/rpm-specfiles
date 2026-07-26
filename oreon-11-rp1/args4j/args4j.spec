%global source0_hash b4305ca1ff31d3492dd93770f302242c2bf536b440bca24b2580646b184a3733

Name:           args4j
Version:        2.33
Release:        32%{?dist}
Summary:        Java command line arguments parser
License:        MIT
URL:            https://args4j.kohsuke.org
Source0:        https://github.com/kohsuke/%{name}/archive/%{name}-site-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

# Fix build on Java 11/17
Patch0: 0001-Remove-usage-of-internal-sun-class-removed-in-Java-9.patch

# Stopped shipping these unused subpackages in F34
Obsoletes: %{name}-tools < 2.33-13
Obsoletes: %{name}-parent < 2.33-13

%description
args4j is a small Java class library that makes it easy
to parse command line options/arguments in your CUI application.
- It makes the command line parsing very easy by using annotations
- You can generate the usage screen very easily
- You can generate HTML/XML that lists all options for your documentation
- Fully supports localization
- It is designed to parse javac like options (as opposed to GNU-style
  where ls -lR is considered to have two options l and R)

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-site-%{version}
%patch -P0 -p1

# removing bundled stuff
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Not needed for RPM builds
%pom_remove_plugin -r :maven-site-plugin

# we don't need these now
%pom_disable_module args4j-maven-plugin
%pom_disable_module args4j-maven-plugin-example
%pom_disable_module args4j-tools

# Remove reliance on the parent pom
%pom_remove_parent

# Remove hard-coded source/target
%pom_xpath_remove pom:plugin/pom:configuration/pom:target
%pom_xpath_remove pom:plugin/pom:configuration/pom:source

# Don't package the parent pom
%mvn_package :args4j-site __noinstall

# install also compat symlinks
%mvn_file ":{*}" %{name}/@1 @1

%build
%mvn_build -- -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%license %{name}/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license %{name}/LICENSE.txt

%changelog
%autochangelog
