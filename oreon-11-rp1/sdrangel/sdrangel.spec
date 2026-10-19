%global source0_hash eec945efc55d743cc9b0c6e7a8a9e20c9d289d4a70dfb907c3b923a6b555a8ff
Name:		sdrangel
Version:	7.27.2
Release:        1%{?dist}
Summary:        Software defined radio (SDR) and signal analyzer frontend to various hardware
License:	GPL-3.0-or-later
URL:		https://github.com/f4exb/sdrangel
Source0:        https://github.com/f4exb/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	org.sdrangel.SDRangel.metainfo.xml
ExclusiveArch:	%{qt5_qtwebengine_arches}
ExcludeArch:    %{ix86}
Provides:	bundled(jrtplib) = 3.11.1
Provides:	bundled(qthid)
Provides:	bundled(QtWebApp)
Requires:	hicolor-icon-theme
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  airspyone_host-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  codec2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  gr-osmosdr-devel
BuildRequires:  graphviz
BuildRequires:  hackrf-devel
BuildRequires:  hidapi-devel
BuildRequires:  libappstream-glib
BuildRequires:  libiio-devel
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  opencv-devel
BuildRequires:  opus-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtcharts-devel
BuildRequires:  qt5-qtgamepad-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtspeech-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebengine-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  serialdv-devel
BuildRequires:  uhd-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
SDRangel uses sample source plugins to collect I/Q samples from a hardware
device. Then in the passband returned possibly decimated one or more channel
Rx plugins can be used to demodulate, decode or analyze some part of this
spectrum.

Conversely SDRangel uses sample sink plugins to send I/Q samples to a
hardware device. One or more channel Tx plugins can be used to produce
modulated samples that are mixed into a transmission passband with possible
subsequent interpolation before being sent to the device or written to file.

More information is available on the project Wiki:
https://github.com/f4exb/sdrangel/wiki/Quick-start

%prep
%oreon_prep
%build

%cmake -DARCH_OPT="" \
%if "%{?_lib}"=="lib64"
  -DLIB_SUFFIX=64
%endif
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/
rm -f %{buildroot}%{_datadir}/%{name}/Readme.md
%oreon_autofiles main

%check

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/sdrangel.desktop
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.sdrangel.SDRangel.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
