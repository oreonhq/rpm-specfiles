%global source0_hash ef1fe160ac3ff602ae4029d413b0d530036e352a1e6a427402776c1a7aaf3716
Name:           nbd
Version:        3.27.1
Release:        1%{?dist}
Summary:        Network Block Device user-space tools (TCP version)
License:        GPL-2.0-only
URL:            https://github.com/NetworkBlockDevice/nbd
Source0:        https://github.com/NetworkBlockDevice/nbd/releases/download/nbd-%{version}/nbd-%{version}.tar.xz
Source1:        nbd-server.service
Source2:        nbd-server.sysconfig
%{?systemd_requires}
# oreon:deps
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
Tools for the Linux Kernel's network block device, allowing you to use
remote block devices over a TCP/IP network.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# wait longer for nbd-server to fully start,
# five seconds may not be enough on Fedora building infra
sed -i 's/tv_sec = 5/tv_sec = 30/' tests/run/nbd-tester-client.c

%build

%configure --enable-syslog --enable-lfs
%make_build
%install
%make_install
install -pDm644 systemd/nbd@.service %{buildroot}%{_unitdir}/nbd@.service
mkdir -p %{buildroot}%{_unitdir}/nbd@.service.d
cat > %{buildroot}%{_unitdir}/nbd@.service.d/modprobe.conf <<EOF
[Service]
ExecStartPre=/sbin/modprobe nbd
EOF
install -pDm644 %{S:1} %{buildroot}%{_unitdir}/nbd-server.service
install -pDm644 %{S:2} %{buildroot}%{_sysconfdir}/sysconfig/nbd-server
%oreon_autofiles main

%check

DELAY=10 make check
%post

%systemd_post nbd-server.service
%preun

%systemd_preun nbd-server.service
%postun

%systemd_postun nbd-server.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
