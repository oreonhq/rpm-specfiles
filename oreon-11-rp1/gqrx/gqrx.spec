%global source0_hash 4aaab8a3c185cd99d6dda56d95b8f1b20128a6acfd2e86e0349d432a5fdcbce4
Name:           gqrx
Version:        2.17.7
Release:        1%{?dist}
Summary:        Software defined radio receiver powered by GNU Radio and Qt
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://gqrx.dk/
Source0:        https://github.com/gqrx-sdr/gqrx/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  CGAL-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gnuradio-devel
BuildRequires:  gr-osmosdr-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libappstream-glib
BuildRequires:  libsndfile-devel
BuildRequires:  libunwind-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gnuradio-analog)
BuildRequires:  pkgconfig(gnuradio-blocks)
BuildRequires:  pkgconfig(gnuradio-digital)
BuildRequires:  pkgconfig(gnuradio-fft)
BuildRequires:  pkgconfig(gnuradio-filter)
BuildRequires:  pkgconfig(gnuradio-runtime)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  spdlog-devel
# /oreon:deps
%description
Gqrx is a software defined radio receiver powered by the GNU Radio SDR
framework and the Qt graphical toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
install -Dpm 644 resources/%{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm 644 resources/icons/%{name}.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications dk.%{name}.%{name}.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/dk.%{name}.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
