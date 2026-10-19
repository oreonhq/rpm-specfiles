%global source0_hash 034d241f4935e675f1ea56a2d264e4f94b17049d22eabea7f18237f21e29681a
Name: rshim
Version: 2.9.1
Release:        1%{?dist}
Summary:        User-space driver for Mellanox BlueField SoC
License: (GPL-2.0-only OR BSD-3-Clause) AND MIT
URL: https://github.com/mellanox/rshim-user-space
Source0:        https://github.com/Mellanox/rshim-user-space/archive/refs/tags/%{name}-%{version}.tar.gz#/rshim-%{version}.tar.gz
Requires: kmod(cuse.ko)
Suggests: kernel-modules-extra
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This is the user-space driver to access the BlueField SoC via the rshim
interface. It provides ways to push boot stream, debug the target or login
via the virtual console or network interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rshim-user-space-%{name}-%{version}
%oreon_prep
%build

./bootstrap.sh
%configure
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_prefix}/lib/systemd/network
mv %{buildroot}/etc/systemd/network/10-tmfifo-net.link \
   %{buildroot}%{_prefix}/lib/systemd/network/
%oreon_autofiles main

%post

%systemd_post rshim.service
%preun

%systemd_preun rshim.service
%postun

%systemd_postun_with_restart rshim.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
