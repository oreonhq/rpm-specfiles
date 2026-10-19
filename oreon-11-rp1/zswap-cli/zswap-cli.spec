%global source0_hash f7bdee8b3522c8516e828b0086ad174d58dc2c778a88d9bcbfadddd92f4f6a8f
Name: zswap-cli
Version: 2.0.0
Release:        1%{?dist}
License: MIT
Summary:        Command-line tool to control the zswap options
URL: https://github.com/xvitaly/%{name}
Source0:        https://github.com/xvitaly/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%{?systemd_requires}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-headers
BuildRequires:  kernel-headers
BuildRequires:  ninja-build
BuildRequires:  pandoc
BuildRequires:  systemd
# /oreon:deps
%description
Zswap-cli is a command-line tool to control the zswap kernel module
options.

Zswap is a compressed cache for swap pages. It takes pages that are in the
process of being swapped out to disk and tries to compress them into a
RAM-based memory pool with dynamic allocation.

It trades CPU cycles for a significant performance boost since reading from
a compressed cache is much faster than reading from a swap device.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_MANPAGE:BOOL=ON \
    -DBUILD_SHELL_COMPLETION:BOOL=ON \
    -DSYSTEMD_INTEGRATION:BOOL=ON
%cmake_build
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
