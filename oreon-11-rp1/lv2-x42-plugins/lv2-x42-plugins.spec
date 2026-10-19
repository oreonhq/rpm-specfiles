%global source0_hash 1c110d4dbd411b104320e5adb3009eeadd2613354d65feb93612e3b1f1382989
%global prerelease 20250512
Name:           lv2-x42-plugins
Version:        0.21.0
Release:        1%{?dist}
Summary:        A number of LV2 plugins
License:        GPL-2.0-or-later AND ISC
URL:            https://github.com/x42/x42-plugins
Source0:        https://gareus.org/misc/x42-plugins/x42-plugins-%{prerelease}.tar.xz
Source1:        README.md
Requires:       lv2 >= 1.8.1
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       gnu-free-mono-fonts
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  fftw3-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libltc-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lv2-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  zita-convolver-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
