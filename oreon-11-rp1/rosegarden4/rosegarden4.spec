%global source0_hash 75d9f01c6aa46d1a08c1ac29ee375e4aab1dcdb670fb7230a9e69c09458d3bd9
%global major 26.06
Name:          rosegarden4
Version:       %{major}
Release:        1%{?dist}
Summary:        MIDI, audio and notation editor
License:       GPL-2.0-or-later
URL:           https://www.rosegardenmusic.com/
Source0:        https://downloads.sourceforge.net/project/rosegarden/rosegarden/%{version}/rosegarden-%{version}.tar.xz
Requires:      lilypond-emmentaler-fonts
Provides:      rosegarden = %{version}-%{release}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  fftw-devel
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  libappstream-glib
BuildRequires:  liblo-devel
BuildRequires:  liblrdf-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lirc-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Rosegarden is a professional audio and MIDI sequencer, score editor, and
general purpose music composition and editing environment.

Rosegarden is an easy to learn, attractive application, ideal for composers,
musicians, music students, and small studio or home recording environments.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n rosegarden-%{version}

# Fix permissions:
chmod 644 src/gui/widgets/BaseTextFloat.*

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
appstream-util replace-screenshots %{buildroot}%{_datadir}/metainfo/rosegarden.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rosegarden/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rosegarden/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rosegarden/c.png
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original \
  --remove-category X-SuSE-Sequencer \
  --remove-category X-Red-Hat-Base \
  %{buildroot}%{_datadir}/applications/com.rosegardenmusic.rosegarden.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
