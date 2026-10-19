%global source0_hash 9eb40490e7e927868ecbccfa3c59a0913f01fb004b812617d9aa4d545fd362b0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-jaxrs-api_2.0_spec
Name:          jboss-jaxrs-2.0-api
Version:       1.0.0
Release:        1%{?dist}
Summary:        JAX-RS 2.0: The Java API for RESTful Web Services
License:       (CDDL-1.0 or GPL-2.0-only WITH Classpath-exception-2.0) and Apache-2.0
URL:           https://github.com/jboss/jboss-jaxrs-api_spec
Source0:        https://github.com/jboss/jboss-jaxrs-api_spec/archive/refs/tags/%{oname}-%{version}%{namedreltag}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:        0001-Update-to-use-jakarta.xml.bind-package.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
# /oreon:deps
%description
JSR 339: JAX-RS 2.0: The Java API for RESTful Web Services.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n jboss-jaxrs-api_spec-%{oname}-%{namedversion}
%patch -P1 -p1

# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

# Fix JDK11 build, add missing javax.xml.bind
%pom_add_dep jakarta.xml.bind:jakarta.xml.bind-api

%mvn_file :%{oname} %{name}

# remove after upgrading narayana
%mvn_alias ":jboss-jaxrs-api_2.0_spec" "org.jboss.resteasy:jaxrs-api"

%build

%mvn_build -j
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-33
- Prepare for Oreon 11 (RP1)
