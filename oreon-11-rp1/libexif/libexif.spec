%global source0_hash 0830ed253fceeb60444fb309598bc8a9491d3007dc054aad3a50a347c5597c57

Summary:	Library for extracting extra information from image files
Name:		libexif
Version:	0.6.26
Release:	%autorelease
License:	LGPL-2.1-or-later
URL:		https://libexif.github.io/
Source0:        https://github.com/libexif/libexif/releases/download/v%{version}/libexif-%{version}.tar.bz2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	pkgconfig

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package devel
Summary:	Files needed for libexif application development
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The libexif-devel package contains the libraries and header files
for writing programs that use libexif.

%package doc
Summary:	The EXIF Library API documentation
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description doc
API Documentation for programmers wishing to use libexif in their programs.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
autoreconf -fiv
iconv -f latin1 -t utf-8 < COPYING > COPYING.utf8; cp COPYING.utf8 COPYING
iconv -f latin1 -t utf-8 < README > README.utf8; cp README.utf8 README


%build
%configure --disable-static
%make_build


%install
%make_install

rm -rf %{buildroot}%{_datadir}/doc/libexif

%find_lang libexif-12


%check
%make_build check


%files -f libexif-12.lang
%doc README NEWS
%license COPYING
%{_libdir}/libexif.so.12*

%files devel
%{_includedir}/libexif
%{_libdir}/libexif.so
%{_libdir}/pkgconfig/libexif.pc

%files doc
%doc doc/doxygen-output/libexif-api.html


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.26-1
- Import
