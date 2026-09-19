%global source0_hash 29196881cfa8cf1b242f62302dad93e4fde59dbfb9f6aa298bdbcf659dd817c5

%global major_version 1
%global minor_version 3
%global patch_version 8

# For handling bump release by rpmdev-bumpspec and mass rebuild
%global baserelease 7
%define _unpackaged_files_terminate_build 0

Name:           credentials-fetcher
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        %{baserelease}%{?dist}
Summary:        credentials-fetcher is a daemon that refreshes tickets or tokens periodically

License:        Apache-2.0
URL:            https://github.com/aws/credentials-fetcher
Source0:        https://github.com/aws/credentials-fetcher/archive/refs/tags/v.%{version}.tar.gz

# fix protobuf detection for modern protobuf
# https://github.com/aws/credentials-fetcher/pull/116
# Cherry-picked to v.1.3.6 and re-created against the released archive
# Patch:          credentials-fetcher-1.3.6-fixprotobuf.patch
# Bump dotnet-sdk to 8.0
#Patch:          credentials-fetcher-1.3.6-fix-dotnet-version.patch
# Disable integ-tests for Fedora, for now
Patch0:         credentials-fetcher-1.3.8-disable-integ-tests-for-Fedora.patch
# Also disable integ-tests for EL targets, for now
Patch1:         credentials-fetcher-1.3.7-no-api-tests-on-el.patch

BuildRequires:  cmake3 make chrpath openldap-clients grpc-devel gcc-c++ glib2-devel jsoncpp-devel
BuildRequires:  openssl-devel zlib-devel protobuf-devel re2-devel krb5-devel systemd-devel
BuildRequires:  systemd-rpm-macros dotnet-sdk-8.0 grpc-plugins

%if 0%{?amzn} >= 2023
BuildRequires:  aws-sdk-cpp-devel aws-sdk-cpp aws-sdk-cpp-static
%endif
 
Requires: bind-utils openldap openldap-clients awscli dotnet-runtime-8.0 jsoncpp

ExclusiveArch: x86_64 aarch64 s390x

# https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/

%description
This daemon creates and refreshes kerberos tickets, these
tickets can be used to launch new containers.
The gMSA feature can be implemented using this daemon.
Kerberos tickets are refreshed when tickets expire
or when a gMSA password changes.
The same method can be used to refresh other types of security tokens.
This spec file is specific to Fedora, use this file to rpmbuild on Fedora.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n credentials-fetcher-v.%{version} -p1
# abseil-cpp LTS 20230125 requires at least C++14; string_view requires C++17:
sed -r -i 's/(std=c\+\+)11/\117/' CMakeLists.txt

%build
# Use the distributions optflags
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# We need to set ENABLE_DEBUGGING or else the binaries get stripped
%cmake3 -DENABLE_DEBUGGING=ON
%cmake_build
%install

%cmake_install
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_removing_rpath
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_rpath_for_internal_libraries

# https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
ls -al %{buildroot}/usr/sbin/credentials-fetcherd
chrpath --delete %{buildroot}/usr/sbin/credentials-fetcherd

# We don't package this krb5.conf
rm -rf %{buildroot}/usr/sbin/krb5.conf

%check
# TBD: Run tests from top-level directory
ctest

%files
/usr/sbin/credentials-fetcherd
%{_unitdir}/credentials-fetcher.service
%license LICENSE
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
%doc CONTRIBUTING.md NOTICE README.md
%attr(0700, -, -) /usr/sbin/credentials_fetcher_utf16_private.exe
%attr(0700, -, -) /usr/sbin/credentials_fetcher_utf16_private.runtimeconfig.json

%changelog
%autochangelog
