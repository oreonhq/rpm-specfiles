%global source0_hash f811bbe3c04d4ebe697ce46b4a80ab1b2af7b5359d2d88dec4ff8f96fdb2efac
%global source1_hash 8150e476031c4e51d0aa0c427eb26729b1cb7a3f91198c066b59cbff81003d64

%global namedreltag .Final
%global namedversion %{version}%{namedreltag}

Name:           resteasy
Version:        3.0.26
Release:        41%{?dist}
Summary:        Framework for RESTful Web services and Java applications
License:        Apache-2.0
URL:            http://resteasy.jboss.org/
Source0:        https://github.com/resteasy/Resteasy/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Source1:        resteasy-jakarta.patch
Patch1:         0001-RESTEASY-2559-Improper-validation-of-response-header.patch
Patch2:         0001-Remove-Log4jLogger.patch
Patch3:         0001-Replace-javax.activation-imports-with-jakarta.activa.patch
Patch4:         0001-Update-to-new-jakarta-xml-bind-namespace.patch

BuildArch:      noarch
%if 0%{?fedora} || (0%{?oreon} >= 11)
ExclusiveArch:  %{java_arches} noarch
%endif

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} < 43 || (0%{?oreon} >= 11)
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk21
%endif

BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

%if 0%{?rhel} && 0%{?rhel} < 10 || 0%{?fedora} && 0%{?fedora} < 43 || (0%{?oreon} >= 11)
BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)
%elif 0%{?rhel}
BuildRequires:  tomcat9-servlet-4.0-api
%else
BuildRequires:  tomcat-servlet-6.0-api
BuildRequires:  tomcat-jakartaee-migration
%endif

# Jackson 2
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)

BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%description
%global desc \
RESTEasy contains a JBoss project that provides frameworks to help\
build RESTful Web Services and RESTful Java applications. It is a fully\
certified and portable implementation of the JAX-RS specification.
%{desc}
%global extdesc %{desc}\
\
This package contains

%package -n     pki-%{name}
Summary:        Framework for RESTful Web services and Java applications
Obsoletes:      %{name} < %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

Requires:       pki-%{name}-client              = %{version}-%{release}
Requires:       pki-%{name}-core                = %{version}-%{release}
Requires:       pki-%{name}-jackson2-provider   = %{version}-%{release}
Requires:       pki-%{name}-servlet-initializer = %{version}-%{release}

# subpackages removed in fedora 32
Obsoletes:      %{name}-fastinfoset-provider < 3.0.26-1
Obsoletes:      %{name}-jackson-provider < 3.0.26-1
Obsoletes:      %{name}-jettison-provider < 3.0.26-1
Obsoletes:      %{name}-json-p-provider < 3.0.26-1
Obsoletes:      %{name}-multipart-provider < 3.0.26-1
Obsoletes:      %{name}-netty3 < 3.0.26-1
Obsoletes:      %{name}-optional < 3.0.26-1
Obsoletes:      %{name}-test < 3.0.26-1
Obsoletes:      %{name}-validator-provider-11 < 3.0.26-1
Obsoletes:      %{name}-yaml-provider < 3.0.26-1

%description -n pki-%{name}
%{desc}

%package -n     pki-%{name}-core
Summary:        Core modules for %{name}
Obsoletes:      resteasy-jaxrs-api < 3.0.7
Obsoletes:      %{name}-core < %{version}-%{release}
Conflicts:      %{name}-core < %{version}-%{release}
Provides:       %{name}-core = %{version}-%{release}

%description -n pki-%{name}-core
%{extdesc} %{summary}.

%package -n     pki-%{name}-jackson2-provider
Summary:        Module jackson2-provider for %{name}
Obsoletes:      %{name}-jackson2-provider < %{version}-%{release}
Conflicts:      %{name}-jackson2-provider < %{version}-%{release}
Provides:       %{name}-jackson2-provider = %{version}-%{release}

%description -n pki-%{name}-jackson2-provider
%{extdesc} %{summary}.

%package -n     pki-%{name}-client
Summary:        Client for %{name}
Obsoletes:      %{name}-client < %{version}-%{release}
Conflicts:      %{name}-client < %{version}-%{release}
Provides:       %{name}-client = %{version}-%{release}

%description -n pki-%{name}-client
%{extdesc} %{summary}.

%package -n     pki-%{name}-servlet-initializer
Summary:        %{name} Servlet Initializer
Obsoletes:      %{name}-servlet-initializer < %{version}-%{release}
Conflicts:      %{name}-servlet-initializer < %{version}-%{release}
Provides:       %{name}-servlet-initializer = %{version}-%{release}

%description -n pki-%{name}-servlet-initializer
%{extdesc} %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -n Resteasy-%{namedversion}
%patch 1 -p 1
%patch 2 -p 1
%patch 3 -p 1
%patch 4 -p 1
%if 0%{?fedora} >= 43 || (0%{?oreon} >= 11)
patch -p 1 < %{_sourcedir}/resteasy-jakarta.patch
%endif

%pom_disable_module arquillian
%pom_disable_module eagledns
%pom_disable_module jboss-modules
%pom_disable_module profiling-tests
%pom_disable_module resteasy-bom
%pom_disable_module resteasy-cache
%pom_disable_module resteasy-cdi
%pom_disable_module resteasy-dependencies-bom
%pom_disable_module resteasy-guice
%pom_disable_module resteasy-jaxrs-testsuite
%pom_disable_module resteasy-jsapi
%pom_disable_module resteasy-jsapi-testing
%pom_disable_module resteasy-links
%pom_disable_module resteasy-spring
%pom_disable_module resteasy-wadl
%pom_disable_module resteasy-wadl-undertow-connector
%pom_disable_module security
%pom_disable_module server-adapters
%pom_disable_module testsuite
%pom_disable_module tjws

pushd providers
%pom_disable_module fastinfoset
%pom_disable_module jackson
%pom_disable_module jettison
%pom_disable_module json-p-ee7
%pom_disable_module multipart
%pom_disable_module resteasy-atom
%pom_disable_module resteasy-html
%pom_disable_module resteasy-validator-provider-11
%pom_disable_module yaml
%pom_disable_module jaxb
popd

find -name '*.jar' -print -delete

%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-javadoc-plugin

# depend on jakarta-activation
%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api:2.1.1 resteasy-jaxrs
%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api:2.1.1 resteasy-spring

# depend on jakarta-annotations
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api jboss-modules
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api providers/jaxb
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-dependencies-bom
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-guice
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-jaxrs
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-links
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-spring
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/keystone/keystone-core
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/resteasy-crypto
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/skeleton-key-idm/skeleton-key-core
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/skeleton-key-idm/skeleton-key-idp
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api server-adapters/resteasy-jdk-http

# remove resteasy-dependencies pom
%pom_remove_dep "org.jboss.resteasy:resteasy-dependencies"

# remove redundant jcip-dependencies dep from resteasy-jaxrs
%pom_remove_dep net.jcip:jcip-annotations resteasy-jaxrs

# remove junit dependency from all modules
%pom_remove_dep junit:junit resteasy-client
%pom_remove_dep junit:junit providers/resteasy-atom
%pom_remove_dep junit:junit providers/jaxb
%pom_remove_dep junit:junit resteasy-jaxrs
%pom_remove_dep junit:junit resteasy-servlet-initializer

# remove log4j dependency
%pom_remove_dep log4j:log4j resteasy-jaxrs

# depend on servlet-api from pki-servlet-4.0-api
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api resteasy-jaxrs
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api resteasy-servlet-initializer
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/abdera-atom
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jaxb
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jackson2

# add dependencies for EE APIs that were removed in Java 11
%pom_add_dep jakarta.xml.bind:jakarta.xml.bind-api resteasy-jaxrs
%pom_add_dep jakarta.xml.bind:jakarta.xml.bind-api resteasy-servlet-initializer

%pom_remove_plugin :maven-clean-plugin

%mvn_package ":resteasy-jaxrs" core
%mvn_package ":providers-pom" core
%mvn_package ":resteasy-jaxrs-all" core
%mvn_package ":resteasy-pom" core
%mvn_package ":resteasy-jackson2-provider" jackson2-provider
%mvn_package ":resteasy-client" client
%mvn_package ":resteasy-servlet-initializer" servlet-initializer

# Disable useless artifacts generation, package __noinstall do not work
%pom_add_plugin org.apache.maven.plugins:maven-source-plugin . '
<configuration>
 <skipSource>true</skipSource>
</configuration>'

%build

%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install

%mvn_install

%if 0%{?rhel} >= 10 || 0%{?fedora} && 0%{?fedora} >= 43 || (0%{?oreon} >= 11)
/usr/bin/javax2jakarta -logLevel=ALL -profile=EE %{buildroot}%{_datadir}/java/resteasy/%{name}-client.jar %{buildroot}%{_datadir}/java/resteasy/%{name}-client.jar
/usr/bin/javax2jakarta -logLevel=ALL -profile=EE %{buildroot}%{_datadir}/java/resteasy/%{name}-jackson2-provider.jar %{buildroot}%{_datadir}/java/resteasy/%{name}-jackson2-provider.jar
/usr/bin/javax2jakarta -logLevel=ALL -profile=EE %{buildroot}%{_datadir}/java/resteasy/%{name}-jaxrs.jar  %{buildroot}%{_datadir}/java/resteasy/%{name}-jaxrs.jar
/usr/bin/javax2jakarta -logLevel=ALL -profile=EE %{buildroot}%{_datadir}/java/resteasy/%{name}-servlet-initializer.jar %{buildroot}%{_datadir}/java/resteasy/%{name}-servlet-initializer.jar
%endif

%files -n pki-%{name}
%doc README.md
%license License.html

%files -n pki-%{name}-core -f .mfiles-core
%license License.html

%files -n pki-%{name}-jackson2-provider -f .mfiles-jackson2-provider
%license License.html

%files -n pki-%{name}-client -f .mfiles-client
%license License.html

%files -n pki-%{name}-servlet-initializer -f .mfiles-servlet-initializer
%license License.html

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.26-41
- Import
