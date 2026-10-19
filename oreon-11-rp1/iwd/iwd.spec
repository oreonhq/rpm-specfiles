%global source0_hash d89a5e45c7180170e19be828f9e944a768c593758094fc57a358d0e7c4cb1a49
Name:           iwd
Version:        3.12
Release:        1%{?dist}
Summary:        Wireless daemon for Linux
License:        LGPL-2.1-or-later
URL:            https://iwd.wiki.kernel.org/
Source0:        https://www.kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.xz
Requires:       dbus
Requires:       systemd
Recommends:     wireless-regdb
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ell)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  python3-docutils
BuildRequires:  readline-devel
# /oreon:deps
%description
The daemon and utilities for controlling and configuring the Wi-Fi network
hardware.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure			\
	--enable-external-ell	\
	--enable-sim-hardcoded	\
	--enable-ofono		\
	--enable-wired		\
	--enable-hwsim		\
	--enable-tools		\
	--with-systemd-unitdir=%{_unitdir} \
	--with-systemd-networkdir=%{_systemd_util_dir}/network \
	--with-systemd-modloaddir=%{_modulesloaddir}
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_sharedstatedir}/iwd
mkdir -p %{buildroot}%{_sharedstatedir}/ead
rm %{buildroot}/usr/lib/systemd/network/80-iwd.link
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
