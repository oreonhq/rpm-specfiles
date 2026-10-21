%global source0_hash e6738e29597f733270731aa90600f37ffdc045079dfc27ec7e8192cc81085c3e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gcc
Version: 16.2.0
Release: 2%{?dist}
Summary: GNU Compiler Collection (GCC)
License: GPL-3.0-or-later
URL: https://gcc.gnu.org/
Source0: https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: binutils
BuildRequires: gmp-devel
BuildRequires: mpfr-devel
BuildRequires: mpc-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: glibc-devel
BuildRequires: zlib-devel
BuildRequires: kernel-headers
Requires: binutils%{?_isa}
Requires: cpp%{?_isa} = %{version}-%{release}
Requires: glibc-devel%{?_isa}
Requires: libgcc%{?_isa} = %{version}-%{release}
%endif

%description
This directory contains the GNU Compiler Collection (GCC).

%if %{without bootstrap} && !0%{?bootstrap}
%package -n cpp
Summary: GNU C preprocessor
License: GPL-3.0-or-later
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n cpp
GNU C preprocessor.

%package -n gcc-c++
Summary: GNU C++ compiler
License: GPL-3.0-or-later
Requires: gcc%{?_isa} = %{version}-%{release}
Requires: libstdc++-devel%{?_isa} = %{version}-%{release}
%description -n gcc-c++
GNU C++ compiler.

%package -n gcc-plugin-devel
Summary: GCC plugin headers
License: GPL-3.0-or-later
Requires: gcc%{?_isa} = %{version}-%{release}
%description -n gcc-plugin-devel
Headers and generator for GCC plugins.

%package -n libgcc
Summary: GCC shared support library
License: GPL-3.0-or-later WITH GCC-exception-3.1
%description -n libgcc
GCC shared support library.

%package -n libstdc++
Summary: GNU C++ standard library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n libstdc++
GNU C++ standard library.

%package -n libstdc++-devel
Summary: GNU C++ standard library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: gcc%{?_isa} = %{version}-%{release}
Requires: libstdc++%{?_isa} = %{version}-%{release}
%description -n libstdc++-devel
GNU C++ standard library headers and link library.

%package -n libstdc++-static
Summary: GNU C++ standard library
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libstdc++-devel%{?_isa} = %{version}-%{release}
%description -n libstdc++-static
GNU C++ standard library static archives.

%package -n libgomp
Summary: GCC OpenMP runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n libgomp
GCC OpenMP runtime.

%package -n libgomp-devel
Summary: GCC OpenMP runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgomp%{?_isa} = %{version}-%{release}
%description -n libgomp-devel
GCC OpenMP link library.

%package -n libatomic
Summary: GCC atomic runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n libatomic
GCC atomic runtime.

%package -n libatomic-devel
Summary: GCC atomic runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libatomic%{?_isa} = %{version}-%{release}
%description -n libatomic-devel
GCC atomic link library.

%package -n libitm
Summary: GCC transactional memory runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n libitm
GCC transactional memory runtime.

%package -n libitm-devel
Summary: GCC transactional memory runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libitm%{?_isa} = %{version}-%{release}
%description -n libitm-devel
GCC transactional memory link library.

%package -n libssp
Summary: GCC stack smashing protection runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n libssp
GCC stack smashing protection runtime.

%package -n libssp-devel
Summary: GCC stack smashing protection runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libssp%{?_isa} = %{version}-%{release}
%description -n libssp-devel
GCC stack smashing protection link library.

%ifarch x86_64
%package -n libquadmath
Summary: GCC quad-precision math runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n libquadmath
GCC quad-precision math runtime.

%package -n libquadmath-devel
Summary: GCC quad-precision math runtime
License: GPL-3.0-or-later WITH GCC-exception-3.1
Requires: libquadmath%{?_isa} = %{version}-%{release}
%description -n libquadmath-devel
GCC quad-precision math link library.
%endif

%package -n libcc1
Summary: GCC library for GDB
License: GPL-3.0-or-later
Requires: gcc%{?_isa} = %{version}-%{release}
Requires: libgcc%{?_isa} = %{version}-%{release}
%description -n libcc1
GCC library used by GDB to call the compiler.

%package -n libcc1-devel
Summary: GCC library for GDB
License: GPL-3.0-or-later
Requires: gcc-plugin-devel%{?_isa} = %{version}-%{release}
Requires: libcc1%{?_isa} = %{version}-%{release}
%description -n libcc1-devel
Link library for the GCC GDB plugin.
%endif

%prep
%oreon_sha256
%autosetup -p1

%build
# fortify flags break this build
unset CFLAGS CXXFLAGS LDFLAGS
mkdir -p %{_builddir}/gcc-build
cd %{_builddir}/gcc-build
%if %{with bootstrap} || 0%{?bootstrap}
%{_builddir}/gcc-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --mandir=%{_mandir} \
  --enable-languages=c \
  --disable-shared \
  --disable-threads \
  --disable-libstdcxx \
  --without-headers \
  --with-newlib \
  --disable-bootstrap \
  --disable-multilib \
  --disable-nls \
  --disable-decimal-float \
  --disable-libgomp \
  --disable-libquadmath \
  --disable-libatomic \
  --disable-libssp \
  --disable-libvtv \
  --disable-libsanitizer \
  --disable-libitm
%else
%{_builddir}/gcc-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --mandir=%{_mandir} \
  --enable-languages=c,c++ \
  --enable-shared \
  --enable-threads=posix \
  --enable-default-pie \
  --with-system-zlib \
  --with-linker-hash-style=gnu \
  --disable-bootstrap \
  --disable-multilib \
  --disable-nls \
  --disable-libsanitizer
%endif
make -s -j%{?_smp_build_ncpus}

%install
cd %{_builddir}/gcc-build
make -s install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name '*.la' -delete
%if %{with bootstrap} || 0%{?bootstrap}
%oreon_filelist
%else
if [ ! -e %{buildroot}%{_libdir}/libquadmath.so.0 ]; then
  rm -f %{buildroot}%{_infodir}/libquadmath.info*
fi
out=%{_builddir}
rm -f "$out"/*.files
: > "$out/gcc.miss"
add() { printf '%%s\n' "$2" >> "$out/$1.files"; }
find %{buildroot} \( -type f -o -type l \) | sort | while read -r path; do
  rel=${path#%{buildroot}}
  case "$rel" in
    /usr/share/licenses/*) continue ;;
    /usr/share/man/man1/cpp.1*) add cpp "%{_mandir}/man1/cpp.1*" ;;
    /usr/share/man/man1/g++.1*) add gcc-c++ "%{_mandir}/man1/g++.1*" ;;
    /usr/share/man/man1/gcc.1*) add gcc "%{_mandir}/man1/gcc.1*" ;;
    /usr/share/man/man1/gcov.1*) add gcc "%{_mandir}/man1/gcov.1*" ;;
    /usr/share/man/man1/gcov-dump.1*) add gcc "%{_mandir}/man1/gcov-dump.1*" ;;
    /usr/share/man/man1/gcov-tool.1*) add gcc "%{_mandir}/man1/gcov-tool.1*" ;;
    /usr/share/man/man1/lto-dump.1*) add gcc "%{_mandir}/man1/lto-dump.1*" ;;
    /usr/share/man/man7/*) add gcc "%{_mandir}/man7/*" ;;
    /usr/share/info/libgomp.info*) add libgomp "%{_infodir}/libgomp.info*" ;;
    /usr/share/info/libitm.info*) add libitm "%{_infodir}/libitm.info*" ;;
    /usr/share/info/libquadmath.info*) add libquadmath "%{_infodir}/libquadmath.info*" ;;
    %{_includedir}/c++/*) add libstdc++-devel "$rel" ;;
    %{_datadir}/gcc-%{version}/python/*) add libstdc++ "$rel" ;;
    %{_bindir}/cpp) add cpp "$rel" ;;
    %{_bindir}/g++|%{_bindir}/c++) add gcc-c++ "$rel" ;;
    *-g++|*-c++) add gcc-c++ "$rel" ;;
    %{_bindir}/gcc|%{_bindir}/gcc-ar|%{_bindir}/gcc-nm|%{_bindir}/gcc-ranlib|%{_bindir}/gcov|%{_bindir}/gcov-dump|%{_bindir}/gcov-tool|%{_bindir}/lto-dump) add gcc "$rel" ;;
    *-gcc|*-gcc-*) add gcc "$rel" ;;
    %{_libexecdir}/gcc/*/cc1) add cpp "$rel" ;;
    %{_libexecdir}/gcc/*/cc1plus|%{_libexecdir}/gcc/*/g++-mapper-server) add gcc-c++ "$rel" ;;
    %{_libexecdir}/gcc/*/plugin/*) add gcc-plugin-devel "$rel" ;;
    %{_libexecdir}/gcc/*) add gcc "$rel" ;;
    %{_libdir}/gcc/*/include/quadmath.h|%{_libdir}/gcc/*/include/quadmath_weak.h) add libquadmath-devel "$rel" ;;
    %{_libdir}/gcc/*/include/ssp/*) add libssp-devel "$rel" ;;
    %{_libdir}/gcc/*/plugin/libcc1plugin.so.*) add libcc1 "$rel" ;;
    %{_libdir}/gcc/*/plugin/libcc1plugin.so) add libcc1-devel "$rel" ;;
    %{_libdir}/gcc/*/plugin/*) add gcc-plugin-devel "$rel" ;;
    %{_libdir}/gcc/*) add gcc "$rel" ;;
    %{_libdir}/libgcc_s.so.*) add libgcc "$rel" ;;
    %{_libdir}/libgcc_s.so|%{_libdir}/libgcc_s_asneeded.so) add gcc "$rel" ;;
    %{_libdir}/libstdc++.so.*) add libstdc++ "$rel" ;;
    %{_libdir}/libstdc++.so|%{_libdir}/libstdc++.modules.json) add libstdc++-devel "$rel" ;;
    %{_libdir}/libstdc++.a|%{_libdir}/libstdc++fs.a|%{_libdir}/libstdc++exp.a|%{_libdir}/libsupc++.a) add libstdc++-static "$rel" ;;
    %{_libdir}/libgomp.so.*) add libgomp "$rel" ;;
    %{_libdir}/libgomp.so|%{_libdir}/libgomp.a|%{_libdir}/libgomp.spec) add libgomp-devel "$rel" ;;
    %{_libdir}/libatomic.so.*) add libatomic "$rel" ;;
    %{_libdir}/libatomic.so|%{_libdir}/libatomic.a|%{_libdir}/libatomic_asneeded.a|%{_libdir}/libatomic_asneeded.so) add libatomic-devel "$rel" ;;
    %{_libdir}/libitm.so.*) add libitm "$rel" ;;
    %{_libdir}/libitm.so|%{_libdir}/libitm.a|%{_libdir}/libitm.spec) add libitm-devel "$rel" ;;
    %{_libdir}/libssp.so.*) add libssp "$rel" ;;
    %{_libdir}/libssp.so|%{_libdir}/libssp.a|%{_libdir}/libssp_nonshared.a) add libssp-devel "$rel" ;;
    %{_libdir}/libquadmath.so.*) add libquadmath "$rel" ;;
    %{_libdir}/libquadmath.so|%{_libdir}/libquadmath.a) add libquadmath-devel "$rel" ;;
    %{_libdir}/libcc1.so.*) add libcc1 "$rel" ;;
    %{_libdir}/libcc1.so) add libcc1-devel "$rel" ;;
    *) echo "$rel" >> "$out/gcc.miss" ;;
  esac
done
if [ -s "$out/gcc.miss" ]; then
  cat "$out/gcc.miss" >&2
  exit 1
fi
find %{buildroot} -type d | sort | while read -r d; do
  rel=${d#%{buildroot}}
  [ -n "$rel" ] || continue
  case "$rel" in
    /usr|/usr/bin|%{_libdir}|/usr/lib|%{_includedir}|%{_datadir}|%{_mandir}|%{_mandir}/*|%{_infodir}|%{_libexecdir}) continue ;;
  esac
  owner=
  case "$rel" in
    %{_includedir}/c++|%{_includedir}/c++/*) owner=libstdc++-devel ;;
    */include/ssp|*/include/ssp/*) owner=libssp-devel ;;
    */plugin|*/plugin/*) owner=gcc-plugin-devel ;;
    %{_datadir}/gcc-%{version}|%{_datadir}/gcc-%{version}/*) owner=libstdc++ ;;
    %{_libexecdir}/gcc|%{_libexecdir}/gcc/*|%{_libdir}/gcc|%{_libdir}/gcc/*) owner=gcc ;;
  esac
  [ -n "$owner" ] || continue
  echo "%%dir $rel" >> "$out/$owner.files"
done
for f in "$out"/*.files; do
  sort -u -o "$f" "$f"
done
for need in gcc cpp gcc-c++ gcc-plugin-devel libgcc libstdc++ libstdc++-devel libstdc++-static libgomp libgomp-devel libatomic libatomic-devel libitm libitm-devel libssp libssp-devel libcc1 libcc1-devel; do
  test -s "$out/$need.files"
done
%endif

%files -f %{_builddir}/gcc.files
%license COPYING3

%if %{without bootstrap} && !0%{?bootstrap}
%files -n cpp -f %{_builddir}/cpp.files
%license COPYING3

%files -n gcc-c++ -f %{_builddir}/gcc-c++.files
%license COPYING3

%files -n gcc-plugin-devel -f %{_builddir}/gcc-plugin-devel.files
%license COPYING3

%files -n libgcc -f %{_builddir}/libgcc.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libstdc++ -f %{_builddir}/libstdc++.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libstdc++-devel -f %{_builddir}/libstdc++-devel.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libstdc++-static -f %{_builddir}/libstdc++-static.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libgomp -f %{_builddir}/libgomp.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libgomp-devel -f %{_builddir}/libgomp-devel.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libatomic -f %{_builddir}/libatomic.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libatomic-devel -f %{_builddir}/libatomic-devel.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libitm -f %{_builddir}/libitm.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libitm-devel -f %{_builddir}/libitm-devel.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libssp -f %{_builddir}/libssp.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libssp-devel -f %{_builddir}/libssp-devel.files
%license COPYING.RUNTIME COPYING3.LIB

%ifarch x86_64
%files -n libquadmath -f %{_builddir}/libquadmath.files
%license COPYING.RUNTIME COPYING3.LIB

%files -n libquadmath-devel -f %{_builddir}/libquadmath-devel.files
%license COPYING.RUNTIME COPYING3.LIB
%endif

%files -n libcc1 -f %{_builddir}/libcc1.files
%license COPYING3

%files -n libcc1-devel -f %{_builddir}/libcc1-devel.files
%license COPYING3
%endif
