%global source0_hash 2f338af0231e930539c5e5e04dac7c3384257866cc29fda112215f8c410898c9
%global forgeurl https://github.com/sonic-visualiser/sonic-visualiser
Name:           sonic-visualiser
Version:        5.2.1
Release:        1%{?dist}
Summary:        A program for viewing and exploring audio data
License:        GPL-2.0-or-later
URL:            https://sonicvisualiser.org/
Source0:        %{forgeurl}/releases/download/sv_v%{version}/%{name}-%{version}.tar.gz
Patch:          svcore-atomic-qt-fix.patch
Patch:          svgui-qt-fix.patch
Requires:       hicolor-icon-theme
Requires:       vamp-plugin-sdk%{?_isa} >= 2.10
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  bzip2-devel
BuildRequires:  capnproto
BuildRequires:  dataquay-devel
BuildRequires:  desktop-file-utils
BuildRequires:  liblo-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(capnp)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(fishsound)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libopusenc)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(oggz)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  vamp-plugin-sdk-devel
# /oreon:deps
%description
Sonic Visualiser is an application for viewing and analyzing the
contents of music audio files.

The aim of Sonic Visualiser is to be the first program you reach for
when want to study a musical recording rather than simply listen to
it.

As well as a number of features designed to make exploring audio data
as revealing and fun as possible, Sonic Visualiser also has powerful
annotation capabilities to help you to describe what you find, and the
ability to run automated annotation and analysis plugins in the Vamp
analysis plugin format – as well as applying standard audio effects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/sonic-visualiser.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
