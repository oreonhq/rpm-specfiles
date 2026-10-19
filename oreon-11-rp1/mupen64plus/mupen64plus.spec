%global source0_hash 297e17180cd76a7b8ea809d1a1be2c98ed5c7352dc716965a80deb598b21e131
%global debug_package %{nil}
Name:		mupen64plus
Version:	2.6.0
Release:        1%{?dist}
Summary:        Nintendo 64 Emulator
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:		http://www.mupen64plus.org/
Source0:        https://github.com/mupen64plus/mupen64plus-core/releases/download/%{version}/mupen64plus-bundle-src-%{version}.tar.gz
Patch1:		search-lib64.patch
Patch2:		add-includes.patch
Patch3:		upstream-prs-1122-1123-1080-1119.patch
Requires:	hicolor-icon-theme
Conflicts:	mupen64plus-qt
Conflicts:	mupen64plus-cli
ExcludeArch:	s390x
ExcludeArch:	%{ix86}
# oreon:deps
BuildRequires:  binutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  nasm
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lirc)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vulkan)
# /oreon:deps
%description
Mupen64plus is a Nintendo 64 Emulator.
This package includes all the plug-ins.

%package devel
Summary:	Development files for mupen64plus
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for mupen64plus

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-bundle-src-%{version}

# Need to avoid filename conflicts so they can be included in the package
cp -a source/mupen64plus-rsp-hle/LICENSES LICENSE-rsp-hle
cp -a source/mupen64plus-rom/mupen64plus/assets/LICENSES LICENSE-assets
cp -a source/mupen64plus-rom/LICENSES LICENSE-rom
cp -a source/mupen64plus-input-sdl/LICENSES LICENSE-input-sdl
cp -a source/mupen64plus-video-glide64mk2/LICENSES LICENSE-video-glide64mk2
cp -a source/mupen64plus-video-rice/LICENSES LICENSE-video-rice
cp -a source/mupen64plus-ui-console/LICENSES LICENSE-ui-console
cp -a source/mupen64plus-core/LICENSES LICENSE-core
cp -a source/mupen64plus-audio-sdl/LICENSES LICENSE-audio-sdl

%build

ADDITIONAL_FLAGS=""
if [[ "$(uname -m)" = arm* ]] ; then
	ADDITIONAL_FLAGS="NEON=1 VFP_HARD=1 NO_SSE=1"
elif [[ "$(uname -m)" = aarch64 ]] ; then
	ADDITIONAL_FLAGS="NO_SSE=1"
elif [[ "$(uname -m)" = ppc* ]] ; then
	ADDITIONAL_FLAGS="NO_SSE=1"
fi
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
sh m64p_build.sh LIRC=1 $ADDITIONAL_FLAGS
%install
./m64p_install.sh DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir} LIBDIR=%{_libdir} PIC=1 LDCONFIG='true'
find %{buildroot}%{_libdir} -type f -name "*.so*" -exec chmod 0755 "{}" \;
ln -sf libmupen64plus.so.2.0.0 %{buildroot}%{_libdir}/libmupen64plus.so
desktop-file-validate %{buildroot}/%{_datadir}/applications/mupen64plus.desktop
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n mupen64plus-devel -f %{oreon_filedir}/mupen64plus-devel.list

%changelog

%autochangelog
