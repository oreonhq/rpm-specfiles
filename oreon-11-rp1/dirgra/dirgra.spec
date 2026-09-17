%global source0_hash c12bf9809eecfcce28ca99776011702ca1df942fc1c4eb73699848e27279958a

Name:           dirgra
Version:        0.4
Release:        %autorelease
Summary:        Simple Directed Graph
License:        EPL-1.0
URL:            https://github.com/jruby/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25

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

%files -f .mfiles
%license LICENSE.txt

%changelog
%autochangelog
