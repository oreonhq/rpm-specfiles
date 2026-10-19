%global source0_hash 0e98b9aea613b111c9d7cc2b9a0ce14c2b3ba4e90861b3cdcfcb8ec1ebfcab93
Name:           dsp
Version:        1.9
Release:        1%{?dist}
Summary:        An audio processing program with an interactive mode
License:        ISC
URL:            https://github.com/bmc0/dsp
Source0:        https://github.com/bmc0/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zita-convolver-devel
# /oreon:deps
%description
dsp is an audio processing program with an interactive mode.

%package -n ladspa-dsp-plugin
Summary:        dsp's LADSPA frontend
Requires:       ladspa
%description -n ladspa-dsp-plugin
dsp's LADSPA frontend.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./configure --libdir=/%{_lib} --disable-ffmpeg
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build
%install
%make_install
%oreon_autofiles ladspa-dsp-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ladspa-dsp-plugin -f %{oreon_filedir}/ladspa-dsp-plugin.list

%changelog

%autochangelog
