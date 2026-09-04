%global source0_hash 6a33aff0ce727477903a51da04f864a5ae6bb8ea80f224b859dcb9e96e938be8

Name:           jdependency
Version:        2.16
Release:        1%{?dist}
Summary:        Class dependency analysis library for Java
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://github.com/tcurdt/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/tcurdt/%{name}/archive/%{name}-%{version}.tar.gz#/jdependency-2.12.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)

%description
%{name} is a small library that helps you analyze class level
dependencies, clashes and missing classes.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin "org.jacoco:jacoco-maven-plugin"

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12-4
- Prepare for Oreon 11 (RP1)
