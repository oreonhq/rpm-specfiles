%global source0_hash be4521fdac10eddc9ba046399149064ca23d4630b7987301abdee9e0044b8d5c
%global __cmake_in_source_build 1
%bcond_with     pfring
%bcond_without  debug
Name:           zmap
Version:        4.4.0
Release:        1%{?dist}
Summary:        Network scanner for Internet-wide network studies
License:        Apache-2.0
URL:            https://zmap.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         zmap-bin-sbin-merge.patch
# oreon:deps
BuildRequires:  Judy-devel
BuildRequires:  byacc
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gengetopt
BuildRequires:  gmp-devel
BuildRequires:  json-c-devel
BuildRequires:  libpcap-devel
BuildRequires:  libunistring-devel
# /oreon:deps
%description
ZMap is an open-source network scanner that enables researchers to easily 
perform Internet-wide network studies. With a single machine and a well 
provisioned network uplink, ZMap is capable of performing a complete scan of 
the IPv4 address space in under 45 minutes, approaching the theoretical limit
of gigabit Ethernet.

ZMap can be used to study protocol adoption over time, monitor service 
availability, and help us better understand large systems distributed across 
the Internet.

========== WARNING ==========
While ZMap is a powerful tool for researchers, please keep in mind that by 
running ZMap, you are potentially scanning the ENTIRE IPv4 address space and 
some users may not appreciate your scanning. We encourage ZMap users to 
respect requests to stop scanning and to exclude these networks from ongoing 
scanning.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DENABLE_DEVELOPMENT=OFF           \
       -DENABLE_LOG_TRACE=OFF             \
       -DWITH_JSON=ON                     \
       -DWITH_PFRING=OFF
%cmake_build
chmod 644 -v examples/udp-probes/*
find ./examples/ -type f -exec sed -i 's/\r$//' {} \+
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
