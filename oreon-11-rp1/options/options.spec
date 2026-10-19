%global source0_hash 28dc3981039a7db87bfbb4d10b4e88772a7224ad3be95bea069a28bea34bf459
Name:           options
Version:        1.7
Release:        1%{?dist}
Summary:        Library for managing sets of JVM properties to configure an app or library
License:        Apache-2.0
URL:            https://github.com/headius/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/headius/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
