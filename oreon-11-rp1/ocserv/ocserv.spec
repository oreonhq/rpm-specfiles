%global source1_hash 0ce83e81a36a4c1c86216705d5636ed60c516af16147c6b5ea930213a810ad86
%global source0_hash 42ced08958b9576ab134fcb7bdc7f8df5e13214fd147855f99021fedcf0eedbe
Version:	1.5.0
Release:        1%{?dist}
%global _hardened_build 1
%define use_systemd 0
%define have_gpgv2 0
%if 0%{?fedora} >= 28 || 0%{?rhel} > 7 || 0%{?oreon} >= 11
%define use_libwrap 0
%define use_geoip 0
%else
%define use_libwrap 1
%define use_geoip 1
%endif
%define use_local_protobuf 0
Name:		ocserv
Summary:        OpenConnect SSL VPN server
License:	GPL-2.0-or-later AND BSD-3-Clause AND MIT AND CC0-1.0
URL:		https://ocserv.openconnect-vpn.net/
Source0:        https://www.infradead.org/ocserv/download/%{name}-%{version}.tar.xz
Source1:	https://www.infradead.org/ocserv/download/%{name}-%{version}.tar.xz.sig
Source2:	gpgkey-1F42418905D8206AA754CCDC29EE58B996865171.gpg
Source3:	ocserv.conf
Source4:	ocserv.service
Source5:	ocserv-pamd.conf
Source6:	PACKAGE-LICENSING
Source8:	ocserv-genkey
Source9:	ocserv-script
Source10:	gpgkey-56EE7FA9E8173B19FE86268D763712747F343FA7.gpg
Source11:	ocserv.init
%if (0%{?use_local_protobuf} == 0)
%endif
%if %{use_libwrap}
%endif
%if %{use_geoip}
%else
%endif
%if %{use_systemd}
%ifnarch aarch64 %{ix86} %{arm}
%endif
%ifarch x86_64 %{ix86} %{arm} aarch64
%endif
%endif
Recommends:		gnutls-utils
Recommends:		iproute
Recommends:		pam
%if %{use_systemd}
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%endif
Provides:		bundled(gnulib)
Provides:		bundled(bobjenkins-hash) bundled(ccan-container_of) 
Provides:		bundled(ccan-htable) bundled(ccan-list)
Provides:		bundled(ccan-check_type) bundled(ccan-build_assert)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  gnutls-utils
BuildRequires:  gperf
BuildRequires:  ipcalc
BuildRequires:  iproute
BuildRequires:  krb5-devel
BuildRequires:  libev-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  llhttp-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  openconnect
BuildRequires:  pam-devel
BuildRequires:  protobuf-c-devel
BuildRequires:  radcli-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
OpenConnect server (ocserv) is an SSL VPN server. Its purpose is to be a 
secure, small, fast and configurable VPN server. It implements the OpenConnect 
SSL VPN protocol, and has also (currently experimental) compatibility with 
clients using the AnyConnect SSL VPN protocol. The OpenConnect VPN protocol 
uses the standard IETF security protocols such as TLS 1.2, and Datagram TLS 
to provide the secure VPN service. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{have_gpgv2}
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0} || gpgv2 --keyring %{SOURCE10} %{SOURCE1} %{SOURCE0}
%endif

%autosetup -p1

%if (0%{?use_local_protobuf} == 0)
rm -rf src/protobuf/protobuf-c/
touch src/*.proto
%endif
rm -rf src/ccan/talloc
sed -i 's|/etc/ocserv.conf|/etc/ocserv/ocserv.conf|g' src/config.c
sed -i 's/run-as-group = nogroup/run-as-group = nobody/g' tests/data/*.config

# Create a sysusers.d config file
cat >ocserv.sysusers.conf <<EOF
u ocserv - 'ocserv' %{_localstatedir}/lib/ocserv -
EOF

%build

%configure \
        --without-pcl-lib \
%if %{use_systemd}
	--enable-systemd \
%else
	--disable-systemd \
%endif
%if %{use_local_protobuf}
	--without-protobuf \
%endif
%if %{use_libwrap}
	--with-libwrap
%else
	--without-libwrap
%endif
make %{?_smp_mflags}
%pre

mkdir -p %{_sysconfdir}/pki/ocserv/public
mkdir -p -m 700 %{_sysconfdir}/pki/ocserv/private
mkdir -p %{_sysconfdir}/pki/ocserv/cacerts
%check

make check %{?_smp_mflags} VERBOSE=1
%if %{use_systemd}
%post

%systemd_post ocserv.service
%preun

%systemd_preun ocserv.service
%postun

%systemd_postun_with_restart ocserv.service
%endif
%install
rm -rf %{buildroot}
cp -a %{SOURCE6} PACKAGE-LICENSING
mkdir -p %{buildroot}/%{_sysconfdir}/pam.d/
mkdir -p %{buildroot}/%{_sysconfdir}/ocserv/
install -p -m 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/pam.d/ocserv
install -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/ocserv/
mkdir -p %{buildroot}%{_localstatedir}/lib/ocserv/
install -p -m 644 doc/profile.xml %{buildroot}%{_localstatedir}/lib/ocserv/
mkdir -p %{buildroot}/%{_sbindir}
install -p -m 755 %{SOURCE8} %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE9} %{buildroot}/%{_bindir}
%if %{use_systemd}
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}
%else
mkdir -p %{buildroot}/%{_initrddir}
install -D -m 0755 %{SOURCE11} %{buildroot}/%{_initrddir}/%{name}
%endif
%make_install
install -m0644 -D ocserv.sysusers.conf %{buildroot}%{_sysusersdir}/ocserv.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
