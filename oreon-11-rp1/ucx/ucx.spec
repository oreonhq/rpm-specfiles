%global source0_hash 258941cddd14ca60d38c0d31b9b09ec1052c901086841011a498da8b55a3cb24
%{!?configure_options: %global configure_options %{nil}}
%bcond_without cma
%bcond_with    cuda
%bcond_with    gdrcopy
%bcond_without ib
%bcond_with    knem
%bcond_without rdmacm
%bcond_with    ugni
%bcond_with    xpmem
%bcond_with    vfs
%bcond_with    mad
%bcond_without mlx5
%bcond_with    efa
%ifarch x86_64
%bcond_without rocm
%else
%bcond_with rocm
%endif
Name: ucx
Version: 1.22.0
Release:        1%{?dist}
Summary:        UCX is a communication library implementing high-performance messaging
License: BSD-3-Clause AND MIT AND CC-PDDC AND (BSD-3-Clause OR Apache-2.0)
URL: http://www.openucx.org
Source0:        https://github.com/openucx/%{name}/releases/download/v%{version}/ucx-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Prefix: %{_prefix}
ExclusiveArch: aarch64 ppc64le x86_64 riscv64
%if %{defined extra_deps}
Requires: %{?extra_deps}
%endif
%if "%{_vendor}" == "suse"
%else
%endif
%if %{with cma}
%endif
%if %{with gdrcopy}
%endif
%if %{with ib}
%endif
%if %{with mlx5}
%endif
%if %{with efa}
%endif
%if %{with knem}
%endif
%if %{with rdmacm}
%endif
%if %{with rocm}
%endif
%if %{with xpmem}
%endif
%if %{with vfs}
%endif
%if %{with mad}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  libtool
BuildRequires:  numactl-devel
BuildRequires:  rdma-core-devel
# /oreon:deps
%description
UCX is an optimized communication framework for high-performance distributed
applications. UCX utilizes high-speed networks, such as RDMA (InfiniBand, RoCE,
etc), Cray Gemini or Aries, for inter-node communication. If no such network is
available, TCP is used instead. UCX supports efficient transfer of data in
either main memory (RAM) or GPU memory (through CUDA and ROCm libraries). In
addition, UCX provides efficient intra-node communication, by leveraging the
following shared memory mechanisms: posix, sysv, cma, knem, and xpmem.
The acronym UCX stands for "Unified Communication X".

%if "%{_vendor}" == "suse"
%debug_package
%endif

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Header files required for developing with UCX
%description devel
Provides header files and examples for developing with UCX.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
# https://github.com/openucx/ucx/issues/10542
# With ROCm 6.3+ libhsakmt is bundled with libhsa-runtime64
# Remove this nonexistent library
sed -i 's@-lhsakmt@@' config/m4/rocm.m4

# Relax use of -Werror
sed -i 's@-Werror@@' config/m4/compiler.m4

autoreconf -fiv
# https://github.com/openucx/ucx/commit/b0a275a5492125a13020cd095fe9934e0b5e7c6a
# can be removed on release after 1.17.0
sed -i '/#include <limits.h>/a #include <math.h>' src/ucs/time/time.h

%build

%set_build_flags
export CFLAGS="$CFLAGS -std=gnu17"
%define _with_arg()   %{expand:%%{?with_%{1}:--with-%{2}}%%{!?with_%{1}:--without-%{2}}}
%define _enable_arg() %{expand:%%{?with_%{1}:--enable-%{2}}%%{!?with_%{1}:--disable-%{2}}}
%configure --disable-optimizations \
           --disable-logging \
           --disable-debug \
           --disable-assertions \
           --disable-params-check \
           --without-java \
%if %{with rocm}
           --with-rocm=%{_prefix} \
%endif
           %_enable_arg cma cma \
           %_with_arg cuda cuda \
           %_with_arg gdrcopy gdrcopy \
           %_with_arg ib verbs \
           %_with_arg mlx5 mlx5 \
           %_with_arg efa efa \
           %_with_arg knem knem \
           %_with_arg rdmacm rdmacm \
           %_with_arg xpmem xpmem \
           %_with_arg vfs fuse3 \
           %_with_arg ugni ugni \
           %_with_arg mad mad \
           %{?configure_options}
make %{?_smp_mflags} V=1
%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/ucx/*.la
rm -f %{buildroot}%{_libdir}/ucx/lib*.so
rm -f %{buildroot}%{_libdir}/ucx/lib*.a
%if %{with rocm}
chrpath -d %{buildroot}%{_libdir}/ucx/libucx_perftest_rocm.so.0.0.0
chrpath -d %{buildroot}%{_libdir}/ucx/libucm_rocm.so.0.0.0
chrpath -d %{buildroot}%{_libdir}/ucx/libuct_rocm.so.0.0.0
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%package cma
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX CMA support
%description cma
Provides CMA (Linux cross-memory-attach) transport for UCX. It utilizes the
system calls process_vm_readv/writev() for one-shot memory copy from another
process.

%package cuda
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX CUDA support
%description cuda
Provide CUDA (NVIDIA GPU) support for UCX. Enables passing GPU memory pointers
to UCX communication routines, and transports taking advantage of GPU-Direct
technology for direct data transfer between GPU and RDMA devices.

%package gdrcopy
Requires: %{name}-cuda%{?_isa} = %{version}-%{release}
Summary: UCX GDRCopy support
%description gdrcopy
Provide GDRCopy support for UCX. GDRCopy is a low-latency GPU memory copy
library, built on top of the NVIDIA GPUDirect RDMA technology.

%package ib
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX RDMA support
%description ib
Provides support for IBTA-compliant transports for UCX. This includes RoCE,
InfiniBand, OmniPath, and any other transport supported by IB Verbs API.
Typically these transports provide RDMA support, which enables a fast and
hardware-offloaded data transfer.

%package knem
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX KNEM transport support
%description knem
Provides KNEM (fast inter-process copy) transport for UCX. KNEM is a Linux
kernel module that enables high-performance intra-node MPI communication
for large messages.

%package rdmacm
Requires: %{name}-ib%{?_isa} = %{version}-%{release}
Requires: ucx-ib = %{version}-%{release}
Summary: UCX RDMA connection manager support
%description rdmacm
Provides RDMA connection-manager support to UCX, which enables client/server
based connection establishment for RDMA-capable transports.

%package rocm
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX ROCm GPU support
%description rocm
Provides Radeon Open Compute (ROCm) Runtime support for UCX.

%package rocmgdr
Requires: %{name}-rocm%{?_isa} = %{version}-%{release}
Summary: UCX GDRCopy support for ROCM
%description rocmgdr
Provide GDRCopy support for UCX ROCM. GDRCopy is a low-latency GPU
memory copy library, built on top of the NVIDIA GPUDirect RDMA
technology.

%package ugni
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX Gemini/Aries transport support.
%description ugni
Provides Gemini/Aries transport for UCX.

%package xpmem
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX XPMEM transport support.
%description xpmem
Provides XPMEM transport for UCX. XPMEM is a Linux kernel module that enables a
process to map the memory of another process into its virtual address space.

%package vfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX Virtual Filesystem support.
%description vfs
Provides a virtual filesystem over FUSE which allows real-time
monitoring of UCX library internals, protocol objects, transports
status, and more.

%package ib-mlx5
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX IB MLX5 RDMA provider support
Group: System Environment/Libraries
%description ib-mlx5
Provides support for DevX, Direct Verbs and DC transports for Infiniband
devices.

%package ib-efa
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX EFA device RDMA support
Group: System Environment/Libraries
%description ib-efa
Provides support for EFA device as an IBTA transport for UCX.

%package mad
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: UCX Infiniband MAD support
Group: System Environment/Libraries
%description mad
Provide Infiniband MAD support for UCX. Enables running perftest using
Infiniband datagrams for out-of-band communications.

%files -f %{oreon_filedir}/main.list
%files -n ucx-devel -f %{oreon_filedir}/ucx-devel.list
%files -n ucx-cma -f %{oreon_filedir}/ucx-cma.list
%files -n ucx-ib -f %{oreon_filedir}/ucx-ib.list
%files -n ucx-rdmacm -f %{oreon_filedir}/ucx-rdmacm.list
%files -n ucx-ib-mlx5 -f %{oreon_filedir}/ucx-ib-mlx5.list

%changelog

%autochangelog
