%global source0_hash none

Name:		sdrangel
Version:	7.23.1
Release:	1%{?dist}
Summary:	Software defined radio (SDR) and signal analyzer frontend to various hardware
License:	GPL-3.0-or-later
URL:		https://github.com/f4exb/sdrangel
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	org.sdrangel.SDRangel.metainfo.xml
ExclusiveArch:	%{qt5_qtwebengine_arches}
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Provides:	bundled(jrtplib) = 3.11.1
Provides:	bundled(qthid)
Provides:	bundled(QtWebApp)
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	pkgconf-pkg-config
BuildRequires:	codec2-devel
BuildRequires:	airspyone_host-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	hackrf-devel
BuildRequires:	uhd-devel
BuildRequires:	rtl-sdr-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtwebsockets-devel
BuildRequires:	qt5-qtwebengine-devel
BuildRequires:	qt5-qtmultimedia-devel
# qtpositioning
BuildRequires:	qt5-qtlocation-devel
BuildRequires:	qt5-qtcharts-devel
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	qt5-qtspeech-devel
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:	qt5-qtgamepad-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	boost-devel
BuildRequires:	gr-osmosdr-devel
BuildRequires:	fftw-devel
BuildRequires:	libusbx-devel
BuildRequires:	zlib-devel
#BuildRequires:	faad2-devel
BuildRequires:	opencv-devel
BuildRequires:	serialdv-devel
BuildRequires:	opus-devel
BuildRequires:	libiio-devel
#BuildRequires:	ffmpeg-devel
BuildRequires:	hidapi-devel
BuildRequires:	flac-devel
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme

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
%autosetup -p1

%build
# LIB_SUFFIX workaround for https://github.com/pothosware/SoapyUHD/commit/6b521393cc45c66770f3d4bc69eac7dda982174c.patch
# https://github.com/f4exb/sdrangel/issues/2419
%cmake -DARCH_OPT="" \
%if "%{?_lib}"=="lib64"
  -DLIB_SUFFIX=64
%endif

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/

# drop duplicate readme file, already installed as the doc
rm -f %{buildroot}%{_datadir}/%{name}/Readme.md

%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/sdrangel.desktop

appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.sdrangel.SDRangel.metainfo.xml

%files
%license LICENSE
%doc CHANGELOG Readme.md
%{_bindir}/sdrangel
%{_bindir}/sdrangelbench
%{_bindir}/sdrangelsrv
%{_libdir}/sdrangel
%{_datadir}/applications/sdrangel.desktop
%{_datadir}/icons/hicolor/scalable/apps/sdrangel_icon.svg
%{_metainfodir}/org.sdrangel.SDRangel.metainfo.xml

%changelog
%autochangelog
