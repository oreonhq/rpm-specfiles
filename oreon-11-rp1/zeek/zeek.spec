%global source0_hash 1345474b3ea04c700f5421c30c7b81cf570056a16842abba03dfa5e2b6e3ed4e
%if 0%{?el8}
%undefine __cmake_in_source_build
%endif
%global binpac_so_majver 0
%global binpac_soversion 0.61
%global broker_so_majver 4
%global broker_soversion 2.6
Name:           zeek
Version:        9.0.0
Release:        1%{?dist}
Summary:        Powerful framework for network analysis and security monitoring
License:        BSD-3-Clause AND Apache-2.0 AND BSL-1.0 AND ISC AND LGPL-3.0-or-later AND MIT AND NCSA 
URL:            https://zeek.org
Source0:        https://download.zeek.org/%{name}-%{version}.tar.gz
Requires:       zeek-core%{?_isa} = %{version}-%{release}
Requires:       zeek-zkg%{?_isa} = %{version}-%{release}
Provides: bundled(bifcl)
Provides: bundled(binpac)
Provides: bundled(broker)
Provides: bundled(btest)
Provides: bundled(genzam)
Provides: bundled(highwayhash)
Provides: bundled(libkqueue)
Provides: bundled(netcontrol-connectors)
Provides: bundled(package-manager)
Provides: bundled(paraglob)
Provides: bundled(rapidjson)
Provides: bundled(zeek-archiver)
Provides: bundled(zeek-aux)
Provides: bundled(zeekctl)
Provides: bundled(paraglob)
# oreon:deps
BuildRequires:  bind-devel
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperftools-devel
BuildRequires:  jemalloc-devel
BuildRequires:  krb5-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description

%package -n zeek-core
Summary:        The core zeek installation without zeekctl
Requires:   systemd
%description -n zeek-core

%package -n zeek-devel
Summary:        Development files for Zeek
Requires:       libbroker-devel%{?_isa} = %{version}-%{release}
Requires:       libpcap-devel
Requires:       openssl-devel
Requires:       zlib-devel
%description -n zeek-devel
Development files for Zeek; these files are needed when building binary packages
for Zeek.

%package -n libbroker
Summary:        Zeek's Messaging Library
%description -n libbroker
The Broker library implements Zeek's high-level communication patterns.

%package -n libbroker-devel
Summary:        Development files for Zeek's Messaging Library
%description -n libbroker-devel
The Broker library implements Zeek's high-level communication patterns. This
package bundles the library files and headers that were used during the Zeek
build process; they may be needed when building packages for Zeek.

%package -n     libbinpac
Summary:        Zeek binpac library
%description -n libbinpac
Zeek binpac library

%package -n zeekctl
Summary:        Zeek Control
Requires:       python3
Requires:       zeek-core%{?_isa} = %{version}-%{release}
%description -n zeekctl
ZeekControl is Zeek's interactive shell for operating Zeek installations.

%package zkg
Summary:       The Zeek Package Manager
Requires:      python3
Requires:      zeek-core%{?_isa} = %{version}-%{release}
Requires:      zeekctl%{?_isa} = %{version}-%{release}
Requires:      zeek-btest%{?_isa} = %{version}-%{release}
%description zkg
Zkg is Zeek's package manager.

%package btest
Summary:       The BTest test framework
Requires:      python3
Requires:      zeek-btest-data = %{version}-%{release}
%description btest
A Generic Driver for Powerful System Tests

%package btest-data
Summary:       Data for testing
BuildArch:     noarch
%description btest-data
This package contains test data in the form of pcaps that can he helpful when
writing btests.

%pre -n zeek-core

%sysusers_create_compat %{SOURCE1}
%prep

%autosetup -p1
for f in \
  .cmake-format.json \
  .pre-commit-config.yaml \
; do
  find . -name $f -delete
done

%build

%cmake \
  -DZEEK_ETC_INSTALL_DIR=%{_sysconfdir}/%{name} \
  -DZEEK_LOCAL_STATE_DIR=%{_localstatedir}/lib/%{name} \
  -DDISABLE_SPICY=ON \
  -DINSTALL_BTEST=ON \
  -DINSTALL_BTEST_PCAPS=ON \
  -DINSTALL_ZEEK_ARCHIVER=ON \
  -DINSTALL_ZEEK_CLIENT=OFF \
  -DINSTALL_AUX_TOOLS=ON \
  -DINSTALL_ZEEKCTL=ON \
  -DINSTALL_ZKG=ON \
  -DZEEK_SPOOL_DIR=%{_localstatedir}/log/%{name}/spool \
  -DZEEK_LOG_DIR=%{_localstatedir}/log/%{name}/logs
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/zeek/plugins/packages
mkdir -p %{buildroot}%{_datadir}/zeek/site/packages
mkdir -p %{buildroot}%{_localstatedir}/log/zeek/spool
mkdir -p %{buildroot}%{_localstatedir}/log/zeek/logs
rm %{buildroot}%{_datadir}/zeekctl/scripts/zeekctl-config.sh
rm %{buildroot}%{_libdir}/{broctl,libparaglob.a}
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/zeek.conf
for f in \
  %{buildroot}%{_bindir}/{bifcl,binpac,broker-benchmark,capstats,gen-zam,paraglob-test,zeek{,-archiver}} \
  %{buildroot}%{_libdir}/libbinpac.so.%{binpac_soversion} \
  %{buildroot}%{_libdir}/libbroker.so.%{broker_soversion} \
; do
  chrpath --delete ${f}
done
for f in \
  zeek/python/_SubnetTree.so \
  zeek/python/broker/_broker.so \
; do
  chrpath --delete %{buildroot}%{_libdir}/${f}
done
%oreon_autofiles zeek-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles zeek-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libbroker usr/*/lib*.so.*
%oreon_autofiles libbroker-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libbinpac usr/*/lib*.so.*
%oreon_autofiles zeekctl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n zeek-core -f %{oreon_filedir}/zeek-core.list
%files -n zeek-devel -f %{oreon_filedir}/zeek-devel.list
%files -n libbroker -f %{oreon_filedir}/libbroker.list
%files -n libbroker-devel -f %{oreon_filedir}/libbroker-devel.list
%files -n libbinpac -f %{oreon_filedir}/libbinpac.list
%files -n zeekctl -f %{oreon_filedir}/zeekctl.list
%files -n zeek-zkg -f %{oreon_filedir}/zeek-zkg.list
%files -n zeek-btest -f %{oreon_filedir}/zeek-btest.list
%files -n zeek-btest-data -f %{oreon_filedir}/zeek-btest-data.list

%changelog

%autochangelog
