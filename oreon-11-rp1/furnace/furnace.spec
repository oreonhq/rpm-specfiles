%global source1_hash 46da29342d2968ff222ba00e07c646e038b76af2e6c86de037c653059a056251
%global source0_hash 46da29342d2968ff222ba00e07c646e038b76af2e6c86de037c653059a056251
%global forgeurl https://github.com/tildearrow/furnace
Version:        0.6.8.3
%forgemeta
Name:           furnace
Release:        1%{?dist}
Summary:        a multi-system chiptune tracker compatible with DefleMask modules
License:        GPL-2.0-or-later AND BSD-3-Clause AND Zlib AND Unlicense AND LGPL-2.1-or-later AND GPL-2.0-only AND MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/superctr/adpcm/archive/ef7a217154badc3b99978ac481b268c8aab67bd8.tar.gz
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
%{summary}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

tar xf %{SOURCE1} -C extern/adpcm --strip-components=1

%build

%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_FREETYPE=ON \
    -DSYSTEM_FFTW=ON \
    -DSYSTEM_FMT=ON \
    -DSYSTEM_FREETYPE=ON \
    -DSYSTEM_LIBSNDFILE=ON \
    -DSYSTEM_PORTAUDIO=ON \
    -DSYSTEM_RTMIDI=ON \
    -DSYSTEM_ZLIB=ON \
    -DSYSTEM_SDL2=ON
%cmake_build
%install
%cmake_install
%find_lang furnace
rm -r %{buildroot}%{_datadir}/icons/hicolor/1024x1024
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n furnace-doc -f %{oreon_filedir}/furnace-doc.list

%changelog

%autochangelog
