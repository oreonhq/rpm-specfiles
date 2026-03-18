# We don't want to bring luajit in RHEL
%if 0%{?rhel} > 0
%bcond_with lua
%else
# luajit is not available for some architectures
%ifarch ppc64 ppc64le s390x riscv64
%bcond_with lua
%else
%bcond_without lua
%endif
%endif

%bcond_with llvm_static

%if %{without llvm_static}
%global with_llvm_shared 1
%endif


Name:           bcc
Version:        0.35.0
Release:        5%{?dist}
Summary:        BPF Compiler Collection (BCC)
License:        Apache-2.0
URL:            https://github.com/iovisor/bcc
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix build with clang 21
Patch0:         %{url}/pull/5369.patch

# Arches will be included as upstream support is added and dependencies are
# satisfied in the respective arches
ExclusiveArch:  x86_64 %{power64} aarch64 s390x armv7hl riscv64

BuildRequires:  bison
BuildRequires:  cmake >= 2.8.7
BuildRequires:  flex
BuildRequires:  libxml2-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  elfutils-libelf-devel
BuildRequires:  elfutils-debuginfod-client-devel
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
%if %{with llvm_static}
BuildRequires:  llvm-static
%endif
BuildRequires:  ncurses-devel
%if %{with lua}
BuildRequires:  pkgconfig(luajit)
%endif
BuildRequires:  libbpf-devel >= 2:0.8.0-1, libbpf-static >= 2:0.8.0-1

Requires:       libbpf >= 2:0.8.0-1
Requires:       tar
Recommends:     kernel-devel
Recommends:     %{name}-tools = %{version}-%{release}

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
%autosetup -p1


%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DREVISION_LAST=%{version} -DREVISION=%{version} -DPYTHON_CMD=python3 \
       -DCMAKE_USE_LIBBPF_PACKAGE:BOOL=TRUE -DENABLE_NO_PIE=OFF \
       %{?with_llvm_shared:-DENABLE_LLVM_SHARED=1}
%cmake_build

# It was discussed and agreed to package libbpf-tools with
# 'bpf-' prefix (https://github.com/iovisor/bcc/pull/3263)
# Installing libbpf-tools binaries in temp directory and
# renaming them in there and the install code will just
# take them.
pushd libbpf-tools;
%make_build BPFTOOL=bpftool LIBBPF_OBJ=%{_libdir}/libbpf.a CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
%make_install DESTDIR=./tmp-install prefix=
(
    cd tmp-install/bin
    for file in *; do
        mv $file bpf-$file
    done
    # now fix the broken symlinks
    for file in `find . -type l`; do
        dest=$(readlink "$file")
        ln -s -f bpf-$dest $file
    done
)
popd

%install
%cmake_install

# Fix python shebangs
find %{buildroot}%{_datadir}/%{name}/{tools,examples} -type f -exec \
  sed -i -e '1s=^#!/usr/bin/python\([0-9.]\+\)\?$=#!%{__python3}=' \
         -e '1s=^#!/usr/bin/env python\([0-9.]\+\)\?$=#!%{__python3}=' \
         -e '1s=^#!/usr/bin/env bcc-lua$=#!/usr/bin/bcc-lua=' {} \;

# Move man pages to the right location
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{_datadir}/%{name}/man/* %{buildroot}%{_mandir}/
# Avoid conflict with other manpages
# https://bugzilla.redhat.com/show_bug.cgi?id=1517408
for i in `find %{buildroot}%{_mandir} -name "*.gz"`; do
  tname=$(basename $i)
  rename $tname %{name}-$tname $i
done
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/examples %{buildroot}%{_docdir}/%{name}/

# Delete static libraries we don't want to ship
rm -f %{buildroot}%{_libdir}/lib%{name}*.a

# Delete old tools we don't want to ship
rm -rf %{buildroot}%{_datadir}/%{name}/tools/old/

# We cannot run the test suit since it requires root and it makes changes to
# the machine (e.g, IP address)
# %%check

mkdir -p %{buildroot}/%{_sbindir}
# We cannot use `install` because some of the tools are symlinks and `install`
# follows those. Since all the tools already have the correct permissions set,
# we just need to copy them to the right place while preserving those
cp -a libbpf-tools/tmp-install/bin/* %{buildroot}/%{_sbindir}/

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/lib%{name}.so.*
%{_libdir}/libbcc_bpf.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/libbcc_bpf.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_includedir}/%{name}/

%files -n python3-%{name}
%{python3_sitelib}/%{name}*

%files doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/examples/

%files tools
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/tools/
%{_datadir}/%{name}/introspection/
%{_mandir}/man8/*

%if %{with lua}
%files lua
%{_bindir}/bcc-lua
%endif

%files -n libbpf-tools
%{_sbindir}/bpf-*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35.0-5
- Prepare for Oreon 11 (RP1)
