%global source0_hash 2a9dad2b26e002d4295505ddc5389b6dd8af25dfff5906f814d5c94f65def085
%global srcname jsp-api
Name:           jakarta-server-pages
Version:        2.3.6
Release:        1%{?dist}
Summary:        Jakarta Server Pages (JSP)
License:        (EPL-2.0 OR LicenseRef-Callaway-GPLv2-with-exceptions) AND Apache-2.0
%global upstream_version IMPL-%{version}-RELEASE
URL:            https://github.com/eclipse-ee4j/jsp-api
Source0:        https://github.com/eclipse-ee4j/%{srcname}/archive/%{upstream_version}/%{srcname}-%{upstream_version}.tar.gz
Patch1:         0001-enable-support-for-JDTJavaCompiler-and-AntJavaCompil.patch
Patch2:         0002-Port-to-latest-version-of-Servlet-API.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Provides:       glassfish-jsp = %{version}-%{release}
Obsoletes:      glassfish-jsp < 2.3.4-9
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.el:jakarta.el-api)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.glassfish:javax.el)
# /oreon:deps
%description
Jakarta Server Pages provides a container-independent implementation of
the JSP API.

%package api
Summary:        Jakarta Server Pages (JSP) API
Provides:       glassfish-jsp-api = %{version}-%{release}
Obsoletes:      glassfish-jsp-api < 2.3.3-6
%description api
Jakarta Server Pages provides a container-independent implementation of
the JSP API. This package contains the API only.

%package javadoc
Summary:        Javadoc for %{name}
Provides:       glassfish-jsp-javadoc = %{version}-%{release}
Obsoletes:      glassfish-jsp-javadoc < 2.3.4-9
Provides:       glassfish-jsp-api-javadoc = %{version}-%{release}
Obsoletes:      glassfish-jsp-api-javadoc < 2.3.3-6
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{upstream_version} -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent . api impl

# do not build specification documentation
%pom_disable_module spec

# do not install useless parent POM
%mvn_package org.eclipse.ee4j.jsp:jsp-parent __noinstall

# reset jsp-api version from 2.3.7-SNAPSHOT to 2.3.6 (no code changes)
sed -i "s/2\.3\.7-SNAPSHOT/2.3.6/" api/pom.xml
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" api
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" api

# ant and ecj should be optional OSGi requirements
%pom_xpath_inject "pom:dependency[pom:groupId='org.apache.ant']" "<optional>true</optional>" impl
%pom_xpath_inject "pom:dependency[pom:groupId='org.eclipse.jdt']" "<optional>true</optional>" impl
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" impl
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" impl

# this source file is excluded by maven-compiler-plugin configuration;
# remove it entirely to fix building javadocs
rm impl/src/main/java/org/apache/jasper/runtime/PerThreadTagHandlerPool.java

# add aliases for old maven artifact coordinates
%mvn_alias org.glassfish.web:jakarta.servlet.jsp \
    org.eclipse.jetty.orbit:org.apache.jasper.glassfish \
    org.glassfish.web:javax.servlet.jsp

%mvn_alias jakarta.servlet.jsp:jakarta.servlet.jsp-api \
    javax.servlet.jsp:javax.servlet.jsp-api \
    javax.servlet.jsp:jsp-api \
    javax.servlet:jsp-api

# add compat symlinks for the old classpaths
%mvn_file :jakarta.servlet.jsp     %{name}/jakarta.servlet.jsp     glassfish-jsp     javax.servlet.jsp
%mvn_file :jakarta.servlet.jsp-api %{name}/jakarta.servlet.jsp-api glassfish-jsp-api

%build

%mvn_build -s
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jakarta-server-pages-api -f %{oreon_filedir}/jakarta-server-pages-api.list
%files -n jakarta-server-pages-javadoc -f %{oreon_filedir}/jakarta-server-pages-javadoc.list

%changelog

%autochangelog
