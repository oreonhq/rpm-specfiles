%global source0_hash 95679abc3f5e4ea3d45c964cba4f2b2617c3f87e55f54988fc33ec023a873efb

Name:           amsynth
Version:        1.13.4
Release:        5%{?dist}
Summary:        A classic synthesizer with dual oscillators

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://amsynth.github.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/release-%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  mesa-libGL-devel mesa-libEGL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  intltool
BuildRequires:  pandoc
BuildRequires:  lv2-devel
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

%description
Amsynth is a software synthesis that provides a
classic subtractive synthesizer topology, with:

- Dual oscillators with classic waveforms - sine / saw / square / noise
- 12/24 dB/octave low/high/band-pass resonant filter
- Independent ADSR envelopes for filter and amplitude
- LFO which can modulate the oscillators, filter, and amplitude
- Distortion
- Reverb

%package data
BuildArch: noarch
Summary: Data files for amsynth
%description data
Sound banks and skins used in amsynth

%package -n lv2-amsynth-plugin
Summary: Amsynth lv2 plugin
Requires: lv2
Requires: %{name}-data = %{version}-%{release}
Obsoletes: lv2-amsynth-plugins < 1.6.0

%description -n lv2-amsynth-plugin
Amsynth plugin for the lv2 audio standard

%package -n dssi-amsynth-plugin
Summary: Amsynth dssi plugin
BuildRequires: dssi-devel liblo liblo-devel
BuildRequires: make
Requires:      dssi
Requires: %{name}-data = %{version}-%{release}
Obsoletes: dssi-amsynth-plugins < 1.6.0

%description -n dssi-amsynth-plugin
Amsynth plugin for the dssi audio API

%package -n vst-amsynth-plugin
Summary: Amsynth vst plugin
Requires: %{name}-data = %{version}-%{release}
Obsoletes: vst-amsynth-plugins < 1.6.0

%description -n vst-amsynth-plugin
Amsynth plugin for the vst protocol

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --with-jack --with-alsa --with-sndfile --with-lash --with-dssi
%make_build V=1

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*%{name}.*.xml

%find_lang %{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/de/man1/amsynth.1*
%{_mandir}/fr/man1/amsynth.1*
%{_mandir}/man1/amsynth.1*

%files data -f %{name}.lang
%doc README AUTHORS
%license COPYING
%{_datadir}/%{name}

%files -n lv2-amsynth-plugin
%{_libdir}/lv2/%{name}.lv2/
%{_datadir}/appdata/lv2-%{name}-plugin.metainfo.xml

%files -n dssi-amsynth-plugin
%{_libdir}/dssi/%{name}_dssi.so
%{_libdir}/dssi/%{name}_dssi/
%{_datadir}/appdata/dssi-%{name}-plugin.metainfo.xml

%files -n vst-amsynth-plugin
%{_libdir}/vst/%{name}_vst.so
%{_datadir}/appdata/vst-%{name}-plugin.metainfo.xml

%changelog
%autochangelog
