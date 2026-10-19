%global source0_hash 29196881cfa8cf1b242f62302dad93e4fde59dbfb9f6aa298bdbcf659dd817c5
%global major_version 1
%global minor_version 3
%global patch_version 8
%global baserelease 7
%define _unpackaged_files_terminate_build 0
Name:           credentials-fetcher
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        1%{?dist}
Summary:        credentials-fetcher is a daemon that refreshes tickets or tokens periodically
License:        Apache-2.0
URL:            https://github.com/aws/credentials-fetcher
Source0:        https://github.com/aws/credentials-fetcher/archive/refs/tags/v.%{version}.tar.gz
Patch0:         credentials-fetcher-1.3.8-disable-integ-tests-for-Fedora.patch
Patch1:         credentials-fetcher-1.3.7-no-api-tests-on-el.patch
%if 0%{?amzn} >= 2023
%endif
Requires: bind-utils openldap openldap-clients awscli dotnet-runtime-8.0 jsoncpp
ExclusiveArch: x86_64 aarch64 s390x
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake3
BuildRequires:  dotnet-sdk-8.0
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  grpc-devel
BuildRequires:  grpc-plugins
BuildRequires:  jsoncpp-devel
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  openldap-clients
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  re2-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
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

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%cmake3 -DENABLE_DEBUGGING=ON
%cmake_build
%install
%cmake_install
ls -al %{buildroot}/usr/sbin/credentials-fetcherd
chrpath --delete %{buildroot}/usr/sbin/credentials-fetcherd
rm -rf %{buildroot}/usr/sbin/krb5.conf
%oreon_autofiles main

%check

ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
