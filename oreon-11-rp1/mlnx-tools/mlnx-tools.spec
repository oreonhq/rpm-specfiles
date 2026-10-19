%global source0_hash e8739813ed75b4ed699b3da82c7227d666e7e1d65d11e26cc425ac41d77e54cc
%global commit 54a51a79b3f161577e7226c30c3a5c01183fb956
Name:           mlnx-tools
Version:        23.07
Release:        1%{?dist}
Summary:        Mellanox userland tools and scripts
License:        CPL-1.0 OR BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/Mellanox/mlnx-tools
Source0:        https://github.com/Mellanox/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{url}/pull/59.patch
Requires:       ethtool
Requires:       iproute
Requires:       pciutils
Requires:       systemd-udev
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
This package provides various Mellanox userland tools and scripts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

# Fix Python shebangs
sed -i "\|#!/usr/bin/python|d" python/Python/dcbnetlink.py
sed -i 's:#!/usr/bin/python:#!/usr/bin/python3:' \
  python/mlnx_dump_parser \
  python/mlnx_perf \
  python/mlnx_qos \
  python/mlx_fs_dump \
  python/tc_wrap.py

sed -i 's:#!/usr/bin/env python:#!/usr/bin/env python3:' \
  python/ib2ib_setup \
  python/mlnx_tune

%build

%install
%make_install SBIN_DIR="%{_sbindir}" SBIN_TDIR="%{_sbindir}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
