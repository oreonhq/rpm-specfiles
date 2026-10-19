%global source1_hash 540fb721619a6aba3bdeef7d940d8e9e0e6d2c193595bc243241b77ff9e93620
%global source0_hash 540fb721619a6aba3bdeef7d940d8e9e0e6d2c193595bc243241b77ff9e93620
%?mingw_package_header
%undefine _auto_set_build_flags
Name:           mingw-wine-gecko
Version:        3.5.2
Release:        1%{?dist}
Summary:        Gecko library required for Wine
License:        LicenseRef-Callaway-MPLv1.1 OR GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+
URL:            http://wiki.winehq.org/Gecko
Source0:        http://dl.winehq.org/wine/wine-gecko/%{version}/wine-gecko-%{version}-src.tar.xz
Source1:        https://github.com/libffi/libffi/releases/download/v3.4.2/libffi-3.4.2.tar.gz
Patch1:       %{name}-gcc11.patch
Patch3:       %{name}-header.patch
Patch4:       22.patch
Patch5:       23.patch
Patch6:       30.patch
Patch7:       0001-Hacky-resolve-of-two-or-more-data-types-in-declarati.patch
Patch8:       0001-Nuke-true-false-redefinitions.patch
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64
# oreon:deps
BuildRequires:  autoconf213
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cpp
BuildRequires:  mingw32-crt
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-winpthreads-static
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cpp
BuildRequires:  mingw64-crt
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-winpthreads-static
BuildRequires:  perl-Getopt-Long
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  wine-core
BuildRequires:  wine-devel
BuildRequires:  yasm
BuildRequires:  zip
# /oreon:deps
%description
Windows Gecko library required for Wine.

%package -n mingw32-wine-gecko
Summary:       Gecko library for 32bit wine
Requires:      wine-common
%description -n mingw32-wine-gecko
Windows Gecko library required for Wine.

%package -n mingw64-wine-gecko
Summary:       Gecko library for 64bit wine
Requires:      wine-common
%description -n mingw64-wine-gecko
Windows Gecko library required for Wine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n wine-gecko-%{version}
cd wine-gecko-%{version}/
pushd js/src/ctypes/libffi
rm -rf ./*
gzip -dc %{SOURCE1} | tar -xf - --strip-components=1
popd
%patch -P 1 -p1
#patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1

# fix nsprpub cross compile detection
sed -i 's,cross_compiling=.*$,cross_compiling=yes,' nsprpub/configure

# remove blank includes
rm -f media/libstagefright/ports/win32/include/pthread.h

# fix wine cabinet tool
sed -i 's,$WINE cabarc.exe -r -m mszip N $cabfile msi/files,$WINE cabarc.exe -r -m mszip N $cabfile msi/files/*,' wine/make_package

%build

cd wine-gecko-%{version}
echo "mk_add_options MOZ_MAKE_FLAGS=%{_smp_mflags}" >> wine/mozconfig-common
echo "export CFLAGS=\"$CFLAGS -Wno-error=incompatible-pointer-types -Wno-error=int-conversion -DWINE_GECKO_SRC\"" >> wine/mozconfig-common
cp wine/mozconfig-common wine/mozconfig-common.build
TOOLCHAIN_PREFIX=i686-w64-mingw32- MAKEOPTS="-j1" ./wine/make_package --msi-package -win32
TOOLCHAIN_PREFIX=x86_64-w64-mingw32- MAKEOPTS="-j1" ./wine/make_package --msi-package -win64
%install
mkdir -p %{buildroot}%{_datadir}/wine/gecko
install -p -m 0644 wine-gecko-%{version}-x86/dist/wine-gecko-%{version}-x86.msi \
   %{buildroot}%{_datadir}/wine/gecko/wine-gecko-%{version}-x86.msi
install -p -m 0644 wine-gecko-%{version}-x86_64/dist/wine-gecko-%{version}-x86_64.msi \
   %{buildroot}%{_datadir}/wine/gecko/wine-gecko-%{version}-x86_64.msi
%oreon_autofiles mingw32-wine-gecko usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-wine-gecko usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-wine-gecko -f %{oreon_filedir}/mingw32-wine-gecko.list
%files -n mingw64-wine-gecko -f %{oreon_filedir}/mingw64-wine-gecko.list

%changelog

%autochangelog
