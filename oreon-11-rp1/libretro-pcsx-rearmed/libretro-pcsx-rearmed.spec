%global source1_hash 03da010b3c7a90ae10be344975a4568277aed0c35107171d6eae979cca24f5c4
%global source0_hash c85021be6ecd615ce9634764cb8364b69afcf62d9eff0309b58adefbcaf2f46a
%global commit  8d91fbdff8f4db6e256370f030a9f6ac8c7f2c62
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20251216
%global corename pcsx-rearmed
%global filename pcsx_rearmed
Name:           libretro-%{corename}
Version:        15
Release:        1%{?dist}
Summary:        ARM optimized PCSX fork
License:        GPL-2.0-only AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/libretro/pcsx_rearmed
Source0:        https://github.com/libretro/%{filename}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{filename}.libretro
ExcludeArch:    armv7hl
Supplements:    gnome-games
Supplements:    retroarch
Provides:       bundled(crypto)
Provides:       bundled(flac) = 1.3.2
Provides:       bundled(libchdr)
Provides:       bundled(lzma) = 22.01
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
PCSX ReARMed is yet another PCSX fork based on the PCSX-Reloaded project, which
itself contains code from PCSX, PCSX-df and PCSX-Revolution. This version was
originally ARM architecture oriented (hence the name) with its MIPS->ARM dynamic
recompilation and assembly optimizations, but more recently it targets other
architectures too. A fork of this emulator was used in PS Classic (without any
coordination or even notification).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{filename}-%{commit}

# wrong-file-end-of-line-encoding
sed -i 's/\r$//' ChangeLog

%build

%set_build_flags
%make_build -f Makefile.libretro \
    GIT_VERSION=%{shortcommit}   \
    HAVE_CHD=1                   \
    WANT_ZLIB=0                  \
    %{nil}
%install
install -Dpm 0755 %{filename}_libretro.so %{buildroot}%{_libdir}/libretro/%{filename}_libretro.so
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{filename}.libretro
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
