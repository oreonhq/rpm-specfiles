%global source0_hash ebdf77a8f5c0a8f7a9e42323844fa09502b34eb1d1fece7b5f54da41fe2122ec
%{?mingw_package_header}
%global base libtheora
Name:           mingw-%{base}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Theora Video Compression Codec
License:        BSD-3-Clause
URL:            http://www.theora.org
Source0:        http://downloads.xiph.org/releases/theora/%{base}-%{version}.tar.xz
Patch0:         libtheora-1.1.1-fix-pp_sharp_mod-calc.patch
Patch1:         libtheora-1.1.1-libpng16.patch
Patch2:         libtheora-1.1.1-libm.patch
Patch3:         libtheora-1.1.1-libadd.patch
Patch4:         mingw-libtheora-1.1.1-rint.patch
Patch5:         mingw-libtheora-getopt.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libogg
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libvorbis
# /oreon:deps
%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

%package -n mingw32-%{base}
Summary:        Theora Video Compression Codec
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
Summary:        Theora Video Compression Codec
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
%oreon_autofiles mingw32-theora-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-theora-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libtheora -f %{oreon_filedir}/mingw32-libtheora.list
%files -n mingw32-theora-tools -f %{oreon_filedir}/mingw32-theora-tools.list
%files -n mingw64-libtheora -f %{oreon_filedir}/mingw64-libtheora.list
%files -n mingw64-theora-tools -f %{oreon_filedir}/mingw64-theora-tools.list

%changelog

%autochangelog
