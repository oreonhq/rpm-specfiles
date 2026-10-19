%global source0_hash c89f63bafc688abb4749e901006321e329ab90941433d85f442f9c03bb3c7824
%ifarch ppc64 ppc64le s390x riscv64
%bcond_with lua
%endif
%bcond_with llvm_static
%if %{without llvm_static}
%global with_llvm_shared 1
%endif
Name:           bcc
Version:        0.37.0
Release:        1%{?dist}
Summary:        BPF Compiler Collection (BCC)
License:        Apache-2.0
URL:            https://github.com/iovisor/bcc
Source0:        https://github.com/iovisor/bcc/archive/refs/tags/v0.37.0.tar.gz#/bcc-0.37.0.tar.gz
ExclusiveArch:  x86_64 %{power64} aarch64 s390x armv7hl riscv64
%global _smp_mflags -j1
%global _lto_cflags %{nil}
%if %{with llvm_static}
%endif
%if %{with lua}
%endif
Requires:       libbpf >= 2:0.8.0-1
Requires:       tar
Recommends:     kernel-devel
Recommends:     %{name}-tools = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  bpftool
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  elfutils-debuginfod-client-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  libbpf-devel
BuildRequires:  libbpf-static
BuildRequires:  libxml2-devel
BuildRequires:  llvm-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(luajit)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
BCC is a toolkit for creating efficient kernel tracing and manipulation
programs, and includes several useful tools and examples. It makes use of
extended BPF (Berkeley Packet Filters), formally known as eBPF, a new feature
that was first added to Linux 3.15. BCC makes BPF programs easier to write,
with kernel instrumentation in C (and includes a C wrapper around LLVM), and
front-ends in Python and lua. It is suited for many tasks, including
performance analysis and network traffic control.

%package devel
Summary:        Shared library for BPF Compiler Collection (BCC)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       elfutils-debuginfod-client
%description devel
The %{name}-devel package contains libraries and header files for developing
application that use BPF Compiler Collection (BCC).

%package doc
Summary:        Examples for BPF Compiler Collection (BCC)
Recommends:     python3-%{name} = %{version}-%{release}
Recommends:     %{name}-lua = %{version}-%{release}
BuildArch:      noarch
%description doc
Examples for BPF Compiler Collection (BCC)

%package -n python3-%{name}
Summary:        Python3 bindings for BPF Compiler Collection (BCC)
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description -n python3-%{name}
Python3 bindings for BPF Compiler Collection (BCC)

%if %{with lua}
%package lua
Summary:        Standalone tool to run BCC tracers written in Lua
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description lua
Standalone tool to run BCC tracers written in Lua
%endif

%package tools
Summary:        Command line tools for BPF Compiler Collection (BCC)
Requires:       bcc = %{version}-%{release}
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-netaddr
%description tools
Command line tools for BPF Compiler Collection (BCC)

%package -n libbpf-tools
Summary:        Command line libbpf tools for BPF Compiler Collection (BCC)
BuildRequires:  libbpf-devel >= 2:0.8.0-1, libbpf-static >= 2:0.8.0-1
BuildRequires:  bpftool
%description -n libbpf-tools
Command line libbpf tools for BPF Compiler Collection (BCC)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export RPM_BUILD_NCPUS=1
export CMAKE_BUILD_PARALLEL_LEVEL=1
export NINJAFLAGS="-j1"
export CFLAGS="%{optflags} -fno-var-tracking-assignments -g1"
export CXXFLAGS="%{optflags} -fno-var-tracking-assignments -g1"
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DREVISION_LAST=%{version} -DREVISION=%{version} -DPYTHON_CMD=python3 \
       -DCMAKE_USE_LIBBPF_PACKAGE:BOOL=TRUE -DENABLE_NO_PIE=OFF \
       %{?with_llvm_shared:-DENABLE_LLVM_SHARED=1}
%cmake_build
pushd libbpf-tools;
%make_build BPFTOOL=bpftool LIBBPF_OBJ=%{_libdir}/libbpf.a CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
%make_install DESTDIR=./tmp-install prefix=
(
    cd tmp-install/bin
    for file in *; do
        mv $file bpf-$file
    done
    for file in `find . -type l`; do
        dest=$(readlink "$file")
        ln -s -f bpf-$dest $file
    done
)
popd
%install
%cmake_install
find %{buildroot}%{_datadir}/%{name}/{tools,examples} -type f -exec \
  sed -i -e '1s=^#!/usr/bin/python\([0-9.]\+\)\?$=#!%{__python3}=' \
         -e '1s=^#!/usr/bin/env python\([0-9.]\+\)\?$=#!%{__python3}=' \
         -e '1s=^#!/usr/bin/env bcc-lua$=#!/usr/bin/bcc-lua=' {} \;
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{_datadir}/%{name}/man/* %{buildroot}%{_mandir}/
for i in `find %{buildroot}%{_mandir} -name "*.gz"`; do
  tname=$(basename $i)
  rename $tname %{name}-$tname $i
done
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/examples %{buildroot}%{_docdir}/%{name}/
rm -f %{buildroot}%{_libdir}/lib%{name}*.a
rm -rf %{buildroot}%{_datadir}/%{name}/tools/old/
mkdir -p %{buildroot}/%{_sbindir}
cp -a libbpf-tools/tmp-install/bin/* %{buildroot}/%{_sbindir}/
%ldconfig_scriptlets
%oreon_autofiles libbpf-tools usr/*/lib*.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libbpf-tools -f %{oreon_filedir}/libbpf-tools.list

%changelog

* Wed Apr 15 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35.0-12
- Restore %%_smp_mflags -j1, %%_lto_cflags nil, ninja env, -g1 and -fno-var-tracking-assignments for clang_frontend OOM and bogus assembler after SIGKILL

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35.0-6
- Add upstream patch for llvm-22 createDiagnostics API changes

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35.0-5
- Prepare for Oreon 11 (RP1)
