%global source0_hash 84e7a56680cd0f1866f98e89bb9ae8d05bd9f87892e6e50dafc63415dbee3122

Name:           jackson-core
Version:        2.22.2
Release:        1%{?dist}
Summary:        Core part of Jackson
License:        Apache-2.0

URL:            https://github.com/FasterXML/jackson-core
Source0:        https://github.com/FasterXML/jackson-core/archive/refs/tags/jackson-core-2.18.2.tar.gz#/jackson-core-2.18.2.tar.gz
Patch1:         0001-Remove-ch.randelshofer.fastdoubleparser.patch

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
Buildrequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} >= 10
ExclusiveArch:  %{java_arches} noarch
%endif

%description
Core part of Jackson that defines Streaming API as well
as basic shared abstractions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{name}-%{version} -p 1

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin "org.apache.maven.plugins:maven-shade-plugin"
%pom_remove_plugin "org.jacoco:jacoco-maven-plugin"
%pom_remove_plugin "org.moditect:moditect-maven-plugin"
%pom_remove_plugin "de.jjohannes:gradle-module-metadata-maven-plugin"
%pom_remove_plugin "io.github.floverfelt:find-and-replace-maven-plugin"
%pom_remove_dep "ch.randelshofer:fastdoubleparser"

%pom_add_plugin "org.apache.felix:maven-bundle-plugin" . "<extensions>true</extensions>"

cp -p src/main/resources/META-INF/jackson-core-NOTICE .
sed -i 's/\r//' LICENSE jackson-core-NOTICE

%mvn_file : %{name}

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE jackson-core-NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.2-6
- Prepare for Oreon 11 (RP1)
