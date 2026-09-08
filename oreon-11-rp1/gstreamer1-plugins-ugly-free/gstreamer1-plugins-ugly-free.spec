%global source0_hash 0c04763200467b9b61a916b33646a6916a97cc9869d8b6dca57427b1f2734dee

%global         majorminor 1.0

#global gitrel     140
#global gitcommit  4ca3a22b6b33ad8be4383063e76f79c4d346535d
#global shortcommit %%(c=%%{gitcommit}; echo ${c:0:5})

Name:           gstreamer1-plugins-ugly-free
Version:        1.28.3
Release:        1%{?dist}
Summary:        GStreamer streaming media framework "ugly" plugins

License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0
URL:            http://gstreamer.freedesktop.org/
%if 0%{?gitrel}
# git clone git://anongit.freedesktop.org/gstreamer/gst-plugins-ugly
# cd gst-plugins-ugly; git reset --hard %%{gitcommit}; ./autogen.sh; make; make distcheck
Source0:        https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz
%else
Source0:        https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz
%endif

BuildRequires:	meson >= 0.48.0
BuildRequires:	gcc

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  check
BuildRequires:  gettext-devel

BuildRequires:  liba52-devel
BuildRequires:  libcdio-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libmpeg2-devel

# when asfdemux, dvdlpcmdec, dvdsub, and realmedia were moved here
Conflicts: gstreamer1-plugins-ugly < 1.22.7-2

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins whose license is not fully compatible with LGPL.

%package devel
Summary:        Development files for the GStreamer media framework "ugly" plug-ins
Requires:       %{name} = %{version}-%{release}
Requires:       gstreamer1-plugins-base-devel


%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins whose license
is not fully compatible with LGPL.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n gst-plugins-ugly-%{version}


%build
# libsidplay was removed as obsolete, not forbidden
%meson \
    -D package-name="Fedora GStreamer-plugins-ugly package" \
    -D package-origin="http://download.fedoraproject.org" \
    -D doc=disabled \
    -D sidplay=disabled \
    -D x264=disabled \
    -D gpl=enabled

%meson_build

%install
%meson_install

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/gstreamer-ugly-free.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 Richard Hughes <richard@hughsie.com> -->
<component type="codec">
  <id>gstreamer-ugly-free</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - Extra</name>
  <summary>Multimedia playback for CD, DVD, and MP3</summary>
  <description>
    <p>
      This addon includes several additional codecs that have good quality and
      correct functionality, but whose license is not fully compatible with LGPL.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <keywords>
    <keyword>CD</keyword>
    <keyword>DVD</keyword>
    <keyword>MP3</keyword>
  </keywords>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%find_lang gst-plugins-ugly-%{majorminor}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files -f gst-plugins-ugly-%{majorminor}.lang
%license COPYING
%doc README.md README.static-linking RELEASE

%{_metainfodir}/*.metainfo.xml

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstasf.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdsub.so
%{_libdir}/gstreamer-%{majorminor}/libgstrealmedia.so

# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdio.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdread.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so

%if 0
%files devel
%doc %{_datadir}/gtk-doc/html/gst-plugins-ugly-plugins-%{majorminor}
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.3-1
- Import
