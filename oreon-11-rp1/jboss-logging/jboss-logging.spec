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
# oreon url source checksums begin
%global source0_sha256 1ad3268671b520a23bb99569f1c0ab903ba333bedbcad776ffa698a374475d39
%global source0_file jboss-logging-3.6.0.Final.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jboss-logging-3.6.0.Final.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1ad3268671b520a23bb99569f1c0ab903ba333bedbcad776ffa698a374475d39" || { echo "oreon: Source0 SHA256 mismatch for jboss-logging-3.6.0.Final.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
