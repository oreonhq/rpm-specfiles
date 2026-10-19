%global source0_hash 4c77fb601d10fdffe4a4749f9008a969d778c3bb0e6734bda39e7f46cd11c38c
%global qt_module qtmultimedia
%global openal 1
%global gst 0.10
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%global gst 1.0
%endif
Summary:        Qt5 - Multimedia support
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        2%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Patch1:   0001-Pass-explicit-GL-api-when-initializing-GStreamer-bac.patch
Patch2:   0002-Drop-obsolete-QtOpengl-dependency.patch
Patch100: %{name}-gcc11.patch
%global __provides_exclude_from ^(%{_qt5_archdatadir}/qml/.*\\.so|%{_qt5_plugindir}/.*\\.so)$
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%if "%{?gst}" == "0.10"
%endif
%if 0%{?openal}
%endif
Provides: bundled(fftreal) = 2.00
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(xv)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.
This ranges from the playback and recording of audio and video content to
the use of available devices like cameras and radios.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtdeclarative-devel%{?_isa}
Requires: pkgconfig(libpulse-mainloop-glib)
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

%build

%{qmake_qt5} \
  CONFIG+=git_build \
  GST_VERSION=%{gst}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
pushd %{buildroot}%{_qt5_libdir}
for prl_file in *.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtmultimedia-devel -f %{oreon_filedir}/qt5-qtmultimedia-devel.list
%files -n qt5-qtmultimedia-examples -f %{oreon_filedir}/qt5-qtmultimedia-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
