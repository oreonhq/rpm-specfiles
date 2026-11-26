# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1a4eb36ca65cc3b1b936566d677a9786e13c11cd5806e951ac55f3f5ce3984af

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xorg-server
Version: 21.1.24
Release: 1%{?dist}
Summary: X server
License: MIT
URL: https://www.x.org
Source0: https://www.x.org/pub/individual/xserver/xorg-server-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig
BuildRequires: xorgproto
BuildRequires: xtrans
BuildRequires: pixman-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXfont2-devel
BuildRequires: libxkbfile-devel
BuildRequires: xkbcomp
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: libglvnd-devel
BuildRequires: mesa-libGL-devel

Provides: xorg-x11-server-Xvfb = %{version}-%{release}
Requires: xkbcomp
Requires: xkeyboard-config

%description
Virtual framebuffer X server used to run X11 tests.

%prep
%oreon_sha256
%autosetup -p1 -n xorg-server-%{version}

%build
%meson \
  -Dxorg=false \
  -Dxephyr=false \
  -Dxnest=false \
  -Dxvfb=true \
  -Dglamor=false \
  -Dglx=true \
  -Dudev=false \
  -Dudev_kms=false \
  -Dsystemd_logind=false \
  -Ddri1=false \
  -Ddri2=false \
  -Ddri3=false \
  -Dlinux_acpi=false \
  -Dlinux_apm=false \
  -Dint10=false \
  -Dpciaccess=false \
  -Dhal=false \
  -Ddga=false \
  -Dxselinux=false \
  -Dsecure-rpc=false \
  -Dxf86-input-inputtest=false \
  -Ddefault_font_path=%{_datadir}/fonts
%meson_build

%install
%meson_install
cat > %{buildroot}%{_bindir}/xvfb-run <<'EOF'
#!/bin/sh
args=
while [ $# -gt 0 ]; do
  case "$1" in
    -s) args=$2; shift 2 ;;
    *) break ;;
  esac
done
n=99
while [ -e /tmp/.X${n}-lock ]; do
  n=$((n + 1))
done
Xvfb :$n $args >/dev/null 2>&1 &
pid=$!
i=0
while [ ! -e /tmp/.X${n}-lock ] && [ "$i" -lt 50 ]; do
  i=$((i + 1))
  sleep 0.1
done
DISPLAY=:$n "$@"
rc=$?
kill "$pid" 2>/dev/null
wait "$pid" 2>/dev/null
exit "$rc"
EOF
chmod 0755 %{buildroot}%{_bindir}/xvfb-run

%check
%meson_test

%files
%license COPYING
%{_bindir}/Xvfb
%{_bindir}/xvfb-run
%{_mandir}/man1/Xvfb.1*
%{_mandir}/man1/Xserver.1*

%changelog
%autochangelog
