%global source0_hash 8e8585f567c0a36be7a219b4b76145b4d8464411a2c9dae70584f321b64c5865
Name:	gstreamer-plugins-espeak
Version:	0.6.0
Release:        1%{?dist}
Summary:        A simple gstreamer plugin to use espeak
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://wiki.sugarlabs.org/go/Activity_Team/gst-plugins-espeak
Source0:        http://download.sugarlabs.org/sources/honey/gst-plugins-espeak/gst-plugins-espeak-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  espeak-ng-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
A simple gstreamer plugin to use espeak as a sound source.
It was developed to simplify the espeak usage in the Sugar Speak activity.
The plugin uses given text to produce audio output. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gst-plugins-espeak-%{version}

sed -i 's#espeak/speak_lib.h#espeak-ng/speak_lib.h#' src/espeak.c

%build

autoreconf -vif
sed -i 's/NANO=1/NANO=0/g' configure
%configure
%{make_build}
%install
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gstreamer-espeak.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 Richard Hughes <richard@hughsie.com> -->
<component type="codec">
  <id>gstreamer-espeak</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>eSpeak GStreamer Multimedia Codec</name>
  <summary>Multimedia playback for eSpeak</summary>
  <description>
    <p>
      eSpeak is a compact open source text-to-speech synthesizer for English
      and other languages.
      This codec includes different voices, whose characteristics can be altered.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
find %{buildroot} -name '*.la' -delete
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
