%global source0_hash 046186a558bcca490e1e940490272d83b548418bf3dab166ac692f7aaee07612
Name:           jackson-annotations
Version:        2.22
Release:        1%{?dist}
Summary:        Core annotations for Jackson data processor
License:        Apache-2.0
URL:            https://github.com/FasterXML/jackson-annotations
Source0:        https://github.com/FasterXML/jackson-annotations/archive/refs/tags/jackson-annotations-%{version}.tar.gz#/jackson-annotations-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
# /oreon:deps
%description
Core annotations used for value types,
used by Jackson data-binding package.

%package javadoc
Summary: Javadoc for %{name}
%description javadoc
This package contains API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin "org.moditect:moditect-maven-plugin"
%pom_remove_plugin "org.codehaus.mojo:build-helper-maven-plugin"

sed -i 's/\r//' LICENSE

%mvn_file : %{name}

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jackson-annotations-javadoc -f %{oreon_filedir}/jackson-annotations-javadoc.list

%changelog

%autochangelog
