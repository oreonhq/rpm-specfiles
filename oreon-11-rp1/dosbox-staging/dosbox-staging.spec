%global source0_hash 9b36be5a666784adaeffa560bd0950691f851a76bdb97e7ae3c989561e91caf3
Name:    dosbox-staging
Version: 0.83.0
Release:        1%{?dist}
Summary:        Modern continuation of DOSBox with advanced features
URL:     https://www.dosbox-staging.org/
License: GPL-2.0-or-later AND Unlicense AND (MIT-0 OR Unlicense) AND MIT AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND Fair AND LGPL-2.1-or-later AND (MIT OR Unlicense) AND (MIT OR WTFPL) AND BSD-2-Clause
Source0:        https://github.com/dosbox-staging/dosbox-staging/archive/v%{version}/%{name}-%{version}.tar.gz
Provides:  dosbox = %{version}-%{release}
Requires: hicolor-icon-theme
Requires: fluid-soundfont-gm
Requires: libEGL
Provides: bundled(enet)
Provides: bundled(gulrak-filesystem)
Provides: bundled(gui_tk)
Provides: bundled(loguru)
Provides: bundled(nuked-opl3)
Provides: bundled(libsidplayfp)
Provides: bundled(gpakosz-whereami)
Provides: bundled(archive)
Provides: bundled(dr_libs)
Provides: bundled(stb_vorbis)
Provides: bundled(xxhash)
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  iir1-devel
BuildRequires:  libXi-devel
BuildRequires:  libappstream-glib
BuildRequires:  libatomic
BuildRequires:  libpng-devel
BuildRequires:  libslirp-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  mt32emu-devel
BuildRequires:  opusfile-devel
BuildRequires:  speexdsp-devel
# /oreon:deps
%description
DOSBox Staging is a modern continuation of DOSBox with advanced features and
current development practices.

It is a (mostly) drop-in replacement for older DOSBox versions — your existing
configurations will continue to work, and you will have access to many advanced
features.

DOSBox Staging comes with sensible defaults, so you’ll need to write a lot less
configuration than with older DOSBox versions. Most games and applications
require no tweaking and will work fine with the stock settings. However, the
extensive configuration options and advanced features are available if you wish
to delve deeper.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove unused file
rm src/libs/decoders/stb.h

%build

%meson -Duse_zlib_ng=false
%meson_build
%install
%meson_install
mkdir -p  %{buildroot}%{_datadir}/bash-completion/completions
cp contrib/linux/bash-completion/dosbox %{buildroot}%{_datadir}/bash-completion/completions
%oreon_autofiles main

%check

%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
