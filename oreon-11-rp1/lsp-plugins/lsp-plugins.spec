%global source0_hash none

Name:           lsp-plugins
Version:        1.2.27
Release:        1%{?dist}
Summary:        Linux Studio Plugins

License:        LGPL-3.0-or-later and Zlib
URL:            https://lsp-plug.in/
Source0:        https://github.com/lsp-plugins/%{name}/releases/download/%{version}/%{name}-src-%{version}.tar.gz

# Fixed atomic operations for AArch64
# https://github.com/lsp-plugins/lsp-common-lib/commit/156be4d61c57d805745b85d7fadb781a4bc581b0
# Patch0:         156be4d61c57d805745b85d7fadb781a4bc581b0.patch

ExcludeArch: %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libstdc++-devel >= 4.7
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pipewire-jack-audio-connection-kit
%else
BuildRequires:  jack-audio-connection-kit-devel >= 1.9.5
%endif
BuildRequires:  lv2-devel >= 1.10
BuildRequires:  ladspa-devel >= 1.13
BuildRequires:  expat-devel >= 2.1
BuildRequires:  libsndfile-devel >= 1.0.25
BuildRequires:  cairo-devel >= 1.14
BuildRequires:  php >= 5.5.14
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libGL-devel
BuildRequires:  php-cli
BuildRequires:  desktop-file-utils
BuildRequires:  libXrandr-devel
BuildRequires:  pkgconfig(gstreamer-audio-1.0)

Requires:       redhat-menus
Requires:       hicolor-icon-theme

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
#Requires:       Carla-vst%{?_isa}

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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files -n liblsp-r3d-glx
%license COPYING COPYING.LESSER
%{_libdir}/liblsp-r3d-glx-lib-1.0.27.so

%files -n liblsp-r3d-glx-devel
%{_libdir}/liblsp-r3d-glx-lib.so
%{_libdir}/pkgconfig/lsp-r3d-glx-lib.pc

%files doc
%license COPYING COPYING.LESSER
%doc doc/%{name}/*

%files ladspa
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/ladspa/%{name}*

%files lv2
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/lv2/%{name}*

%files vst
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/vst/%{name}*

%files vst3
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%dir %{_libdir}/vst3
%{_libdir}/vst3/%{name}*

%files jack
%license COPYING COPYING.LESSER
%doc CHANGELOG README.md
%{_libdir}/%{name}

%files clap
%dir %{_libdir}/clap
%{_libdir}/clap/%{name}.clap

%files gstreamer
%{_libdir}/gstreamer-1.0/libgstlsp-plugins*.so

%changelog
%autochangelog
