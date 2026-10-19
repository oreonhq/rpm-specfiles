%global source0_hash 64286bbb4129099491f3923a5d02ad97e4597a85134264edaacfaefb5f84ec98
%undefine __cmake_in_source_build
Name:		xrootd-s3-http
Version:	0.6.5
Release:        1%{?dist}
Summary:        S3/HTTP/Globus filesystem plugins for XRootD
License:	Apache-2.0
URL:		https://github.com/PelicanPlatform/%{name}
Source0:        https://github.com/PelicanPlatform/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Requires:	xrootd-server
# oreon:deps
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  hostname
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  procps
BuildRequires:  tinyxml2-devel
BuildRequires:  xrootd-server
BuildRequires:  xrootd-server-devel
# /oreon:deps
%description
These filesystem plugins for XRootD allow you to serve objects from S3
and HTTP backends through an XRootD server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Drop json version requirement for EPEL 8
sed 's!nlohmann_json 3.11.2 QUIET!nlohmann_json QUIET!' -i CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DXROOTD_EXTERNAL_TINYXML2:BOOL=ON \
       -DXROOTD_PLUGINS_EXTERNAL_GTEST:BOOL=ON \
       -DENABLE_TESTS:BOOL=ON \
       -DEXE_BIN:PATH=/bin/true
%cmake_build
%check

%ctest -- -E 's3-unit'
%install
%cmake_install
rm %{buildroot}%{_libdir}/libXrdPelicanHttpCore.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
