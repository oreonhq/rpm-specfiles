%global source0_hash bdc662c12d041b2539d0e638f3a6e741130cdb33a644ef3496963a443482d164

%{?mingw_package_header}

Name:           mingw-libidn
Version:        1.43
Release:        3%{?dist}
Summary:        MinGW Windows Internationalized Domain Name support library

License:        (LGPL-3.0-or-later OR GPL-2.0-or-later) AND GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            http://www.gnu.org/software/libidn/
Source0:        http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv

BuildRequires:  pkgconfig gettext-devel

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

# Win32
%package -n mingw32-libidn
Summary:        MinGW Windows zlib compression library for the win32 target
Requires:       pkgconfig

%description -n mingw32-libidn
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package -n mingw32-libidn-static
Summary:        Static version of the MinGW Windows IDN library
Requires:       mingw32-libidn = %{version}-%{release}

%description -n mingw32-libidn-static
Static version of the MinGW Windows IDN library.

# Win64
%package -n mingw64-libidn
Summary:        MinGW Windows zlib compression library for the win64 target
Requires:       pkgconfig

%description -n mingw64-libidn
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package -n mingw64-libidn-static
Summary:        Static version of the MinGW Windows IDN library
Requires:       mingw64-libidn = %{version}-%{release}

%description -n mingw64-libidn-static
Static version of the MinGW Windows IDN library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libidn-%{version}

%build
%mingw_configure --disable-nls --disable-csharp --enable-static --enable-shared
%mingw_make_build

%install
%mingw_make_install

# Remove documentation which duplicates native Fedora package.
rm -r %{buildroot}%{mingw32_datadir}/emacs
rm -r %{buildroot}%{mingw64_datadir}/emacs
rm -r %{buildroot}%{mingw32_infodir}
rm -r %{buildroot}%{mingw64_infodir}
rm -r %{buildroot}%{mingw32_mandir}/man*
rm -r %{buildroot}%{mingw64_mandir}/man*

# The .def file isn't interesting for other libraries/applications
rm -f %{buildroot}%{mingw32_bindir}/libidn-12.def
rm -f %{buildroot}%{mingw64_bindir}/libidn-12.def

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-libidn
%license COPYING*
%{mingw32_bindir}/idn.exe
%{mingw32_bindir}/libidn-12.dll
%{mingw32_libdir}/libidn.dll.a
%{mingw32_libdir}/pkgconfig/libidn.pc
%{mingw32_includedir}/*.h

%files -n mingw32-libidn-static
%{mingw32_libdir}/libidn.a

# Win64
%files -n mingw64-libidn
%license COPYING*
%{mingw64_bindir}/idn.exe
%{mingw64_bindir}/libidn-12.dll
%{mingw64_libdir}/libidn.dll.a
%{mingw64_libdir}/pkgconfig/libidn.pc
%{mingw64_includedir}/*.h

%files -n mingw64-libidn-static
%{mingw64_libdir}/libidn.a

%changelog
%autochangelog
