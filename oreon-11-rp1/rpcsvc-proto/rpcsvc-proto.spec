%global source0_hash eaa227686b84e8ae20181d2119c0ccac29d82371441844008019a134dafe3613
Name:           rpcsvc-proto
Version:        1.4
Release:        1%{?dist}
Summary:        RPC protocol definitions
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
Url:            https://github.com/thkukuk/rpcsvc-proto
Source0:        https://github.com/thkukuk/rpcsvc-proto/archive/refs/tags/v%{version}.tar.gz#/rpcsvc-proto-%{version}.tar.gz
Conflicts: glibc-headers < 2.26.9000-36
Conflicts: glibc-common < 2.26.9000-36
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package devel
Summary:        RPC protocol definitions
%description devel
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package -n rpcgen
Summary:        RPC protocol compiler
Provides:       rpcgen
%description -n rpcgen
rpcgen is a tool that generates C code to implement an RPC protocol.
The input to rpcgen is a language similar to C known as RPC Language
(Remote Procedure Call Language).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_prefix}/include/rpcsvc/rquota.[hx]
%oreon_autofiles rpcgen usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rpcsvc-proto-devel -f %{oreon_filedir}/rpcsvc-proto-devel.list
%files -n rpcgen -f %{oreon_filedir}/rpcgen.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4-19
- Import
