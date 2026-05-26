Name:             xdp-tools
Version:          1.6.2
Release:          1%{?dist}
Summary:          Utilities and example programs for use with XDP
%global _soversion 1.6.0

License:          GPL-2.0-only
URL:              https://github.com/xdp-project/%{name}
Source0:          https://github.com/xdp-project/%{name}/releases/download/v%{version}/xdp-tools-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 e2211dcbd38fa6729853af3dc3b55816793a6563afa4361dd5ae04945a166332
%global source0_file xdp-tools-1.6.2.tar.gz
# oreon url source checksums end

BuildRequires:    kernel-headers
BuildRequires:    libbpf-devel
BuildRequires:    elfutils-libelf-devel
BuildRequires:    zlib-devel
BuildRequires:    libpcap-devel
BuildRequires:    libcap-ng-devel
BuildRequires:    clang >= 10.0.0
BuildRequires:    llvm >= 10.0.0
BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    pkgconfig
BuildRequires:    m4
BuildRequires:    emacs-nox
BuildRequires:    wireshark-cli

%ifnarch i686
BuildRequires:    bpftool
%endif

# Always keep xdp-tools and libxdp packages in sync
Requires:         libxdp = %{version}-%{release}

%global _hardened_build 1

%description
Utilities and example programs for use with XDP

%package -n libxdp
Summary:          XDP helper library
License:          LGPL-2.1-only OR BSD-2-Clause

%package -n libxdp-devel
Summary:          Development files for libxdp
License:          LGPL-2.1-only OR BSD-2-Clause
Requires:         kernel-headers
Requires:         libxdp = %{version}-%{release}

%package -n libxdp-static
Summary:          Static library files for libxdp
License:          LGPL-2.1-only OR BSD-2-Clause
Requires:         libxdp-devel = %{version}-%{release}

%description -n libxdp
The libxdp package contains the libxdp library for managing XDP programs,
used by the %{name} package

%description -n libxdp-devel
The libxdp-devel package contains headers used for building XDP programs using
libxdp.

%description -n libxdp-static
The libxdp-static package contains the static library version of libxdp.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xdp-tools-1.6.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e2211dcbd38fa6729853af3dc3b55816793a6563afa4361dd5ae04945a166332" || { echo "oreon: Source0 SHA256 mismatch for xdp-tools-1.6.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{name}-%{version}


%build
export CFLAGS='%{build_cflags}'
export LDFLAGS='%{build_ldflags}'
export LIBDIR='%{_libdir}'
export RUNDIR='%{_rundir}'
export CLANG=$(which clang)
export PRODUCTION=1
export DYNAMIC_LIBXDP=1
export FORCE_SYSTEM_LIBBPF=1
export FORCE_EMACS=1
./configure
make %{?_smp_mflags} V=1

%install
export DESTDIR='%{buildroot}'
export SBINDIR='%{_sbindir}'
export LIBDIR='%{_libdir}'
export RUNDIR='%{_rundir}'
export MANDIR='%{_mandir}'
export DATADIR='%{_datadir}'
export HDRDIR='%{_includedir}/xdp'
make install V=1

%files
%{_sbindir}/xdp-filter
%{_sbindir}/xdp-loader
%{_sbindir}/xdpdump
%ifnarch i686
%{_sbindir}/xdp-bench
%{_sbindir}/xdp-forward
%{_sbindir}/xdp-monitor
%{_sbindir}/xdp-trafficgen
%endif
%{_mandir}/man8/*
%{_libdir}/bpf/xdpfilt_*.o
%{_libdir}/bpf/xdpdump_*.o
%{_datadir}/xdp-tools/
%license LICENSES/*

%files -n libxdp
%{_libdir}/libxdp.so.1
%{_libdir}/libxdp.so.%{_soversion}
%{_libdir}/bpf/xdp-dispatcher.o
%{_libdir}/bpf/xsk_def_xdp_prog*.o
%{_mandir}/man3/*
%license LICENSES/*

%files -n libxdp-static
%{_libdir}/libxdp.a

%files -n libxdp-devel
%{_includedir}/xdp/*.h
%{_libdir}/libxdp.so
%{_libdir}/pkgconfig/libxdp.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.2-1
- Prepare for Oreon 11 (RP1)
