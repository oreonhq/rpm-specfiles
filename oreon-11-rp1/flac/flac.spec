%global source0_hash f2c1c76592a82ffff8413ba3c4a1299b6c7ab06c734dee03fd88630485c2b920

Name:           flac
Version:        1.5.0
Release:        8%{?dist}
Summary:        An encoder/decoder for the Free Lossless Audio Codec

License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.3-or-later
URL:            https://www.xiph.org/flac/
Source:         https://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(ogg)

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package contains the command-line tools and documentation.

%package        libs
Summary:        Libraries for the Free Lossless Audio Codec

%description    libs
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package contains the FLAC libraries.

%package        devel
Summary:        Development libraries and header files from FLAC

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# The flac binary is needed by the cmake support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains all the files needed to develop applications that
will use the Free Lossless Audio Codec.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# Disable thorough tests
sed -i 's|FLAC__TEST_LEVEL=1|FLAC__TEST_LEVEL=0|' test/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

rm -rfv %{buildroot}%{_docdir}/FLAC

mkdir %{buildroot}%{_datadir}/aclocal
install src/libFLAC/libFLAC.m4 %{buildroot}%{_datadir}/aclocal/
install src/libFLAC++/libFLAC++.m4 %{buildroot}%{_datadir}/aclocal/

%check
%ctest -j1

%files
%{_bindir}/flac
%{_bindir}/metaflac
%{_mandir}/man1/flac.1.*
%{_mandir}/man1/metaflac.1.*

%files libs
%doc AUTHORS README.md CHANGELOG.md
%license COPYING.*
%{_libdir}/libFLAC.so.14*
%{_libdir}/libFLAC++.so.11*

%files devel
%doc doc/api
%{_includedir}/FLAC
%{_includedir}/FLAC++
%{_libdir}/cmake/FLAC/
%{_libdir}/libFLAC.so
%{_libdir}/libFLAC++.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-8
- Prepare for Oreon 11 (RP1)
