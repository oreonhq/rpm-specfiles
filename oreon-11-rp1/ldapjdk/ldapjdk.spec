%global source0_hash aaaac8177a0536d60cc3f8f1932957ffdbadae38da09e4d8f6834f6b787f96ad
Name:             ldapjdk
%global           vendor_id dogtag
%global           product_id %{vendor_id}-ldapjdk
%global           major_version 5
%global           minor_version 7
%global           update_version 0
%global           release_number 1
%undefine         timestamp
%undefine         commit_id
Summary:        LDAP SDK
URL:              https://github.com/dogtagpki/ldap-sdk
License:          MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Version:          %{major_version}.%{minor_version}.%{update_version}
Release:        1%{?dist}
Source0:        https://github.com/%{vendor_id}pki/ldap-sdk/archive/refs/tags/v%{version}.tar.gz#/ldap-sdk-%{version}.tar.gz
BuildArch:        noarch
%if 0%{?java_arches:1}
ExclusiveArch:    %{java_arches} noarch
%endif
%define java_devel java-25-openjdk-devel
%define java_headless java-25-openjdk-headless
%define java_home %{_jvmdir}/jre-25-openjdk
%define maven_local maven-local-openjdk25
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-openjdk-devel
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.dogtagpki.jss:jss-base)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)
# /oreon:deps
%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

################################################################################
%package -n %{product_id}
Summary:          LDAP SDK
Requires:         %{java_headless}
Requires:         mvn(org.slf4j:slf4j-api)
Requires:         mvn(org.slf4j:slf4j-jdk14)
Requires:         mvn(org.dogtagpki.jss:jss-base) >= 5.6.0
Obsoletes:        ldapjdk < %{version}-%{release}
Provides:         ldapjdk = %{version}-%{release}
Provides:         ldapjdk = %{major_version}.%{minor_version}
Provides:         %{product_id} = %{major_version}.%{minor_version}
%description -n %{product_id}
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%license docs/ldapjdk/license.txt

################################################################################
%package -n %{product_id}-javadoc
Summary:          Javadoc for LDAP SDK
Obsoletes:        ldapjdk-javadoc < %{version}-%{release}
Provides:         ldapjdk-javadoc = %{version}-%{release}
Provides:         ldapjdk-javadoc = %{major_version}.%{minor_version}
Provides:         %{product_id}-javadoc = %{major_version}.%{minor_version}
%description -n %{product_id}-javadoc
Javadoc for LDAP SDK

################################################################################
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
################################################################################

%autosetup -n ldap-sdk-%{version}%{?phase:-}%{?phase} -p 1

# flatten-maven-plugin is not available in RPM
%pom_remove_plugin org.codehaus.mojo:flatten-maven-plugin

# specify Maven artifact locations
%mvn_file org.dogtagpki.ldap-sdk:ldapjdk     ldapjdk/ldapjdk    ldapjdk
%mvn_file org.dogtagpki.ldap-sdk:ldapbeans   ldapjdk/ldapbeans  ldapbeans
%mvn_file org.dogtagpki.ldap-sdk:ldapfilter  ldapjdk/ldapfilter ldapfilt
%mvn_file org.dogtagpki.ldap-sdk:ldapsp      ldapjdk/ldapsp     ldapsp
%mvn_file org.dogtagpki.ldap-sdk:ldaptools   ldapjdk/ldaptools  ldaptools

################################################################################
%build

export JAVA_HOME=%{java_home}
%mvn_build
%install
%mvn_install
ln -sf %{name}/ldapjdk.pom %{buildroot}%{_mavenpomdir}/JPP-ldapjdk.pom
ln -sf %{name}/ldapsp.pom %{buildroot}%{_mavenpomdir}/JPP-ldapsp.pom
ln -sf %{name}/ldapfilter.pom %{buildroot}%{_mavenpomdir}/JPP-ldapfilter.pom
ln -sf %{name}/ldapbeans.pom %{buildroot}%{_mavenpomdir}/JPP-ldapbeans.pom
ln -sf %{name}/ldaptools.pom %{buildroot}%{_mavenpomdir}/JPP-ldaptools.pom
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dogtag-ldapjdk -f %{oreon_filedir}/dogtag-ldapjdk.list
%files -n dogtag-ldapjdk-javadoc -f %{oreon_filedir}/dogtag-ldapjdk-javadoc.list

%changelog

%autochangelog
