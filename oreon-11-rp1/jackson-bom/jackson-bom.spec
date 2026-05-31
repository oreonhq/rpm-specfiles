%global source0_hash 9b6bfdaea317c0cb26949e2b81c7c5f5d616ef77b47f327673c2ac7283507340

Name:           jackson-bom
Version:        2.18.2
Release:        6%{?dist}
Summary:        Bill of materials POM for Jackson projects
License:        Apache-2.0

URL:            https://github.com/FasterXML/jackson-bom
Source0:        https://github.com/FasterXML/jackson-bom/archive/jackson-bom-2.18.2.tar.gz

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:) >= 2.17
BuildRequires:  mvn(junit:junit)

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} >= 10
ExclusiveArch:  %{java_arches} noarch
%endif

%description
A "bill of materials" POM for Jackson dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}

# Disable plugins not needed during RPM builds
%pom_remove_plugin ":maven-enforcer-plugin" base
%pom_remove_plugin ":nexus-staging-maven-plugin" base

# New EE coords
%pom_change_dep "javax.activation:javax.activation-api" "jakarta.activation:jakarta.activation-api" base

# Remove dep on junit-bom
%pom_remove_dep "org.junit:junit-bom" base

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.2-6
- Prepare for Oreon 11 (RP1)
