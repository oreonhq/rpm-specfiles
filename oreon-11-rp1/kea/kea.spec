%global source10_hash 48eb719545eb32d4889ae1b7ae6e395b257f57e653ac335c6af1445e10cdc05f
%global source3_hash b48cebfc751d86778169820f903e262345286922da5353b9b2fe900805d7d764
%global source1_hash f732a6c1c219fb90a230eb0865e71a7b0b271a1be8f310495ee350aca7269872
%global source0_hash 14bf695d37b65b9b1bf550fea5d0adaf9806c50e5419ef2a176a4b8e9aade3df
%global source2_hash bf79d401b6f1b507713615ad49ecfdd372ac715d426b5fc0f42ce2dcef1f9960
Name:           kea
Version:        3.2.0
Release:        1%{?dist}
Summary:        DHCPv4, DHCPv6 and DDNS server from ISC
License:        MPL-2.0 AND BSL-1.0
URL:            http://kea.isc.org
%bcond_with sysrepo
%bcond_with tests
%global keama_version 4.5.0
%global bind_version 9.11.36
%global upstream_name kea
%define upstream_name_compat() \
%if "%{name}" != "%{upstream_name}" \
Provides: %1 = %{version}-%{release} \
Conflicts: %1 \
%endif
Source0:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz
Source1:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz.asc
Source2:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz
Source3:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz.asc
Source10:       https://www.isc.org/docs/isc-keyblock.asc
Source11:        kea-dhcp4.service
Source12:        kea-dhcp6.service
Source13:        kea-dhcp-ddns.service
Source14:        kea-ctrl-agent.service
Source15:        systemd-tmpfiles.conf
Source16:        systemd-sysusers.conf
Patch1:         kea-sd-daemon.patch
%if 0%{?fedora} || (0%{?oreon} >= 11)
%endif
%if 0%{?fedora} || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%else
%endif
%if %{with sysrepo}
%endif
%if %{with tests}
%ifarch %{valgrind_arches}
%endif
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%upstream_name_compat %{upstream_name}
Requires: coreutils util-linux
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gpgverify
BuildRequires:  gtest-devel
BuildRequires:  krb5-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  log4cplus-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
DHCP implementation from Internet Systems Consortium, Inc. that features fully
functional DHCPv4, DHCPv6 and Dynamic DNS servers.
Both DHCP servers fully support server discovery, address assignment, renewal,
rebinding and release. The DHCPv6 server supports prefix delegation. Both
servers support DNS Update mechanism, using stand-alone DDNS daemon.

%package doc
Summary: Documentation for Kea DHCP server
BuildArch: noarch
%description doc
Documentation and example configuration for Kea DHCP server.

%package devel
Summary: Development headers and libraries for Kea DHCP server
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: boost-devel
Requires: openssl-devel
Requires: pkgconfig
%description devel
Header files and API documentation.

%package hooks
Summary: Hooks libraries for kea
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description hooks
Hooking mechanism allow Kea to load one or more dynamically-linked libraries
(known as "hooks libraries") and, at various points in its processing
("hook points"), call functions in them.  Those functions perform whatever
custom processing is required.

%package libs
Summary: Shared libraries used by Kea DHCP server
%upstream_name_compat %{upstream_name}-libs
%description libs
This package contains shared libraries used by Kea DHCP server.

%package keama
Summary: Experimental migration assistant for Kea
Provides: bundled(bind-libs) = %{bind_version}
%description keama
The KEA Migration Assistant is an experimental tool which helps to translate
ISC DHCP configurations to Kea.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{S:10}' --signature='%{S:1}' --data='%{S:0}'
%{gpgverify} --keyring='%{S:10}' --signature='%{S:3}' --data='%{S:2}'

%autosetup -T -b2 -N -n keama-%{keama_version}
%autosetup -p1 -n kea-%{version}

%build

export KEA_PKG_TYPE_IN_CONFIGURE="rpm"
%meson \
    --install-umask 0022 \
%if %{with sysrepo}
    -D netconf=enabled \
%else
    -D netconf=disabled \
%endif
%if %{with tests}
    -D tests=enabled \
%else
    -D tests=disabled \
%endif
    -D crypto=openssl \
    -D krb5=enabled \
    -D mysql=enabled \
    -D postgresql=enabled \
    -D systemd=enabled
%meson_build
%meson_build doc
pushd ../keama-%{keama_version}
tar -C bind/ -zxvf bind/bind.tar.gz
pushd bind/bind-%{bind_version}/
autoreconf --verbose --force --install
popd
autoreconf --verbose --force --install
%configure \
    --disable-dependency-tracking \
    --disable-silent-rules
%make_build
popd
%if %{with tests}
%check

%meson_test
%endif
%install
%meson_install
pushd ../keama-%{keama_version}
%make_install
popd
rm %{buildroot}/%{_libdir}/libdhcp.a
rm -rf %{buildroot}/%{_includedir}/omapip/
rm -rf %{buildroot}%{_mandir}/man5/
rm %{buildroot}%{_sysconfdir}/kea/keactrl.conf
rm %{buildroot}%{_sbindir}/keactrl 
rm %{buildroot}%{_mandir}/man8/keactrl.8*
%if %{without sysrepo}
rm %{buildroot}%{_mandir}/man8/kea-netconf.8
%endif
rm %{buildroot}%{_pkgdocdir}/COPYING
rm -rf %{buildroot}/usr/share/kea/meson-info/
install -m 0640 /dev/null %{buildroot}%{_sysconfdir}/kea/kea-api-password
install -Dpm 0644 %{S:11} %{buildroot}%{_unitdir}/kea-dhcp4.service
install -Dpm 0644 %{S:12} %{buildroot}%{_unitdir}/kea-dhcp6.service
install -Dpm 0644 %{S:13} %{buildroot}%{_unitdir}/kea-dhcp-ddns.service
install -Dpm 0644 %{S:14} %{buildroot}%{_unitdir}/kea-ctrl-agent.service
mkdir -p %{buildroot}%{_sharedstatedir}/kea/
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases4.csv
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases6.csv
install -Dpm 0644 %{S:16} %{buildroot}%{_sysusersdir}/kea.conf
install -Dpm 0644 %{S:15} %{buildroot}%{_tmpfilesdir}/kea.conf
mkdir -p %{buildroot}%{_rundir}
install -dm 0750 %{buildroot}%{_rundir}/kea/
mkdir -p %{buildroot}%{_localstatedir}/log
install -dm 0750 %{buildroot}%{_localstatedir}/log/kea/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

if [[ ! -s %{_sysconfdir}/kea/kea-api-password && -n `grep '"password-file": "kea-api-password"' %{_sysconfdir}/kea/kea-ctrl-agent.conf` ]]; then
    (umask 0027; head -c 32 /dev/urandom | base64 > %{_sysconfdir}/kea/kea-api-password)
    chown root:kea %{_sysconfdir}/kea/kea-api-password
fi
%systemd_post kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service
%preun

%systemd_preun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service
%postun

%systemd_postun_with_restart kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n kea-doc -f %{oreon_filedir}/kea-doc.list
%files -n kea-devel -f %{oreon_filedir}/kea-devel.list
%files -n kea-hooks -f %{oreon_filedir}/kea-hooks.list
%files -n kea-libs -f %{oreon_filedir}/kea-libs.list
%files -n kea-keama -f %{oreon_filedir}/kea-keama.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.3-1
- Import
