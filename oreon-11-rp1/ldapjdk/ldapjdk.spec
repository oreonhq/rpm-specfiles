%global source0_hash none

################################################################################
Name:             ldapjdk
################################################################################

%global           vendor_id dogtag
%global           product_id %{vendor_id}-ldapjdk

# Upstream version number:
%global           major_version 5
%global           minor_version 6
%global           update_version 0

# Downstream release number:
# - development/stabilization (unsupported): 0.<n> where n >= 1
# - GA/update (supported): <n> where n >= 1
%global           release_number 1

# Development phase:
# - development (unsupported): alpha<n> where n >= 1
# - stabilization (unsupported): beta<n> where n >= 1
# - GA/update (supported): <none>
#global           phase alpha1

%undefine         timestamp
%undefine         commit_id

Summary:          LDAP SDK
URL:              https://github.com/dogtagpki/ldap-sdk
License:          MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Version:          %{major_version}.%{minor_version}.%{update_version}
Release:          %{release_number}%{?phase:.}%{?phase}%{?timestamp:.}%{?timestamp}%{?commit_id:.}%{?commit_id}%{?dist}.1

# To create a tarball from a version tag:
# $ git archive \
#     --format=tar.gz \
#     --prefix ldap-sdk-<version>/ \
#     -o ldap-sdk-<version>.tar.gz \
#     <version tag>
Source:        https://github.com/dogtagpki/ldap-sdk/archive/v%{version}%{?phase:-}%{?phase}/ldap-sdk-%{version}%{?phase:-}%{?phase}.tar.gz

# To create a patch for all changes since a version tag:
# $ git format-patch \
#     --stdout \
#     <version tag> \
#     > ldap-sdk-VERSION-RELEASE.patch
# Patch: ldap-sdk-VERSION-RELEASE.patch

BuildArch:        noarch
%if 0%{?java_arches:1}
ExclusiveArch:    %{java_arches} noarch
%endif

################################################################################
# Java
################################################################################

%define java_devel java-25-openjdk-devel
%define java_headless java-25-openjdk-headless
%define java_home %{_jvmdir}/jre-25-openjdk
%define maven_local maven-local-openjdk25

################################################################################
# Build Dependencies
################################################################################

BuildRequires:    ant-openjdk25 
BuildRequires:    %{java_devel}
BuildRequires:    %{maven_local}
BuildRequires:    mvn(org.slf4j:slf4j-api)
BuildRequires:    mvn(org.slf4j:slf4j-jdk14)
BuildRequires:    mvn(org.dogtagpki.jss:jss-base) >= 5.6.0

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

################################################################################
%package -n %{product_id}
################################################################################

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
################################################################################

Summary:          Javadoc for LDAP SDK

Obsoletes:        ldapjdk-javadoc < %{version}-%{release}
Provides:         ldapjdk-javadoc = %{version}-%{release}
Provides:         ldapjdk-javadoc = %{major_version}.%{minor_version}
Provides:         %{product_id}-javadoc = %{major_version}.%{minor_version}

%description -n %{product_id}-javadoc
Javadoc for LDAP SDK

################################################################################
%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
################################################################################

export JAVA_HOME=%{java_home}

%mvn_build

################################################################################
%install
################################################################################

%mvn_install

ln -sf %{name}/ldapjdk.pom %{buildroot}%{_mavenpomdir}/JPP-ldapjdk.pom
ln -sf %{name}/ldapsp.pom %{buildroot}%{_mavenpomdir}/JPP-ldapsp.pom
ln -sf %{name}/ldapfilter.pom %{buildroot}%{_mavenpomdir}/JPP-ldapfilter.pom
ln -sf %{name}/ldapbeans.pom %{buildroot}%{_mavenpomdir}/JPP-ldapbeans.pom
ln -sf %{name}/ldaptools.pom %{buildroot}%{_mavenpomdir}/JPP-ldaptools.pom

################################################################################
%files -n %{product_id} -f .mfiles
################################################################################

%{_mavenpomdir}/JPP-ldapjdk.pom
%{_mavenpomdir}/JPP-ldapsp.pom
%{_mavenpomdir}/JPP-ldapfilter.pom
%{_mavenpomdir}/JPP-ldapbeans.pom
%{_mavenpomdir}/JPP-ldaptools.pom

################################################################################
%files -n %{product_id}-javadoc -f .mfiles-javadoc
################################################################################

################################################################################
%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{major_version}.%{minor_version}.%{update_version}-1
- Prepare for Oreon 11 (RP1)
