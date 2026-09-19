%global source0_hash 447bac4aaf9ebbd451957dcd6873feef23be21616751a39d728f09f34d337443

Name:           jol
Version:        0.17
Release:        12%{?dist}
Summary:        Java Object Layout

# GPL-2.0-only: the project as a whole
# GPL-2.0-only WITH Classpath-exception-2.0:
#   Every file containing the following text: "Oracle designates this
#   particular file as subject to the "Classpath" exception as provided by
#   Oracle in the LICENSE file that accompanied this code.
# BSD-3-Clause: jol-samples/ (not shipped in any binary RPM)
License:        GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.java.net/projects/code-tools/jol/
Source0:        https://github.com/openjdk/jol/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires:  mvn(org.ow2.asm:asm)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%global _desc %{expand:
JOL (Java Object Layout) is a tiny toolbox to analyze Java object
layouts.  These tools use Unsafe, JVMTI, and Serviceability Agent (SA)
heavily to decode the actual object layout, footprint, and references.
This makes JOL much more accurate than other tools relying on heap dumps,
specification assumptions, etc.}

%description %_desc

%{?javadoc_package}

%package        parent
Summary:        Java Object Layout parent POM

%description    parent %_desc

This package contains the parent POM for JOL.

%package        core
Summary:        Java Object Layout core classes

%description    core %_desc

This package contains the core classes for JOL.

%package        cli
Summary:        Java Object Layout command line interface
Requires:       %{name}-core = %{version}-%{release}

%description    cli %_desc

This package contains a command line interface to JOL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-source-plugin

# We do not need benchmarks or samples
%pom_disable_module jol-benchmarks
%pom_disable_module jol-samples

%build
%mvn_build -s --force

%install
%mvn_install

%files parent -f .mfiles-jol-parent
%license LICENSE

%files core -f .mfiles-jol-core
%doc README.md
%license LICENSE

%files cli -f .mfiles-jol-cli

%changelog
%autochangelog
