%global source0_hash 540fb721619a6aba3bdeef7d940d8e9e0e6d2c193595bc243241b77ff9e93620

%?mingw_package_header
# Fedora 36 change
# https://fedoraproject.org/wiki/Changes/SetBuildFlagsBuildCheck
%undefine _auto_set_build_flags

Name:           mingw-wine-gecko
Version:        2.47.4
Release:        10%{?dist}
Summary:        Gecko library required for Wine

# Automatically converted from old format: MPLv1.1 or GPLv2+ or LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MPLv1.1 OR GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+
URL:            http://wiki.winehq.org/Gecko
Source0:        http://dl.winehq.org/wine/wine-gecko/%{version}/wine-gecko-%{version}-src.tar.xz
# https://bugs.winehq.org/show_bug.cgi?id=52455
Source1:        https://github.com/libffi/libffi/releases/download/v3.4.2/libffi-3.4.2.tar.gz
# https://bugs.winehq.org/show_bug.cgi?id=52085
Patch1:       %{name}-gcc11.patch
#Patch2:       %%{name}-python311.patch
# bad hack for mingw header issue
Patch3:       %{name}-header.patch
# https://gitlab.winehq.org/wine/wine-gecko/-/merge_requests/22
Patch4:       22.patch
# https://gitlab.winehq.org/wine/wine-gecko/-/merge_requests/23
Patch5:       23.patch
# https://gitlab.winehq.org/wine/wine-gecko/-/merge_requests/30
Patch6:       30.patch
Patch7:       0001-Hacky-resolve-of-two-or-more-data-types-in-declarati.patch
Patch8:       0001-Nuke-true-false-redefinitions.patch

BuildArch:      noarch

# This project is only useful with wine, and wine doesn't support PPC.
# We will adopt the same arch support that wine does.
ExclusiveArch:  %{ix86} x86_64

# 64
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-cpp
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-crt
BuildRequires:  mingw64-winpthreads-static
# 32
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-cpp
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-crt
BuildRequires:  mingw32-winpthreads-static

BuildRequires:  autoconf213
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig
%if 0%{?fedora} > 36
BuildRequires:  python3.10
%else
BuildRequires:  python3
%endif
BuildRequires:  perl-Getopt-Long
BuildRequires:  yasm
BuildRequires:  zip
BuildRequires:  wine-core
BuildRequires:  wine-devel

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
# setup build options...
echo "mk_add_options MOZ_MAKE_FLAGS=%{_smp_mflags}" >> wine/mozconfig-common
echo "export CFLAGS=\"$CFLAGS -Wno-error=incompatible-pointer-types -Wno-error=int-conversion -DWINE_GECKO_SRC\"" >> wine/mozconfig-common

cp wine/mozconfig-common wine/mozconfig-common.build

# ... and build

%if 0%{?fedora} > 36
python3.10 -m venv env
source env/bin/activate
%endif

# Make jobserver is broken under Python 3.10
#TOOLCHAIN_PREFIX=i686-w64-mingw32- MAKEOPTS="%%{_smp_mflags}" ./wine/make_package --msi-package -win32
TOOLCHAIN_PREFIX=i686-w64-mingw32- MAKEOPTS="-j1" ./wine/make_package --msi-package -win32

#TOOLCHAIN_PREFIX=x86_64-w64-mingw32- MAKEOPTS="%%{_smp_mflags}" ./wine/make_package --msi-package -win64
TOOLCHAIN_PREFIX=x86_64-w64-mingw32- MAKEOPTS="-j1" ./wine/make_package --msi-package -win64

%install
mkdir -p %{buildroot}%{_datadir}/wine/gecko
install -p -m 0644 wine-gecko-%{version}-x86/dist/wine-gecko-%{version}-x86.msi \
   %{buildroot}%{_datadir}/wine/gecko/wine-gecko-%{version}-x86.msi
install -p -m 0644 wine-gecko-%{version}-x86_64/dist/wine-gecko-%{version}-x86_64.msi \
   %{buildroot}%{_datadir}/wine/gecko/wine-gecko-%{version}-x86_64.msi

%files -n mingw32-wine-gecko
%license wine-gecko-%{version}/LICENSE
%doc wine-gecko-%{version}/LEGAL
%doc wine-gecko-%{version}/README.txt
%{_datadir}/wine/gecko/wine-gecko-%{version}-x86.msi

%files -n mingw64-wine-gecko
%license wine-gecko-%{version}/LICENSE
%doc wine-gecko-%{version}/LEGAL
%doc wine-gecko-%{version}/README.txt
%{_datadir}/wine/gecko/wine-gecko-%{version}-x86_64.msi

%changelog
%autochangelog
