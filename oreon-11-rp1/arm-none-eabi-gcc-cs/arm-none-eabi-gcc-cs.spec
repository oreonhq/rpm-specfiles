%global source0_hash none

%global processor_arch arm
%global target         %{processor_arch}-none-eabi
%global gcc_ver        %{version}
%global gcc_short_ver  15.1

# we need newlib to compile complete gcc, but we need gcc to compile newlib,
# so compile minimal gcc first
%global bootstrap      0

Name:           %{target}-gcc-cs
Epoch:          1
Version:        15.2.0
Release:        4%{?dist}
Summary:        GNU GCC for cross-compilation for %{target} target
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            https://gcc.gnu.org/
Source0:        http://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

Source1:        README.fedora
Source2:        bootstrapexplain
Patch1:         gcc-15.2.0-ftbfs01.patch

#BuildRequires:	autoconf = 2.69
BuildRequires:  gcc-c++
BuildRequires:  %{target}-binutils >= 2.21, zlib-devel gmp-devel mpfr-devel libmpc-devel flex autogen
%if ! %{bootstrap}
BuildRequires:  %{target}-newlib
BuildRequires: make
%endif
Requires:       %{target}-binutils >= 2.21
Provides:       %{target}-gcc = %{gcc_ver}

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# ppl-devel is no longer available for 32bit, so we have to skip it too
ExcludeArch:    %{ix86}
%endif

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %{target} platform, instead of for the
native %{_arch} platform.

%package c++
Summary:        Cross Compiling GNU GCC targeted at %{target}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       %{target}-gcc-c++ = %{gcc_ver}

%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %{target} platform, instead of for the native 
%{_arch} platform.

%prep
%setup -q -c
pushd gcc-%{gcc_ver}/libiberty
#autoconf -f
popd
pushd gcc-%{gcc_ver}
%patch -P 1 -p3 -b .ftbfs01

contrib/gcc_update --touch
popd
cp -a %{SOURCE1} .

# Extract %%__os_install_post into os_install_post~
cat << \EOF > os_install_post~
%__os_install_post
EOF

# Generate customized brp-*scripts
cat os_install_post~ | while read a x y; do
case $a in
# Prevent brp-strip* from trying to handle foreign binaries
*/brp-strip*)
  b=$(basename $a)
  sed -e 's,find "*$RPM_BUILD_ROOT"*,find "$RPM_BUILD_ROOT%_bindir" "$RPM_BUILD_ROOT%_libexecdir",' $a > $b
  chmod a+x $b
  ;;
esac
done

sed -e 's,^[ ]*/usr/lib/rpm.*/brp-strip,./brp-strip,' \
< os_install_post~ > os_install_post 

%build
# This package's testsuite fails on s390 when LTO is enabled.  Disable
# LTO for now on s390x until the root cause is identified
%ifarch s390x
%define _lto_cflags %{nil}
%endif
mkdir -p gcc-%{target} gcc-nano-%{target}

#### normal version

pushd gcc-%{target}
FILTERED_RPM_OPT_FLAGS=$(echo "${RPM_OPT_FLAGS}" | sed 's/Werror=format-security/Wno-format-security/g')
export CFLAGS=$FILTERED_RPM_OPT_FLAGS
export CXXFLAGS=$FILTERED_RPM_OPT_FLAGS
CC="%{__cc} ${FILTERED_RPM_OPT_FLAGS} -fno-stack-protector" \
../gcc-%{gcc_ver}/configure --prefix=%{_prefix} --mandir=%{_mandir} \
  --with-pkgversion="Fedora %{version}-%{release}" \
  --with-bugurl="https://bugzilla.redhat.com/" \
  --infodir=%{_infodir} --target=%{target} \
  --enable-interwork --enable-multilib \
  --with-python-dir=share/%{target}/gcc-%{version}/python \
  --with-multilib-list=rmprofile \
  --enable-plugins \
  --disable-decimal-float \
  --disable-libffi \
  --disable-libgomp \
  --disable-libmudflap \
  --disable-libquadmath \
  --disable-libssp \
  --disable-libstdcxx-pch \
  --disable-nls \
  --disable-shared \
  --disable-threads \
  --disable-tls \
%if %{bootstrap}
   --enable-languages=c --with-newlib --disable-nls --disable-shared --disable-threads --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --without-headers --with-system-zlib
%else
   --enable-languages=c,c++ --with-newlib --disable-nls --disable-shared --disable-threads --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --with-headers=yes --with-system-zlib --with-sysroot=/usr/%{target}
%endif

%if %{bootstrap}
make all-gcc  INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
%else
make %{_smp_mflags} INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
%endif
popd

######### nano version build part (only relevant if not bootstrap)
%if %{bootstrap}
%else

mkdir -p gcc-nano-%{target}
pushd gcc-nano-%{target}

export CFLAGS_FOR_TARGET="$CFLAGS_FOR_TARGET -fno-exceptions -Os "
export CXXFLAGS_FOR_TARGET="$CXXFLAGS_FOR_TARGET -fno-exceptions -Os "

CC="%{__cc} ${RPM_OPT_FLAGS}  -fno-stack-protector " \
../gcc-%{gcc_ver}/configure --prefix=%{_prefix} --mandir=%{_mandir} \
  --with-pkgversion="Fedora %{version}-%{release}" \
  --with-bugurl="https://bugzilla.redhat.com/" \
  --infodir=%{_infodir} --target=%{target} \
  --enable-interwork --enable-multilib \
  --with-python-dir=share/%{target}/gcc-%{version}/python \
  --with-multilib-list=rmprofile \
  --enable-plugins \
  --disable-decimal-float \
  --disable-libffi \
  --disable-libgomp \
  --disable-libmudflap \
  --disable-libquadmath \
  --disable-libssp \
  --disable-libstdcxx-pch \
  --disable-nls \
  --disable-shared \
  --disable-threads \
  --disable-tls \
  --with-sysroot=/usr/%{target} \
 --enable-languages=c,c++ --with-newlib --disable-nls --disable-shared --disable-threads --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --with-headers=yes --with-system-zlib
make %{_smp_mflags} INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
popd
%endif

%install
pushd gcc-%{target}
%if %{bootstrap}
make install-gcc DESTDIR=$RPM_BUILD_ROOT
install -p -m 0755 -D %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}/%{target}-g++
install -p -m 0755 -D %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}/%{target}-c++
%else
make install DESTDIR=$RPM_BUILD_ROOT
%endif
popd

##### nano version (only relevant non-bootstrap)

%if %{bootstrap}
%else
# everybody needs to end up built with the One True DESTDIR
# to arrange for that, move the non-nano DESTDIR out of the way
# temporarily, and make an empty one for the nano build to
# populate.  Later we'll pick just the bits from the nano one
# into the non-nano one, and switch the non-nano one to be
# the One True DESTDIR again.
#
# Without this sleight-of-hand we get rpmbuild errors noticing that
# the DESTDIR the nano bits were built with is not the One True
# DESTDIR.

rm -rf $RPM_BUILD_ROOT-non-nano
mv $RPM_BUILD_ROOT $RPM_BUILD_ROOT-non-nano
pushd gcc-nano-%{target}

make install DESTDIR=$RPM_BUILD_ROOT
popd
pushd $RPM_BUILD_ROOT
for i in libstdc++.a libsupc++.a ; do
	find . -name "$i" | while read line ; do
		R=`echo $line | sed "s/\.a/_nano\.a/g"`
		echo "$RPM_BUILD_ROOT/$line -> $RPM_BUILD_ROOT-non-nano/$R"
		cp $line $RPM_BUILD_ROOT-non-nano/$R
	done 
done
popd

# junk the nano DESTDIR now we picked out the bits we needed into
# the non-nano destdir
rm -rf $RPM_BUILD_ROOT

# put the "non-nano + picked nano bits" destdir back at the
# One True DESTDIR location.  Even though it has bits from two different
# builds, all the bits feel they were installed to DESTDIR
mv $RPM_BUILD_ROOT-non-nano $RPM_BUILD_ROOT

%endif
### end of nano version install magic

# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/libiberty.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libcc1* ||:
# these directories are often empty
rmdir $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver} ||:
rmdir $RPM_BUILD_ROOT/usr/%{target}/share ||:
# and these aren't usefull for embedded targets
rm -r $RPM_BUILD_ROOT%{_prefix}/lib*/gcc/%{target}/%{gcc_ver}/install-tools ||:
rm -r $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{gcc_ver}/install-tools ||:
rm -f $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{gcc_ver}/*.la

mkdir -p $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver}/
mv $RPM_BUILD_ROOT/%{_datadir}/gcc-%{gcc_ver}/* $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver}/ ||:
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gcc-%{gcc_ver} ||:

%global __os_install_post . ./os_install_post

%check
exit 0 # broken test, temporarily disable
%if %{bootstrap}
exit 0
%endif

%ifarch ppc64
# test does not work, upstream ignores it, https://gcc.gnu.org/bugzilla/show_bug.cgi?id=57591
exit 0
%endif

pushd gcc-%{target}
#BuildRequires: autoge may be needed
make check
popd

%files
%license gcc-%{gcc_ver}/COPYING*
%doc gcc-%{gcc_ver}/README README.fedora
%{_bindir}/%{target}-*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{target}
%{_prefix}/lib/gcc/%{target}/%{gcc_ver}
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{target}
%{_libexecdir}/gcc/%{target}/%{gcc_ver}
%{_mandir}/man1/%{target}-*.1.gz
%if ! %{bootstrap}
/usr/%{target}/lib/
%dir /usr/share/%{target}/gcc-%{gcc_ver}/python/
%exclude %{_bindir}/%{target}-?++
%exclude %{_libexecdir}/gcc/%{target}/%{gcc_ver}/cc1plus
%exclude %{_mandir}/man1/%{target}-g++.1.gz
%endif

%files c++
%{_bindir}/%{target}-?++
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{target}/%{gcc_ver}/cc1plus
/usr/%{target}/include/c++/
/usr/share/%{target}/gcc-%{gcc_ver}/python/libstdcxx/
%{_mandir}/man1/%{target}-g++.1.gz
%endif

%changelog
%autochangelog
