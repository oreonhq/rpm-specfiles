%global source0_hash 816c96e8e8f193b40151dad7e8ff37b1221d019dbcb9c35cd3fadbfe6477dfec
%{?mingw_package_header}
Name: mingw-brotli
Version: 1.2.0
Release:        1%{?dist}
Summary:        MinGW port of Lossless compression algorithm
License: MIT
URL: https://github.com/google/brotli
Source0:        https://github.com/google/brotli/archive/v%{version}/brotli-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package -n mingw32-brotli
Summary:        MinGW port of Lossless compression algorithm
%description -n mingw32-brotli
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package -n mingw64-brotli
Summary:        MinGW port of Lossless compression algorithm
%description -n mingw64-brotli
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%{?mingw_debug_package}

%prep

%autosetup -n brotli-%{version}
# fix permissions for -debuginfo
# rpmlint will complain if I create an extra %%files section for
# -debuginfo for this so we'll put it here instead
chmod 644 c/enc/*.[ch]
chmod 644 c/include/brotli/*.h
chmod 644 c/tools/brotli.c

%build

%mingw_cmake
%mingw_make %{?_smp_mflags}
%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*-static.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*-static.a
find $RPM_BUILD_ROOT -name "*.la" -delete
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc
%oreon_autofiles mingw32-brotli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-brotli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-brotli -f %{oreon_filedir}/mingw32-brotli.list
%files -n mingw64-brotli -f %{oreon_filedir}/mingw64-brotli.list

%changelog

%autochangelog
