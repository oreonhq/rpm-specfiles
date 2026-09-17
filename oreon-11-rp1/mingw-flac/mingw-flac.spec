%global source0_hash 6c58e69cd22348f441b861092b825e591d0b822e106de6eb0ee4d05d27205b70

%{?mingw_package_header}

Name:           mingw-flac
Version:        1.4.3
Release:        4%{?dist}
Summary:        Encoder/decoder for the Free Lossless Audio Codec

License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.1-or-later
URL:            https://xiph.org/flac/
Source0:        https://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libogg
BuildRequires:  mingw64-win-iconv

BuildRequires:  automake autoconf libtool gettext-devel
BuildRequires:  nasm

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

%package -n mingw32-flac
Summary:        %{summary}

%description -n mingw32-flac
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac library for the Win32 target.

%package -n mingw32-flac-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw32-flac = %{version}-%{release}

%description -n mingw32-flac-tools
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac tools for the Win32 target.

%package -n mingw64-flac
Summary:        %{summary}

%description -n mingw64-flac
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac library for the Win64 target.

%package -n mingw64-flac-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw64-flac = %{version}-%{release}

%description -n mingw64-flac-tools
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac tools for the Win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n flac-%{version}

%build
# use our libtool to avoid problems with RPATH
./autogen.sh -V

%mingw_configure \
    --disable-silent-rules \
    --disable-thorough-tests

%mingw_make %{?_smp_mflags}

%install
%mingw_make_install

# documentation in native package
rm -rf %{buildroot}%{mingw32_docdir}/flac*
rm -rf %{buildroot}%{mingw64_docdir}/flac*
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la

%files -n mingw32-flac
%doc AUTHORS README.md CHANGELOG.md
%license COPYING*
%{mingw32_bindir}/libFLAC-12.dll
%{mingw32_bindir}/libFLAC++-10.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libFLAC.dll.a
%{mingw32_libdir}/libFLAC++.dll.a
%{mingw32_libdir}/pkgconfig/flac.pc
%{mingw32_libdir}/pkgconfig/flac++.pc
%{mingw32_datadir}/aclocal/libFLAC.m4
%{mingw32_datadir}/aclocal/libFLAC++.m4

%files -n mingw32-flac-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-flac
%doc AUTHORS README.md
%license COPYING*
%{mingw64_bindir}/libFLAC-12.dll
%{mingw64_bindir}/libFLAC++-10.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libFLAC.dll.a
%{mingw64_libdir}/libFLAC++.dll.a
%{mingw64_libdir}/pkgconfig/flac.pc
%{mingw64_libdir}/pkgconfig/flac++.pc
%{mingw64_datadir}/aclocal/libFLAC.m4
%{mingw64_datadir}/aclocal/libFLAC++.m4

%files -n mingw64-flac-tools
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
