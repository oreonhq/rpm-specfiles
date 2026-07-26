%global source0_hash 9717ae363760dedf573dad241420c5fea86256b65bc21d2cf71b2b12f0544f4b

%{?mingw_package_header}

Name:           mingw-xz
Version:        5.2.4
Release:        16%{?dist}
Summary:        Cross-compiled LZMA compression utilities

# Scripts xz{grep,diff,less,more} and symlinks (copied from gzip) are
# GPLv2+, binaries are Public Domain (linked against LGPL getopt_long but its
# OK), documentation is Public Domain.
License:        0BSD AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            http://tukaani.org/xz/
Source0:        http://tukaani.org/xz/xz-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.

# Mingw32
%package -n mingw32-xz
Summary:        Cross-compiled LZMA compression utilities
Requires:       mingw32-xz-libs = %{version}-%{release}

%description -n mingw32-xz
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.

%package -n mingw32-xz-libs
Summary:        Libraries for decoding LZMA compression
License:        0BSD

%description -n mingw32-xz-libs
Libraries for decoding files compressed with LZMA or XZ utils.

%package -n mingw32-xz-libs-static
Summary:        Static version of the xz library
License:        0BSD
Requires:       mingw32-xz-libs = %{version}-%{release}

%description -n mingw32-xz-libs-static
Static version of the xz library.

# Mingw64
%package -n mingw64-xz
Summary:        Cross-compiled LZMA compression utilities
Requires:       mingw64-xz-libs = %{version}-%{release}

%description -n mingw64-xz
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.

%package -n mingw64-xz-libs
Summary:        Libraries for decoding LZMA compression
License:        0BSD

%description -n mingw64-xz-libs
Libraries for decoding files compressed with LZMA or XZ utils.

%package -n mingw64-xz-libs-static
Summary:        Static version of the xz library
License:        0BSD
Requires:       mingw64-xz-libs = %{version}-%{release}

%description -n mingw64-xz-libs-static
Static version of the xz library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n xz-%{version}

%build
MINGW32_CFLAGS="%{mingw32_cflags} -D_FILE_OFFSET_BITS=64" \
MINGW64_CFLAGS="%{mingw64_cflags} -D_FILE_OFFSET_BITS=64" \
%mingw_configure --disable-nls \
                 --disable-lzmadec \
                 --disable-lzmainfo \
                 --disable-lzma-links \
                 --disable-scripts
%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

iconv -f latin1 -t utf-8 < NEWS > NEWS.utf8; cp NEWS.utf8 NEWS
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name cpio.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name mtree.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name tar.5 -exec rm -f {} ';'

# Remove documentation which duplicates that found in the native package.
rm -r $RPM_BUILD_ROOT/%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT/%{mingw64_prefix}/share

# Win32
%files -n mingw32-xz
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv2.1
%{mingw32_bindir}/unxz.exe
%{mingw32_bindir}/xz.exe
%{mingw32_bindir}/xzcat.exe
%{mingw32_bindir}/xzdec.exe

%files -n mingw32-xz-libs
%license COPYING
%{mingw32_bindir}/liblzma-5.dll
%{mingw32_includedir}/lzma
%{mingw32_includedir}/lzma.h
%{mingw32_libdir}/liblzma.dll.a
%{mingw32_libdir}/pkgconfig/liblzma.pc

%files -n mingw32-xz-libs-static
%license COPYING
%{mingw32_libdir}/liblzma.a

# Win64
%files -n mingw64-xz
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv2.1
%{mingw64_bindir}/unxz.exe
%{mingw64_bindir}/xz.exe
%{mingw64_bindir}/xzcat.exe
%{mingw64_bindir}/xzdec.exe

%files -n mingw64-xz-libs
%license COPYING
%{mingw64_bindir}/liblzma-5.dll
%{mingw64_includedir}/lzma
%{mingw64_includedir}/lzma.h
%{mingw64_libdir}/liblzma.dll.a
%{mingw64_libdir}/pkgconfig/liblzma.pc

%files -n mingw64-xz-libs-static
%license COPYING
%{mingw64_libdir}/liblzma.a

%changelog
%autochangelog
