%global source0_hash e6738e29597f733270731aa90600f37ffdc045079dfc27ec7e8192cc81085c3e
%global source1_hash 5202c52a364afc0b310a2fff71082d37351590f6339f1a42eacb8a974df7a200
%global source2_hash 7372fd759173c636a318b5a1eef2f09d5a2ef598eefd78870abdf474ae47d316
%global source3_hash 01b06e2dba0e2635544fb8b301eda1105da36d63131054a42bb230b378d6d2c3
%global nvptx_rev 212da2e781ed0f9423824e85eb04819958513f7a
%global newlib_rev d35cc82b5ec15bb8a5fe0fe11e183d1887992e99
%global annobin_ver 13.33
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global __brp_python_bytecompile %{nil}
%global __brp_strip_static_archive %{nil}

Name: gcc
Version: 16.2.0
Release: 3%{?dist}
Summary: GNU Compiler Collection
License: GPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1)
URL: https://gcc.gnu.org
Source0: https://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.xz
Source1: https://codeload.github.com/MentorEmbedded/nvptx-tools/tar.gz/%{nvptx_rev}#/nvptx-tools-%{nvptx_rev}.tar.gz
Source2: https://codeload.github.com/mirror/newlib-cygwin/tar.gz/%{newlib_rev}#/newlib-cygwin-%{newlib_rev}.tar.gz
Source3: https://nickc.fedorapeople.org/annobin-%{annobin_ver}.tar.xz
Patch0: gcc16-csetjmp.patch

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: mpfr-devel
BuildRequires: mpc-devel
BuildRequires: zlib-devel
%if %{without bootstrap} && !0%{?bootstrap}
Requires: binutils
Requires: cpp = %{version}-%{release}
Requires: glibc-devel
Requires: libgcc = %{version}-%{release}
BuildRequires: texinfo
BuildRequires: bison
BuildRequires: flex
BuildRequires: file
BuildRequires: python3
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libxml2-devel
BuildRequires: gcc-gnat
BuildRequires: libgnat
BuildRequires: gcc-gdc
BuildRequires: libgphobos-static
%ifarch x86_64
BuildRequires: llvm
BuildRequires: lld
%endif
%endif

%description
This directory contains the GNU Compiler Collection (GCC).

The GNU Compiler Collection is free software.  See the files whose
names start with COPYING for copying permission.  The manuals, and
some of the runtime libraries, are under different terms; see the
individual source files for details.

%if %{without bootstrap} && !0%{?bootstrap}
%package -n cpp
Summary: GNU C preprocessor
Requires: libgcc = %{version}-%{release}
%description -n cpp
The GNU C preprocessor. It is used by the C compiler to transform programs before compilation.

%package -n gcc-c++
Summary: GNU C++ compiler
Requires: gcc = %{version}-%{release}
Requires: libstdc++-devel = %{version}-%{release}
%description -n gcc-c++
C++ support for the GNU Compiler Collection.

%package -n gcc-objc
Summary: GNU Objective-C compiler
Requires: gcc = %{version}-%{release}
Requires: libobjc = %{version}-%{release}
%description -n gcc-objc
Objective-C support for the GNU Compiler Collection.

%package -n gcc-objc++
Summary: GNU Objective-C++ compiler
Requires: gcc-c++ = %{version}-%{release}
Requires: gcc-objc = %{version}-%{release}
%description -n gcc-objc++
Objective-C++ support for the GNU Compiler Collection.

%package -n gcc-gfortran
Summary: GNU Fortran compiler
Requires: gcc = %{version}-%{release}
Requires: libgfortran = %{version}-%{release}
%ifarch x86_64
Requires: libquadmath = %{version}-%{release}
Requires: libquadmath-devel = %{version}-%{release}
%endif
%description -n gcc-gfortran
Fortran support for the GNU Compiler Collection.

%package -n gcc-gdc
Summary: GNU D compiler
Requires: gcc = %{version}-%{release}
Requires: libgphobos = %{version}-%{release}
%description -n gcc-gdc
D support for the GNU Compiler Collection.

%package -n gcc-gm2
Summary: GNU Modula-2 compiler
Requires: gcc-c++ = %{version}-%{release}
Requires: libgm2 = %{version}-%{release}
%description -n gcc-gm2
Modula-2 support for the GNU Compiler Collection.

%package -n gcc-gcobol
Summary: GNU COBOL compiler
Requires: gcc = %{version}-%{release}
Requires: libgcobol = %{version}-%{release}
%description -n gcc-gcobol
COBOL support for the GNU Compiler Collection.

%package -n gcc-algol68
Summary: GNU Algol 68 compiler
Requires: gcc = %{version}-%{release}
Requires: libga68 = %{version}-%{release}
%description -n gcc-algol68
Algol 68 support for the GNU Compiler Collection.

%package -n gcc-gnat
Summary: GNU Ada compiler
Requires: gcc-c++ = %{version}-%{release}
Requires: libgnat = %{version}-%{release}
%description -n gcc-gnat
Ada support for the GNU Compiler Collection.

%package -n gcc-go
Summary: GNU Go compiler
Requires: gcc = %{version}-%{release}
Requires: libgo = %{version}-%{release}
%description -n gcc-go
Go support for the GNU Compiler Collection.

%package -n gcc-gdb-plugin
Summary: GCC plugin for GDB
Requires: gcc = %{version}-%{release}
Requires: libgcc = %{version}-%{release}
%description -n gcc-gdb-plugin
GCC plugin for GDB C expression evaluation.

%package -n gcc-plugin-devel
Summary: Files for building GCC plugins
Requires: gcc = %{version}-%{release}
Requires: gmp-devel
Requires: mpfr-devel
Requires: mpc-devel
%description -n gcc-plugin-devel
Header files for compiling GCC plugins.

%package -n gcc-plugin-annobin
Summary: Annobin plugin built by this GCC
Requires: gcc = %{version}-%{release}
%description -n gcc-plugin-annobin
Annobin plugin built by the same GCC it is installed with.

%package -n libgcc
Summary: GCC shared support library
License: GPL-3.0-or-later WITH GCC-exception-3.1
%description -n libgcc
GCC shared support library.

%package -n libstdc++
Summary: GNU Standard C++ Library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libstdc++
GNU Standard C++ Library.

%package -n libstdc++-devel
Summary: GNU Standard C++ Library headers
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libstdc++ = %{version}-%{release}
Requires: gcc = %{version}-%{release}
%description -n libstdc++-devel
Headers and link libraries for the GNU Standard C++ Library.

%package -n libstdc++-static
Summary: GNU Standard C++ static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libstdc++-devel = %{version}-%{release}
%description -n libstdc++-static
Static GNU Standard C++ Library.

%package -n libstdc++-docs
Summary: GNU Standard C++ Library documentation
License: GFDL-1.3-or-later
%description -n libstdc++-docs
Documentation for the GNU Standard C++ Library.

%package -n libgomp
Summary: GCC OpenMP runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libgomp
GCC OpenMP runtime library.

%package -n libatomic
Summary: GCC atomic operations library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libatomic
GCC support library for atomic operations.

%package -n libitm
Summary: GNU Transactional Memory library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libitm
GNU Transactional Memory runtime library.

%package -n libitm-devel
Summary: GNU Transactional Memory headers
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libitm = %{version}-%{release}
Requires: gcc = %{version}-%{release}
%description -n libitm-devel
Headers for the GNU Transactional Memory library.

%package -n libitm-static
Summary: GNU Transactional Memory static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libitm-devel = %{version}-%{release}
%description -n libitm-static
Static GNU Transactional Memory library.

%package -n libasan
Summary: Address Sanitizer runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libasan
Address Sanitizer runtime library.

%package -n libasan-static
Summary: Address Sanitizer static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libasan = %{version}-%{release}
%description -n libasan-static
Static Address Sanitizer runtime library.

%package -n libhwasan
Summary: Hardware-assisted Address Sanitizer runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libhwasan
Hardware-assisted Address Sanitizer runtime library.

%package -n libhwasan-static
Summary: Hardware-assisted Address Sanitizer static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libhwasan = %{version}-%{release}
%description -n libhwasan-static
Static Hardware-assisted Address Sanitizer runtime library.

%package -n libtsan
Summary: Thread Sanitizer runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libtsan
Thread Sanitizer runtime library.

%package -n libtsan-static
Summary: Thread Sanitizer static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libtsan = %{version}-%{release}
%description -n libtsan-static
Static Thread Sanitizer runtime library.

%package -n liblsan
Summary: Leak Sanitizer runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n liblsan
Leak Sanitizer runtime library.

%package -n liblsan-static
Summary: Leak Sanitizer static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: liblsan = %{version}-%{release}
%description -n liblsan-static
Static Leak Sanitizer runtime library.

%package -n libubsan
Summary: Undefined Behavior Sanitizer runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libubsan
Undefined Behavior Sanitizer runtime library.

%package -n libubsan-static
Summary: Undefined Behavior Sanitizer static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libubsan = %{version}-%{release}
%description -n libubsan-static
Static Undefined Behavior Sanitizer runtime library.

%package -n libgfortran
Summary: GNU Fortran runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%ifarch x86_64
Requires: libquadmath = %{version}-%{release}
%endif
%description -n libgfortran
Fortran runtime library.

%package -n libgfortran-static
Summary: GNU Fortran static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgfortran = %{version}-%{release}
Requires: gcc-gfortran = %{version}-%{release}
%description -n libgfortran-static
Static Fortran runtime library.

%package -n libgphobos
Summary: GNU D runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libgphobos
D runtime library.

%package -n libgphobos-static
Summary: GNU D static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgphobos = %{version}-%{release}
%description -n libgphobos-static
Static D runtime library.

%package -n libgm2
Summary: GNU Modula-2 runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libgm2
Modula-2 runtime library.

%package -n libgm2-static
Summary: GNU Modula-2 static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgm2 = %{version}-%{release}
%description -n libgm2-static
Static Modula-2 runtime library.

%package -n libgcobol
Summary: GNU COBOL runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libgcobol
COBOL runtime library.

%package -n libgcobol-static
Summary: GNU COBOL static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcobol = %{version}-%{release}
%description -n libgcobol-static
Static COBOL runtime library.

%package -n libga68
Summary: GNU Algol 68 runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libga68
Algol 68 runtime library.

%package -n libga68-static
Summary: GNU Algol 68 static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libga68 = %{version}-%{release}
%description -n libga68-static
Static Algol 68 runtime library.

%package -n libgnat
Summary: GNU Ada runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libgnat
Ada runtime library.

%package -n libgnat-devel
Summary: GNU Ada development files
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgnat = %{version}-%{release}
Requires: gcc-gnat = %{version}-%{release}
%description -n libgnat-devel
Ada source and link files.

%package -n libgnat-static
Summary: GNU Ada static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgnat-devel = %{version}-%{release}
%description -n libgnat-static
Static Ada runtime library.

%package -n libgo
Summary: Go runtime
License: BSD-3-Clause
Requires: libgcc = %{version}-%{release}
%description -n libgo
Go runtime library.

%package -n libgo-devel
Summary: Go development files
License: BSD-3-Clause
Requires: libgo = %{version}-%{release}
Requires: gcc-go = %{version}-%{release}
%description -n libgo-devel
Go headers and link library.

%package -n libgo-static
Summary: Go static library
License: BSD-3-Clause
Requires: libgo-devel = %{version}-%{release}
%description -n libgo-static
Static Go runtime library.

%package -n libobjc
Summary: Objective-C runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libobjc
Objective-C runtime library.

%package -n libgccjit
Summary: GCC just-in-time library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libgccjit
Library for embedding GCC in a program.

%package -n libgccjit-devel
Summary: GCC just-in-time headers
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgccjit = %{version}-%{release}
%description -n libgccjit-devel
Headers for embedding GCC in a program.

%package -n libgdiagnostics
Summary: GCC diagnostics library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libgdiagnostics
Library for emitting compiler diagnostics.

%package -n libgdiagnostics-devel
Summary: GCC diagnostics headers
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgdiagnostics = %{version}-%{release}
%description -n libgdiagnostics-devel
Headers for the GCC diagnostics library.

%ifarch x86_64
%package -n libquadmath
Summary: GCC quad-precision math library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc = %{version}-%{release}
%description -n libquadmath
GCC __float128 math library.

%package -n libquadmath-devel
Summary: GCC quad-precision math headers
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libquadmath = %{version}-%{release}
Requires: gcc = %{version}-%{release}
%description -n libquadmath-devel
Headers for the GCC __float128 math library.

%package -n libquadmath-static
Summary: GCC quad-precision math static library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libquadmath-devel = %{version}-%{release}
%description -n libquadmath-static
Static GCC __float128 math library.

%package -n libgomp-offload-nvptx
Summary: OpenMP offload plugin for NVPTX
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgomp = %{version}-%{release}
%description -n libgomp-offload-nvptx
OpenMP offload plugin for Nvidia PTX.

%package -n libgomp-offload-amdgcn
Summary: OpenMP offload plugin for AMD GCN
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgomp = %{version}-%{release}
%description -n libgomp-offload-amdgcn
OpenMP offload plugin for AMD GCN.

%package -n gcc-offload-nvptx
Summary: GCC offloading compiler for NVPTX
Requires: gcc = %{version}-%{release}
Requires: libgomp-offload-nvptx = %{version}-%{release}
%description -n gcc-offload-nvptx
Offloading compiler for Nvidia PTX.

%package -n gcc-offload-amdgcn
Summary: GCC offloading compiler for AMD GCN
Requires: gcc = %{version}-%{release}
Requires: libgomp-offload-amdgcn = %{version}-%{release}
Requires: llvm
Requires: lld
%description -n gcc-offload-amdgcn
Offloading compiler for AMD GCN.
%endif
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%autosetup -p1
tar -xf %{SOURCE1} -C %{_builddir}
tar -xf %{SOURCE2} -C %{_builddir}
tar -xf %{SOURCE3} -C %{_builddir}

%build
unset CFLAGS CXXFLAGS FFLAGS FCFLAGS OBJCFLAGS GOFLAGS DFLAGS LDFLAGS
export CFLAGS="-O2 -g"
export CXXFLAGS="-O2 -g"
export CFLAGS_FOR_TARGET="-O2 -g"
export CXXFLAGS_FOR_TARGET="-O2 -g"
export FCFLAGS_FOR_TARGET="-O2 -g"
jobs=%{?_smp_build_ncpus}
if [ -z "$jobs" ]; then jobs=1; fi
src=%{_builddir}/gcc-%{version}
target=$("$src/config.guess")

step() {
  name=$1
  shift
  echo "oreon gcc step $name"
  log=%{_builddir}/gcc-step.log
  set -o pipefail
  if ! "$@" 2>&1 | tail -n 400 >"$log"; then
    set +o pipefail
    echo "oreon gcc step $name failed"
    cat "$log"
    exit 1
  fi
  set +o pipefail
  rm -f "$log"
}

common() {
  "$src/configure" \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --enable-threads=posix \
    --enable-checking=release \
    --with-system-zlib \
    --with-gcc-major-version-only \
    --disable-multilib \
    --disable-nls \
    --disable-libssp \
    "$@"
}

%if %{with bootstrap} || 0%{?bootstrap}
mkdir -p %{_builddir}/gcc-build
cd %{_builddir}/gcc-build
step bootstrap-configure common \
  --enable-languages=c \
  --disable-shared \
  --disable-threads \
  --disable-libstdcxx \
  --without-headers \
  --with-newlib \
  --disable-bootstrap \
  --disable-decimal-float \
  --disable-libgomp \
  --disable-libquadmath \
  --disable-libatomic \
  --disable-libvtv \
  --disable-libsanitizer \
  --disable-libitm
step bootstrap-make make -s -j"$jobs"
%else
%ifarch x86_64
ln -sfn %{_builddir}/newlib-cygwin-%{newlib_rev}/newlib "$src/newlib"
mkdir -p %{_builddir}/offload-root
cd %{_builddir}/nvptx-tools-%{nvptx_rev}
step nvptx-tools-configure ./configure --prefix=%{_prefix}
step nvptx-tools-make make -s -j"$jobs"
step nvptx-tools-install make -s install DESTDIR=%{_builddir}/offload-root

mkdir -p %{_builddir}/accel-nvptx
cd %{_builddir}/accel-nvptx
step nvptx-configure common \
  --enable-shared \
  --target=nvptx-none \
  --enable-as-accelerator-for="$target" \
  --enable-languages=c,c++,fortran,lto \
  --disable-bootstrap \
  --enable-threads=single \
  --disable-sjlj-exceptions \
  --with-newlib \
  --enable-newlib-io-long-long \
  --disable-libsanitizer \
  --with-build-time-tools=%{_builddir}/offload-root%{_prefix}/nvptx-none/bin
step nvptx-make make -s -j"$jobs"
step nvptx-install make -s install DESTDIR=%{_builddir}/offload-root

mkdir -p %{_builddir}/amdgcn-bin
ln -sfn %{_bindir}/llvm-ar %{_builddir}/amdgcn-bin/ar
ln -sfn %{_bindir}/llvm-ar %{_builddir}/amdgcn-bin/ranlib
ln -sfn %{_bindir}/llvm-mc %{_builddir}/amdgcn-bin/as
ln -sfn %{_bindir}/llvm-nm %{_builddir}/amdgcn-bin/nm
ln -sfn %{_bindir}/lld %{_builddir}/amdgcn-bin/ld
mkdir -p %{_builddir}/accel-amdgcn
cd %{_builddir}/accel-amdgcn
step amdgcn-configure common \
  --enable-shared \
  --target=amdgcn-amdhsa \
  --enable-as-accelerator-for="$target" \
  --enable-languages=c,c++,fortran,lto \
  --disable-bootstrap \
  --enable-threads=single \
  --disable-sjlj-exceptions \
  --with-newlib \
  --disable-libsanitizer \
  --with-build-time-tools=%{_builddir}/amdgcn-bin
step amdgcn-make make -s -j"$jobs"
step amdgcn-install make -s install DESTDIR=%{_builddir}/offload-root
rm -f "$src/newlib"
rm -rf \
  %{_builddir}/accel-nvptx \
  %{_builddir}/accel-amdgcn \
  %{_builddir}/nvptx-tools-%{nvptx_rev} \
  %{_builddir}/amdgcn-bin \
  %{_builddir}/newlib-cygwin-%{newlib_rev}
%endif

mkdir -p %{_builddir}/gcc-build
cd %{_builddir}/gcc-build
step host-configure common \
  --enable-shared \
  --with-linker-hash-style=gnu \
  --enable-languages=c,c++,fortran,objc,obj-c++,go,d,m2,cobol,algol68,ada,lto \
  --enable-default-pie \
  --enable-linker-build-id \
  --enable-bootstrap \
%ifarch x86_64
  --enable-offload-targets=nvptx-none=%{_builddir}/offload-root%{_prefix},amdgcn-amdhsa=%{_builddir}/offload-root%{_prefix} \
%else
  --disable-libquadmath \
%endif
  --disable-libvtv
step host-make make -s -j"$jobs" LDFLAGS_FOR_TARGET="-Wl,-z,relro,-z,now"
rm -rf stage1-*
step libstdcxx-docs make -s -C "$target/libstdc++-v3" doc-html-doxygen

mkdir -p %{_builddir}/gcc-jit
cd %{_builddir}/gcc-jit
step jit-configure common \
  --enable-shared \
  --with-linker-hash-style=gnu \
  --enable-languages=jit \
  --enable-host-shared \
  --enable-libgdiagnostics \
  --disable-bootstrap \
  --enable-linker-build-id \
  --enable-default-pie \
%ifnarch x86_64
  --disable-libquadmath \
%endif
  --disable-libvtv
step jit-make make -s -j"$jobs" all-gcc
%endif

%install
%if %{with bootstrap} || 0%{?bootstrap}
cd %{_builddir}/gcc-build
make -s install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist
%else
step() {
  name=$1
  shift
  echo "oreon gcc step $name"
  log=%{_builddir}/gcc-step.log
  set -o pipefail
  if ! "$@" 2>&1 | tail -n 400 >"$log"; then
    set +o pipefail
    echo "oreon gcc step $name failed"
    cat "$log"
    exit 1
  fi
  set +o pipefail
  rm -f "$log"
}
cd %{_builddir}/gcc-build
step host-install make -s install DESTDIR=%{buildroot} LDFLAGS_FOR_TARGET="-Wl,-z,relro,-z,now"
%ifarch x86_64
target=$(%{_builddir}/gcc-%{version}/config.guess)
off=%{_builddir}/offload-root%{_prefix}
dest=%{buildroot}%{_prefix}
mkdir -p "$dest/bin"
for b in "$off"/bin/nvptx-none-* "$off"/bin/amdgcn-amdhsa-*; do
  [ -e "$b" ] || continue
  cp -a "$b" "$dest/bin/"
done
for tree in nvptx-none amdgcn-amdhsa; do
  [ -d "$off/$tree" ] || continue
  mkdir -p "$dest/$tree"
  cp -a "$off/$tree/." "$dest/$tree/"
done
for src in "$off"/lib64/gcc/$target/*/accel "$off"/libexec/gcc/$target/*/accel \
  "$off"/lib64/gcc/nvptx-none "$off"/lib64/gcc/amdgcn-amdhsa \
  "$off"/libexec/gcc/nvptx-none "$off"/libexec/gcc/amdgcn-amdhsa; do
  [ -d "$src" ] || continue
  rel=${src#"$off/"}
  mkdir -p "$dest/$(dirname "$rel")"
  rm -rf "$dest/$rel"
  cp -a "$src" "$dest/$rel"
done
for acc in nvptx-none amdgcn-amdhsa; do
  for base in "$dest"/libexec/gcc/$target/*/accel/$acc "$dest"/lib64/gcc/$target/*/accel/$acc \
    "$dest"/libexec/gcc/$acc/* "$dest"/lib64/gcc/$acc/*; do
    [ -d "$base" ] || continue
    rm -rf "$base/install-tools" "$base/plugin" "$base/g++-mapper-server" \
      "$base/cc1" "$base/cc1plus" "$base/f951" "$base/include-fixed"
  done
  accdir=$(echo "$dest"/lib64/gcc/$target/*/accel/$acc)
  [ -d "$accdir" ] || continue
  if [ -d "$dest/$acc/lib" ]; then
    find "$dest/$acc/lib" \( -name '*.a' -o -name '*.spec' \) -print | while read f; do
      rel=${f#"$dest/$acc/lib/"}
      mkdir -p "$accdir/$(dirname "$rel")"
      mv -f "$f" "$accdir/$rel"
    done
  fi
  srcbase=$(echo "$dest"/lib64/gcc/$acc/*)
  if [ -d "$srcbase" ]; then
    find "$srcbase" \( -name '*.a' -o -name '*.spec' \) -print | while read f; do
      rel=${f#"$srcbase/"}
      mkdir -p "$accdir/$(dirname "$rel")"
      mv -f "$f" "$accdir/$rel"
    done
  fi
done
for d in "$dest"/lib64/gcc/nvptx-none "$dest"/lib64/gcc/amdgcn-amdhsa \
  "$dest"/lib64/gcc/$target/*/accel "$dest"/nvptx-none "$dest"/amdgcn-amdhsa; do
  [ -d "$d" ] || continue
  find "$d" -name '*.la' -delete
done
%endif
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir} %{buildroot}%{_bindir}
cp -a %{_builddir}/gcc-jit/gcc/libgccjit.so* %{buildroot}%{_libdir}/
cp -a %{_builddir}/gcc-%{version}/gcc/jit/libgccjit*.h %{buildroot}%{_includedir}/
cp -a %{_builddir}/gcc-jit/gcc/libgdiagnostics.so* %{buildroot}%{_libdir}/
cp -a %{_builddir}/gcc-%{version}/gcc/libgdiagnostics*.h %{buildroot}%{_includedir}/
cp -a %{_builddir}/gcc-jit/gcc/sarif-replay %{buildroot}%{_bindir}/
if [ -f %{_builddir}/gcc-jit/gcc/doc/libgccjit.info ]; then
  mkdir -p %{buildroot}%{_infodir}
  cp -a %{_builddir}/gcc-jit/gcc/doc/libgccjit.info %{buildroot}%{_infodir}/
fi
rm -rf %{_builddir}/gcc-jit
find %{buildroot} -name '*.a' > %{_builddir}/gcc-archives
while read a; do
  member=$(ar t "$a" 2>/dev/null | head -1 || true)
  [ -n "$member" ] || continue
  ar p "$a" "$member" > %{_builddir}/gcc-ar-member.o 2>/dev/null || continue
  if file -b %{_builddir}/gcc-ar-member.o | grep -Eq 'x86-64|80386|ARM aarch64'; then
    strip -g "$a" || exit 1
  fi
done < %{_builddir}/gcc-archives
rm -f %{_builddir}/gcc-ar-member.o
target=$(%{_builddir}/gcc-%{version}/config.guess)
doc=%{_builddir}/gcc-build/$target/libstdc++-v3/doc/doxygen/html
if ! test -d "$doc"; then
  echo "missing libstdc++ docs $doc"
  exit 1
fi
mkdir -p %{buildroot}%{_docdir}/libstdc++-docs
cp -a "$doc" %{buildroot}%{_docdir}/libstdc++-docs/html
plug=$(echo %{buildroot}%{_libdir}/gcc/*/*/plugin)
test -d "$plug"
pin=$plug/include
test -d "$pin"
b=%{_builddir}/gcc-build
flags=$b/$target/libstdc++-v3/scripts/testsuite_flags
test -x "$flags"
libs=
for d in \
  "$b/prev-$target/libstdc++-v3/src/.libs" \
  "$b/$target/libstdc++-v3/src/.libs" \
  "$b/$target/libgcc/.libs" \
  "$b/gcc"
do
  [ -d "$d" ] || continue
  libs=${libs:+$libs:}$d
done
unset CFLAGS CXXFLAGS FFLAGS FCFLAGS OBJCFLAGS LDFLAGS
export CFLAGS="-O2 -g -I$pin"
export CXXFLAGS="-O2 -g -I$pin $($flags --build-includes)"
export LDFLAGS="-L$b/$target/libstdc++-v3/src/.libs -L$b/$target/libstdc++-v3/libsupc++/.libs"
export LD_LIBRARY_PATH="$libs"
mkdir -p %{_builddir}/annobin-build
cd %{_builddir}/annobin-build
CC="$b/gcc/xgcc -B$b/gcc/ -B$b/$target/libgcc/" \
CXX="$b/gcc/xg++ -B$b/gcc/ -B$b/$target/libgcc/ -B$b/$target/libstdc++-v3/src/.libs -B$b/$target/libstdc++-v3/libsupc++/.libs -L$b/$target/libstdc++-v3/src/.libs -L$b/$target/libstdc++-v3/libsupc++/.libs" \
%{_builddir}/annobin-%{annobin_ver}/configure \
  --prefix=%{_prefix} \
  --with-gcc-plugin-dir="${plug#%{buildroot}}" \
  --with-clang-plugin=no \
  --with-llvm-plugin=no \
  --without-annocheck \
  --without-docs \
  --without-tests \
  --without-debuginfod \
  --disable-rpath
make -s -j%{?_smp_build_ncpus}
make -s install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_libdir}/gcc/*/*/install-tools
rm -rf %{buildroot}%{_libexecdir}/gcc/*/*/install-tools

out=%{_builddir}/gcc-split
rm -rf "$out"
mkdir -p "$out"
miss=%{_builddir}/gcc.miss
: > "$miss"
ROOT=%{buildroot}

classify() {
  rel=$1
  bn=${rel##*/}
  case $rel in
    %{_docdir}/libstdc++-docs|%{_docdir}/libstdc++-docs/*) echo libstdc++-docs; return ;;
    %{_prefix}/nvptx-none/*|%{_bindir}/nvptx-none-*|*accel-nvptx-none-*|*/accel/nvptx-none/*|%{_libdir}/gcc/nvptx-none/*|%{_libexecdir}/gcc/nvptx-none/*) echo gcc-offload-nvptx; return ;;
    %{_prefix}/amdgcn-amdhsa/*|%{_bindir}/amdgcn-amdhsa-*|*accel-amdgcn-amdhsa-*|*/accel/amdgcn-amdhsa/*|%{_libdir}/gcc/amdgcn-amdhsa/*|%{_libexecdir}/gcc/amdgcn-amdhsa/*) echo gcc-offload-amdgcn; return ;;
    */plugin/annobin.so*|*/plugin/gcc-annobin.so*) echo gcc-plugin-annobin; return ;;
    */plugin/libcc1plugin.so*|*/plugin/libcp1plugin.so*|*/libcc1.so*) echo gcc-gdb-plugin; return ;;
    */plugin/include/*|*/plugin/*.h|*/plugin/gtype.state) echo gcc-plugin-devel; return ;;
    */plugin/liblto_plugin.so*) echo gcc; return ;;
    */include/c++/*) echo libstdc++-devel; return ;;
    */include/objc/*) echo gcc-objc; return ;;
    */adainclude/*) echo libgnat-devel; return ;;
    %{_prefix}/lib/go/*|%{_libdir}/go/*) echo libgo-devel; return ;;
    */share/gcc-*/python/*) echo libstdc++; return ;;
    */auto-load/*libstdc++*) echo libstdc++; return ;;
    */auto-load/*libgfortran*) echo libgfortran; return ;;
    */auto-load/*libgomp*) echo libgomp; return ;;
    */auto-load/*libgcc*) echo libgcc; return ;;
    */auto-load/*libobjc*) echo libobjc; return ;;
    */auto-load/*libgnat*|*/auto-load/*libgnarl*) echo libgnat; return ;;
    %{_docdir}/annobin*|%{_docdir}/annobin*/*) echo gcc-plugin-annobin; return ;;
    */gfortran/*) echo gcc-gfortran; return ;;
  esac
  name=$bn
  case $name in
    "$target"-*) name=${name#"$target-"} ;;
  esac
  case $name in
    cc1) echo cpp; return ;;
    cc1plus|g++-mapper-server) echo gcc-c++; return ;;
    cc1obj) echo gcc-objc; return ;;
    cc1objplus) echo gcc-objc++; return ;;
    f951) echo gcc-gfortran; return ;;
    d21) echo gcc-gdc; return ;;
    cc1gm2|gm2l) echo gcc-gm2; return ;;
    cobol1) echo gcc-gcobol; return ;;
    a681) echo gcc-algol68; return ;;
    gnat1) echo gcc-gnat; return ;;
    go1) echo gcc-go; return ;;
    lto1|collect2|lto-wrapper) echo gcc; return ;;
    cpp) echo cpp; return ;;
    gcc|gcc-[0-9]*|gcc-ar|gcc-nm|gcc-ranlib|gcov|gcov-dump|gcov-tool|lto-dump|c89|c99) echo gcc; return ;;
    g++|c++) echo gcc-c++; return ;;
    gfortran) echo gcc-gfortran; return ;;
    gdc) echo gcc-gdc; return ;;
    gm2) echo gcc-gm2; return ;;
    gcobol|gcobc) echo gcc-gcobol; return ;;
    ga68) echo gcc-algol68; return ;;
    gccgo|go|gofmt) echo gcc-go; return ;;
    gnat|gnatbind|gnatmake|gnatlink|gnatls|gnatchop|gnatkr|gnatname|gnatprep|gnatclean|gnatsym|gnatdll) echo gcc-gnat; return ;;
    sarif-replay) echo libgdiagnostics; return ;;
    libgcc_s*) echo libgcc; return ;;
    libsanitizer.spec) echo gcc; return ;;
    libstdc++.so.[0-9]*) echo libstdc++; return ;;
    libstdc++.so|libstdc++.modules.json) echo libstdc++-devel; return ;;
    *libstdc++*-gdb.py) echo libstdc++; return ;;
    *libgfortran*-gdb.py) echo libgfortran; return ;;
    *libgomp*-gdb.py) echo libgomp; return ;;
    *libgcc*-gdb.py) echo libgcc; return ;;
    *libobjc*-gdb.py) echo libobjc; return ;;
    *libgnat*-gdb.py|*libgnarl*-gdb.py) echo libgnat; return ;;
    libstdc++*.a|libsupc++*.a) echo libstdc++-static; return ;;
    libgomp-plugin-nvptx.so*) echo libgomp-offload-nvptx; return ;;
    libgomp-plugin-gcn.so*) echo libgomp-offload-amdgcn; return ;;
    libgomp.so*|libgomp.a|libgomp.spec|omp.h|openacc.h|omp_lib.h|omp_lib.mod|omp_lib.f90|oacc_lib.h) echo libgomp; return ;;
    libatomic*) echo libatomic; return ;;
    libitm.so.[0-9]*) echo libitm; return ;;
    libitm.so) echo libitm-devel; return ;;
    libitm.a|libitm.spec) echo libitm-static; return ;;
    libasan.so*|libasan.spec|libasan_preinit.o) echo libasan; return ;;
    libasan.a) echo libasan-static; return ;;
    libhwasan.so*|libhwasan.spec|libhwasan_preinit.o) echo libhwasan; return ;;
    libhwasan.a) echo libhwasan-static; return ;;
    libtsan.so*|libtsan.spec|libtsan_preinit.o) echo libtsan; return ;;
    libtsan.a) echo libtsan-static; return ;;
    liblsan.so*|liblsan.spec|liblsan_preinit.o) echo liblsan; return ;;
    liblsan.a) echo liblsan-static; return ;;
    libubsan.so*|libubsan.spec) echo libubsan; return ;;
    libubsan.a) echo libubsan-static; return ;;
    libquadmath.so.[0-9]*) echo libquadmath; return ;;
    libquadmath.so|quadmath.h|quadmath_weak.h) echo libquadmath-devel; return ;;
    libquadmath.a) echo libquadmath-static; return ;;
    libgfortran.so*|libgfortran.spec) echo libgfortran; return ;;
    libgfortran.a) echo libgfortran-static; return ;;
    libgphobos.so*|libgdruntime.so*) echo libgphobos; return ;;
    libgphobos.a|libgdruntime.a) echo libgphobos-static; return ;;
    libgm2.so*|libm2*.so.[0-9]*) echo libgm2; return ;;
    libm2*.so) echo gcc-gm2; return ;;
    libgm2.a|libm2*.a) echo libgm2-static; return ;;
    libgcobol.so*) echo libgcobol; return ;;
    libgcobol.a) echo libgcobol-static; return ;;
    libga68.so*) echo libga68; return ;;
    libga68.a) echo libga68-static; return ;;
    libgnat.so|libgnarl.so) echo libgnat-devel; return ;;
    libgnat.a|libgnarl.a) echo libgnat-static; return ;;
    libgnat*|libgnarl*) echo libgnat; return ;;
    libgo.so.[0-9]*) echo libgo; return ;;
    libgo.so) echo libgo-devel; return ;;
    libgo.a|libgobegin.a|libgolibbegin.a) echo libgo-static; return ;;
    libobjc.so*|libobjc.a) echo libobjc; return ;;
    libgccjit.so.[0-9]*) echo libgccjit; return ;;
    libgccjit.so|libgccjit*.h|libgccjit.a) echo libgccjit-devel; return ;;
    libgdiagnostics.so.[0-9]*) echo libgdiagnostics; return ;;
    libgdiagnostics.so|libgdiagnostics*.h|libgdiagnostics.a) echo libgdiagnostics-devel; return ;;
    itm.h|itm2.h) echo libitm-devel; return ;;
    fsf-funding.7|gfdl.7|gpl.7) echo gcc; return ;;
  esac
  info=$name
  info=${info%.gz}
  case $info in
    cpp.*) echo cpp; return ;;
    g++.*) echo gcc-c++; return ;;
    gcc.*|gccint.*|gccinstall.*|cppinternals.*|gcov.*|gcov-dump.*|gcov-tool.*|lto-dump.*) echo gcc; return ;;
    gfortran.*|libgfortran.*) echo gcc-gfortran; return ;;
    gdc.*|libgphobos.*) echo gcc-gdc; return ;;
    gm2.*|libgm2.*|m2.*) echo gcc-gm2; return ;;
    gcobol*|libgcobol.*) echo gcc-gcobol; return ;;
    ga68*|libga68.*) echo gcc-algol68; return ;;
    gccgo.*|libgo.*|go.*|gofmt.*) echo gcc-go; return ;;
    gnat*|libgnat.*) echo gcc-gnat; return ;;
    libgomp.*) echo libgomp; return ;;
    libquadmath.*) echo libquadmath; return ;;
    libitm.*) echo libitm; return ;;
    libgccjit.*) echo libgccjit-devel; return ;;
    libgdiagnostics.*) echo libgdiagnostics-devel; return ;;
  esac
  case $rel in
    %{_prefix}/lib/gcc/*|%{_libdir}/gcc/*|%{_libexecdir}/gcc/*) echo gcc; return ;;
  esac
  return 1
}

set +x
find "$ROOT" -print | sort | while read p; do
  rel=${p#"$ROOT"}
  [ -n "$rel" ] || continue
  if [ -d "$p" ]; then
    continue
  fi
  entry=$rel
  case $rel in
    *.1|*.3|*.7|*.info|*.info-[0-9]*|*.py) entry="${rel}*" ;;
    *.1.gz|*.3.gz|*.7.gz|*.info.gz) entry="${rel%.gz}*" ;;
  esac
  pkg=$(classify "$rel") || { echo "$rel" >> "$miss"; continue; }
  printf '%%s\n' "$entry" >> "$out/$pkg.files"
done
if [ -s "$miss" ]; then
  echo "unpackaged gcc files:" >&2
  cat "$miss" >&2
  exit 1
fi

skip="|%{_prefix}|%{_bindir}|%{_libdir}|/usr/lib|%{_includedir}|%{_datadir}|%{_mandir}|%{_infodir}|%{_docdir}|%{_libexecdir}|%{_mandir}/man1|%{_mandir}/man3|%{_mandir}/man7|"
find "$ROOT" -type d | sort | while read p; do
  rel=${p#"$ROOT"}
  [ -n "$rel" ] || continue
  case $skip in
    *"|$rel|"*) continue ;;
  esac
  owner=
  best=0
  for list in "$out"/*.files; do
    n=$(grep -F -c "${rel}/" "$list" || true)
    if [ "$n" -gt "$best" ]; then
      best=$n
      owner=$(basename "$list" .files)
    fi
  done
  if [ -n "$owner" ]; then
    echo "%%dir $rel" >> "$out/$owner.files"
  fi
done

req="cpp gcc gcc-c++ gcc-objc gcc-objc++ gcc-gfortran gcc-gdc gcc-gm2 gcc-gcobol gcc-algol68 gcc-gnat gcc-go gcc-gdb-plugin gcc-plugin-devel gcc-plugin-annobin libgcc libstdc++ libstdc++-devel libstdc++-static libstdc++-docs libgomp libatomic libitm libitm-devel libitm-static libasan libasan-static libhwasan libhwasan-static libtsan libtsan-static liblsan liblsan-static libubsan libubsan-static libgfortran libgfortran-static libgphobos libgphobos-static libgm2 libgm2-static libgcobol libgcobol-static libga68 libga68-static libgnat libgnat-devel libgnat-static libgo libgo-devel libgo-static libobjc libgccjit libgccjit-devel libgdiagnostics libgdiagnostics-devel"
%ifarch x86_64
req="$req libquadmath libquadmath-devel libquadmath-static libgomp-offload-nvptx libgomp-offload-amdgcn gcc-offload-nvptx gcc-offload-amdgcn"
%endif
for n in $req; do
  if ! test -s "$out/$n.files"; then
    echo "empty gcc package $n"
    exit 1
  fi
done
%endif

%if %{without bootstrap} && !0%{?bootstrap}
%files -f %{_builddir}/gcc-split/gcc.files
%license COPYING3

%files -n cpp -f %{_builddir}/gcc-split/cpp.files
%license COPYING3
%files -n gcc-c++ -f %{_builddir}/gcc-split/gcc-c++.files
%license COPYING3
%files -n gcc-objc -f %{_builddir}/gcc-split/gcc-objc.files
%license COPYING3
%files -n gcc-objc++ -f %{_builddir}/gcc-split/gcc-objc++.files
%license COPYING3
%files -n gcc-gfortran -f %{_builddir}/gcc-split/gcc-gfortran.files
%license COPYING3
%files -n gcc-gdc -f %{_builddir}/gcc-split/gcc-gdc.files
%license COPYING3
%files -n gcc-gm2 -f %{_builddir}/gcc-split/gcc-gm2.files
%license COPYING3
%files -n gcc-gcobol -f %{_builddir}/gcc-split/gcc-gcobol.files
%license COPYING3
%files -n gcc-algol68 -f %{_builddir}/gcc-split/gcc-algol68.files
%license COPYING3
%files -n gcc-gnat -f %{_builddir}/gcc-split/gcc-gnat.files
%license COPYING3
%files -n gcc-go -f %{_builddir}/gcc-split/gcc-go.files
%license COPYING3
%files -n gcc-gdb-plugin -f %{_builddir}/gcc-split/gcc-gdb-plugin.files
%license COPYING3
%files -n gcc-plugin-devel -f %{_builddir}/gcc-split/gcc-plugin-devel.files
%license COPYING3
%files -n gcc-plugin-annobin -f %{_builddir}/gcc-split/gcc-plugin-annobin.files
%license COPYING3
%files -n libgcc -f %{_builddir}/gcc-split/libgcc.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libstdc++ -f %{_builddir}/gcc-split/libstdc++.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libstdc++-devel -f %{_builddir}/gcc-split/libstdc++-devel.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libstdc++-static -f %{_builddir}/gcc-split/libstdc++-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libstdc++-docs -f %{_builddir}/gcc-split/libstdc++-docs.files
%files -n libgomp -f %{_builddir}/gcc-split/libgomp.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libatomic -f %{_builddir}/gcc-split/libatomic.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libitm -f %{_builddir}/gcc-split/libitm.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libitm-devel -f %{_builddir}/gcc-split/libitm-devel.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libitm-static -f %{_builddir}/gcc-split/libitm-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libasan -f %{_builddir}/gcc-split/libasan.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libasan-static -f %{_builddir}/gcc-split/libasan-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libhwasan -f %{_builddir}/gcc-split/libhwasan.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libhwasan-static -f %{_builddir}/gcc-split/libhwasan-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libtsan -f %{_builddir}/gcc-split/libtsan.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libtsan-static -f %{_builddir}/gcc-split/libtsan-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n liblsan -f %{_builddir}/gcc-split/liblsan.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n liblsan-static -f %{_builddir}/gcc-split/liblsan-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libubsan -f %{_builddir}/gcc-split/libubsan.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libubsan-static -f %{_builddir}/gcc-split/libubsan-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgfortran -f %{_builddir}/gcc-split/libgfortran.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgfortran-static -f %{_builddir}/gcc-split/libgfortran-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgphobos -f %{_builddir}/gcc-split/libgphobos.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgphobos-static -f %{_builddir}/gcc-split/libgphobos-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgm2 -f %{_builddir}/gcc-split/libgm2.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgm2-static -f %{_builddir}/gcc-split/libgm2-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgcobol -f %{_builddir}/gcc-split/libgcobol.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgcobol-static -f %{_builddir}/gcc-split/libgcobol-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libga68 -f %{_builddir}/gcc-split/libga68.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libga68-static -f %{_builddir}/gcc-split/libga68-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgnat -f %{_builddir}/gcc-split/libgnat.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgnat-devel -f %{_builddir}/gcc-split/libgnat-devel.files
%license COPYING3
%files -n libgnat-static -f %{_builddir}/gcc-split/libgnat-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgo -f %{_builddir}/gcc-split/libgo.files
%license libgo/LICENSE
%files -n libgo-devel -f %{_builddir}/gcc-split/libgo-devel.files
%license libgo/LICENSE
%files -n libgo-static -f %{_builddir}/gcc-split/libgo-static.files
%license libgo/LICENSE
%files -n libobjc -f %{_builddir}/gcc-split/libobjc.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgccjit -f %{_builddir}/gcc-split/libgccjit.files
%license COPYING3
%files -n libgccjit-devel -f %{_builddir}/gcc-split/libgccjit-devel.files
%license COPYING3
%files -n libgdiagnostics -f %{_builddir}/gcc-split/libgdiagnostics.files
%license COPYING3
%files -n libgdiagnostics-devel -f %{_builddir}/gcc-split/libgdiagnostics-devel.files
%license COPYING3
%ifarch x86_64
%files -n libquadmath -f %{_builddir}/gcc-split/libquadmath.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libquadmath-devel -f %{_builddir}/gcc-split/libquadmath-devel.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libquadmath-static -f %{_builddir}/gcc-split/libquadmath-static.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgomp-offload-nvptx -f %{_builddir}/gcc-split/libgomp-offload-nvptx.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n libgomp-offload-amdgcn -f %{_builddir}/gcc-split/libgomp-offload-amdgcn.files
%license COPYING.RUNTIME COPYING3.LIB
%files -n gcc-offload-nvptx -f %{_builddir}/gcc-split/gcc-offload-nvptx.files
%license COPYING3
%files -n gcc-offload-amdgcn -f %{_builddir}/gcc-split/gcc-offload-amdgcn.files
%license COPYING3
%endif
%else
%files -f %{_builddir}/gcc.files
%license COPYING3
%endif
