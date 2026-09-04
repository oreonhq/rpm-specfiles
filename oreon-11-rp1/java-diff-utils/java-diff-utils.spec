%global source0_hash 860162748b8e3db9302e65c0aacce4da7931fa4aca31d560b1ab991421ebabdd

Name:           java-diff-utils
Version:        4.17
Release:        %{autorelease}
Summary:        Java library for performing diff operations

License:        Apache-2.0
URL:            https://java-diff-utils.github.io/java-diff-utils/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-parent-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%global _desc %{expand:
Diff Utils library is an OpenSource library for performing the comparison / diff operations 
between texts or some kind of data: computing diffs, applying patches, generating unified 
diffs or parsing them, generating diff output for easy future displaying (like side-by-side 
view) and so on.}

%description %_desc

%package        parent
Summary:        Java Diff Utils parent POM

%description    parent %_desc

This package contains the parent POM for Java Diff Utils.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-parent-%{version}

# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_disable_module java-diff-utils-jgit

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-java-diff-utils
%license LICENSE

%files parent -f .mfiles-java-diff-utils-parent
%license LICENSE

%changelog
%autochangelog
