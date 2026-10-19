%global source0_hash 35a6dc0e425a9282c3426d9a3043144011bf0534aed4b73ab62c52aee0af1503
%global source19_hash 9779ccb2c448bb8cc099c3ab7d0fc40e5cd72fcc9627a85853dd646cd360139b
%{?!with_python2:     %global with_python2     0}
%{?!with_python3:     %global with_python3     1}
%{?!with_munin:       %global with_munin       1}
%bcond_without dnstap
%bcond_without systemd
%bcond_without doh
%bcond_without redis
%global forgeurl0 https://github.com/NLnetLabs/unbound
%global downloads https://nlnetlabs.nl/downloads
%global _hardened_build 1
%global upstream_sources 0 1
%global pgp_signed_sources 1
%if 0%{with_python2}
%global python_primary %{__python2}
%endif
%if 0%{with_python3}
%global python_primary %{__python3}
%endif
Summary:        Validating, recursive, and caching DNS(SEC) resolver
Name: unbound
Version: 1.26.1
Release:        1%{?dist}
License: BSD-3-Clause
Url: https://nlnetlabs.nl/projects/unbound/
VCS: git:%{forgeurl0}
Source0:        %{downloads}/%{name}/%{name}-%{version}.tar.gz
Source1: %{downloads}/%{name}/%{name}-%{version}%{?extra_version}.tar.gz.asc
Source2: unbound.service
Source3: unbound.munin
Source4: unbound_munin_
Source5: mkroot.sh
Source7: unbound-keygen.service
Source8: tmpfiles-unbound.conf
Source9: example.com.key
Source10: example.com.conf
Source11: block-example.com.conf
Source13: root.anchor
Source14: unbound.sysconfig
Source15: unbound-anchor.timer
Source16: unbound-munin.README
Source17: unbound-anchor.service
Source19: https://nlnetlabs.nl/downloads/keys/releases-g2.asc#/nlnetlabs2026-g2.asc
Source20: unbound.sysusers
Source21: remote-control.conf
Source23: unbound-as112-networks.conf
Source24: unbound-local-root.conf
Source25: openssl-sha1.conf
Source26: remote-control-include.conf
Source27: fedora-defaults.conf
Source28: module-setup.sh
Source29: tmpfiles-unbound-libs.conf
Patch1:   unbound-fedora-config.patch
Patch6:   unbound-1.26.0-disabled-ipsecmod-fix.patch
Patch7:   unbound-1.26.0-replace-python2-c-api-macros.patch
%if 0%{with_python2}
%endif
%if 0%{with_python3}
%endif
%if %{with dnstap}
%endif
%if %{with systemd}
%endif
%if %{with doh}
%endif
%if %{with redis}
%endif
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%else
%endif
%if %{with ngtcp2}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-anchor%{?_isa} = %{version}-%{release}
Recommends: %{name}-utils%{?_isa} = %{version}-%{release}
Requires: openssl
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  dns-root-data
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  fstrm-devel
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  hiredis-devel
BuildRequires:  libevent-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c-devel
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%package devel
Summary: Development package that includes the unbound header files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}, openssl-devel
Requires: pkgconfig
%description devel
The devel package contains the unbound library and the include files

%package libs
Summary: Libraries used by the unbound server and client applications
Recommends: %{name}-anchor
Requires: dns-root-data >= 2026260100
%if ! 0%{with_python2}
Obsoletes: python2-unbound < 1.9.3
%endif
%description libs
Contains libraries used by the unbound server and client applications.

%package anchor
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Summary: DNSSEC trust anchor maintaining tool
%description anchor
Contains tool maintaining trust anchor using RFC 5011 key rollover algorithm.

%package utils
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Summary: Unbound DNS lookup utilities
%description utils
Contains tools for making DNS queries. Can make queries to DNS servers
also over TLS connection or validate DNSSEC signatures. Similar to
bind-utils.

%if 0%{with_python2}
%package -n python2-unbound
%{?python_provide:%python_provide python2-unbound}
Summary: Python 2 modules and extensions for unbound
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: unbound-python = %{version}-%{release}
Obsoletes: unbound-python < %{version}-%{release}
%description -n python2-unbound
Python 2 modules and extensions for unbound
%endif

%if 0%{with_python3}
%package -n python3-unbound
Summary: Python 3 modules and extensions for unbound
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if ! 0%{with_python2}
Conflicts: python2-unbound < 1.9.3
%endif
%description -n python3-unbound
Python 3 modules and extensions for unbound
%endif

%package dracut
Summary: Unbound dracut module
Requires: dracut%{?_isa}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description dracut
Unbound dracut module allowing use of Unbound for name resolution
in initramfs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source19_hash}" = "none" || { f="%{SOURCE19}"; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source19_hash}" || { echo "oreon: Source19 hash mismatch" >&2; exit 1; }; }
%global pkgname %{name}-%{version}%{?extra_version}

%if 0%{with_python2} && 0%{with_python3}
%global python_primary %{__python3}
%global dir_secondary %{pkgname}_python2
%global python_secondary %{__python2}
%endif

%autosetup -N -n %{pkgname}

# patches go here
%autopatch -p1

%if 0%{with_python2} && 0%{with_python3}
  cp -a . %{dir_secondary}
%endif

%build

%global configure_args --with-libevent --with-pthreads --with-ssl \\\
            --disable-rpath --disable-static \\\
            --enable-relro-now --enable-pie \\\
            --enable-subnet --enable-ipsecmod \\\
            --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf \\\
            --with-share-dir=%{_datadir}/%{name} \\\
            --with-pidfile=%{_rundir}/%{name}/%{name}.pid \\\
            --enable-sha2 --disable-gost --enable-ecdsa \\\
            --with-rootkey-file=%{_sharedstatedir}/%{name}/root.key \\\
            --with-username=unbound \\\
            --enable-linux-ip-local-port-range --enable-system-tls \\\
            --with-dynlibmodule \\\
rm -f config.h.in aclocal.m4 configure ltmain.sh
rm -f {ax_pthread,ax_swig_python}.m4
cp -p %{_datadir}/aclocal/{ax_pthread,ax_swig_python}.m4 .
rm -f util/configparser.{c,h} util/configlexer.c
autoreconf -fiv
%configure  \
%if 0%{?python_primary:1}
            --with-pythonmodule --with-pyunbound PYTHON=%{python_primary} \
%endif
%if %{with dnstap}
            --enable-dnstap \
%endif
%if %{with systemd}
            --enable-systemd \
%endif
%if %{with doh}
            --with-libnghttp2 \
%endif
%if %{with redis}
            --with-libhiredis \
            --enable-cachedb \
%endif
%if %{with ngtcp2}
            --with-libngtcp2 \
%endif
            %{configure_args}
%make_build
%make_build streamtcp
%if 0%{?python_secondary:1}
pushd %{dir_secondary}
%configure  \
            --with-pythonmodule --with-pyunbound PYTHON=%{python_secondary} \
%if %{with dnstap}
            --enable-dnstap \
%endif
%if %{with systemd}
            --enable-systemd \
%endif
%if %{with ngtcp2}
            --with-libngtcp2 \
%endif
            %{configure_args}
%make_build
popd
%endif
gzip --best -k doc/Changelog
%install
install -p -m 0644 %{SOURCE16} .
%if 0%{?python_secondary:1}
pushd %{dir_secondary}
%make_install unbound-event-install
popd
%endif
%make_install unbound-event-install
install -m 0755 streamtcp %{buildroot}%{_sbindir}/unbound-streamtcp
install -p -m 0644 doc/example.conf %{buildroot}%{_sysconfdir}/unbound/unbound.conf
install -d -m 0755 %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/unbound.service
install -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/unbound-keygen.service
install -p -m 0644 %{SOURCE15} %{buildroot}%{_unitdir}/unbound-anchor.timer
install -p -m 0644 %{SOURCE17} %{buildroot}%{_unitdir}/unbound-anchor.service
ln -sr %{buildroot}%{_datadir}/dns-root-data/icannbundle.pem %{buildroot}%{_sysconfdir}/unbound
install -p -m 0644 %{SOURCE14} %{buildroot}%{_sysconfdir}/sysconfig/unbound
install -p -D -m 0644 %{SOURCE20} %{buildroot}%{_sysusersdir}/%{name}.conf
install -p -m 0644 testcode/streamtcp.1 %{buildroot}/%{_mandir}/man1/unbound-streamtcp.1
install -p -D -m 0644 contrib/libunbound.pc %{buildroot}/%{_libdir}/pkgconfig/libunbound.pc
install -d -m 0755 %{buildroot}%{_tmpfilesdir} %{buildroot}%{_sharedstatedir}/unbound
install -p -m 0644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/unbound.conf
install -p -m 0644 %{SOURCE29} %{buildroot}%{_tmpfilesdir}/unbound-libs.conf
sh %{SOURCE5} root.key
install -m 0644 root.key %{buildroot}%{_sysconfdir}/unbound/
ln -sr "%{buildroot}%{_sysconfdir}/unbound/dnssec-root.key" "%{buildroot}%{_sharedstatedir}/unbound/root.key"
ln -sr "%{buildroot}%{_datadir}/dns-root-data/root.key" "%{buildroot}%{_sysconfdir}/unbound/dnssec-root.key"
rm %{buildroot}%{_libdir}/*.la
%if 0%{with_python2}
rm %{buildroot}%{python2_sitearch}/*.la
%endif
%if 0%{with_python3}
rm %{buildroot}%{python3_sitearch}/*.la
%endif
mkdir -p %{buildroot}%{_rundir}/unbound
mkdir -p %{buildroot}%{_sysconfdir}/unbound/{keys.d,conf.d,local.d}
install -p -m 0644 %{SOURCE9} %{buildroot}%{_sysconfdir}/unbound/keys.d/
install -p -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/unbound/conf.d/
install -p -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/unbound/local.d/
install -p -m 0644 %{SOURCE26} %{buildroot}%{_sysconfdir}/unbound/conf.d/remote-control.conf
install -p -m 0644 %{SOURCE25} %{buildroot}%{_sysconfdir}/unbound/openssl-sha1.conf
mkdir -p %{buildroot}%{_datadir}/%{name}/conf.d
install -p -m 0644 %{SOURCE21} %{buildroot}%{_datadir}/%{name}/conf.d/
install -p -m 0644 %{SOURCE23} %{buildroot}%{_datadir}/%{name}/conf.d/
install -p -m 0644 %{SOURCE24} %{buildroot}%{_datadir}/%{name}/conf.d/
install -p -m 0644 %{SOURCE27} %{buildroot}%{_datadir}/%{name}/
echo ".so man8/unbound-control.8" > %{buildroot}/%{_mandir}/man8/unbound-control-setup.8
mkdir -p %{buildroot}%{_prefix}/lib/dracut/modules.d/70unbound
install -p -m 0755 %{SOURCE28} %{buildroot}%{_prefix}/lib/dracut/modules.d/70unbound
%oreon_autofiles python3-unbound usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post unbound.service
%systemd_post unbound-keygen.service
%post anchor

%systemd_post unbound-anchor.service unbound-anchor.timer
if [ "$1" -eq 1 ]; then
    /bin/systemctl start unbound-anchor.timer >/dev/null 2>&1 || :
fi
%preun

%systemd_preun unbound.service
%systemd_preun unbound-keygen.service
%preun anchor

%systemd_preun unbound-anchor.service unbound-anchor.timer
%postun

%systemd_postun_with_restart unbound.service
%systemd_postun unbound-keygen.service
%postun anchor

%systemd_postun_with_restart unbound-anchor.service unbound-anchor.timer
%triggerun -- unbound < 1.23.1-4

if [ "$(stat -c '%%a %%G' %{_sysconfdir}/%{name}/unbound_control.key 2>/dev/null)" = '600 unbound' ]; then
   %{_bindir}/chmod g+r "%{_sysconfdir}/%{name}/unbound_control.key" || :
fi
%check

export OPENSSL_CONF="%{buildroot}%{_sysconfdir}/unbound/openssl-sha1.conf"
make check
%if 0%{?python_secondary:1}
pushd %{dir_secondary}
make check
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n unbound-devel -f %{oreon_filedir}/unbound-devel.list
%files -n unbound-libs -f %{oreon_filedir}/unbound-libs.list
%files -n unbound-anchor -f %{oreon_filedir}/unbound-anchor.list
%files -n unbound-utils -f %{oreon_filedir}/unbound-utils.list
%files -n python3-unbound -f %{oreon_filedir}/python3-unbound.list
%files -n unbound-dracut -f %{oreon_filedir}/unbound-dracut.list

%changelog

%autochangelog
