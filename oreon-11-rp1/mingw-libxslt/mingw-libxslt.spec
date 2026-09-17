%global source0_hash 4e574ba219df34495f2ee63ae27bf904afa477c40d9a2969a330cf87f48053b6

%{?mingw_package_header}

Name:           mingw-libxslt
Version:        1.1.43
Release:        5%{?dist}
Summary:        MinGW Windows Library providing the Gnome XSLT engine

License:        MIT
URL:            https://gitlab.gnome.org/GNOME/libxslt
Source0:        https://gitlab.gnome.org/GNOME/libxslt/-/archive/v%{version}/libxslt-v%{version}.tar.bz2
# Proposed fix for CVE-2025-7424
# https://gitlab.gnome.org/GNOME/libxslt/-/issues/139#note_2479564
Patch0:         gnome-libxslt-bug-139-apple-fix.patch
# Backport fix for CVE-2025-11731
Patch1:         https://gitlab.gnome.org/GNOME/libxslt/-/commit/fe508f201efb9ea37bfbe95413b8b28251497de3.patch
# Backport proposed fix for CVE-2025-10911
Patch2:         https://gitlab.gnome.org/GNOME/libxslt/-/merge_requests/77.patch

BuildArch:      noarch

BuildRequires:  automake autoconf libtool
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-libxml2 >= 2.7.2-3

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-libxml2 >= 2.7.2-3

BuildRequires:  pkgconfig

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

# Win32
%package -n mingw32-libxslt
Summary:        MinGW Windows Library providing the Gnome XSLT engine
Requires:       mingw32-libxml2 >= 2.7.2-3
Requires:       pkgconfig

%description -n mingw32-libxslt
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package -n mingw32-libxslt-static
Summary:        Static version of the MinGW Windows LibXSLT library
Requires:       mingw32-libxslt = %{version}-%{release}

%description -n mingw32-libxslt-static
Static version of the MinGW Windows LibXSLT library.

# Win64
%package -n mingw64-libxslt
Summary:        MinGW Windows Library providing the Gnome XSLT engine
Requires:       mingw64-libxml2 >= 2.7.2-3
Requires:       pkgconfig

%description -n mingw64-libxslt
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package -n mingw64-libxslt-static
Summary:        Static version of the MinGW Windows LibXSLT library
Requires:       mingw64-libxslt = %{version}-%{release}

%description -n mingw64-libxslt-static
Static version of the MinGW Windows LibXSLT library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libxslt-v%{version} -p1
NOCONFIGURE=1 ./autogen.sh

%build
%mingw_configure --without-python --enable-shared --enable-static
%mingw_make_build

%install
%mingw_make_install

# Remove doc and man which duplicate stuff already in Fedora native package.
rm -r %{buildroot}%{mingw32_datadir}/gtk-doc
rm -r %{buildroot}%{mingw32_docdir}
rm -r %{buildroot}%{mingw32_mandir}
rm -r %{buildroot}%{mingw64_datadir}/gtk-doc
rm -r %{buildroot}%{mingw64_docdir}
rm -r %{buildroot}%{mingw64_mandir}

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-libxslt
%license Copyright
%{mingw32_bindir}/xslt-config
%{mingw32_bindir}/xsltproc.exe
%{mingw32_includedir}/libexslt
%{mingw32_includedir}/libxslt
%{mingw32_bindir}/libexslt-0.dll
%{mingw32_libdir}/libexslt.dll.a
%{mingw32_bindir}/libxslt-1.dll
%{mingw32_libdir}/libxslt.dll.a
%{mingw32_libdir}/pkgconfig/libexslt.pc
%{mingw32_libdir}/pkgconfig/libxslt.pc
%{mingw32_libdir}/cmake/libxslt/
%{mingw32_libdir}/xsltConf.sh

%files -n mingw32-libxslt-static
%{mingw32_libdir}/libexslt.a
%{mingw32_libdir}/libxslt.a

# Win64
%files -n mingw64-libxslt
%license Copyright
%{mingw64_bindir}/xslt-config
%{mingw64_bindir}/xsltproc.exe
%{mingw64_includedir}/libexslt
%{mingw64_includedir}/libxslt
%{mingw64_bindir}/libexslt-0.dll
%{mingw64_libdir}/libexslt.dll.a
%{mingw64_bindir}/libxslt-1.dll
%{mingw64_libdir}/libxslt.dll.a
%{mingw64_libdir}/pkgconfig/libexslt.pc
%{mingw64_libdir}/pkgconfig/libxslt.pc
%{mingw64_libdir}/cmake/libxslt/
%{mingw64_libdir}/xsltConf.sh

%files -n mingw64-libxslt-static
%{mingw64_libdir}/libexslt.a
%{mingw64_libdir}/libxslt.a

%changelog
%autochangelog
