%global source0_hash c3d8c0c34aa39098f66576fe51969db12a5100b956233dc56506f7a8679be995

%{?mingw_package_header}

Name:           mingw-libxml2
Version:        2.12.10
Release:        3%{?dist}
Summary:        MinGW Windows libxml2 XML processing library

License:        MIT
URL:            http://xmlsoft.org/
# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        https://download.gnome.org/sources/libxml2/%{release_version}/libxml2-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  automake autoconf libtool
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib

%description
MinGW Windows libxml2 XML processing library.

# Win32
%package -n mingw32-libxml2
Summary:        MinGW Windows libxml2 XML processing library
Requires:       pkgconfig

%description -n mingw32-libxml2
MinGW Windows libxml2 XML processing library.

%package -n mingw32-libxml2-static
Summary:        Static version of the MinGW Windows XML processing library
Requires:       mingw32-libxml2 = %{version}-%{release}

%description -n mingw32-libxml2-static
Static version of the MinGW Windows XML processing library.

# Win64
%package -n mingw64-libxml2
Summary:        MinGW Windows libxml2 XML processing library
Requires:       pkgconfig

%description -n mingw64-libxml2
MinGW Windows libxml2 XML processing library.

%package -n mingw64-libxml2-static
Summary:        Static version of the MinGW Windows XML processing library
Requires:       mingw64-libxml2 = %{version}-%{release}

%description -n mingw64-libxml2-static
Static version of the MinGW Windows XML processing library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libxml2-%{version}

%build
NOCONFIGURE=1 ./autogen.sh

# LibXML2 can't build static and shared libraries in one go, so we build LibXML2 twice here
MINGW32_CPPFLAGS="-DLIBXML_STATIC_FOR_DLL" \
MINGW64_CPPFLAGS="-DLIBXML_STATIC_FOR_DLL" \
MINGW_BUILDDIR_SUFFIX=static %mingw_configure --without-python --with-modules --enable-static --disable-shared --with-threads=win32
MINGW_BUILDDIR_SUFFIX=shared %mingw_configure --without-python --with-modules --disable-static --enable-shared --with-threads=win32

MINGW_BUILDDIR_SUFFIX=static %mingw_make_build
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_build

%install
MINGW_BUILDDIR_SUFFIX=static %mingw_make_install
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_install

# Remove documentation which duplicates Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc/

rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc/

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-libxml2
%license Copyright
%{mingw32_bindir}/libxml2-2.dll
%{mingw32_bindir}/xml2-config
%{mingw32_bindir}/xmlcatalog.exe
%{mingw32_bindir}/xmllint.exe
%{mingw32_libdir}/libxml2.dll.a
%{mingw32_libdir}/cmake/libxml2/
%{mingw32_libdir}/pkgconfig/libxml-2.0.pc
%{mingw32_includedir}/libxml2
%{mingw32_datadir}/aclocal/*

%files -n mingw32-libxml2-static
%{mingw32_libdir}/libxml2.a

# Win64
%files -n mingw64-libxml2
%license Copyright
%{mingw64_bindir}/libxml2-2.dll
%{mingw64_bindir}/xml2-config
%{mingw64_bindir}/xmlcatalog.exe
%{mingw64_bindir}/xmllint.exe
%{mingw64_libdir}/libxml2.dll.a
%{mingw64_libdir}/cmake/libxml2/
%{mingw64_libdir}/pkgconfig/libxml-2.0.pc
%{mingw64_includedir}/libxml2
%{mingw64_datadir}/aclocal/*

%files -n mingw64-libxml2-static
%{mingw64_libdir}/libxml2.a

%changelog
%autochangelog
