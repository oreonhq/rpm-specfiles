%global source0_hash 28dc3981039a7db87bfbb4d10b4e88772a7224ad3be95bea069a28bea34bf459

Name:           options
Version:        1.7
Release:        16%{?dist}
Summary:        Library for managing sets of JVM properties to configure an app or library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/headius/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)

%description
Provides a simple mechanism for defining JVM property-based
configuration for an application or library.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files  -f .mfiles
%license LICENSE
%doc README.md

%changelog
%autochangelog
