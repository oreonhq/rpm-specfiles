%global source0_hash b33cc4934322bcbf6efcbacf49e3ca01aadbea4114ec9589d1b1e9d20f72954b
%{?mingw_package_header}
Name:           mingw-libvorbis
Version:        1.3.7
Release:        16%{?dist}
Summary:        MinGW Windows libvorbis library
License:        LicenseRef-Callaway-BSD
URL:            https://www.xiph.org/vorbis/
Source0:        https://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libogg
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libogg
# /oreon:deps
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
%global oreon_srcdir libvorbis-%{version}
%oreon_prep
%build

%mingw_configure --disable-static
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_libdir}/*.la
rm -rf %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_datadir}/doc/
rm -rf %{buildroot}%{mingw64_datadir}/doc/
%oreon_autofiles mingw32-libvorbis usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libvorbis usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libvorbis -f %{oreon_filedir}/mingw32-libvorbis.list
%files -n mingw64-libvorbis -f %{oreon_filedir}/mingw64-libvorbis.list

%changelog

%autochangelog
