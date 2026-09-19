%global source0_hash e3a1a3e203c0f8cb6fe4dffbc0c7436deda8c85c7f90087f2df5267589200607

Name:		voms-api-java
Version:	3.3.7
Release:	2%{?dist}
Summary:	Virtual Organization Membership Service Java API

License:	Apache-2.0
URL:		https://github.com/italiangrid/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#		Helper scripts for generating test certificates
Source1:	https://baltig.infn.it/mw-devel/helper-scripts/-/archive/master/helper-scripts-master.tar.gz
#		Disable tests requiring non-local network
Patch0:		%{name}-test.patch

BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch

%if %{?fedora}%{!?fedora:0} >= 43
BuildRequires:	maven-local-openjdk25
%else
BuildRequires:	maven-local
%endif
BuildRequires:	mvn(eu.eu-emi.security:canl) >= 2.8.3
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.hamcrest:hamcrest-library)
BuildRequires:	mvn(org.mockito:mockito-core)
BuildRequires:	faketime
BuildRequires:	openssl
Requires:	mvn(eu.eu-emi.security:canl) >= 2.8.3

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides a java client API for VOMS.

%package javadoc
Summary:	Virtual Organization Membership Service Java API Documentation

%description javadoc
Virtual Organization Membership Service (VOMS) Java API Documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1
%patch -P0 -p1

# Remove unused dependency
%pom_remove_dep net.jcip:jcip-annotations

# F33+ and EPEL8+ doesn't use the maven-javadoc-plugin to generate javadoc
# Remove maven-javadoc-plugin configuration to avoid build failure
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

%if %{?rhel}%{!?rhel:0} == 9
# Modify bouncycastle dependencies for RHEL 9
%pom_change_dep org.bouncycastle:bcprov-jdk18on org.bouncycastle:bcprov-jdk15on
%pom_change_dep org.bouncycastle:bcpkix-jdk18on org.bouncycastle:bcpkix-jdk15on
%endif

# Generate test certificates
export PATH=$PWD/helper-scripts-master/x509-scripts/scripts:$PATH
pushd src/test/resources
./setup.sh
popd

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
