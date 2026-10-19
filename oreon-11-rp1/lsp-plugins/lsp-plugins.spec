%global source0_hash 022accad721bed284fad445dcc89acb3b9d1f12731921dbe1edbd0cde672e1a3
Name:           lsp-plugins
Version:        1.2.27
Release:        1%{?dist}
Summary:        Linux Studio Plugins
License:        LGPL-3.0-or-later and Zlib
URL:            https://lsp-plug.in/
Source0:        https://github.com/lsp-plugins/%{name}/releases/download/%{version}/%{name}-src-%{version}.tar.gz
ExcludeArch: %{ix86}
Requires:       redhat-menus
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  libGL-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libstdc++-devel
BuildRequires:  lv2-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  php
BuildRequires:  php-cli
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
# /oreon:deps
%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with CLAP, LADSPA, LV2, VST2/LinuxVST, VST3 and
JACK standalone formats.

%package -n liblsp-r3d-glx
Summary:        liblsp-r3d-glx plugin
%description -n liblsp-r3d-glx
Library liblsp-r3d-glx plugin.

%package -n liblsp-r3d-glx-devel
Summary:        liblsp-r3d-glx plugin development
Requires:       liblsp-r3d-glx%{?_isa} = %{version}-%{release}
%description -n liblsp-r3d-glx-devel
Library liblsp-r3d-glx plugin development.

%package doc
Summary:        Linux Studio Plugins documentation
BuildArch:      noarch
%description doc
Documentation for Linux Studio Plugins

%package ladspa
Summary:        Linux Studio Plugins LADSPA format
Requires:       ladspa%{?_isa}
%description ladspa
Linux Studio Plugins (LSP) compatible with the obsolete LADSPA format.

%package lv2
Summary:        Linux Studio Plugins LV2 format
Requires:       lv2%{?_isa}
%description lv2
Linux Studio Plugins (LSP) compatible with the LV2 format (recommended format).

%package vst
Summary:        Linux Studio Plugins VST format
Requires:       Carla-vst%{?_isa}
%description vst
Linux Studio Plugins (LSP) and UIs for Steinberg's VST 2.4 format ported on GNU/Linux Platform.

%package vst3
Summary:        Linux Studio Plugins VST 3 format
%description vst3
Linux Studio Plugins (LSP) and UIs for Steinberg's VST 3 format ported on GNU/Linux Platform.

%package jack
Summary:        Linux Studio Plugins JACK format
%description jack
Linux Studio Plugins (LSP) standalone versions for JACK Audio connection Kit with UI

%package clap
Summary:        Linux Studio Plugins CLAP format
%description clap
Linux Studio Plugins (LSP) compatible with the CLAP format.

%package gstreamer
Summary:        Linux Studio Plugins gstreamer format
%description gstreamer
Linux Studio Plugins (LSP) compatible with the gstreamer format.

%prep

%autosetup -p1 -n %{name}
rm -rf include/3rdparty/ladspa
sed -i "s|\$\(LDFLAGS_EXT\) -r|\$\(LDFLAGS_EXT\) -r %{build_ldflags}|" make/tools.mk
# sed -i 's|march=i586|march=i686|' make/system.mk
# sed -i 's|gst/|gstreamer-1.0/gst/|' modules/lsp-plugin-fw/include/lsp-plug.in/plug-fw/wrap/gstreamer/defs.h

%build

%ifarch %ix86
%global optflags %{optflags} -DLSP_PROFILING
%endif
%{set_build_flags}
make config ADD_FEATURES=xdg \
  PREFIX=%{_prefix} LIBDIR=%{_libdir} ETCDIR=%{_sysconfdir} \
  CFLAGS_EXT="%optflags" CXXFLAGS_EXT="%optflags"
%make_build
%install
%make_install GSTREAMER_INSTDIR=%{_libdir}/gstreamer-1.0
mv %{buildroot}%{_datadir}/doc .
rm %{buildroot}%{_libdir}/*.a
%oreon_autofiles liblsp-r3d-glx usr/*/lib*.so.*
%oreon_autofiles liblsp-r3d-glx-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n liblsp-r3d-glx -f %{oreon_filedir}/liblsp-r3d-glx.list
%files -n liblsp-r3d-glx-devel -f %{oreon_filedir}/liblsp-r3d-glx-devel.list
%files -n lsp-plugins-doc -f %{oreon_filedir}/lsp-plugins-doc.list
%files -n lsp-plugins-ladspa -f %{oreon_filedir}/lsp-plugins-ladspa.list
%files -n lsp-plugins-lv2 -f %{oreon_filedir}/lsp-plugins-lv2.list
%files -n lsp-plugins-vst -f %{oreon_filedir}/lsp-plugins-vst.list
%files -n lsp-plugins-vst3 -f %{oreon_filedir}/lsp-plugins-vst3.list
%files -n lsp-plugins-jack -f %{oreon_filedir}/lsp-plugins-jack.list
%files -n lsp-plugins-clap -f %{oreon_filedir}/lsp-plugins-clap.list
%files -n lsp-plugins-gstreamer -f %{oreon_filedir}/lsp-plugins-gstreamer.list

%changelog

%autochangelog
