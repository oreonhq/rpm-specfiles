%global source0_hash 3d7d4e14479abea30fbc5eb5dc12a0c7012bc6a5b686ec3a990c68f18a414bf3

%global __python %{__python3}
%global gstreamer1_min_version 1.18.0

Name:           pitivi
Version:        2023.03
Release:        20%{?dist}
Summary:        Non-linear video editor

License:        LGPL-2.0-or-later
URL:            http://www.pitivi.org/
Source0:        https://download.gnome.org/sources/pitivi/2023/pitivi-%{version}.tar.xz

Patch0:         485.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  python3
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  gettext
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer1_min_version}
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  %{_bindir}/desktop-file-validate
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  gst-devtools-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel

Requires:	gstreamer1 >= %{gstreamer1_min_version}
Requires:	gstreamer1-plugins-good >= %{gstreamer1_min_version}
Requires:	gstreamer1-plugins-bad-free >= %{gstreamer1_min_version}
Requires:	gstreamer1-plugins-bad-free-gtk >= %{gstreamer1_min_version}
Requires:       gstreamer1-plugin-libav >= %{gstreamer1_min_version}
Requires:       gstreamer1-plugins-bad-free-opencv >= %{gstreamer1_min_version}
Requires:	python3-gstreamer1 >= 1.6.0
Requires:	gst-editing-services >= %{gstreamer1_min_version}
Requires:	hicolor-icon-theme
Requires:	gnome-desktop3
Requires:	frei0r-plugins
Requires:	python3-numpy
Requires:	python3-matplotlib
Requires:	python3-matplotlib-gtk3
Requires:	yelp
Requires:	python3-cairo >= 1.0.0
Requires:	libnotify
Requires:	python3-inotify
Requires:	python3-canberra
Requires:	python3-gobject
Requires:       python3-scipy
Requires:	gobject-introspection
Requires:	opus-tools
Requires:       gsound
%if 0%{?fedora} >= 39
Requires:       libpeas1
%else
Requires:       libpeas
%endif

%description
Pitivi is an application using the GStreamer multimedia framework to
manipulate a large set of multimedia sources.

At this level of development it can be compared to a classic video editing
program.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup

%patch -P 0 -p1

# https://gitlab.gnome.org/GNOME/pitivi/commit/0f3e399e387e64dcc3c5015a8aacb26fbe49800f
sed -i -e "/Pycairo_CAPI/d" pitivi/coptimizations/renderer.c

rm -rf subprojects/gst-transcoder
sed -i "/subproject('gst-transcoder')/d" meson.build
sed -i "/gst_transcoder_dep/d" meson.build

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{python3_sitearch}/pitivi
mv %{buildroot}%{_libdir}/pitivi/python/pitivi %{buildroot}%{python3_sitearch}/
rmdir %{buildroot}%{_libdir}/pitivi/python

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.pitivi.Pitivi.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.pitivi.Pitivi.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/org.pitivi.Pitivi.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/org.pitivi.Pitivi-mime.xml
%{_datadir}/help/*
%{_datadir}/metainfo/org.pitivi.Pitivi.appdata.xml
%{python3_sitearch}/pitivi/

%changelog
%autochangelog
