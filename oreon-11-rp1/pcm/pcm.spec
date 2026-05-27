%global source0_hash 55f81be395929c8fc15ad8c6e8bacff9ff24cbd7e58477b86dd14e70101516bd

Name:           pcm
Version:        202604
Release:        0%{?dist}
Summary:        Intel(r) Performance Counter Monitor
License:        BSD-3-Clause
Url:            https://github.com/intel/pcm
Source0:        https://github.com/intel/pcm/archive/202604/pcm-202604.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  systemd
BuildRequires:  openssl-devel
ExclusiveArch:  %{ix86} x86_64

%description

Intel(r) Performance Counter Monitor (Intel(r) PCM) is an application
programming interface (API) and a set of tools based on the API to
monitor performance and energy metrics of Intel(r) Core(tm), Xeon(r),
Atom(tm) and Xeon Phi(tm) processors. PCM works on Linux, Windows,
Mac OS X, FreeBSD and DragonFlyBSD operating systems.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%set_build_flags
cat src/CMakeLists.txt | sed 's/CMAKE_INSTALL_SBINDIR/CMAKE_INSTALL_BINDIR/g' > src/CMakeLists.txt.no-sbin
mv src/CMakeLists.txt.no-sbin src/CMakeLists.txt
cat src/pcm-sensor-server.service.in | sed 's/CMAKE_INSTALL_SBINDIR/CMAKE_INSTALL_BINDIR/g' > src/pcm-sensor-server.service.in.no-sbin
mv src/pcm-sensor-server.service.in.no-sbin src/pcm-sensor-server.service.in
%cmake -DCMAKE_BUILD_TYPE=CUSTOM -DLINUX_SYSTEMD=TRUE -DLINUX_SYSTEMD_UNITDIR=%{_unitdir}/
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/usr/share/doc/PCM/*.md
rm -rf %{buildroot}/usr/share/doc/PCM/*.txt

%files
%license LICENSE
%doc doc/LINUX_HOWTO.txt README.md doc/FAQ.md doc/CUSTOM-COMPILE-OPTIONS.md doc/ENVVAR_README.md doc/PCM-EXPORTER.md doc/PCM-SENSOR-SERVER-README.md doc/PCM_RAW_README.md doc/DOCKER_README.md doc/license.txt doc/LATENCY-OPTIMIZED-MODE.md doc/PCM_IIO_README.md
%{_sbindir}/%{name}-core
%{_sbindir}/%{name}-iio
%{_sbindir}/%{name}-latency
%{_sbindir}/%{name}-memory
%{_sbindir}/%{name}-msr
%{_sbindir}/%{name}-mmio
%{_sbindir}/%{name}-tpmi
%{_sbindir}/%{name}-numa
%{_sbindir}/%{name}-accel
%{_sbindir}/%{name}-pcicfg
%{_sbindir}/%{name}-pcie
%{_sbindir}/%{name}-power
%{_sbindir}/%{name}-sensor
%{_sbindir}/%{name}-sensor-server
%{_sbindir}/%{name}-tsx
%{_sbindir}/%{name}-raw
%{_sbindir}/%{name}
%{_bindir}/%{name}-client
%{_sbindir}/%{name}-daemon
%{_sbindir}/%{name}-bw-histogram
%{_datadir}/%{name}/
%{_unitdir}/%{name}-sensor-server.service

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 202604-0
- Import
