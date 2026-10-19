%global source0_hash d20243f9c37d97c51e1203c01b4dd76c65aa22f3b7c290f28c0f8e07989afb40
Name:           dirgra
Version:        0.6
Release:        1%{?dist}
Summary:        Simple Directed Graph
License:        EPL-1.0
URL:            https://github.com/jruby/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/jruby/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  maven-local-openjdk25
# /oreon:deps
%description
Simple Directed Graph Implementation.

%{?javadoc_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

%pom_remove_parent

%pom_xpath_remove pom:extensions

%pom_remove_plugin :maven-source-plugin

%pom_remove_plugin :maven-javadoc-plugin

%build

%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
