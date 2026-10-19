%global source1_hash f115ff5ba0194358a4784912b103521804db435f75a9cfa52bc4df3b1aa9e7b8
%global source0_hash e0def0bda91a7e818ea28970774ec96e3969a602a3578da78f25f67ced3c8308
Name:		libntirpc
Version:	7.2
Release:        2%{?dist}
Summary:        New Transport Independent RPC Library
License:	BSD-3-Clause
Url:		https://github.com/nfs-ganesha/ntirpc
%global prometh_ver_long	48d09c45ee6deb90e02579b03037740e1c01fd27
%global prometh_ver_short	48d09c45
Source0:        https://github.com/nfs-ganesha/ntirpc/archive/v%{version}/ntirpc-%{version}.tar.gz
Source1:	https://github.com/biaks/prometheus-cpp-lite/archive/%{prometh_ver_long}/prometheus-cpp-lite-%{prometh_ver_short}.tar.gz
Patch:		0001-CMakeLists.txt.patch
%ifarch x86_64 aarch64
%endif
Requires:	libtirpc
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  librdmacm
BuildRequires:  rdma-core-devel
BuildRequires:  userspace-rcu-devel
# /oreon:deps
%description
This package contains a new implementation of the original libtirpc, 
transport-independent RPC (TI-RPC) library for NFS-Ganesha. It has
the following features not found in libtirpc:
 1. Bi-directional operation
 2. Full-duplex operation on the TCP (vc) transport
 3. Thread-safe operating modes
 3.1 new locking primitives and lock callouts (interface change)
 3.2 stateless send/recv on the TCP transport (interface change)
 4. Flexible server integration support
 5. Event channels (remove static arrays of xprt handles, new EPOLL/KEVENT
    integration)

%package devel
Summary:	Development headers for %{name}
Requires:	%{name}%{?_isa} = %{version}
%description devel
Development headers and auxiliary files for developing with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

tar xpf %{SOURCE1}
%autosetup -p1 -n ntirpc-%{version}%{?dev:%{dev}}

%build

export VERBOSE=1
mv ../prometheus-cpp-lite-%{prometh_ver_long}/* ./src/monitoring/prometheus-cpp-lite
%cmake \
    -DOVERRIDE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DTIRPC_EPOLL=1 \
    -DUSE_GSS=ON \
    -DUSE_RPC_RDMA=ON \
%ifarch x86_64 aarch64
    -DCMAKE_LINKER=%{_bindir}/ld.mold \
%endif
    "-GUnix Makefiles"
export GCC_COLORS=
%cmake_build
%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
%cmake_install
install -p -m 644 src/monitoring/include/monitoring.h %{buildroot}%{_includedir}/ntirpc
mv src/monitoring/prometheus-cpp-lite/core/include/prometheus %{buildroot}%{_includedir}/ntirpc
ln -s %{name}.so.%{version} %{buildroot}%{_libdir}/%{name}.so.7
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libntirpc-devel -f %{oreon_filedir}/libntirpc-devel.list

%changelog

%autochangelog
