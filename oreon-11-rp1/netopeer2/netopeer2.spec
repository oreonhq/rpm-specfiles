%global source0_hash 63d42493752062e7dfb3d3aca9c4157f49298401bdc5cd5166975f2cbc5f6f1b

Name: netopeer2
Version: 2.4.5
Release: 4%{?dist}
Summary: Netopeer2 NETCONF tools suite
Url: https://github.com/CESNET/netopeer2
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source2: netopeer2-server.service
License: BSD-3-Clause

Patch0: 0000-force-remove-modules.patch

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: pkgconfig(libyang) >= 2.2.0
BuildRequires: pkgconfig(libnetconf2) >= 3.5.4
BuildRequires: pkgconfig(sysrepo) >= 2.12.0
BuildRequires: sysrepo-tools
BuildRequires: libcurl-devel
BuildRequires: libssh-devel
BuildRequires: openssl-devel
BuildRequires: systemd-devel
BuildRequires: systemd

%if 0%{?fedora}
# c_rehash needed by CLI
BuildRequires: openssl-perl
%endif

Requires: %{name}-server%{?_isa} = %{version}-%{release}
Requires: %{name}-cli%{?_isa} = %{version}-%{release}

%package server
Summary: netopeer2 NETCONF server

Requires: libyang >= 2.0.231
# needed by script setup.sh (run in post)
Requires: sysrepo-tools
# for provided systemd units
Requires: systemd
# needed for some yang files provided by libnetconf2
Requires: libnetconf2 >= 3.7.10

%package cli
Summary: netopeer2 NETCONF CLI client

%if 0%{?fedora}
Requires: openssl-perl
%endif

%description
Virtual package for both netopeer2-server and netopeer2-cli NETCONF tools.

%description server
netopeer2-server is a server for implementing network configuration management
based on the NETCONF Protocol. This is the second generation, originally
available as the Netopeer project. Netopeer2 is based on the new generation of
the NETCONF and YANG libraries - libyang and libnetconf2. The Netopeer2 server
uses sysrepo as a NETCONF datastore implementation.

Server configuration is stored as "ietf-netconf-server" YANG module
data in sysrepo. They are accessible for "root" and any user beloning to
the group "netconf", which is created if it does not exist.

%description cli
netopeer2-cli is a complex NETCONF command-line client with support for
a single established NETCONF session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
       -DCMAKE_INSTALL_SYSCONFDIR=/etc \
       -DSYSREPO_SETUP=OFF \
       -DPIDFILE_PREFIX=/run \
       -DSERVER_DIR=%{_sharedstatedir}/netopeer2-server
%cmake_build

%install
%cmake_install
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/netopeer2-server.service
mkdir -p -m=700 %{buildroot}%{_sharedstatedir}/netopeer2-server

%pre server
if [ $1 -gt 1 ] ; then
rm -rf /dev/shm/sr_*
rm -rf /dev/shm/srsub_*
fi

%post server
set -e
export NP2_MODULE_DIR=%{_datadir}/yang/modules/netopeer2
export NP2_MODULE_PERMS=600
export NP2_MODULE_OWNER=root
export LN2_MODULE_DIR=%{_datadir}/yang/modules/libnetconf2

%{_datadir}/netopeer2/scripts/setup.sh

%systemd_post netopeer2-server.service

%preun server
set -e
%{_datadir}/netopeer2/scripts/remove.sh

%files
# just a virtual package requiring -cli and -server

%files server
%license LICENSE
%{_sbindir}/netopeer2-server
%{_datadir}/man/man8/netopeer2-server.8.gz
%{_unitdir}/netopeer2-server.service
%{_datadir}/yang/modules/netopeer2/*.yang
%{_datadir}/netopeer2/scripts/*.sh
%{_sysconfdir}/pam.d/netopeer2.conf
%dir %{_datadir}/yang/modules/netopeer2/
%dir %{_datadir}/netopeer2/
%dir %{_sharedstatedir}/netopeer2-server/

%files cli
%license LICENSE
%{_bindir}/netopeer2-cli
%{_datadir}/man/man1/netopeer2-cli.1.gz

%changelog
%autochangelog
