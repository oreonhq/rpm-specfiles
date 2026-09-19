%global source0_hash 2ab5c870909cf1306ebe0a35786c1261680a27dc997862399f759bca9bd32743

Name:           soundconverter
Version:        4.1.3
Release:        1%{?dist}
Summary:        Simple sound converter application for GNOME
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only

URL:            https://soundconverter.org
Source0:        https://github.com/kassoulet/soundconverter/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-base
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib

Requires:       python3-gobject-base
Requires:       gtk3
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

%generate_buildrequires
%pyproject_buildrequires

%description
SoundConverter is the leading audio file converter for the GNOME Desktop. It
reads anything GStreamer can read (Ogg Vorbis, AAC, MP3, FLAC, WAV, AVI, MPEG,
MOV, M4A, AC3, DTS, ALAC, MPC, Shorten, APE, SID, MOD, XM, S3M, etc...), and
writes to Opus, Ogg Vorbis, FLAC, WAV, AAC, and MP3 files, or use any GNOME
Audio Profile.

SoundConverter aims to be simple to use, and very fast. Thanks to its
multithreaded design, it will use as many cores as possible to speed up the
conversion. It can also extract the audio from videos.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install

%find_lang %{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --add-category X-OutputGeneration \
  --delete-original \
  build/share/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

rm -f %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.soundconverter.gschema.xml
%{_docdir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.dist-info

%changelog
%autochangelog
