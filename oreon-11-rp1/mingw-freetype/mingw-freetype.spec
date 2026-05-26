# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 32427e8c471ac095853212a37aef816c60b42052d4d9e48230bab3bdf2936ccc
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{?mingw_package_header}

Name:           mingw-freetype
# NOTE See comment for Patch2 below
Version:        2.14.1
Release:        2%{?dist}
Summary:        Free and portable font rendering engine

License:        FTL OR GPL-2.0-or-later
URL:            http://www.freetype.org
Source0:        http://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.xz

# Patches from native Fedora package:

# Enable subpixel rendering (ClearType)
Patch0:         freetype-2.3.0-enable-spr.patch
# Enable otvalid and gxvalid modules
Patch1:         freetype-2.2.1-enable-valid.patch
# Re-add symbol downstream for ABI compatibility only. Remove once soname has been bumped from -6.
Patch2:         freetype-2.10.0-internal-outline.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-libpng

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-libpng

%description
MinGW Windows Freetype library.

# Win32
%package -n mingw32-freetype
Summary:        Free and portable font rendering engine

%description -n mingw32-freetype
MinGW Windows Freetype library.

%package -n mingw32-freetype-static
Summary:        Static version of the MinGW Windows Freetype library
Requires:       mingw32-freetype = %{version}-%{release}

%description -n mingw32-freetype-static
Static version of the MinGW Windows Freetype library.

# Win64
%package -n mingw64-freetype
Summary:        Free and portable font rendering engine

%description -n mingw64-freetype
MinGW Windows Freetype library.

%package -n mingw64-freetype-static
Summary:        Static version of the MinGW Windows Freetype library
Requires:       mingw64-freetype = %{version}-%{release}

%description -n mingw64-freetype-static
Static version of the MinGW Windows Freetype library.


%{?mingw_debug_package}


%prep
%oreon_verify_sources
%autosetup -p1 -n freetype-%{version}


%build
%mingw_configure \
           --enable-static \
           --enable-shared \
           --with-zlib=yes \
           --with-bzip2=yes \
           --with-png=yes \
           --enable-freetype-config \
           --with-harfbuzz=no

%mingw_make_build

# The ft2demos Makefile is hacky and doesn't understand
# cross-compilation.  This nearly works, but not quite, so
# disable. it.
#pushd ft2demos-%{version}
#make TOP_DIR=".." PLATFORM=win32
#popd


%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Remove redundent man pages
rm -rf %{buildroot}%{mingw32_mandir} %{buildroot}%{mingw64_mandir}


%files -n mingw32-freetype
%license LICENSE.TXT
%{mingw32_bindir}/freetype-config
%{mingw32_bindir}/libfreetype-6.dll
%{mingw32_includedir}/freetype2
%{mingw32_libdir}/libfreetype.dll.a
%{mingw32_libdir}/pkgconfig/freetype2.pc
%{mingw32_datadir}/aclocal/freetype2.m4

%files -n mingw32-freetype-static
%{mingw32_libdir}/libfreetype.a

%files -n mingw64-freetype
%license LICENSE.TXT
%{mingw64_bindir}/freetype-config
%{mingw64_bindir}/libfreetype-6.dll
%{mingw64_includedir}/freetype2
%{mingw64_libdir}/libfreetype.dll.a
%{mingw64_libdir}/pkgconfig/freetype2.pc
%{mingw64_datadir}/aclocal/freetype2.m4

%files -n mingw64-freetype-static
%{mingw64_libdir}/libfreetype.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.14.1-2
- Prepare for Oreon 11 (RP1)
