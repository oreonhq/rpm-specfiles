%global source0_hash 28eb403f51f0f7405249132cecfe82ea5c0ef97f1b32c5a65828814ae0d34775

%{?mingw_package_header}

Name:           mingw-libpng
Version:        1.6.58
Release:        1%{?dist}
Summary:        MinGW Windows Libpng library

License:        Zlib
URL:            http://www.libpng.org/pub/png/
Source0:        https://downloads.sourceforge.net/libpng/libpng-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-zlib


%description
MinGW Windows Libpng library.


# Win32
%package -n mingw32-libpng
Summary:        MinGW Windows Libpng library
Requires:       pkgconfig

%description -n mingw32-libpng
MinGW Windows Libpng library.

%package -n mingw32-libpng-static
Summary:        Static version of MinGW Windows Libpng library
Requires:       mingw32-libpng = %{version}-%{release}

%description -n mingw32-libpng-static
MinGW Windows Libpng library.

This package contains static cross-compiled libraries.

# Win64
%package -n mingw64-libpng
Summary:        MinGW Windows Libpng library
Requires:       pkgconfig

%description -n mingw64-libpng
MinGW Windows Libpng library.

%package -n mingw64-libpng-static
Summary:        Static version of MinGW Windows Libpng library
Requires:       mingw64-libpng = %{version}-%{release}

%description -n mingw64-libpng-static
MinGW Windows Libpng library.

This package contains static cross-compiled libraries.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libpng-%{version}


%build
%mingw_configure
%mingw_make_build


%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# No need to distribute manpages which appear in the Fedora
# native packages already.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


# Win32
%files -n mingw32-libpng
%license LICENSE
%doc ANNOUNCE CHANGES README TODO
%{mingw32_bindir}/libpng-config
%{mingw32_bindir}/libpng16-16.dll
%{mingw32_bindir}/libpng16-config
%{mingw32_bindir}/png-fix-itxt.exe
%{mingw32_bindir}/pngfix.exe
%{mingw32_includedir}/libpng16
%{mingw32_includedir}/png.h
%{mingw32_includedir}/pngconf.h
%{mingw32_includedir}/pnglibconf.h
%{mingw32_libdir}/libpng.dll.a
%{mingw32_libdir}/libpng16.dll.a
%{mingw32_libdir}/pkgconfig/libpng.pc
%{mingw32_libdir}/pkgconfig/libpng16.pc

%files -n mingw32-libpng-static
%{mingw32_libdir}/libpng.a
%{mingw32_libdir}/libpng16.a

# Win64
%files -n mingw64-libpng
%license LICENSE
%doc ANNOUNCE CHANGES README TODO
%{mingw64_bindir}/libpng-config
%{mingw64_bindir}/libpng16-16.dll
%{mingw64_bindir}/libpng16-config
%{mingw64_bindir}/png-fix-itxt.exe
%{mingw64_bindir}/pngfix.exe
%{mingw64_includedir}/libpng16
%{mingw64_includedir}/png.h
%{mingw64_includedir}/pngconf.h
%{mingw64_includedir}/pnglibconf.h
%{mingw64_libdir}/libpng.dll.a
%{mingw64_libdir}/libpng16.dll.a
%{mingw64_libdir}/pkgconfig/libpng.pc
%{mingw64_libdir}/pkgconfig/libpng16.pc

%files -n mingw64-libpng-static
%{mingw64_libdir}/libpng.a
%{mingw64_libdir}/libpng16.a


%changelog
%autochangelog
