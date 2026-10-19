%global source2_hash 27def688ff92966d3315ccdca99bd4c42538c507604d49943180dae056767cfa
%global source1_hash aabe2f13b14863bfb5347125241a33b399868ce6c1b48acc32743015020346b8
%global source0_hash b3601235c6769fd4c5c3390ec44ac12c429e95556768f9276fe0adac38ce2435
%global dpf_commit f60444f27480383005d488d82c834529fa1440f6
%global dpf_shortcommit %(c=%{dpf_commit}; echo ${c:0:7})
%global dpf_date 20250517
%global pugl_commit d4d964f129b4bf999c53ba40381bd1095fafb649
%global pugl_shortcommit %(c=%{pugl_commit}; echo ${c:0:7})
%global pugl_date 20250208
Name:           zam-plugins
Version:        4.4
Release:        1%{?dist}
Summary:        A collection of audio plugins for LV2, LADSPA, JACK, CLAP, VST3
License:        GPL-2.0-or-later AND ISC
URL:            http://www.zamaudio.com/
Source0:        https://github.com/zamaudio/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/DISTRHO/DPF/archive/%{dpf_commit}/DPF-%{dpf_shortcommit}.tar.gz
Source2:        https://github.com/DISTRHO/pugl/archive/%{pugl_commit}/pugl-%{pugl_shortcommit}.tar.gz
Provides:       bundled(dpf) = 0~git%{dpf_date}.%{dpf_shortcommit}
Provides:       bundled(pugl) = 0~git%{pugl_date}.%{pugl_shortcommit}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  make
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(x11)
BuildRequires:  zita-convolver-devel
# /oreon:deps
%package -n lv2-zam-plugins
Summary:        A collection of LV2 audio plugins
%package -n ladspa-zam-plugins
Summary:        A collection of LADSPA audio plugins
%package -n clap-zam-plugins
Summary:        A collection of CLAP audio plugins
%package -n vst3-zam-plugins
Summary:        A collection of VST3 audio plugins
%description
This is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.

This package contains the standalone JACK programs.

%description -n lv2-zam-plugins
This is a collection of LV2 audio plugins for sound processing developed
in-house at ZamAudio.

%description -n ladspa-zam-plugins
This is a collection of LADSPA audio plugins for sound processing
developed in-house at ZamAudio.

%description -n clap-zam-plugins
This is a collection of CLAP audio plugins for sound processing
developed in-house at ZamAudio.

%description -n vst3-zam-plugins
This is a collection of VST3 audio plugins for sound processing
developed in-house at ZamAudio.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1
%setup -q -T -D -a 2

# Move submodule DPF to main source directory
rmdir dpf
mv DPF-%{dpf_commit} dpf

# Move submodule pugl to main source directory
rmdir dpf/dgl/src/pugl-upstream
mv pugl-%{pugl_commit} dpf/dgl/src/pugl-upstream

# Remove bundled zita-convolver, we want to use the packaged copy
rm -rf lib/zita-convolver*

%build

%set_build_flags
%global common_make_flags \\\
    VERBOSE=true \\\
    PREFIX="%{_prefix}" \\\
    LIBDIR="%{_lib}" \\\
    SKIP_STRIPPING=true \\\
    HAVE_ZITA_CONVOLVER=true
%make_build %common_make_flags
%install
%make_install %common_make_flags
rm -rf %{buildroot}%{_libdir}/vst
chmod +x %{buildroot}%{_libdir}/*/{,*/}/*.so
%oreon_autofiles lv2-zam-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ladspa-zam-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clap-zam-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles vst3-zam-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lv2-zam-plugins -f %{oreon_filedir}/lv2-zam-plugins.list
%files -n ladspa-zam-plugins -f %{oreon_filedir}/ladspa-zam-plugins.list
%files -n clap-zam-plugins -f %{oreon_filedir}/clap-zam-plugins.list
%files -n vst3-zam-plugins -f %{oreon_filedir}/vst3-zam-plugins.list

%changelog

%autochangelog
