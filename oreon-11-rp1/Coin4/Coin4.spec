%global source0_hash a01276052c31e84e4a069ee4452eab3b65a7d101a3fd7a09803be59125616270

Name:           Coin4
Version:        4.0.7
Release:        1%{?dist}
Summary:        High-level 3D visualization library

License:        BSD-3-Clause AND GPL-3.0-or-later

URL:            https://github.com/coin3d/coin/wiki

Source0:        https://github.com/coin3d/coin/releases/download/v%{version}/coin-%{version}-src.tar.gz

Patch1:         0003-man3.patch
Patch2:         0006-inttypes.patch
Patch3:         0011-Fix-SoCamera-manpage.patch
# Per this thread Coin provides a dummy GLX implementation which causes issues
# when running under Wayland so we patch it out.
# https://forum.freecadweb.org/viewtopic.php?f=8&t=33359#p279513
Patch4:         coin-no_glx.patch
# Allow CMake 4.0 builds
# Cherrypicked from:
# - https://github.com/coin3d/coin/commit/36abede21bc47a72a5c9666e7ec321f7c54b70c5
# - https://github.com/coin3d/coin/commit/ecd34feb12b652f935a901e38b1f8bdf63bf43a3
#Patch5:         Coin4-4.0.3-Allow_CMake_4.0.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

BuildRequires:  boost-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  expat-devel
#BuildRequires:  libXext-devel

%description
Coin3D is a high-level, retained-mode toolkit for effective 3D graphics
development. It is API compatible with Open Inventor 2.1.

%package devel
Summary:        Development files for Coin
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel
Requires:       bzip2-devel
Requires:       fontconfig-devel
Requires:       freetype-devel
Requires:       libGLU-devel
Requires:       pkgconfig
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Provides:       pkgconfig(Coin)

%description devel
Development package for Coin.

%package doc
Summary:        HTML developer documentation for Coin

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n coin

# Update doxygen configuration
doxygen -u docs/coin.doxygen.in

#find -name 'Makefile.*' -exec sed -i -e 's,\$(datadir)/Coin,$(datadir)/Coin4,' {} \;

# bogus permissions
find . \( -name '*.h' -o -name '*.cpp' -o -name '*.c' \) -a -executable -exec chmod -x {} \;

# convert sources to utf-8
for a in $(find . -type f -exec file -i {} \; | grep -i iso | sed -e 's,:.*,,'); do \
  /usr/bin/iconv -f ISO-8859-1 -t utf-8 $a > $a~; \
  mv $a~ $a; \
done

# get rid of bundled boost headers
rm -rf include/boost

%build
%cmake -DCOIN_BUILD_DOCUMENTATION=TRUE \
       -DCOIN_BUILD_DOCUMENTATION_MAN=TRUE \
       -DHAVE_MULTIPLE_VERSION=TRUE \
       -DUSE_EXTERNAL_EXPAT=TRUE 

%cmake_build

%install
%cmake_install

cd %{buildroot}%{_mandir}
/usr/bin/rename .3 .3coin4 man3/*
cd - 

mkdir -p %{buildroot}%{_libdir}/Coin4

mv %{buildroot}%{_datadir}/Coin/conf %{buildroot}%{_datadir}/Coin4/conf
mv %{buildroot}%{_bindir}/coin-config %{buildroot}%{_libdir}/Coin4/
ln -sr %{_libdir}/Coin4/coin-config %{buildroot}%{_bindir}/coin-config
mv %{buildroot}%{_libdir}/pkgconfig/Coin.pc %{buildroot}%{_libdir}/pkgconfig/Coin4.pc
ln -sr %{_libdir}/pkgconfig/Coin4.pc %{buildroot}%{_libdir}/pkgconfig/Coin.pc

%check
%ctest

%ldconfig_scriptlets

%post devel
link=$(readlink -e "%{_bindir}/coin-config")
if [ "$link" = "%{_bindir}/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi
if [ "$link" = "%{_libdir}/Coin4/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi

/usr/sbin/alternatives --install "%{_bindir}/coin-config" coin-config \
  "%{_libdir}/Coin4/coin-config" 80 \
  --slave %{_libdir}/pkgconfig/Coin.pc Coin.pc %{_libdir}/pkgconfig/Coin4.pc \
  --slave %{_libdir}/libCoin.so libCoin.so %{_libdir}/libCoin.so.80

%preun devel
if [ $1 = 0 ]; then
  /usr/sbin/alternatives --remove coin-config "%{_libdir}/Coin4/coin-config"
fi

%files
%doc AUTHORS ChangeLog README{,.UNIX} THANKS FAQ*
%license COPYING
%dir %{_datadir}/Coin4
%{_datadir}/Coin4/scxml
%{_libdir}/libCoin.so.*

%files devel
%ghost %{_bindir}/coin-config
%ghost %{_libdir}/libCoin.so
%ghost %{_libdir}/pkgconfig/Coin.pc
%{_includedir}/Coin4/
%{_libdir}/cmake/Coin-%{version}/
%{_libdir}/Coin4/coin-config
%{_libdir}/pkgconfig/Coin4.pc
%dir %{_datadir}/Coin4
%{_datadir}/Coin4/draggerDefaults
%{_datadir}/Coin4/conf/
%{_datadir}/Coin4/shaders
%{_mandir}/man?/*

%files doc
%{_docdir}/Coin4/html/

%changelog
%autochangelog
