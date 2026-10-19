%global source0_hash 55f81be395929c8fc15ad8c6e8bacff9ff24cbd7e58477b86dd14e70101516bd
Name:           pcm
Version:        202604
Release:        1%{?dist}
Summary:        Intel(r) Performance Counter Monitor
License:        BSD-3-Clause
Url:            https://github.com/intel/pcm
Source0:        https://github.com/intel/pcm/archive/refs/tags/%{version}.tar.gz#/pcm-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd
# /oreon:deps
%description

Intel(r) Performance Counter Monitor (Intel(r) PCM) is an application
programming interface (API) and a set of tools based on the API to
monitor performance and energy metrics of Intel(r) Core(tm), Xeon(r),
Atom(tm) and Xeon Phi(tm) processors. PCM works on Linux, Windows,
Mac OS X, FreeBSD and DragonFlyBSD operating systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pcm-202604
%oreon_prep
%build

%set_build_flags
cat src/CMakeLists.txt | sed 's/CMAKE_INSTALL_SBINDIR/CMAKE_INSTALL_BINDIR/g' > src/CMakeLists.txt.no-sbin
mv src/CMakeLists.txt.no-sbin src/CMakeLists.txt
cat src/pcm-sensor-server.service.in | sed 's/CMAKE_INSTALL_SBINDIR/CMAKE_INSTALL_BINDIR/g' > src/pcm-sensor-server.service.in.no-sbin
mv src/pcm-sensor-server.service.in.no-sbin src/pcm-sensor-server.service.in
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=CUSTOM -DLINUX_SYSTEMD=TRUE -DLINUX_SYSTEMD_UNITDIR=%{_unitdir}/
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}/usr/share/doc/PCM/*.md
rm -rf %{buildroot}/usr/share/doc/PCM/*.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 202604-0
- Import
