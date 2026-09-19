%global source0_hash b33cc4934322bcbf6efcbacf49e3ca01aadbea4114ec9589d1b1e9d20f72954b

%{?mingw_package_header}

Name:           mingw-libvorbis
Version:        1.3.7
Release:        16%{?dist}
Summary:        MinGW Windows libvorbis library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://www.xiph.org/vorbis/
Source0:        https://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libogg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-libogg

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

This package contains the MinGW Windows cross compiled libvorbis library.

# Win32
%package -n mingw32-libvorbis
Summary:        MinGW Windows libvorbis library

%description -n mingw32-libvorbis
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

This package contains the MinGW Windows cross compiled libvorbis library.

# Win64
%package -n mingw64-libvorbis
Summary:        MinGW Windows libvorbis library

%description -n mingw64-libvorbis
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

This package contains the MinGW Windows cross compiled libvorbis library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libvorbis-%{version} -p1

%build
%mingw_configure --disable-static
%mingw_make_build

%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_libdir}/*.la
rm -rf %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_datadir}/doc/
rm -rf %{buildroot}%{mingw64_datadir}/doc/

# Win32
%files -n mingw32-libvorbis
%license COPYING
%{mingw32_bindir}/libvorbis-0.dll
%{mingw32_bindir}/libvorbisenc-2.dll
%{mingw32_bindir}/libvorbisfile-3.dll
%{mingw32_includedir}/vorbis/
%{mingw32_libdir}/libvorbis.dll.a
%{mingw32_libdir}/libvorbisenc.dll.a
%{mingw32_libdir}/libvorbisfile.dll.a
%{mingw32_libdir}/pkgconfig/vorbis.pc
%{mingw32_libdir}/pkgconfig/vorbisenc.pc
%{mingw32_libdir}/pkgconfig/vorbisfile.pc
%{mingw32_datadir}/aclocal/vorbis.m4

# Win64
%files -n mingw64-libvorbis
%license COPYING
%{mingw64_bindir}/libvorbis-0.dll
%{mingw64_bindir}/libvorbisenc-2.dll
%{mingw64_bindir}/libvorbisfile-3.dll
%{mingw64_includedir}/vorbis/
%{mingw64_libdir}/libvorbis.dll.a
%{mingw64_libdir}/libvorbisenc.dll.a
%{mingw64_libdir}/libvorbisfile.dll.a
%{mingw64_libdir}/pkgconfig/vorbis.pc
%{mingw64_libdir}/pkgconfig/vorbisenc.pc
%{mingw64_libdir}/pkgconfig/vorbisfile.pc
%{mingw64_datadir}/aclocal/vorbis.m4

%changelog
%autochangelog
