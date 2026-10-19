%global source0_hash 69e390b40a2228964a1d4db85a067065fd4513d26318c858d24b4972f6b73010
%ifarch %{ix86} armv7hl
%global _lto_cflags %{nil}
%endif
Name: pdns-recursor
Version: 5.4.6
Release:        1%{?dist}
Summary:        Modern, advanced and high performance recursing/non authoritative name server
License: GPL-2.0-only
URL: https://powerdns.com
Source0:        https://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2
ExcludeArch: %{arm} %{ix86}
Provides: powerdns-recursor = %{version}-%{release}
%ifarch %{ix86} x86_64 aarch64
%else
%endif
%ifarch ppc64le
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Patch:         serde_yaml.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cargo-rpm-macros
BuildRequires:  curl-devel
BuildRequires:  fstrm-devel
BuildRequires:  gcc-c++
BuildRequires:  hostname
BuildRequires:  libcap-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
PowerDNS Recursor is a non authoritative/recursing DNS server. Use this
package if you need a dns cache for your network.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Create a sysusers.d config file
cat >pdns-recursor.sysusers.conf <<EOF
u pdns-recursor - 'PowerDNS Recursor user' - -
EOF

cd settings/rust

%build

%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --with-libsodium \
    --enable-reproducible \
    --enable-dnstap \
    --enable-dns-over-tls \
%ifarch %{ix86} x86_64 aarch64
    --with-lua=luajit \
%else
    --with-lua \
%endif
    --with-socketdir=%{_rundir}
cd settings/rust
cargo generate-lockfile --offline
%make_build
%install
%make_install
%{__cp} %{buildroot}%{_sysconfdir}/%{name}/recursor.{yml-dist,conf}
install -p -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}/nod
install -p -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}/udr
sed -i \
    -e 's/# setuid=/setuid=pdns-recursor/' \
    -e 's/# setgid=/setgid=pdns-recursor/' \
    -e 's/# security-poll-suffix=secpoll\.powerdns\.com\./security-poll-suffix=/' \
    %{buildroot}%{_sysconfdir}/%{name}/recursor.conf
install -m0644 -D pdns-recursor.sysusers.conf %{buildroot}%{_sysusersdir}/pdns-recursor.conf
%oreon_autofiles main

%post

%systemd_post pdns-recursor.service
%preun

%systemd_preun pdns-recursor.service
%postun

%systemd_postun_with_restart pdns-recursor.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
