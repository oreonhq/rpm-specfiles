%global source0_hash 28bebac7f12025c7cf70a89aff4c7e6cd244ce0deae6ce947cc2806ef6db24be

#
# Copyright (c) 2004-2018, 2022 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%define coin_includedir %{_includedir}/Coin2
%define coin_htmldir %{_datadir}/Coin2

%define libopenal_SONAME libopenal.so.1
%define libsimage_SONAME libsimage.so.20

Summary: High-level 3D visualization library
Name: Coin2
Version: 2.5.0
Release: 54%{?dist}

# LICENSE.GPL says ".. or later" but source files tell "GPLv2"
License: GPL-2.0-only
URL: http://www.coin3d.org

Source0: ftp://ftp.coin3d.org/pub/coin/src/all/Coin-%{version}.tar.gz

Patch0: Coin-2.4.6-simage-soname.diff
Patch1: Coin-2.4.6-openal-soname.diff
Patch2: Coin-2.4.6-man3.diff
Patch3: Coin-2.5.0-doxygen.diff
Patch4: Coin-2.5.0-gcc-4.7.0.diff
Patch5: Coin-2.5.0-inttypes.patch
Patch6: Coin-2.5.0-config.patch
Patch7: Coin-2.5.0-Use-NULL-instead-of-0.patch
Patch8: Coin2-configure-c99.patch

BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libXext-devel

BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: doxygen
BuildRequires: /usr/bin/rename
BuildRequires: /usr/bin/perl
BuildRequires: make

%description
Coin is a 3D graphics library with an Application Programming Interface
based on the Open Inventor 2.1 API.

%package devel
Summary: Development files for Coin
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel bzip2-devel
Requires: fontconfig-devel
Requires: freetype-devel
Requires: libGLU-devel
Requires: pkgconfig
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Provides: pkgconfig(Coin)

%description devel
Development package for Coin2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Coin-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

# Update doxygen configuration
doxygen -u docs/coin.doxygen.in

find -name 'Makefile.*' -exec sed -i -e 's,\$(datadir)/Coin,$(datadir)/Coin2,' {} \;

# bogus permissions
find . \( -name '*.h' -o -name '*.cpp' -o -name '*.c' \) -a -executable -exec chmod -x {} \;

# convert sources to utf-8
for a in $(find . -type f -exec file -i {} \; | grep -i iso | sed -e 's,:.*,,'); do \
  /usr/bin/iconv -f ISO-8859-1 -t utf-8 $a > $a~; \
  mv $a~ $a; \
done

sed -i -e 's,@LIBSIMAGE_SONAME@,"%{libsimage_SONAME}",' \
  src/glue/simage_wrapper.c
sed -i -e 's,@LIBOPENAL_SONAME@,"%{libopenal_SONAME}",' \
  src/glue/openal_wrapper.c

%build
%configure \
	--includedir=%{coin_includedir} \
	--disable-dependency-tracking \
	--enable-shared \
	--disable-dl-libbzip2 \
	--disable-dl-glu \
	--disable-dl-zlib \
	--disable-dl-freetype \
	--disable-dl-fontconfig \
	--disable-spidermonkey \
	--enable-man \
	--enable-html \
	--enable-3ds-import \
	htmldir=%{coin_htmldir}/Coin \
	CPPFLAGS="$(pkg-config --cflags freetype2)"
%{make_build}

# Strip the default libdir
sed -i -e "s,\-L%{_libdir} ,," coin-default.cfg

# coin-config is arch dependent
sed -i -e "s,/share/Coin/conf/,/%{_lib}/Coin2/conf/,g" bin/coin-config

%install
%{make_install}

pushd $RPM_BUILD_ROOT%{_mandir} > /dev/null
/usr/bin/rename .1 .1coin2 man1/*
/usr/bin/rename .3 .3coin2 man3/*
popd > /dev/null
rm -f ${RPM_BUILD_ROOT}%{_libdir}/lib*.la

install -d -m 755 ${RPM_BUILD_ROOT}%{_libdir}/Coin2
mv ${RPM_BUILD_ROOT}%{_datadir}/Coin2/conf ${RPM_BUILD_ROOT}%{_libdir}/Coin2

mv ${RPM_BUILD_ROOT}%{_bindir}/coin-config ${RPM_BUILD_ROOT}%{_libdir}/Coin2/coin-config
ln -s %{_libdir}/Coin2/coin-config ${RPM_BUILD_ROOT}%{_bindir}/coin-config
mv ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin2.pc
ln -s %{_libdir}/pkgconfig/Coin2.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin.pc
mv ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin.m4 ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin2.m4
ln -s %{_datadir}/aclocal/coin2.m4 ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin.m4

%ldconfig_scriptlets

%post devel
link=$(readlink -e "%{_bindir}/coin-config")
if [ "$link" = "%{_bindir}/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi
if [ "$link" = "%{_libdir}/Coin2/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi

/usr/sbin/alternatives --install "%{_bindir}/coin-config" coin-config \
  "%{_libdir}/Coin2/coin-config" 40 \
  --slave %{_libdir}/pkgconfig/Coin.pc Coin.pc %{_libdir}/pkgconfig/Coin2.pc \
  --slave %{_datadir}/aclocal/coin.m4 coin.m4 %{_datadir}/aclocal/coin2.m4 \
  --slave %{_libdir}/libCoin.so libCoin.so %{_libdir}/libCoin.so.40

%preun devel
if [ $1 = 0 ]; then
  /usr/sbin/alternatives --remove coin-config "%{_libdir}/Coin2/coin-config"
fi

%files
%doc AUTHORS ChangeLog* README THANKS FAQ*
%license COPYING LICENSE*
%{_libdir}/libCoin.so.*

%files devel
%ghost %{_bindir}/coin-config
%{coin_includedir}
%ghost %{_libdir}/libCoin.so
%{_datadir}/aclocal/coin2.m4
%ghost %{_datadir}/aclocal/coin.m4
%dir %{_datadir}/Coin2
%{_datadir}/Coin2/draggerDefaults
%{_datadir}/Coin2/shaders
%{_libdir}/Coin2
%{_mandir}/man?/*
%doc %{coin_htmldir}/Coin
%{_libdir}/pkgconfig/Coin2.pc
%ghost %{_libdir}/pkgconfig/Coin.pc

%changelog
%autochangelog
