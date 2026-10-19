%global source0_hash 324dfb37810ec7fbcf5e762cf6ad4fe340a8502f86477483ea38898b5376c95d
%global  fastnetmon_attackdir      %{_localstatedir}/log/fastnetmon_attacks
%global  fastnetmon_user           fastnetmon
%global  fastnetmon_group          %{fastnetmon_user}
%global  fastnetmon_config_path    %{_sysconfdir}/fastnetmon.conf
%global  commit0 420e7b873253fdc1b52b517d9c28db39bf384427
%global  shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global  date 20220528
Name:              fastnetmon
Version:           1.2.9
Release:        1%{?dist}
Summary:        DDoS detection tool with sFlow, Netflow, IPFIX and port mirror support
License:           GPL-2.0-only
URL:               https://fastnetmon.com
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:       %{ix86}
%endif
Source0:        https://github.com/pavel-odintsov/%{name}/archive/%{commit0}.tar.gz
Source1:           fastnetmon.sysusers
Patch0:            fastnetmon-pr968-g++13-header.patch
Patch1:            0001-Boost-migration-patch-by-Marek-Zarychta.-Closes-1027.patch
Requires(pre):     shadow-utils
%{?systemd_requires}
# oreon:deps
BuildRequires:  abseil-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  boost-regex
BuildRequires:  boost-thread
BuildRequires:  capnproto
BuildRequires:  capnproto-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gpm-devel
BuildRequires:  grpc-cpp
BuildRequires:  grpc-devel
BuildRequires:  grpc-plugins
BuildRequires:  json-c-devel
BuildRequires:  libpcap-devel
BuildRequires:  log4cpp-devel
BuildRequires:  make
BuildRequires:  mongo-c-driver-devel
BuildRequires:  ncurses-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
DDoS detection tool with sFlow, Netflow, IPFIX and port mirror support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit0} -p1

%build

CXXFLAGS="${CXXFLAGS} -DOPENSSL_NO_ENGINE"
%cmake -DENABLE_CUSTOM_BOOST_BUILD=FALSE -DDO_NOT_USE_SYSTEM_LIBRARIES_FOR_BUILD=FALSE -DCMAKE_SKIP_BUILD_RPATH=TRUE -DLINK_WITH_ABSL=TRUE -S src
%cmake_build
%install
install -p -D -m 0644 src/packaging/fedora/fastnetmon.service %{buildroot}%{_unitdir}/fastnetmon.service
install -p -D -m 0755 %__cmake_builddir/fastnetmon %{buildroot}%{_sbindir}/fastnetmon
install -p -D -m 0755 %__cmake_builddir/fastnetmon_client %{buildroot}%{_bindir}/fastnetmon_client
install -p -D -m 0755 %__cmake_builddir/fastnetmon_api_client %{buildroot}%{_bindir}/fastnetmon_api_client
install -p -D -m 0644 src/fastnetmon.conf %{buildroot}%{fastnetmon_config_path}
install -p -d -m 0700 %{buildroot}%{fastnetmon_attackdir}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/fastnetmon.conf
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE1}
%post

%systemd_post fastnetmon.service
%preun

%systemd_preun fastnetmon.service
%postun

%systemd_postun_with_restart fastnetmon.service 
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
