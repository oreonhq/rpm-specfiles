%global source0_hash 6cbcb7959a5d90b59253ea6d8bdf0285e2cfbc3b301398704b41e3069293f4fb
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif
%global gomodulesmode GO111MODULE=on
%global _gvisor_installdir %{_libexecdir}/podman
%global desc_gvforwarder Forward traffic from a tap interface over vsock
Name: gvisor-tap-vsock
%if %{defined copr_username}
Epoch: 103
%else
Epoch: 6
%endif
Version: 0.8.9
License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
%if %{defined autorelease}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
Summary:        Go replacement for libslirp and VPNKit
URL: https://github.com/containers/%{name}
Source0:        https://github.com/containers/gvisor-tap-vsock/archive/refs/tags/v0.8.9.tar.gz#/gvisor-tap-vsock-0.8.9.tar.gz
%if %{defined copr_username}
Obsoletes: podman-gvproxy < 102:4.7.0-1
%else
Obsoletes: podman-gvproxy < 5:4.7.0-1
%endif
Provides: podman-gvproxy = %{epoch}:%{version}-%{release}
Requires: %{name}-gvforwarder = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  glibc-static
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  make
# /oreon:deps
%description
A replacement for libslirp and VPNKit, written in pure Go.
It is based on the network stack of gVisor. Compared to libslirp,
gvisor-tap-vsock brings a configurable DNS server and
dynamic port forwarding.

%package gvforwarder
Summary: %{desc_gvforwarder}
Provides: gvforwarder = %{epoch}:%{version}-%{release}
Obsoletes: %{name} < 6:0.7.0-6
Recommends: %{name} = %{epoch}:%{version}-%{release}
%description gvforwarder
%{desc_gvforwarder}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%set_build_flags
export CGO_CFLAGS=$CFLAGS
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')
%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
LDFLAGS=''
%gobuild -o bin/gvproxy ./cmd/gvproxy
%gobuild -o bin/gvforwarder ./cmd/vm
%install
install -dp %{buildroot}%{_gvisor_installdir}
install -p -m0755 bin/gvproxy %{buildroot}%{_gvisor_installdir}
install -p -m0755 bin/gvforwarder %{buildroot}%{_gvisor_installdir}
%{!?_licensedir:%global license %doc}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gvisor-tap-vsock-gvforwarder -f %{oreon_filedir}/gvisor-tap-vsock-gvforwarder.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.8-1
- Prepare for Oreon 11 (RP1)
