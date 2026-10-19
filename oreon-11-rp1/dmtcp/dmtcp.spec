%global source0_hash 8cfb924b4f568df92e84de62c7c2c3a8a4cbf5a1093a851d93d2394411095dd0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global forgeurl https://github.com/dmtcp/dmtcp
Version:        4.1.0
%global tag %{version}
%forgemeta
Name:           dmtcp
Release:        1%{?dist}
Summary:        Distributed MultiThreaded CheckPointing
License:        LGPL-3.0-or-later AND (MIT OR BSD-3-Clause)
URL:            http://dmtcp.sourceforge.net
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch: x86_64 aarch64 riscv64
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
DMTCP is a tool to transparently checkpoint the state of multiple simultaneous
applications, including multi-threaded and distributed applications. It operates
directly on the user binary executable, without any Linux kernel modules or
other kernel modifications.

Among the applications supported by DMTCP are MPI (various implementations),
OpenMP, MATLAB, Python, Perl, R, and many programming languages and shell
scripting languages. DMTCP also supports GNU screen sessions, including
vim/cscope and emacs. With the use of TightVNC, it can also checkpoint and
restart X Window applications. For a multilib (mixture of 32- and 64-bit
processes), see "./configure --enable-multilib".

DMTCP supports the commonly used OFED API for InfiniBand, as well as its
integration with various implementations of MPI, and resource managers (e.g.,
SLURM).

This package contains DMTCP binaries.

%package        devel
Summary:        DMTCP developer package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package provides files for developing DMTCP plugins.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%configure --docdir=%{_pkgdocdir}
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dmtcp-devel -f %{oreon_filedir}/dmtcp-devel.list

%changelog

%autochangelog
