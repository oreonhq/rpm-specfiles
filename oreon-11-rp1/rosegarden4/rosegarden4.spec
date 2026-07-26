%global source0_hash 75fe52b005899471cc4b0e4954be5d35ee1ce8f41659ab8ef48a26178aa5c36d

%global major 25.06

Name:          rosegarden4
Version:       %{major}
Release:       2%{?dist}
Summary:       MIDI, audio and notation editor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://www.rosegardenmusic.com/
Source0:       https://downloads.sourceforge.net/project/rosegarden/rosegarden/%{major}/rosegarden-%{version}.tar.xz

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: dssi-devel
BuildRequires: fftw-devel
BuildRequires: fontpackages-devel
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtx11extras-devel
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: liblrdf-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: lirc-devel
BuildRequires: libappstream-glib
BuildRequires: zlib-devel
# Use lilypond feta fonts
Requires:      lilypond-emmentaler-fonts

Provides:      rosegarden = %{version}-%{release}

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
# TODO: Please submit an issue to upstream (rhbz#2381409)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
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

%files
%doc AUTHORS CONTRIBUTING README.md
%license COPYING
%{_bindir}/rosegarden
%{_datadir}/applications/*rosegarden.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-rosegarden-*.png
%{_datadir}/icons/hicolor/*/apps/rosegarden.png
%{_datadir}/mime/packages/rosegarden.xml
%{_datadir}/metainfo/rosegarden.appdata.xml

%changelog
%autochangelog
