%global source0_hash f36da409947aa2b3dcc6af0a8c2e3144bc19db2ed547d64e9171c59c66561c61

%{?mingw_package_header}

%global base libtheora

Name:           mingw-%{base}
Version:        1.1.1
Release:        28%{?dist}
Summary:        Theora Video Compression Codec

License:        BSD-3-Clause
URL:            http://www.theora.org
Source0:        http://downloads.xiph.org/releases/theora/%{base}-%{version}.tar.xz
# native package and upstream SVN r18268
Patch0:         libtheora-1.1.1-fix-pp_sharp_mod-calc.patch
# native package and upstream SVN r19088
# http://trac.xiph.org/ticket/1947
Patch1:         libtheora-1.1.1-libpng16.patch
# native package and upstream SVN r19087
Patch2:         libtheora-1.1.1-libm.patch
# to fix parallel build with -no-undefined in MinGW
# upstream SVN r16712
Patch3:         libtheora-1.1.1-libadd.patch
# https://trac.xiph.org/ticket/2141
# https://gitlab.xiph.org/xiph/theora/-/issues/2141
Patch4:         mingw-libtheora-1.1.1-rint.patch
Patch5:         mingw-libtheora-getopt.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  autoconf automake libtool
# for autotools
BuildRequires:  SDL-devel

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw32-libpng

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libogg
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw64-libpng

%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

%package -n mingw32-%{base}
Summary:        %{summary}

%description -n mingw32-%{base}
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

This package is MinGW compiled theora library for the Win32 target.

%package -n mingw32-theora-tools
Summary:        Command line tools for Theora videos
Requires:       mingw32-%{base} = %{version}-%{release}

%description -n mingw32-theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.

This package is MinGW compiled theora tools for the Win32 target.

%package -n mingw64-%{base}
Summary:        %{summary}

%description -n mingw64-%{base}
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

This package is MinGW compiled theora library for the Win64 target.

%package -n mingw64-theora-tools
Summary:        Command line tools for Theora videos
Requires:       mingw64-%{base} = %{version}-%{release}

%description -n mingw64-theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.

This package is MinGW compiled theora tools for the Win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{base}-%{version}
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

# no custom CFLAGS please
sed -i 's/CFLAGS="$CFLAGS $cflags_save"/CFLAGS="$cflags_save"/g' configure.ac

# fix syntax of export symbols files
sed -i 's/^EXPORTS//' win32/xmingw32/*.def

%build
autoreconf -fi -I m4
%mingw_configure --disable-static

# disable build of documentation
sed -i 's/\<doc\>//' build_win*/Makefile

%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=%{buildroot} INSTALL="install -p"

mkdir -p %{buildroot}/%{mingw32_bindir}
pushd build_win32/examples
../libtool --mode=install install -p -m 755 dump_video.exe %{buildroot}/%{mingw32_bindir}/theora_dump_video.exe
../libtool --mode=install install -p -m 755 encoder_example.exe %{buildroot}/%{mingw32_bindir}/theora_encode.exe
../libtool --mode=install install -p -m 755 png2theora.exe %{buildroot}/%{mingw32_bindir}/png2theora.exe
popd

mkdir -p %{buildroot}/%{mingw64_bindir}
pushd build_win64/examples
../libtool --mode=install install -p -m 755 dump_video.exe %{buildroot}/%{mingw64_bindir}/theora_dump_video.exe
../libtool --mode=install install -p -m 755 encoder_example.exe %{buildroot}/%{mingw64_bindir}/theora_encode.exe
../libtool --mode=install install -p -m 755 png2theora.exe %{buildroot}/%{mingw64_bindir}/png2theora.exe
popd

rm -fv %{buildroot}/%{mingw32_libdir}/*.la
rm -fv %{buildroot}/%{mingw64_libdir}/*.la

%files -n mingw32-%{base}
%doc README COPYING
%{mingw32_bindir}/libtheora-0.dll
%{mingw32_bindir}/libtheoradec-1.dll
%{mingw32_bindir}/libtheoraenc-1.dll
%{mingw32_includedir}/theora
%{mingw32_libdir}/libtheora.dll.a
%{mingw32_libdir}/libtheoradec.dll.a
%{mingw32_libdir}/libtheoraenc.dll.a
%{mingw32_libdir}/pkgconfig/theora*.pc

%files -n mingw32-theora-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{base}
%doc README COPYING
%{mingw64_bindir}/libtheora-0.dll
%{mingw64_bindir}/libtheoradec-1.dll
%{mingw64_bindir}/libtheoraenc-1.dll
%{mingw64_includedir}/theora
%{mingw64_libdir}/libtheora.dll.a
%{mingw64_libdir}/libtheoradec.dll.a
%{mingw64_libdir}/libtheoraenc.dll.a
%{mingw64_libdir}/pkgconfig/theora*.pc

%files -n mingw64-theora-tools
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
