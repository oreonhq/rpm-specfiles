%global source0_hash 324dfb37810ec7fbcf5e762cf6ad4fe340a8502f86477483ea38898b5376c95d

%global  fastnetmon_attackdir      %{_localstatedir}/log/fastnetmon_attacks
%global  fastnetmon_user           fastnetmon
%global  fastnetmon_group          %{fastnetmon_user}
%global  fastnetmon_config_path    %{_sysconfdir}/fastnetmon.conf

# We use commit version as we're still in progress of testing FastNetMon on Fedora.
# We're planning to cut next stable release in next few weeks
%global  commit0 420e7b873253fdc1b52b517d9c28db39bf384427
%global  shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global  date 20220528

Name:              fastnetmon
Version:           1.2.1
Release:           32.%{date}git%{shortcommit0}%{?dist}

Summary:           DDoS detection tool with sFlow, Netflow, IPFIX and port mirror support
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:           GPL-2.0-only
URL:               https://fastnetmon.com

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:       %{ix86}
%endif

Source0:           https://github.com/pavel-odintsov/fastnetmon/archive/%{commit0}.tar.gz
Source1:           fastnetmon.sysusers
# https://github.com/pavel-odintsov/fastnetmon/pull/968
# Adding missing header for g++13
Patch0:            fastnetmon-pr968-g++13-header.patch
# Boost migration patch by Marek Zarychta. Closes #1027
# https://github.com/pavel-odintsov/fastnetmon/commit/f02063204d2b07a525d70e502571b31514653604
#
# Backported to 420e7b8
#
# Fixes:
#
# Add support for Boost 1.87.0 (Boost.Asio removals)
# https://github.com/pavel-odintsov/fastnetmon/issues/1027
#
# fastnetmon: FTBFS in Fedora Rawhide/F44 with Boost 1.90
# https://bugzilla.redhat.com/show_bug.cgi?id=2429533
Patch1:            0001-Boost-migration-patch-by-Marek-Zarychta.-Closes-1027.patch

BuildRequires:     make
BuildRequires:     gcc
BuildRequires:     gcc-c++
BuildRequires:     boost-devel
BuildRequires:     log4cpp-devel
BuildRequires:     ncurses-devel
BuildRequires:     boost-thread
BuildRequires:     boost-regex
BuildRequires:     libpcap-devel
BuildRequires:     gpm-devel
BuildRequires:     cmake
BuildRequires:     capnproto-devel
BuildRequires:     capnproto
BuildRequires:     grpc-devel
BuildRequires:     grpc-cpp
BuildRequires:     abseil-cpp-devel
BuildRequires:     grpc-plugins
BuildRequires:     mongo-c-driver-devel
BuildRequires:     json-c-devel
BuildRequires:     systemd
BuildRequires:     systemd-rpm-macros

Requires(pre):     shadow-utils

%{?systemd_requires}

%description
DDoS detection tool with sFlow, Netflow, IPFIX and port mirror support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit0} -p1

%build
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/H3OOWA43BGEBTSM2GRBYDN3SLUTETFL5/
CXXFLAGS="${CXXFLAGS} -DOPENSSL_NO_ENGINE"

%cmake -DENABLE_CUSTOM_BOOST_BUILD=FALSE -DDO_NOT_USE_SYSTEM_LIBRARIES_FOR_BUILD=FALSE -DCMAKE_SKIP_BUILD_RPATH=TRUE -DLINK_WITH_ABSL=TRUE -S src

%cmake_build

%install
# install systemd unit file
install -p -D -m 0644 src/packaging/fedora/fastnetmon.service %{buildroot}%{_unitdir}/fastnetmon.service

# install daemon binary
install -p -D -m 0755 %__cmake_builddir/fastnetmon %{buildroot}%{_sbindir}/fastnetmon

# install client binary 
install -p -D -m 0755 %__cmake_builddir/fastnetmon_client %{buildroot}%{_bindir}/fastnetmon_client

# install api client binary
install -p -D -m 0755 %__cmake_builddir/fastnetmon_api_client %{buildroot}%{_bindir}/fastnetmon_api_client

# install config
install -p -D -m 0644 src/fastnetmon.conf %{buildroot}%{fastnetmon_config_path}

# Create log folder
install -p -d -m 0700 %{buildroot}%{fastnetmon_attackdir}

# Create sysuser manifest to create dynamic user for us
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/fastnetmon.conf

%pre
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post fastnetmon.service

%preun
%systemd_preun fastnetmon.service

%postun
%systemd_postun_with_restart fastnetmon.service 

%files

%{_unitdir}/fastnetmon.service

%{_sysusersdir}/fastnetmon.conf

# Binary daemon
%{_sbindir}/fastnetmon
%{_bindir}/fastnetmon_client
%{_bindir}/fastnetmon_api_client

%config(noreplace) %{fastnetmon_config_path}
%attr(700,%{fastnetmon_user},%{fastnetmon_group}) %dir %{fastnetmon_attackdir}

%license LICENSE
%doc README.md SECURITY.md THANKS.md

%changelog
%autochangelog
