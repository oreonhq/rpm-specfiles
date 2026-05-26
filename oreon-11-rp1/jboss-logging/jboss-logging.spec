# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 1ad3268671b520a23bb99569f1c0ab903ba333bedbcad776ffa698a374475d39
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging
Version:          3.6.0
Release:          7%{?dist}
Summary:          The JBoss Logging Framework
License:          Apache-2.0

URL:              https://github.com/jboss-logging/jboss-logging
Source0:        https://github.com/jboss-logging/jboss-logging/archive/3.6.0.Final/jboss-logging-3.6.0.Final.tar.gz
Patch1:           0001-Drop-log4j-dependency.patch
Patch2:           0002-Drop-jboss-logmanager-dependency.patch
Patch3:           0003-Drop-TestCase-that-depend-on-retired-package.patch

BuildArch:        noarch
ExclusiveArch:    %{java_arches} noarch

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:    maven-local
%else
BuildRequires:    maven-local-openjdk25
%endif

BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.junit:junit-bom:pom:)
BuildRequires:    mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:    mvn(org.slf4j:slf4j-api)

%description
This package contains the JBoss Logging Framework.

%prep
%oreon_verify_sources
%autosetup -n %{name}-%{namedversion} -p 1

# Unneeded tasks
%pom_remove_dep ch.qos.logback:logback-classic
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin io.github.dmlloyd.module-info:module-info

%pom_set_parent org.apache.logging:logging-parent

%build
# 1.8 is not valid (8 is the accepted form), but @Deprecated requires >= 9
%mvn_build -j -- -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.0-7
- Prepare for Oreon 11 (RP1)
