%global source0_hash 1c110d4dbd411b104320e5adb3009eeadd2613354d65feb93612e3b1f1382989

%global prerelease 20250512

Name:           lv2-x42-plugins
Version:        0.21.0
Release:        0.3.%{prerelease}%{?dist}
Summary:        A number of LV2 plugins

# files in balance.lv2/pugl are ISC, the rest are GPLv2+
# Automatically converted from old format: GPLv2+ and ISC - review is highly recommended.
License:        GPL-2.0-or-later AND ISC
URL:            https://github.com/x42/x42-plugins
# A tarball is now provided at https://gareus.org/misc/x42-plugins.php
Source0:        https://gareus.org/misc/x42-plugins/x42-plugins-%{prerelease}.tar.xz
Source1:        README.md

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  zita-convolver-devel >= 3.1.0
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libltc-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  fftw3-devel
BuildRequires:  gtk2-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  ftgl-devel
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  mesa-libEGL-devel
Requires:       lv2 >= 1.8.1
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       gnu-free-mono-fonts

%description
A number of lv2 plugins including stereo balance, midi filter, delay,
convolver, fader, parametric equalizer, auto-tune.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n x42-plugins-%{prerelease}
cp -p %{SOURCE1} .

%build
%set_build_flags
export FONTFILE="/usr/share/fonts/gnu-free/FreeSansBold.ttf"
export STRIP=/bin/true
export PKG_CONFIG=pkgconf
export OPTIMIZATIONS="%{optflags}"
%make_build LIBDIR=%{_libdir} LV2DIR=%{_libdir}/lv2 PREFIX=%{_prefix}

%install
%make_install LIBDIR=%{_libdir} LV2DIR=%{_libdir}/lv2 PREFIX=%{_prefix}

%files
# all plugins share the same license
%license balance.lv2/COPYING
%doc plugin.versions plugin.list README.md
%{_libdir}/lv2/*.lv2
%{_bindir}/x42*
%{_mandir}/man1/x42*

%changelog
%autochangelog
