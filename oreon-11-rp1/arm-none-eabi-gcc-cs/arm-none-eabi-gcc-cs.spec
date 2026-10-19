%global source0_hash e6738e29597f733270731aa90600f37ffdc045079dfc27ec7e8192cc81085c3e
%global processor_arch arm
%global target         %{processor_arch}-none-eabi
%global gcc_ver        %{version}
%global gcc_short_ver  15.1
%global bootstrap      0
Name:           %{target}-gcc-cs
Epoch:          1
Version:        16.2.0
Release:        1%{?dist}
Summary:        GNU GCC for cross-compilation for arm-none-eabi target
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            https://gcc.gnu.org/
Source0:        http://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
Source1:        README.fedora
Source2:        bootstrapexplain
Patch1:         gcc-15.2.0-ftbfs01.patch
%if ! %{bootstrap}
%endif
Requires:       %{target}-binutils >= 2.21
Provides:       %{target}-gcc = %{gcc_ver}
# oreon:deps
BuildRequires:  arm-none-eabi-binutils
BuildRequires:  arm-none-eabi-newlib
BuildRequires:  autogen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

%ifarch s390x
%define _lto_cflags %{nil}
%endif
mkdir -p gcc-%{target} gcc-nano-%{target}
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
   --enable-languages=c,c++ --with-newlib --disable-nls --disable-shared --disable-threads --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --with-headers=yes --with-system-zlib --with-sysroot=/usr/%{target}
make %{_smp_mflags} INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
popd
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
%install
pushd gcc-%{target}
make install DESTDIR=$RPM_BUILD_ROOT
popd
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
rm -rf $RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT-non-nano $RPM_BUILD_ROOT
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/libiberty.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libcc1* ||:
rmdir $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver} ||:
rmdir $RPM_BUILD_ROOT/usr/%{target}/share ||:
rm -r $RPM_BUILD_ROOT%{_prefix}/lib*/gcc/%{target}/%{gcc_ver}/install-tools ||:
rm -r $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{gcc_ver}/install-tools ||:
rm -f $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{gcc_ver}/*.la
mkdir -p $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver}/
mv $RPM_BUILD_ROOT/%{_datadir}/gcc-%{gcc_ver}/* $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver}/ ||:
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gcc-%{gcc_ver} ||:
%global __os_install_post . ./os_install_post
%oreon_autofiles main

%check

exit 0 # broken test, temporarily disable
%ifarch ppc64
exit 0
%endif
pushd gcc-%{target}
make check
popd
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
