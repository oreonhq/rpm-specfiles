%global source0_hash none
%global DATE 20260123
%global gitrev 226e8310eed1ce10784f98f199e1aa4b12ca86b7
%global gcc_version 15.2.1
%global gcc_major 15
%global gcc_release 7
%global _performance_build 1
%undefine _hardened_build
%undefine _auto_set_build_flags
%undefine _annotated_build
%define bugurl https://bugzilla.redhat.com/bugzilla
%{!?dist_bug_report_url: %global dist_bug_report_url %bugurl}
%ifarch %{ix86} x86_64 ppc64le
%global build_libquadmath 1
%else
%global build_libquadmath 0
%endif
%ifarch %{ix86} x86_64 ppc64le s390x aarch64 riscv64
%global build_libatomic 1
%else
%global build_libatomic 0
%endif
%ifarch %{ix86} x86_64 ppc64le s390x aarch64 riscv64
%global build_libitm 1
%else
%global build_libitm 0
%endif
%ifarch %{ix86} x86_64 ppc64le s390x aarch64 riscv64
%global attr_ifunc 1
%else
%global attr_ifunc 0
%endif
%global build_annobin_plugin 1
Summary:        Various compatibility compilers (C, C++, Fortran, ...)
Name: gcc%{gcc_major}
Version: %{gcc_version}
Release:        1%{?dist}
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND (GPL-3.0-or-later WITH Texinfo-exception) AND (LGPL-2.1-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GNU-compiler-exception) AND BSL-1.0 AND GFDL-1.3-or-later AND Linux-man-pages-copyleft-2-para AND SunPro AND BSD-1-Clause AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND BSD-4-Clause AND BSD-Source-Code AND Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 WITH LLVM-Exception) AND ZPL-2.1 AND curl
Source0:        gcc-%{version}-%{DATE}.tar.xz
Source1: dummylib.sh
URL: http://gcc.gnu.org
%ifarch ppc64le s390x
%endif
Requires: binutils >= 2.31
Conflicts: gdb < 5.1-2
Requires: glibc-devel >= 2.2.90-12
%ifarch ppc64le s390x
Requires: glibc >= 2.3.90-35
%endif
Requires: libgcc >= %{version}-%{release}
Requires: libgomp >= %{version}-%{release}
Obsoletes: gcc14 < %{version}-%{release}
Requires: make
AutoReq: true
AutoProv: false
Provides: bundled(libiberty)
Provides: bundled(libbacktrace)
Provides: bundled(libffi)
Patch0: gcc15-hack.patch
Patch3: gcc15-libgomp-omp_h-multilib.patch
Patch4: gcc15-libtool-no-rpath.patch
Patch8: gcc15-no-add-needed.patch
Patch9: gcc15-Wno-format-security.patch
Patch10: gcc15-rh1574936.patch
Patch12: gcc15-pr119006.patch
Patch13: gcc15-pr123273.patch
Patch14: gcc15-pr123667.patch
Patch15: gcc15-pr123737.patch
%global _gnu %{nil}
%global gcc_target_platform %{_target_platform}
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  /usr/bin/python
BuildRequires:  annobin-plugin-gcc
BuildRequires:  binutils
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  elfutils-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  glibc-static
BuildRequires:  gmp-devel
BuildRequires:  libgcc
BuildRequires:  libgfortran
BuildRequires:  libgomp
BuildRequires:  libmpc-devel
BuildRequires:  libstdc++
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  sharutils
BuildRequires:  systemtap-sdt-devel
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  xz
BuildRequires:  zlib-devel
# /oreon:deps
%description
The gcc package contains the GNU Compiler Collection version %{gcc_major}
for compatibility purposes.

%package -n gcc%{gcc_major}-c++
Summary: C++ support for GCC %{gcc_major} compatibility compiler
Requires: gcc%{gcc_major} = %{version}-%{release}
Requires: libstdc++ >= %{version}-%{release}
Requires: libstdc++-devel >= %{version}-%{release}
AutoReq: true
AutoProv: false
%description -n gcc%{gcc_major}-c++
This package adds C++ support to the GNU Compiler Collection
%{gcc_major} compatibility compiler.

%package -n gcc%{gcc_major}-gfortran
Summary: Fortran support for GCC %{gcc_major} compatibility compiler
Requires: gcc%{gcc_major} = %{version}-%{release}
Requires: libgfortran >= %{version}-%{release}
AutoReq: true
AutoProv: false
%description -n gcc%{gcc_major}-gfortran
This package provides support for compiling Fortran
programs with the GNU Compiler Collection %{gcc_major}
compatibility compiler.

%prep

%setup -q -n gcc-%{version}-%{DATE}
%autopatch -p0 -m 0 -M 99

echo 'Red Hat %{version}-%{gcc_release}' > gcc/DEV-PHASE

cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

sed -i -e 's/Common Driver Var(flag_report_bug)/& Init(1)/' gcc/common.opt
sed -i -e 's/m_report_bug = false;/m_report_bug = true;/' gcc/diagnostic.cc

%build

export CONFIG_SITE=NONE
CC=gcc
CXX=g++
OPT_FLAGS="%{optflags}"
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=[123]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[123]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/\(-Wp,\)\?-U_FORTIFY_SOURCE//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-flto=auto//g;s/-flto//g;s/-ffat-lto-objects//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-fno-omit-frame-pointer//g;s/-mbackchain//g;s/-mno-omit-leaf-frame-pointer//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Werror=format-security/-Wformat-security/g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables /' \
      libgcc/Makefile.in
    ;;
esac
rm -rf obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}
CONFIGURE_OPTS="\
	--prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--with-bugurl=%dist_bug_report_url \
	--enable-shared --enable-threads=posix --enable-checking=release \
	--disable-multilib \
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
	--enable-libstdcxx-backtrace --with-libstdcxx-zoneinfo=%{_datadir}/zoneinfo \
	--with-linker-hash-style=gnu \
	--enable-plugin --enable-initfini-array \
	--without-isl \
%ifarch ppc64le
	--enable-secureplt \
%endif
%ifarch ppc64le s390x
	--with-long-double-128 \
%endif
%ifarch ppc64le
	--with-long-double-format=ieee \
%endif
%ifarch ppc64le
	--with-cpu-32=power8 --with-tune-32=power8 --with-cpu-64=power8 --with-tune-64=power8 \
%endif
%ifarch %{ix86} x86_64
	--enable-cet \
	--with-tune=generic \
%endif
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
%ifarch s390x
	--with-arch=z13 --with-tune=z14 \
	--enable-decimal-float \
%endif
%ifarch riscv64
	--with-arch=rv64gc --with-abi=lp64d --with-multilib-list=lp64d \
%endif
	--build=%{gcc_target_platform} \
	--with-build-config=bootstrap-lto --enable-link-serialization=1 \
	"
CC="$CC" CXX="$CXX" CFLAGS="$OPT_FLAGS" \
	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Wformat-security / -Wformat -Wformat-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --enable-bootstrap \
	--enable-languages=c,c++,fortran,lto \
	$CONFIGURE_OPTS
make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS" LDFLAGS_FOR_TARGET=-Wl,-z,relro,-z,now profiledbootstrap
CC="`%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cc`"
CXX="`%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cxx` `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-includes`"
perl -pi -e 's/head3/head2/' ../contrib/texi2pod.pl
for i in ../gcc/doc/*.texi; do
  cp -a $i $i.orig; sed 's/ftable/table/' $i.orig > $i
done
make -C gcc generated-manpages
for i in ../gcc/doc/*.texi; do mv -f $i.orig $i; done
cd ..
mkdir -p rpm.doc/gfortran
mkdir -p rpm.doc/changelogs/gcc/cp
for i in {gcc,gcc/cp}/ChangeLog*; do
	cp -p $i rpm.doc/changelogs/$i
done
(cd gcc/fortran; for i in ChangeLog*; do
	cp -p $i ../../rpm.doc/gfortran/$i
done)
rm -f rpm.doc/changelogs/gcc/ChangeLog.[1-9]
find rpm.doc -name \*ChangeLog\* | xargs bzip2 -9
mkdir annobin-plugin
cd annobin-plugin
tar xf %{_usrsrc}/annobin/latest-annobin.tar.xz
cd annobin*
touch aclocal.m4 configure Makefile.in */configure */config.h.in */Makefile.in
ANNOBIN_FLAGS=../../obj-%{gcc_target_platform}/%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags
ANNOBIN_CFLAGS1="%build_cflags -I %{_builddir}/gcc-%{version}-%{DATE}/gcc"
ANNOBIN_CFLAGS1="$ANNOBIN_CFLAGS1 -I %{_builddir}/gcc-%{version}-%{DATE}/obj-%{gcc_target_platform}/gcc"
ANNOBIN_CFLAGS2="-I %{_builddir}/gcc-%{version}-%{DATE}/include -I %{_builddir}/gcc-%{version}-%{DATE}/libcpp/include"
ANNOBIN_LDFLAGS="%build_ldflags -L%{_builddir}/gcc-%{version}-%{DATE}/obj-%{gcc_target_platform}/%{gcc_target_platform}/libstdc++-v3/src/.libs"
CC="`$ANNOBIN_FLAGS --build-cc`" CXX="`$ANNOBIN_FLAGS --build-cxx`" \
  CFLAGS="$ANNOBIN_CFLAGS1 $ANNOBIN_CFLAGS2 $ANNOBIN_LDFLAGS" \
  CXXFLAGS="$ANNOBIN_CFLAGS1 `$ANNOBIN_FLAGS --build-includes` $ANNOBIN_CFLAGS2 $ANNOBIN_LDFLAGS" \
  ./configure --with-gcc-plugin-dir=%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin \
	      --without-annocheck --without-tests --without-docs --disable-rpath --without-debuginfod \
	      --without-clang-plugin --without-llvm-plugin
make
cd ../..
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
%ifarch riscv64
for d in %{buildroot}%{_libdir} %{buildroot}/%{_lib} \
	  %{buildroot}%{_datadir}/gdb/auto-load/%{_prefix}/%{_lib} \
	  %{buildroot}%{_prefix}/include/c++/%{gcc_major}/%{gcc_target_platform}/%{_lib}; do
  mkdir -p $d
  (cd $d && ln -sf . lp64d)
done
%endif
cd obj-%{gcc_target_platform}
TARGET_PLATFORM=%{gcc_target_platform}
make -C %{gcc_target_platform}/libstdc++-v3
make prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir} \
  infodir=%{buildroot}%{_infodir} install
FULLPATH=%{buildroot}%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}
FULLEPATH=%{buildroot}%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}
rm -f %{buildroot}%{_infodir}/dir
gzip -9 %{buildroot}%{_infodir}/*.info*
for f in `find %{buildroot}%{_prefix}/include/c++/%{gcc_major}/%{gcc_target_platform}/ -name c++config.h`; do
  for i in 1 2 4 8; do
    sed -i -e 's/#define _GLIBCXX_ATOMIC_BUILTINS_'$i' 1/#ifdef __GCC_HAVE_SYNC_COMPARE_AND_SWAP_'$i'\
&\
  done
done
rm -rf %{buildroot}%{_prefix}/include/c++/%{gcc_major}/%{gcc_target_platform}/bits/*.h.gch
FULLLSUBDIR=
FULLLPATH=$FULLPATH
find %{buildroot} -name \*.la | xargs rm -f
mv %{buildroot}%{_prefix}/%{_lib}/libgfortran.spec $FULLPATH/
sh %{SOURCE1} %{gcc_target_platform}/libgcc/libgcc_s.so.1 $FULLPATH/libgcc_s_dummy.so \
  %{gcc_target_platform}/libgcc/libgcc.map /%{_lib}/libgcc_s.so.1
rm -f %{buildroot}%{_prefix}/%{_lib}/libgcc_s.so.1
%ifarch %{ix86} x86_64 ppc64le aarch64 riscv64
rm -f $FULLPATH/libgcc_s.so
echo '/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT('`gcc -Wl,--print-output-format -nostdlib -r -o /dev/null`')
GROUP ( libgcc_s_dummy.so libgcc.a )' > $FULLPATH/libgcc_s.so
%else
ln -sf libgcc_s_dummy.so $FULLPATH/libgcc_s.so
%endif
rm -f %{gcc_target_platform}/libgcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s.so %{gcc_target_platform}/libgcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s_dummy.so %{gcc_target_platform}/libgcc/libgcc_s_dummy.so
ln -sf /%{_lib}/libgcc_s.so.1 %{gcc_target_platform}/libgcc/libgcc.so.1
rm -f gcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s.so gcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s_dummy.so gcc/libgcc_s_dummy.so
ln -sf /%{_lib}/libgcc_s.so.1 gcc/libgcc.so.1
mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.spec $FULLPATH/
sed -e 's,\.\./include/,../../../../include/,' \
  %{buildroot}%{_prefix}/%{_lib}/libstdc++.modules.json \
  > $FULLPATH/libstdc++.modules.json
sh %{SOURCE1} %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so.6.* $FULLPATH/libstdc++.so \
  %{gcc_target_platform}/libstdc++-v3/src/libstdc++-symbols.ver %{_prefix}/%{_lib}/libstdc++.so.6
rm -f %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so
cp -a $FULLPATH/libstdc++.so %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so
ln -sf %{_prefix}/%{_lib}/libstdc++.so.6 %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so.6.*
sh %{SOURCE1} %{gcc_target_platform}/libgfortran/.libs/libgfortran.so.5.* $FULLPATH/libgfortran.so \
  %{gcc_target_platform}/libgfortran/gfortran.ver %{_prefix}/%{_lib}/libgfortran.so.5
rm -f %{gcc_target_platform}/libgfortran/.libs/libgfortran.so
cp -a $FULLPATH/libgfortran.so %{gcc_target_platform}/libgfortran/.libs/libgfortran.so
ln -sf %{_prefix}/%{_lib}/libgfortran.so.5 %{gcc_target_platform}/libgfortran/.libs/libgfortran.so.5.*
sh %{SOURCE1} %{gcc_target_platform}/libgomp/.libs/libgomp.so.1.* $FULLPATH/libgomp.so \
  %{gcc_target_platform}/libgomp/libgomp.ver %{_prefix}/%{_lib}/libgomp.so.1
rm -f %{gcc_target_platform}/libgomp/.libs/libgomp.so
cp -a $FULLPATH/libgomp.so %{gcc_target_platform}/libgomp/.libs/libgomp.so
ln -sf %{_prefix}/%{_lib}/libgomp.so.1 %{gcc_target_platform}/libgomp/.libs/libgomp.so.1.*
pushd $FULLPATH
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++fs.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++exp.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libsupc++.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libgfortran.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.*a $FULLLPATH/
rm -f %{buildroot}%{_prefix}/%{_lib}/lib*.so.*
rm -f %{buildroot}%{_prefix}/%{_lib}/lib*.a
strip -g `find . \( -name libgfortran.a -o -name libobjc.a -o -name libgomp.a \
		    -o -name libgcc.a -o -name libgcov.a -o -name libquadmath.a \
		    -o -name libgdruntime.a -o -name libgphobos.a -o -name libm2\*.a \
		    -o -name libitm.a -o -name libgo.a -o -name libcaf\*.a \
		    -o -name libatomic.a -o -name libasan.a -o -name libtsan.a \
		    -o -name libubsan.a -o -name liblsan.a -o -name libcc1.a \) \
		 -a -type f`
popd
for h in `find $FULLPATH/include -name \*.h`; do
  if grep -q 'It has been auto-edited by fixincludes from' $h; then
    rh=`grep -A2 'It has been auto-edited by fixincludes from' $h | tail -1 | sed 's|^.*"\(.*\)".*$|\1|'`
    diff -up $rh $h || :
    rm -f $h
  fi
done
cd ..
rm -f %{buildroot}%{_prefix}/%{_lib}/{libffi*,libiberty.a} || :
rm -f $FULLEPATH/install-tools/{mkheaders,fixincl}
rm -f %{buildroot}%{_prefix}/lib/{32,64}/libiberty.a
rm -f %{buildroot}%{_prefix}/%{_lib}/libssp*
rm -f %{buildroot}%{_prefix}/%{_lib}/libvtv* || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gfortran || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gcc-ar || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gcc-nm || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gcc-ranlib || :
rm -f %{buildroot}%{_prefix}/bin/c++ || :
rm -f $FULLEPATH/plugin/gengtype || :
rm -f $FULLPATH/plugin/lib{cc1,cp1}plugin.so* || :
rm -f %{buildroot}%{mandir}/man3/ffi*
echo gcc-%{version}-%{release}.%{_arch} > $FULLPATH/rpmver
mkdir -p $FULLPATH/plugin
rm -f $FULLPATH/plugin/gcc-annobin*
cp -a %{_builddir}/gcc-%{version}-%{DATE}/annobin-plugin/annobin*/gcc-plugin/.libs/annobin.so.0.0.0 \
  $FULLPATH/plugin/gcc-annobin.so.0.0.0
ln -sf gcc-annobin.so.0.0.0 $FULLPATH/plugin/gcc-annobin.so.0
ln -sf gcc-annobin.so.0.0.0 $FULLPATH/plugin/gcc-annobin.so
ln -sf gcc-annobin.so $FULLPATH/plugin/annobin.so
rm -f %{buildroot}%{_prefix}/bin/*-gcc-%{gcc_major}
for i in %{buildroot}%{_prefix}/bin/{*gcc,*++,gcov,gcov-tool,gcov-dump,gcc-ar,gcc-nm,gcc-ranlib,lto-dump,cpp,gfortran}; do
  mv -f $i ${i}-%{gcc_major}
done
for i in %{buildroot}%{_mandir}/man1/{gcc,gcov,gcov-tool,gcov-dump,lto-dump,cpp,g++,gfortran}.1*; do
  mv -f $i `echo $i | sed 's/\(\.1[^/]*\)$/-%{gcc_major}\1/'`
done
rm -rf $FULLPATH/include-fixed || :
rm -rf $FULLPATH/include/sanitizer || :
rm -rf $FULLPATH/include/ssp || :
rm -rf $FULLPATH/install-tools || :
rm -rf $FULLPATH/plugin/gtype.state || :
rm -rf $FULLPATH/plugin/include || :
rm -rf $FULLEPATH/install-tools || :
rm -rf %{buildroot}%{_prefix}/share/gcc-%{gcc_major}/python || :
rm -rf %{buildroot}%{_infodir} || :
rm -rf %{buildroot}%{_prefix}/share/locale || :
rm -rf %{buildroot}%{_mandir}/man7 || :
rm -rf %{buildroot}%{_prefix}/%{_lib}/*.so || :
rm -rf %{buildroot}%{_prefix}/%{_lib}/*.spec || :
rm -f %{buildroot}%{_prefix}/%{_lib}/libstdc++.modules.json || :
rm -rf %{buildroot}%{_prefix}/%{_lib}/*.o || :
%ifarch ppc64le
rm -rf $FULLPATH/{e,n}crt{i,n}.o || :
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

cd obj-%{gcc_target_platform}
LC_ALL=C make %{?_smp_mflags} -k check ALT_CC_UNDER_TEST=gcc ALT_CXX_UNDER_TEST=g++ \
     RUNTESTFLAGS="--target_board=unix/'{,-fstack-protector-strong}'" || :
%if !%{build_annobin_plugin}
if [ -f %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/annobin.so ]; then
  echo -e '#include <stdio.h>\nint main () { printf ("Hello, world!\\n"); return 0; }' > annobin-test.c
  echo -e '#include <iostream>\nint main () { std::cout << "Hello, world!" << std::endl; return 0; }' > annobin-test.C
  `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cc` \
  -O2 -g -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS \
  -fexceptions -fstack-protector-strong -grecord-gcc-switches -o annobin-test{c,.c} \
  -Wl,-rpath,%{gcc_target_platform}/libgcc/ \
  -fplugin=%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/annobin.so \
  2> ANNOBINOUT1 || echo Annobin test 1 FAIL > ANNOBINOUT2;
  `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cxx` \
  `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-includes` \
  -O2 -g -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS \
  -fexceptions -fstack-protector-strong -grecord-gcc-switches -o annobin-test{C,.C} \
  -Wl,-rpath,%{gcc_target_platform}/libgcc/:%{gcc_target_platform}/libstdc++-v3/src/.libs/ \
  -fplugin=%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/annobin.so \
  -B %{gcc_target_platform}/libstdc++-v3/src/.libs/ \
  2> ANNOBINOUT3 || echo Annobin test 2 FAIL > ANNOBINOUT4;
  [ -f ./annobin-testc ] || echo Annobin test 1 MISSING > ANNOBINOUT5;
  [ -f ./annobin-testc ] && \
  ( ./annobin-testc > ANNOBINRES1 2>&1 || echo Annobin test 1 RUNFAIL > ANNOBINOUT6 );
  [ -f ./annobin-testC ] || echo Annobin test 2 MISSING > ANNOBINOUT7;
  [ -f ./annobin-testC ] && \
  ( ./annobin-testC > ANNOBINRES2 2>&1 || echo Annobin test 2 RUNFAIL > ANNOBINOUT8 );
  cat ANNOBINOUT[1-8] > ANNOBINOUT
  touch ANNOBINRES1 ANNOBINRES2
  [ -s ANNOBINOUT ] && echo Annobin testing FAILed > ANNOBINRES
  cat ANNOBINOUT ANNOBINRES[12] >> ANNOBINRES
  rm -f ANNOBINOUT* ANNOBINRES[12] annobin-test{c,C}
fi
%endif
echo ====================TESTING=========================
( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
%if !%{build_annobin_plugin}
[ -f ANNOBINRES ] && cat ANNOBINRES
%endif
echo ====================TESTING END=====================
mkdir testlogs-%{_target_platform}-%{version}-%{release}
for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
  ln $i testlogs-%{_target_platform}-%{version}-%{release}/ || :
done
tar cf - testlogs-%{_target_platform}-%{version}-%{release} | xz -9e \
  | uuencode testlogs-%{_target_platform}.tar.xz || :
rm -rf testlogs-%{_target_platform}-%{version}-%{release}
%files -f %{oreon_filedir}/main.list
%files -n gcc15-gfortran -f %{oreon_filedir}/gcc15-gfortran.list

%changelog

%autochangelog
