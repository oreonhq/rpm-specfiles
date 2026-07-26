%global source0_hash 69fa312d3586c988789266eaf7ffc9861d9f6396c31fc930a014d551b59bbd6e

%{?mingw_package_header}

%global pkgname hunspell

Name:          mingw-%{pkgname}
Version:       1.7.2
Release:       11%{?dist}
Summary:       MinGW Windows spell checker and morphological analyzer library

URL:           http://hunspell.github.io/
License:       LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
Source0:       https://github.com/hunspell/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: make
BuildRequires: libtool automake autoconf
BuildRequires: bison
BuildRequires: gettext-devel

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gettext
BuildRequires: mingw32-readline

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gettext
BuildRequires: mingw64-readline

%description
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

This is the MinGW build of Hunspell.

# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW Windows spell checker and morphological analyzer library

%description -n mingw32-%{pkgname}
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

This is the MinGW build of Hunspell.

%package -n mingw32-%{pkgname}-static
Summary:        Static version of the MinGW Windows hunspell library
Requires:       mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows hunspell spell checking library.

%package -n mingw32-%{pkgname}-tools
Summary:        MinGW Windows hunspell library tools
Requires:       mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
MinGW Windows hunspell library tools.

# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW Windows spell checker and morphological analyzer library

%description -n mingw64-%{pkgname}
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

This is the MinGW build of Hunspell

%package -n mingw64-%{pkgname}-static
Summary:        Static version of the MinGW Windows hunspell library
Requires:       mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows hunspell spell checking library.

%package -n mingw64-%{pkgname}-tools
Summary:        MinGW Windows hunspell library tools
Requires:       mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
MinGW Windows hunspell library tools.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
autoreconf -ifv
%mingw_configure --enable-static --enable-shared --with-ui --with-readline --enable-threads=win32
%mingw_make_build

%install
%mingw_make_install

# Drop .la files
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la

# Drop the man pages
rm -rf %{buildroot}%{mingw32_datadir}/man
rm -rf %{buildroot}%{mingw64_datadir}/man

# Win32
%files -n mingw32-%{pkgname}
%license COPYING COPYING.LESSER COPYING.MPL license.hunspell license.myspell
%{mingw32_bindir}/libhunspell-1.7-0.dll
%{mingw32_includedir}/hunspell/
%{mingw32_libdir}/libhunspell-1.7.dll.a
%{mingw32_libdir}/pkgconfig/hunspell.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libhunspell-1.7.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/affixcompress
%{mingw32_bindir}/analyze.exe
%{mingw32_bindir}/chmorph.exe
%{mingw32_bindir}/hunspell.exe
%{mingw32_bindir}/hunzip.exe
%{mingw32_bindir}/hzip.exe
%{mingw32_bindir}/ispellaff2myspell
%{mingw32_bindir}/makealias
%{mingw32_bindir}/munch.exe
%{mingw32_bindir}/unmunch.exe
%{mingw32_bindir}/wordforms
%{mingw32_bindir}/wordlist2hunspell

# Win64
%files -n mingw64-%{pkgname}
%license COPYING COPYING.LESSER COPYING.MPL license.hunspell license.myspell
%{mingw64_bindir}/libhunspell-1.7-0.dll
%{mingw64_includedir}/hunspell/
%{mingw64_libdir}/libhunspell-1.7.dll.a
%{mingw64_libdir}/pkgconfig/hunspell.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libhunspell-1.7.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/affixcompress
%{mingw64_bindir}/analyze.exe
%{mingw64_bindir}/chmorph.exe
%{mingw64_bindir}/hunspell.exe
%{mingw64_bindir}/hunzip.exe
%{mingw64_bindir}/hzip.exe
%{mingw64_bindir}/ispellaff2myspell
%{mingw64_bindir}/makealias
%{mingw64_bindir}/munch.exe
%{mingw64_bindir}/unmunch.exe
%{mingw64_bindir}/wordforms
%{mingw64_bindir}/wordlist2hunspell

%changelog
%autochangelog
