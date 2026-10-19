%global source0_hash 6b3c79fbfb837333b279614a97dc5fc70fe13fb163b0b7c3508789a30fef1536
Name:    buildbox
Version: 1.4.27
Release:        1%{?dist}
Summary:        Building blocks to execute actions conforming to the Remote Execution API
License: Apache-2.0
URL:     https://buildgrid.gitlab.io/buildbox/buildbox-home/
Source0:        https://gitlab.com/BuildGrid/buildbox/buildbox/-/archive/%{version}/buildbox-%{version}.tar.bz2
ExcludeArch: %{ix86}
Requires: bubblewrap
# oreon:deps
BuildRequires:  attr
BuildRequires:  cmake
BuildRequires:  fuse3
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  net-tools
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gmock_main)
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(uuid)
# /oreon:deps
%description
buildbox provides a set of building blocks to execute actions conforming to the
Remote Execution API, also supporting the Remote Worker API.

%prep
%oreon_prep
%build

%cmake -GNinja
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
