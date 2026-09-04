%global source0_hash 135cbd1ebd5d00740131abaa2788aca492cf4ce0600ad304f8d87d014008a3c4

%bcond_with     jp_minimal

Name:           jackson-modules-base
Version:        2.22.2
Release:        1%{?dist}
Summary:        Jackson modules: Base
License:        Apache-2.0

URL:            https://github.com/FasterXML/jackson-modules-base
Source0:        https://github.com/FasterXML/jackson-modules-base/archive/refs/tags/jackson-modules-base-2.18.2-take-2.tar.gz#/jackson-modules-base-2.18.2-take-2.tar.gz
Patch1:         0001-Expose-javax.security.auth-from-JDK-internals.patch
Patch2:         0001-Replace-javax.activation-imports-with-jakarta.activa.patch
Patch3:         0001-Use-jakarta.activation-namespace-in-jaxb-api.patch

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42 || (0%{?oreon} >= 11)
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.ow2.asm:asm)

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
ExclusiveArch:  %{java_arches} noarch
%endif

%description
Jackson "base" modules: modules that build directly on databind,
and are not data-type, data format, or JAX-RS provider modules.

%package -n jackson-module-jaxb-annotations
Summary: Support for using JAXB annotations as an alternative to "native" Jackson annotations

%description -n jackson-module-jaxb-annotations
This Jackson extension module provides support for using JAXB (javax.xml.bind)
annotations as an alternative to native Jackson annotations. It is most often
used to make it easier to reuse existing data beans that used with JAXB
framework to read and write XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n jackson-modules-base-jackson-modules-base-2.18.2-take-2
%autosetup -n jackson-modules-base-jackson-modules-base-2.18.2-take-2 -p 1

%pom_remove_dep -r org.glassfish.jaxb:jaxb-runtime
%pom_remove_plugin "de.jjohannes:gradle-module-metadata-maven-plugin"

# no need for Java 9 module stuff
%pom_remove_plugin -r :moditect-maven-plugin

# Disable bundling of asm
%pom_remove_plugin ":maven-shade-plugin" afterburner mrbean paranamer

sed -i 's/\r//' mrbean/src/main/resources/META-INF/{LICENSE,NOTICE}
cp -p mrbean/src/main/resources/META-INF/{LICENSE,NOTICE} .

# Fix OSGi dependency
%pom_change_dep org.osgi:org.osgi.core org.osgi:osgi.core osgi

# NoClassDefFoundError: net/sf/cglib/core/CodeGenerationException
%pom_add_dep cglib:cglib:3.2.4:test guice

%pom_disable_module afterburner
%pom_disable_module android-record
%pom_disable_module guice
%pom_disable_module guice7
%pom_disable_module mrbean
%pom_disable_module osgi
%pom_disable_module paranamer
%pom_disable_module jakarta-xmlbind
%pom_disable_module blackbird
%pom_disable_module no-ctor-deser

# Allow javax,activation to be optional
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" jaxb "
<configuration>
  <instructions>
    <Import-Package>javax.activation;resolution:=optional,*</Import-Package>
  </instructions>
</configuration>"

# Revert jaxb annotation dependency to 2.17 mode
%pom_remove_dep javax.xml.bind:jaxb-api jaxb
%pom_add_dep jakarta.xml.bind:jakarta.xml.bind-api jaxb

# This test fails since mockito was upgraded to 2.x
rm osgi/src/test/java/com/fasterxml/jackson/module/osgi/InjectOsgiServiceTest.java

%mvn_file ":{*}" jackson-modules/@1

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-jackson-modules-base
%doc README.md release-notes
%license LICENSE NOTICE

%files -n jackson-module-jaxb-annotations -f .mfiles-jackson-module-jaxb-annotations
%doc jaxb/README.md jaxb/release-notes
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.2-6
- Import
