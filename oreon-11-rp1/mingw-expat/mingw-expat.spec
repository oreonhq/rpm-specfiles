%global source0_hash 952c03c33a6b337f12dae7a9b0f9dee86f867550d35c994d6bdaaddd37dc8454
%{?mingw_package_header}
Name:           mingw-expat
Version:        2.8.5
Release:        1%{?dist}
Summary:        MinGW Windows port of expat XML parser library
License:        MIT
URL:            http://www.libexpat.org/
Source0:        https://downloads.sourceforge.net/expat/expat-%{version}.tar.bz2
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir expat-%{version}
%oreon_prep
%build

%mingw_configure
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
rm -r %{buildroot}%{mingw32_docdir}
rm -r %{buildroot}%{mingw64_docdir}
rm -r %{buildroot}%{mingw32_mandir}
rm -r %{buildroot}%{mingw64_mandir}
%oreon_autofiles mingw32-expat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-expat-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-expat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-expat-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-expat -f %{oreon_filedir}/mingw32-expat.list
%files -n mingw32-expat-static -f %{oreon_filedir}/mingw32-expat-static.list
%files -n mingw64-expat -f %{oreon_filedir}/mingw64-expat.list
%files -n mingw64-expat-static -f %{oreon_filedir}/mingw64-expat-static.list

%changelog

%autochangelog
