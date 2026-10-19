%global source0_hash 9717ae363760dedf573dad241420c5fea86256b65bc21d2cf71b2b12f0544f4b
%{?mingw_package_header}
Name:           mingw-xz
Version:        5.8.4
Release:        1%{?dist}
Summary:        Cross-compiled LZMA compression utilities
License:        0BSD AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            http://tukaani.org/xz/
Source0:        http://tukaani.org/xz/xz-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
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
rm -r $RPM_BUILD_ROOT/%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT/%{mingw64_prefix}/share
%oreon_autofiles mingw32-xz usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-xz-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-xz-libs-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-xz usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-xz-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-xz-libs-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-xz -f %{oreon_filedir}/mingw32-xz.list
%files -n mingw32-xz-libs -f %{oreon_filedir}/mingw32-xz-libs.list
%files -n mingw32-xz-libs-static -f %{oreon_filedir}/mingw32-xz-libs-static.list
%files -n mingw64-xz -f %{oreon_filedir}/mingw64-xz.list
%files -n mingw64-xz-libs -f %{oreon_filedir}/mingw64-xz-libs.list
%files -n mingw64-xz-libs-static -f %{oreon_filedir}/mingw64-xz-libs-static.list

%changelog

%autochangelog
