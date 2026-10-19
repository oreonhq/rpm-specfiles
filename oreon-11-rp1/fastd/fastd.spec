%global source0_hash 7a3e00b2267c8ee0ed337ec6ef346c3a216e28bc8ce8b4ac947609a4b3d71264
Version:        23
%global forgeurl https://github.com/neocturne/fastd
%forgemeta
Name:           fastd
Release:        1%{?dist}
Summary:        Fast and secure tunneling daemon
License:        BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libcap-devel
BuildRequires:  libmnl-devel
BuildRequires:  libsodium-devel
BuildRequires:  libuecc-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  python3-sphinx
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
fastd is a secure tunneling daemon with some unique features:

 - Very small binary (about 100KB on OpenWRT in the default configuration,
   including all dependencies besides libc)
 - Exchangable crypto methods
 - Transport over UDP for simple usage behind NAT
 - Can run in 1:1 and 1:n scenarios
 - There are no server and client roles defined by the protocol, this is just
   defined by the usage.
 - Only one instance of the daemon is needed on each host to create a full mesh
   If no full mesh is established, a routing protocol is necessary to enable
   hosts that are not connected directly to reach each other

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build

%ifnarch %{ix86} x86_64
  %meson \
    -Dcipher_salsa2012_xmm=disabled \
    -Dmac_ghash_pclmulqdq=disabled \
    -Dcipher_salsa20_xmm=disabled
%else
  %meson
%endif
%meson_build
pushd doc
  make text
popd
%install
%meson_install
install -Dpm 0644 doc/examples/fastd@.service %{buildroot}%{_unitdir}/%{name}@.service
install -Dpm 0644 doc/fastd.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -d %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -dm 0755 %{buildroot}/run/%{name}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
