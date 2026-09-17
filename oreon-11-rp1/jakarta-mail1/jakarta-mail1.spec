%global source0_hash 9188bc218a7a9586f41766ba79453fa26e2cc01304b74b2a9e80974f63f4c31c

%bcond_with bootstrap

Name:           jakarta-mail1
Version:        1.6.7
Release:        9%{?dist}
Summary:        Jakarta Mail API
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/eclipse-ee4j/mail
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/mail/archive/%{version}/mail-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.sun.activation:jakarta.activation)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

%description
The Jakarta Mail API provides a platform-independent and
protocol-independent framework to build mail and messaging applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mail-api-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

# disable unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :osgiversion-maven-plugin
%pom_remove_plugin :directory-maven-plugin

# disable android-specific code
%pom_disable_module android

# remove profiles that only add unnecessary things
%pom_xpath_remove "pom:project/pom:profiles"

# Java version 7 no longer supported - use version 8
%pom_xpath_replace "//pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='base-compile-7']/pom:configuration/pom:release" "<release>8</release>"

# inject OSGi bundle versions manually instead of using osgiversion-maven-plugin
find -name pom.xml -exec sed -i "s/\${mail\.osgiversion}/%{version}/g" {} +

%mvn_compat_version jakarta*: 1

# -Werror is considered harmful
sed -i "/-Werror/d" mail/pom.xml

# add aliases for old maven artifact coordinates
%mvn_alias com.sun.mail:mailapi \
    javax.mail:mailapi
%mvn_alias com.sun.mail:jakarta.mail \
    com.sun.mail:javax.mail \
    javax.mail:mail \
    org.eclipse.jetty.orbit:javax.mail.glassfish
%mvn_alias jakarta.mail:jakarta.mail-api \
    javax.mail:javax.mail-api

%build
# skip javadoc build for compat package
# skip tests due to lack of support for modular projects
# https://bugzilla.redhat.com/show_bug.cgi?id=2033020
# define the variable ${main.basedir} to avoid using directory-maven-plugin
%mvn_build -j -f -- -Dmain.basedir=${PWD}

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
%autochangelog
