%global source0_hash 13fe68831292e7e725e7db1c6909d2b4fe5802080474c229fcac14ddf6445188
Name:           Coin4
Version:        4.0.10
Release:        1%{?dist}
Summary:        High-level 3D visualization library
License:        BSD-3-Clause AND GPL-3.0-or-later
URL:            https://github.com/coin3d/coin/wiki
Source0:        https://github.com/coin3d/coin/releases/download/v%{version}/coin-%{version}-src.tar.gz
Patch1:         0003-man3.patch
Patch2:         0006-inttypes.patch
Patch3:         0011-Fix-SoCamera-manpage.patch
Patch4:         coin-no_glx.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles Coin4-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles Coin4-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n Coin4-devel -f %{oreon_filedir}/Coin4-devel.list
%files -n Coin4-doc -f %{oreon_filedir}/Coin4-doc.list

%changelog

%autochangelog
