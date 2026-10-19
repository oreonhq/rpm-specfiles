%global source0_hash 6d3967b87f300e18b3f4771387e1fdf0ef8f6b860a1b3b34c73d337c33eb4118
%global _pkg_extra_cflags -Wno-error=non-c-typedef-for-linkage -Wno-error=unused-but-set-variable
%global _pkg_extra_cxxflags %{_pkg_extra_cflags}
%{!?configure_options: %global configure_options %{nil}}
Name: libvma
Version: 9.8.84
Release:        1%{?dist}
Summary:        A library for boosting TCP and UDP traffic (over RDMA hardware)
License: GPL-2.0-only OR BSD-2-Clause
Url: https://github.com/Mellanox/libvma
Source0:        https://github.com/Mellanox/libvma/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch: x86_64 ppc64le ppc64 aarch64
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  rdma-core-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
libvma is a LD_PRELOAD-able library that boosts performance of TCP and
UDP traffic. It allows application written over standard socket API to
handle fast path data traffic from user space over Ethernet and/or
Infiniband with full network stack bypass and get better throughput,
latency and packets/sec rate.

No application binary change is required for that.
libvma is supported by RDMA capable devices that support "verbs"
IBV_QPT_RAW_PACKET QP for Ethernet and/or IBV_QPT_UD QP for IPoIB.

%package devel
Summary: Header files required to develop with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package includes headers for building programs with libvma's
interfaces.

%package utils
Summary: Utilities used with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
This package contains the tool for collecting and analyzing libvma statistic.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export revision=1
if [ ! -e configure ] && [ -e autogen.sh ]; then
    PRJ_RELEASE=1 ./autogen.sh
fi
%configure %{?configure_options}
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT%{_libdir} -name '*.la' -delete
install -D -m 644 contrib/scripts/vma.service $RPM_BUILD_ROOT/%{_prefix}/lib/systemd/system/vma.service
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/vma
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%post

%systemd_post vma.service
%preun

%systemd_preun vma.service
%postun

%systemd_postun_with_restart vma.service
%files -f %{oreon_filedir}/main.list
%files -n libvma-devel -f %{oreon_filedir}/libvma-devel.list
%files -n libvma-utils -f %{oreon_filedir}/libvma-utils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.8.84-1
- Prepare for Oreon 11 (RP1)
