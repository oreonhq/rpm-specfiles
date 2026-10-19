%global source0_hash 03aa6dac4ae9f0eb13a69fe4b8102b19b6a414469f4e6e6f6e46a3be7906d1e0
%global _hardened_build 1
Name:           ubridge
Version:        0.9.19
Release:        4%{?dist}
Summary:        Bridge for UDP tunnels, Ethernet, TAP and VMnet interfaces
License:        GPL-3.0-or-later
URL:            https://github.com/GNS3/ubridge
Source0:        https://github.com/GNS3/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Provides: bundled(lxc-libs)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  iniparser-devel
BuildRequires:  libcap
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
# /oreon:deps
%description
uBridge is a simple application to create user-land bridges between various
technologies. Currently bridging between UDP tunnels, Ethernet and TAP
interfaces is supported. Packet capture is also supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make %{?_smp_mflags} SYSTEM_INIPARSER=1 CFLAGS="-DLINUX_RAW $RPM_OPT_FLAGS -lnl-3"
%install
mkdir -p %{buildroot}%{_bindir}
install -p -m4755 %{name} %{buildroot}%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
