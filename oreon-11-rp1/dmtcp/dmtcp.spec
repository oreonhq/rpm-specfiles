%global source0_hash 8cfb924b4f568df92e84de62c7c2c3a8a4cbf5a1093a851d93d2394411095dd0

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global forgeurl https://github.com/dmtcp/dmtcp
Version:        4.1.0
%global tag %{version}
%forgemeta

Name:           dmtcp
Release:        %autorelease
Summary:        Distributed MultiThreaded CheckPointing

# DMTCP is mainly under LGPL-3.0-or-later, except:
# The file include/dmtcp.h is released under MIT/BSD dual license. The user is
# allowed to use these files under either license.
# https://github.com/dmtcp/dmtcp/blob/master/COPYING
License:        LGPL-3.0-or-later AND (MIT OR BSD-3-Clause)
URL:            http://dmtcp.sourceforge.net
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libatomic
BuildRequires:  python3

# This package is functional only on i386, x86_64 and aarch64 architectures.
# It should also work on %%ix86, but Koji seems to have problems with it.
## We're excluding aarch64 for now, because we don't have a trampoline for it.
## In the next relase, we won't need the trampoline.  We'll interpose
##   entirely on pthread_create, and not on __clone3
## ExclusiveArch: x86_64 aarch64
ExclusiveArch: x86_64 aarch64 riscv64

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

# A few tests may take a long time.  If a test times out, the check fails.
# Hopefully, the test machine is fast enough, and timeouts are long
#   enough to avoid that problem.
# 2022-09 - Disabled tests to fix FTBFS on Fedora 36+
# %check
# AUTOTEST="--retry-once --slow" make check

%files
%license COPYING.LESSER
%{_bindir}/dmtcp_*
%{_bindir}/mtcp_restart
%{_libdir}/%{name}
%{_pkgdocdir}/
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/dmtcp.h
%{_includedir}/version.h

%changelog
%autochangelog
