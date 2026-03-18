%{?mingw_package_header}

Name:           mingw-expat
Version:        2.7.4
Release:        1%{?dist}
Summary:        MinGW Windows port of expat XML parser library

License:        MIT
URL:            http://www.libexpat.org/
Source0:        http://downloads.sourceforge.net/expat/expat-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils


%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

# Win32
%package -n mingw32-expat
Summary:        MinGW Windows port of expat XML parser library

%description -n mingw32-expat
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package -n mingw32-expat-static
Summary:        Static version of the MinGW Windows expat XML parser library
Requires:       mingw32-expat = %{version}-%{release}

%description -n mingw32-expat-static
Static version of the MinGW Windows expat XML parser library.

# Win64
%package -n mingw64-expat
Summary:        MinGW Windows port of expat XML parser library

%description -n mingw64-expat
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package -n mingw64-expat-static
Summary:        Static version of the MinGW Windows expat XML parser library
Requires:       mingw64-expat = %{version}-%{release}

%description -n mingw64-expat-static
Static version of the MinGW Windows expat XML parser library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n expat-%{version}


%build
%mingw_configure
%mingw_make_build


%install
%mingw_make_install

# Remove .la files
find %{buildroot} -name "*.la" -delete

# Remove documentation which duplicates that found in the native package.
rm -r %{buildroot}%{mingw32_docdir}
rm -r %{buildroot}%{mingw64_docdir}
rm -r %{buildroot}%{mingw32_mandir}
rm -r %{buildroot}%{mingw64_mandir}


# Win32
%files -n mingw32-expat
%license COPYING
%{mingw32_bindir}/libexpat-1.dll
%{mingw32_bindir}/xmlwf.exe
%{mingw32_libdir}/libexpat.dll.a
%{mingw32_libdir}/pkgconfig/expat.pc
%{mingw32_libdir}/cmake/expat-%{version}/
%{mingw32_includedir}/expat.h
%{mingw32_includedir}/expat_config.h
%{mingw32_includedir}/expat_external.h

%files -n mingw32-expat-static
%{mingw32_libdir}/libexpat.a

# Win64
%files -n mingw64-expat
%license COPYING
%{mingw64_bindir}/libexpat-1.dll
%{mingw64_bindir}/xmlwf.exe
%{mingw64_libdir}/libexpat.dll.a
%{mingw64_libdir}/pkgconfig/expat.pc
%{mingw64_libdir}/cmake/expat-%{version}/
%{mingw64_includedir}/expat.h
%{mingw64_includedir}/expat_config.h
%{mingw64_includedir}/expat_external.h

%files -n mingw64-expat-static
%{mingw64_libdir}/libexpat.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.4-1
- Prepare for Oreon 11 (RP1)
