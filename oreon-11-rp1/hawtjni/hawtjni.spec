%global source0_hash b06633e842016398bd41036de5cfc42805d08cdf7e7077a428eb898523b546d6

Name:             hawtjni
Version:          1.18
Release:          18%{?dist}
Summary:          Code generator that produces the JNI code
# Maven plugin is under ASL 2.0.
# stdint.h, shipped in JAR as resource, used only with M$ VC++, is under BSD.
# Everything else is under EPL-1.0
# Automatically converted from old format: ASL 2.0 and EPL-1.0 and BSD - review is highly recommended.
License:          Apache-2.0 AND EPL-1.0 AND LicenseRef-Callaway-BSD

URL:              http://hawtjni.fusesource.org/
Source0:        https://github.com/fusesource/hawtjni/archive/hawtjni-project-1.18.tar.gz

# trivially port from commons-lang to commons-lang3
Patch0:           00-hawtjni-port-to-commons-lang3.patch

BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:    maven-local-openjdk25
BuildRequires:    mvn(commons-cli:commons-cli)
BuildRequires:    mvn(org.apache.commons:commons-lang3)
BuildRequires:    mvn(org.apache.maven:maven-archiver)
BuildRequires:    mvn(org.apache.maven:maven-artifact)
BuildRequires:    mvn(org.apache.maven:maven-compat)
BuildRequires:    mvn(org.apache.maven:maven-plugin-api)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:    mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:    mvn(org.apache.xbean:xbean-finder)
BuildRequires:    mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:    mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:    mvn(org.codehaus.plexus:plexus-io)
BuildRequires:    mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:    mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires:    mvn(org.ow2.asm:asm)
BuildRequires:    mvn(org.ow2.asm:asm-commons)

Requires:         autoconf
Requires:         automake
Requires:         libtool
Requires:         make

%description
HawtJNI is a code generator that produces the JNI code needed to
implement java native methods. It is based on the jnigen code generator
that is part of the SWT Tools project which is used to generate all the
JNI code which powers the eclipse platform.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%package runtime
Summary:          HawtJNI Runtime

%description runtime
This package provides API that projects using HawtJNI should build
against.

%package -n maven-hawtjni-plugin
Summary:          Use HawtJNI from a maven plugin

%description -n maven-%{name}-plugin
This package allows to use HawtJNI from a maven plugin.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{name}-project-%{version}
%patch 0 -p1

%pom_disable_module hawtjni-example
%pom_disable_module hawtjni-maven-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-eclipse-plugin

%mvn_package ":hawtjni-runtime" runtime

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin hawtjni-runtime

%build
%mvn_build

%install
%mvn_install

%files runtime -f .mfiles-runtime
%doc readme.md license.txt changelog.md

%files -f .mfiles

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.18-18
- Prepare for Oreon 11 (RP1)
