%global source0_hash cb7d112433cf7c2e37a8ec918fb24f0ea5cb293cfa1002488e431de26482f47b

%global glib2_ver 2.40
%global gst_ver 1.0.0
%global gst_plugins_base_ver 1.0.0
%global far farstream

Name:           %{far}02
Version:        0.2.9
Release:        20%{?dist}
Summary:        Libraries for videoconferencing

# Package is LGPLv2 except for a few files in /common/coverage/
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            https://www.freedesktop.org/wiki/Software/Farstream/
Source0:        https://freedesktop.org/software/%{far}/releases/%{far}/%{far}-%{version}.tar.gz
# patch for upstream issue https://gitlab.freedesktop.org/farstream/farstream/issues/16
Patch0:         farstream-0.2.8-configure-add-check-for-glib-mkenums.patch
Patch1:         farstream-0.2.9-build-Adapt-to-backwards-incompatible-change-in-GNU-.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnice-devel >= 0.1.8
BuildRequires:  glib2-devel >= %{glib2_ver}
BuildRequires:  gstreamer1-devel >= %{gst_ver}
BuildRequires:  gstreamer1-plugins-base-devel >= %{gst_plugins_base_ver}
BuildRequires:  gtk-doc
BuildRequires:  gupnp-igd-devel
BuildRequires:  gobject-introspection-devel
BuildRequires: make

Requires:       glib2%{?isa} >= %{glib2_ver}
Requires:       gstreamer1-plugins-good >= 1.0.0
Requires:       gstreamer1-plugins-bad-free >= 1.0.0
Requires:       libnice-gstreamer1


%description
%{name} is a collection of GStreamer modules and libraries for
videoconferencing.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gstreamer1-devel  >= %{gst_ver}
Requires:       gstreamer1-plugins-base-devel >= %{gst_plugins_base_ver}
Requires:       pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{far}-%{version}
%patch -P0 -p1
%patch -P1 -p1


%check
#make check


%build
autoreconf --force --install
%configure                                                  \
  --with-package-name='Fedora Farstream-0.2 package'        \
  --with-package-origin='http://download.fedoraproject.org' \
  --disable-silent-rules                                    \
  --disable-static

# It appears there are dependencies missing in the generated
# Makefiles which can result in libfarstream being referenced
# before or while it is still being built.
#
# This is particularly easy to reproduce with LTO because it
# changes the relative speeds of TU compilation vs linking
# Just disable parallel builds for now
make


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc COPYING NEWS AUTHORS
%{_libdir}/*.so.*
%dir %{_libdir}/%{far}-0.2
%{_libdir}/%{far}-0.2/libmulticast-transmitter.so
%{_libdir}/%{far}-0.2/libnice-transmitter.so
%{_libdir}/%{far}-0.2/librawudp-transmitter.so
%{_libdir}/%{far}-0.2/libshm-transmitter.so
%{_libdir}/gstreamer-1.0/libfsrawconference.so
%{_libdir}/gstreamer-1.0/libfsrtpxdata.so
%{_libdir}/gstreamer-1.0/libfsrtpconference.so
%{_libdir}/gstreamer-1.0/libfsvideoanyrate.so
%{_libdir}/girepository-1.0/Farstream-0.2.typelib
%dir %{_datadir}/%{far}
%dir %{_datadir}/%{far}/0.2
%dir %{_datadir}/%{far}/0.2/fsrtpconference
%dir %{_datadir}/%{far}/0.2/fsrawconference
%{_datadir}/%{far}/0.2/fsrawconference/default-element-properties
%{_datadir}/%{far}/0.2/fsrtpconference/default-codec-preferences
%{_datadir}/%{far}/0.2/fsrtpconference/default-element-properties

%files devel
%{_libdir}/libfarstream-0.2.so
%{_libdir}/pkgconfig/%{far}-0.2.pc
%{_includedir}/%{far}-0.2/%{far}/
%{_datadir}/gir-1.0/Farstream-0.2.gir
%{_datadir}/gtk-doc/html/%{far}-libs-0.2/
%{_datadir}/gtk-doc/html/%{far}-plugins-0.2/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.9-20
- Prepare for Oreon 11 (RP1)
