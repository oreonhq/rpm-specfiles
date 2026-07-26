%global source0_hash 4aaab8a3c185cd99d6dda56d95b8f1b20128a6acfd2e86e0349d432a5fdcbce4

Name:           gqrx
Version:        2.17.7
Release:        5%{?dist}
Summary:        Software defined radio receiver powered by GNU Radio and Qt

# Automatically converted from old format: GPLv3+ and GPLv2+ and BSD - review is highly recommended.
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://gqrx.dk/
Source0:        https://github.com/gqrx-sdr/gqrx/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  gnuradio-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  git
BuildRequires:  gr-osmosdr-devel
BuildRequires:  pkgconfig(gnuradio-analog)
BuildRequires:  pkgconfig(gnuradio-blocks)
BuildRequires:  pkgconfig(gnuradio-digital)
BuildRequires:  pkgconfig(gnuradio-filter)
BuildRequires:  pkgconfig(gnuradio-fft)
BuildRequires:  pkgconfig(gnuradio-runtime)
BuildRequires:  gr-osmosdr-devel
BuildRequires:  boost-devel
# gnuradio dependency
BuildRequires:  spdlog-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
# Needed by gnuradio-devel, not gqrx.
BuildRequires:  CGAL-devel
BuildRequires:  libsndfile-devel
BuildRequires:  fftw-devel
BuildRequires:  libunwind-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  portaudio-devel

%description
Gqrx is a software defined radio receiver powered by the GNU Radio SDR
framework and the Qt graphical toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# man page
install -Dpm 644 resources/%{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1

# icon
install -Dpm 644 resources/icons/%{name}.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# appdata
#install -Dpm 644 dk.%{name}.%{name}.appdata.xml \
#  %{buildroot}%{_datadir}/appdata/dk.%{name}.%{name}.appdata.xml

# desktop-file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications dk.%{name}.%{name}.desktop

%check
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/dk.%{name}.%{name}.appdata.xml

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/applications/dk.%{name}.%{name}.desktop
%{_datadir}/metainfo/dk.%{name}.%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc COPYING README.md

%changelog
%autochangelog
