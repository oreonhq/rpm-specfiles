%global source0_hash cf112a1fb02f5b1c0fce5cab11ea8243852c139e669c44014125874b14b7dfaa

Name: libmng
Version: 2.0.3
Release: 25%{?dist}
URL: http://www.libmng.com/
Summary: Library for Multiple-image Network Graphics support
# This is a common zlib variant.
License: Zlib
Source0:        https://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRequires: zlib-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: lcms2-devel
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: make

%package devel
Summary: Development files for the Multiple-image Network Graphics library
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel
Requires: libjpeg-devel

%description
LibMNG is a library for accessing graphics in MNG (Multi-image Network
Graphics) and JNG (JPEG Network Graphics) formats.  MNG graphics are
basically animated PNGs.  JNG graphics are basically JPEG streams
integrated into a PNG chunk.

%description devel
LibMNG is a library for accessing MNG and JNG format graphics.  The
libmng-devel package contains files needed for developing or compiling
applications which use MNG graphics.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
#cp makefiles/configure.in .
cp makefiles/Makefile.am .
#sed -i '/AM_C_PROTOTYPES/d' configure.in
autoreconf -if
%configure --enable-shared --disable-static --with-zlib --with-jpeg \
	--with-gnu-ld --with-lcms2
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc CHANGES LICENSE README*
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_libdir}/pkgconfig/libmng.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.3-25
- Prepare for Oreon 11 (RP1)
