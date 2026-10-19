%global source0_hash f2c1c76592a82ffff8413ba3c4a1299b6c7ab06c734dee03fd88630485c2b920
%{?mingw_package_header}
Name:           mingw-flac
Version:        1.5.0
Release:        1%{?dist}
Summary:        Encoder/decoder for the Free Lossless Audio Codec
License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.1-or-later
URL:            https://xiph.org/flac/
Source0:        https://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libogg
BuildRequires:  mingw64-win-iconv
BuildRequires:  nasm
# /oreon:deps
%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

%package -n mingw32-flac
Summary:        Encoder/decoder for the Free Lossless Audio Codec
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
Summary:        Tools for Free Lossless Audio Codec
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

./autogen.sh -V
%mingw_configure \
    --disable-silent-rules \
    --disable-thorough-tests
%mingw_make %{?_smp_mflags}
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_docdir}/flac*
rm -rf %{buildroot}%{mingw64_docdir}/flac*
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la
%oreon_autofiles mingw32-flac usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-flac-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-flac usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-flac-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-flac -f %{oreon_filedir}/mingw32-flac.list
%files -n mingw32-flac-tools -f %{oreon_filedir}/mingw32-flac-tools.list
%files -n mingw64-flac -f %{oreon_filedir}/mingw64-flac.list
%files -n mingw64-flac-tools -f %{oreon_filedir}/mingw64-flac-tools.list

%changelog

%autochangelog
