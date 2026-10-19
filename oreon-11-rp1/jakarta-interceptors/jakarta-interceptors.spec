%global source0_hash 7f4ddfb21bdaa525183feba849bad537a884b27753ca13b24604100830f24811
%global srcname interceptor-api
Name:           jakarta-interceptors
Version:        2.2.0
Release:        1%{?dist}
Summary:        Jakarta Interceptors
License:        EPL-2.0 OR LicenseRef-Callaway-GPLv2-with-exceptions
%global upstream_version %{version}-RELEASE
URL:            https://github.com/eclipse-ee4j/interceptor-api
Source0:        https://github.com/eclipse-ee4j/%{srcname}/archive/%{upstream_version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Provides:       geronimo-interceptor = %{version}-%{release}
Obsoletes:      geronimo-interceptor < 1.0.1-25
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
# /oreon:deps
%description
Jakarta Interceptors defines a means of interposing on business method
invocations and specific events—such as lifecycle events and timeout
events—that occur on instances of Jakarta EE components and other
managed classes.

%package javadoc
Summary:        Javadoc for %{name}
Provides:       geronimo-interceptor-javadoc = %{version}-%{release}
Obsoletes:      geronimo-interceptor-javadoc < 1.0.1-25
%description javadoc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{upstream_version} -p1

# remove unnecessary dependencies on parent POM
%pom_remove_parent . api

# do not install useless parent POM
%mvn_package :interceptor-api-parent __noinstall

# do not build specification documentation
%pom_disable_module spec

# remove unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin api .
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# disable spec verification (fails because spec-version-maven-plugin is too old)
%pom_xpath_remove 'pom:goal[text()="check-module"]' api

# provide javax.interceptor packages in addition to jakarta.interceptor
cp -pr api/src/main/java/jakarta api/src/main/java/javax
sed -i -e 's/jakarta\./javax./g' $(find api/src/main/java/javax -name *.java)

# add compatibility alias for old maven artifact coordinates
%mvn_alias :jakarta.interceptor-api \
    org.apache.geronimo.specs:geronimo-interceptor_1.1_spec \
    org.apache.geronimo.specs:geronimo-interceptor_3.0_spec

# add compatibility symlink for old classpath
%mvn_file : %{name}/jakarta.interceptor-api geronimo-interceptor

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jakarta-interceptors-javadoc -f %{oreon_filedir}/jakarta-interceptors-javadoc.list

%changelog

%autochangelog
