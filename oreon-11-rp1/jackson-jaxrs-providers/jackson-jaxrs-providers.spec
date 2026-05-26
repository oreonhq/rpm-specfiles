%bcond_without  jp_minimal

Name:           jackson-jaxrs-providers
Version:        2.18.2
Release:        6%{?dist}
Summary:        Jackson JAX-RS providers
License:        Apache-2.0

URL:            https://github.com/FasterXML/jackson-jaxrs-providers
Source0:        https://github.com/FasterXML/jackson-jaxrs-providers/archive/jackson-jaxrs-providers-2.18.2.tar.gz
# oreon url source checksums begin
%global source0_sha256 1771ada2f5a5bd52c11a65cbf8c306359cb8b941e2fec8d831939e07c9dea0cd
%global source0_file jackson-jaxrs-providers-2.18.2.tar.gz
# oreon url source checksums end

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} >= 10
ExclusiveArch:  %{java_arches} noarch
%endif

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%if %{without jp_minimal}
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(org.glassfish.jersey.containers:jersey-container-servlet)
BuildRequires:  mvn(org.glassfish.jersey.core:jersey-server)
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jaxrs)
%endif

%if %{with jp_minimal}
Obsoletes:      jackson-jaxrs-cbor-provider < 2.10.0-1
Obsoletes:      jackson-jaxrs-smile-provider < 2.10.0-1
Obsoletes:      jackson-jaxrs-xml-provider < 2.10.0-1
Obsoletes:      jackson-jaxrs-yaml-provider < 2.10.0-1
%endif

%description
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats: JSON, Smile (binary JSON), XML, CBOR (another kind of
binary JSON), YAML.

%package -n jackson-jaxrs-json-provider
Summary:       Jackson-JAXRS-JSON

%description -n jackson-jaxrs-json-provider
Functionality to handle JSON input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%if %{without jp_minimal}
%package -n jackson-jaxrs-cbor-provider
Summary:       Jackson-JAXRS-CBOR

%description -n jackson-jaxrs-cbor-provider
Functionality to handle CBOR encoded input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n jackson-jaxrs-smile-provider
Summary:       Jackson-JAXRS-Smile

%description -n jackson-jaxrs-smile-provider
Functionality to handle Smile (binary JSON) input/output for
JAX-RS implementations (like Jersey and RESTeasy) using standard
Jackson data binding.

%package -n jackson-jaxrs-xml-provider
Summary:       Jackson-JAXRS-XML

%description -n jackson-jaxrs-xml-provider
Functionality to handle Smile XML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n jackson-jaxrs-yaml-provider
Summary:       Jackson-JAXRS-YAML

%description -n jackson-jaxrs-yaml-provider
Functionality to handle YAML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.
%endif

%package datatypes
Summary: Functionality for reading/writing core JAX-RS helper types

%description datatypes
Functionality for reading/writing core JAX-RS helper types.

%package parent
Summary: Parent for Jackson JAX-RS providers

%description parent
Parent POM for Jackson JAX-RS providers.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jackson-jaxrs-providers-2.18.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1771ada2f5a5bd52c11a65cbf8c306359cb8b941e2fec8d831939e07c9dea0cd" || { echo "oreon: Source0 SHA256 mismatch for jackson-jaxrs-providers-2.18.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{name}-%{version}

cp -p xml/src/main/resources/META-INF/LICENSE .
cp -p xml/src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%pom_remove_plugin -r :moditect-maven-plugin
%pom_remove_plugin "de.jjohannes:gradle-module-metadata-maven-plugin"

# Disable jar with no-meta-inf-services classifier, breaks build
%pom_remove_plugin :maven-jar-plugin cbor
%pom_remove_plugin :maven-jar-plugin json
%pom_remove_plugin :maven-jar-plugin smile
%pom_remove_plugin :maven-jar-plugin xml
%pom_remove_plugin :maven-jar-plugin yaml
%pom_remove_plugin :maven-jar-plugin datatypes

# Replace jakarta-ws-rs with jboss-jaxrs-2.0-api
%pom_change_dep javax.ws.rs:javax.ws.rs-api org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec

# Add missing deps to fix java.lang.ClassNotFoundException during tests
%pom_add_dep com.google.guava:guava:18.0:test datatypes cbor json smile xml yaml
%pom_add_dep org.ow2.asm:asm:5.1:test cbor json smile xml yaml

# Circular dep?
%pom_remove_dep org.jboss.resteasy:resteasy-jackson2-provider json
rm json/src/test/java/com/fasterxml/jackson/jaxrs/json/resteasy/RestEasyProviderLoadingTest.java

%if %{with jp_minimal}
# Disable extra test deps
%pom_remove_dep org.glassfish.jersey.core:
%pom_remove_dep org.glassfish.jersey.containers:
# Disable extra providers
%pom_disable_module cbor
%pom_disable_module smile
%pom_disable_module xml
%pom_disable_module yaml
%endif

%build
%if %{with jp_minimal}
%mvn_build -s -f
%else
%mvn_build -s
%endif

%install
%mvn_install

%files -f .mfiles-jackson-jaxrs-base
%doc README.md release-notes/*
%license LICENSE NOTICE

%files -n jackson-jaxrs-json-provider -f .mfiles-jackson-jaxrs-json-provider
%if %{without jp_minimal}
%files -n jackson-jaxrs-cbor-provider -f .mfiles-jackson-jaxrs-cbor-provider
%files -n jackson-jaxrs-smile-provider -f .mfiles-jackson-jaxrs-smile-provider
%files -n jackson-jaxrs-xml-provider -f .mfiles-jackson-jaxrs-xml-provider
%files -n jackson-jaxrs-yaml-provider -f .mfiles-jackson-jaxrs-yaml-provider
%endif

%files datatypes -f .mfiles-jackson-datatype-jaxrs
%license LICENSE NOTICE

%files parent -f .mfiles-jackson-jaxrs-providers
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.2-6
- Prepare for Oreon 11 (RP1)
