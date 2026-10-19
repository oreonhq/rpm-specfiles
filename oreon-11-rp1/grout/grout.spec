%global source1_hash 52e90d2a531ef3ded0283bd91abc94980698f1f6471fa09658a0217cf6609526
%global source0_hash 4ccceea87ead25dfbee7d44d25283abc61173caf6bae08c9644fa9a6cb6b9ade
%global forgeurl https://github.com/DPDK/grout
%global _lto_cflags %nil
%global dpdk_version 25.11
%if %{defined el9}
%global toolset gcc-toolset-13
%global __meson /usr/bin/scl run %toolset -- /usr/bin/meson
%endif
%if %{defined epel}
%bcond_with frr
%else
%bcond_without frr
%endif
Name: grout
Version: 0.17.1
Summary:        Graph router based on DPDK
License: BSD-3-Clause
Group: System Environment/Daemons
%forgemeta
URL: %{forgeurl}
Release:        1%{?dist}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: https://fast.dpdk.org/rel/dpdk-%{dpdk_version}.tar.xz
%if %{defined toolset}
%else
%endif
%if %{with frr}
%endif
Provides: bundled(dpdk) = %{dpdk_version}
ExcludeArch: %{ix86}
ExcludeArch: s390x
# oreon:deps
BuildRequires:  frr-headers
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcap-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libecoli-devel
BuildRequires:  libevent-devel
BuildRequires:  libmnl-devel
BuildRequires:  libsmartcols-devel
BuildRequires:  libyang-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  numactl-devel
BuildRequires:  pkgconf
BuildRequires:  python3-pyelftools
BuildRequires:  rdma-core-devel
BuildRequires:  scdoc
BuildRequires:  socat
BuildRequires:  systemd
# /oreon:deps
%description
grout stands for Graph Router. In English, "grout" refers to thin mortar that
hardens to fill gaps between tiles.

grout is a DPDK based network processing application. It uses the rte_graph
library for data path processing.

Its main purpose is to simulate a network function or a physical router for
testing/replicating real (usually closed source) VNF/CNF behavior with an
open-source tool.

It comes with a client library to configure it over a standard UNIX socket and
a CLI that uses that library. The CLI can be used as an interactive shell, but
also in scripts one command at a time, or by batches.

%package headers
Summary: Development headers for building %{name} API clients
BuildArch: noarch
%description headers
This package contains the development headers to build %{name} API clients.

%if %{with frr}
%global frr_version %(rpm -q --qf '%%{version}' frr-headers)

%package frr
Summary: FRR zebra dataplane plugin for grout.
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: frr%{?_isa} = %{frr_version}
%description frr
This package contains the FRR zebra dataplane plugin for grout.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%autopatch -p1
%setup -q -T -D -a 1
mv dpdk-* subprojects/dpdk

%build

export GROUT_VERSION=%{version}-%{release}
%meson -Dfrr=%{?with_frr:enabled}%{!?with_frr:disabled} -Ddpdk_static=true -Ddpdk:machine=generic
%meson_build
%install
%meson_install --skip-subprojects
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n grout-headers -f %{oreon_filedir}/grout-headers.list
%files -n grout-frr -f %{oreon_filedir}/grout-frr.list

%changelog

%autochangelog
