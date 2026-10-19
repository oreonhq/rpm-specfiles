%global source0_hash e6f6643166399a4df51f8d05f41bdbefbfa619f50b69601c7420c71874170a53
Name:           amsynth
Version:        2.0.0
Release:        1%{?dist}
Summary:        A classic synthesizer with dual oscillators
License:        GPL-2.0-or-later
URL:            http://amsynth.github.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/release-%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  libappstream-glib
BuildRequires:  liblo
BuildRequires:  liblo-devel
BuildRequires:  lv2-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  pandoc
# /oreon:deps
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
%oreon_prep
%build

%configure --with-jack --with-alsa --with-sndfile --with-lash --with-dssi
%make_build V=1
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*%{name}.*.xml
%find_lang %{name}
%oreon_autofiles amsynth-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles lv2-amsynth-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dssi-amsynth-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles vst-amsynth-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n amsynth-data -f %{oreon_filedir}/amsynth-data.list
%files -n lv2-amsynth-plugin -f %{oreon_filedir}/lv2-amsynth-plugin.list
%files -n dssi-amsynth-plugin -f %{oreon_filedir}/dssi-amsynth-plugin.list
%files -n vst-amsynth-plugin -f %{oreon_filedir}/vst-amsynth-plugin.list

%changelog

%autochangelog
