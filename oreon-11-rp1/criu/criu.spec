%global source0_hash feffdf4638125ebb12d2434754f80a1d7bbba85a3e6bee98c216f88fb99a5d96
%global py_prefix python3
%global py_binary %{py_prefix}
%undefine _annotated_build
Name: criu
Version: 4.2.1
Release:        1%{?dist}
Summary:        Tool for Checkpoint/Restore in User-space
License: GPL-2.0-only AND LGPL-2.1-only AND MIT
URL: http://criu.org/
Source0:        https://github.com/checkpoint-restore/criu/archive/refs/tags/v%{version}.tar.gz#/criu-%{version}.tar.gz
Patch0: 0001-rseq-use-kernel-rseq.h-when-glibc-detects-it.patch
Patch99: criu.pc.patch
Source5: criu-tmpfiles.conf
Recommends: tar
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x riscv64
# oreon:deps
BuildRequires:  (python3-wheel if python3-setuptools < 71)
BuildRequires:  asciidoctor
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  libbsd-devel
BuildRequires:  libcap-devel
BuildRequires:  libdrm-devel
BuildRequires:  libnet-devel
BuildRequires:  libnl3-devel
BuildRequires:  libselinux-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  nftables-devel
BuildRequires:  perl-interpreter
BuildRequires:  protobuf-c-devel
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  systemd
# /oreon:deps
%description
criu is the user-space part of Checkpoint/Restore in User-space
(CRIU), a project to implement checkpoint/restore functionality for
Linux in user-space.

%package devel
Summary: Header files and libraries for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
%description devel
This package contains header files and libraries for %{name}.

%package libs
Summary: Libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
This package contains the libraries for %{name}

%package amdgpu-plugin
Summary: AMD GPU plugin for %{name}
Requires: %{name} = %{version}-%{release}
%description amdgpu-plugin
This package contains the AMD GPU plugin for %{name}

%package cuda-plugin
Summary: CUDA plugin for %{name}
Requires: %{name} = %{version}-%{release}
%description cuda-plugin
This package contains the CUDA plugin for %{name}

%package -n %{py_prefix}-%{name}
%{?python_provide:%python_provide %{py_prefix}-%{name}}
Summary: Python bindings for %{name}
Requires: %{py_prefix}-protobuf
%description -n %{py_prefix}-%{name}
%{py_prefix}-%{name} contains Python bindings for %{name}.

%package -n crit
Summary: CRIU image tool
Requires: %{py_prefix}-%{name} = %{version}-%{release}
%description -n crit
crit is a tool designed to decode CRIU binary dump files and show
their content in human-readable form.

%package -n criu-ns
Summary: Tool to run CRIU in different namespaces
Requires: %{name} = %{version}-%{release}
%description -n criu-ns
The purpose of the criu-ns wrapper script is to enable restoring a process
tree that might require a specific PID that is already used on the system.
This script can help to workaround the so called "PID mismatch" problem.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 0 -p1
%patch -P 99 -p1

%build

%define _lto_cflags %{nil}
mkdir -p %{_builddir}/bin
cat > %{_builddir}/bin/ld << 'LDWRAPPER'
for arg do
  shift
  case "$arg" in -specs=*) continue ;; esac
  set -- "$@" "$arg"
done
exec /usr/bin/ld "$@"
LDWRAPPER
chmod +x %{_builddir}/bin/ld
CFLAGS+="%{optflags}" make V=1 WERROR=0 LD=%{_builddir}/bin/ld PREFIX=%{_prefix} RUNDIR=/run/criu PYTHON=%{py_binary} PLUGINDIR=%{_libdir}/criu NETWORK_LOCK_DEFAULT=NETWORK_LOCK_NFTABLES
make V=1 WERROR=0 PREFIX=%{_prefix} PLUGINDIR=%{_libdir}/criu amdgpu_plugin
make docs V=1
%install
sed -e "s,--upgrade --ignore-installed,--no-index --no-deps -v --no-build-isolation,g" -i lib/Makefile -i crit/Makefile
make install-criu LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir}
make install-lib LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} PYTHON=%{py_binary} PIPFLAGS="--no-build-isolation --no-index --no-deps --progress-bar off --upgrade --ignore-installed"
make install-amdgpu_plugin LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} PLUGINDIR=%{_libdir}/criu
make install-cuda_plugin LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} PLUGINDIR=%{_libdir}/criu
make install-crit LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}  BINDIR=%{_bindir} SBINDIR=%{_sbindir} PYTHON=%{py_binary} PIPFLAGS="--no-build-isolation --no-index --no-deps --progress-bar off --upgrade --ignore-installed"
make install-man LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/compel.1
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/
rm -f $RPM_BUILD_ROOT%{_libdir}/libcriu.a
%oreon_autofiles criu-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles criu-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles criu-amdgpu-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles criu-cuda-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-criu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles criu-ns usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%tmpfiles_create %{name}.conf
%files -f %{oreon_filedir}/main.list
%files -n criu-devel -f %{oreon_filedir}/criu-devel.list
%files -n criu-libs -f %{oreon_filedir}/criu-libs.list
%files -n criu-amdgpu-plugin -f %{oreon_filedir}/criu-amdgpu-plugin.list
%files -n criu-cuda-plugin -f %{oreon_filedir}/criu-cuda-plugin.list
%files -n python3-criu -f %{oreon_filedir}/python3-criu.list
%files -n crit -f %{oreon_filedir}/crit.list
%files -n criu-ns -f %{oreon_filedir}/criu-ns.list

%changelog

%autochangelog
