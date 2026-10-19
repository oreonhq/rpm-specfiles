%global stable_kf6 stable
%global source0_hash d58fe7dceaceaa18206816558f6b640667073966f237fba14abd177bbdcd9dcd
%undefine _include_frame_pointers
ExcludeArch: %{ix86}
Name:           kwave
Version: 25.12.3
Release:        1%{?dist}
Summary:        Sound Editor for KDE
Summary(de):    Sound-Editor für KDE
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-CC-BY-SA
URL:            http://kwave.sourceforge.net
Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       %{name}-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  alsa-lib-devel
BuildRequires:  audiofile-devel
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fftw-devel
BuildRequires:  flac-devel
BuildRequires:  gettext
BuildRequires:  id3lib-devel
BuildRequires:  libappstream-glib
BuildRequires:  libmad-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  opus-devel
BuildRequires:  poxml
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
With Kwave you can record, play back, import and edit many sorts of audio files
including multi-channel files. Kwave includes some plugins to transform audio
files in several ways and presents a graphical view with a complete zoom- and
scroll capability.

%description -l de
Mit Kwave können Sie ein- oder mehrkanalige Audio-Dateien aufnehmen, wieder-
geben, importieren und bearbeiten. Kwave verfügt über Plugins zum Umwandeln
von Audio-Dateien auf verschiedene Weise. Die grafische Oberfläche bietet
alle Möglichkeiten für Änderungen der Ansichtsgröße und zum Rollen.

%package doc
Summary:        User manuals for %{name}
Summary(de):    Benutzerhandbücher für %{name}
License:        LicenseRef-Callaway-GFDL
BuildArch:      noarch
%description doc
This package contains arch-independent files for %{name}, especially the
HTML documentation.

%description doc -l de
Dieses Paket enthält architekturunabhängige Dateien für %{name},
speziell die HTML-Dokumentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
   -DWITH_MP3=ON
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n kwave-doc -f %{oreon_filedir}/kwave-doc.list

%changelog

%autochangelog
