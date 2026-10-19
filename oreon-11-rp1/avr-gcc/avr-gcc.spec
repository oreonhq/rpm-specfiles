%global source0_hash e6738e29597f733270731aa90600f37ffdc045079dfc27ec7e8192cc81085c3e
%define target avr
Name:           %{target}-gcc
Version:        16.2.0
Release:        1%{?dist}
Epoch:          1
Summary:        Cross Compiling GNU GCC targeted at avr
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            http://gcc.gnu.org/
Source0:        http://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
Source2:        README.fedora
Patch0:         avr-gcc-4.5.3-mint8.patch
Patch1:		avr-gcc-config.patch
Patch2:         gcc-15.2.0-ftbfs01.patch
Requires:       %{target}-binutils >= 1:2.23
Provides:       bundled(libiberty)
# oreon:deps
BuildRequires:  automake
BuildRequires:  avr-binutils
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
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
%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %{target} platform, instead of for the native %{_arch}
platform.

%prep

%setup -q -c
[ -d gcc-%{version} ] || mv gcc-4.7-* gcc-%{version}

pushd gcc-%{version}
%patch -P0 -p2 -b .mint8
#patch -P1 -p2 -b .config
%patch -P 2 -p3 -b .ftbfs01

pushd libiberty
#autoconf -f
popd

contrib/gcc_update --touch
popd
cp -a %{SOURCE2} .

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

pushd gcc-%{version}
acv=$(autoreconf --version | head -n1)
acv=${acv##* }
sed -i "/_GCC_AUTOCONF_VERSION/s/2.64/$acv/" config/override.m4
popd
mkdir -p gcc-%{target}
pushd gcc-%{target}
FILTERED_RPM_OPT_FLAGS=$(echo "${RPM_OPT_FLAGS}" | sed 's/Werror=format-security/Wno-format-security/g')
export CFLAGS=$FILTERED_RPM_OPT_FLAGS
export CXXFLAGS=$FILTERED_RPM_OPT_FLAGS
CC="%{__cc} ${FILTERED_RPM_OPT_FLAGS} -fno-stack-protector" \
../gcc-%{version}/configure --prefix=%{_prefix} --mandir=%{_mandir} \
  --infodir=%{_infodir} --target=%{target} --enable-languages=c,c++ \
  --disable-nls --disable-libssp --with-system-zlib \
  --enable-version-specific-runtime-libs \
  --with-pkgversion="Fedora %{version}-%{release}" \
  --with-bugurl="https://bugzilla.redhat.com/"
make
popd
%install
pushd gcc-%{target}
make install DESTDIR=$RPM_BUILD_ROOT
popd
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm    $RPM_BUILD_ROOT%{_libdir}/libiberty.a ||:
rm    $RPM_BUILD_ROOT%{_libdir}/libcc1* ||:
rm -r $RPM_BUILD_ROOT/usr/lib/gcc/%{target}/%{version}/install-tools ||:
rm -r $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{version}/install-tools ||:
%define __os_install_post . ./os_install_post
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
