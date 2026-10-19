%global source0_hash 40f73bb3facc480effe0e771442a706ff0488edea7a5f2505d4ccb2aa8163108
Name:           tinc
Version:        1.0.36
Release:        17%{?dist}
Summary:        A virtual private network daemon
License:        GPL-2.0-or-later
URL:            http://www.tinc-vpn.org/
Source0:        http://www.tinc-vpn.org/packages/%{name}-%{version}.tar.gz
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  systemd
BuildRequires:  systemd-units
# /oreon:deps
%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --with-systemd=%{_unitdir}
%make_build
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%oreon_autofiles main

%post

%systemd_post %{name}@.service
%preun

%systemd_preun %{name}@.service
%postun

%systemd_postun_with_restart %{name}@.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
