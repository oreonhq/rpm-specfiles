%global source0_hash 87f0d96873f502eb28d21281084a0435e9cb14e17383ae2afaa83a3f7eb8d7a5
%global commit 0a8cef484174aae5c1b7be6710f31a643e7d7197
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global prerelease 20171126
Name:           lv2-sorcer
Version:        1.1.3
Release:        1%{?dist}
Summary:        An audio compressor for JACK
License:        GPL-3.0-or-later
URL:            http://openavproductions.com/sorcer/
Source0:        https://github.com/harryhaaren/openAV-Sorcer/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-lv2.patch
Requires:       lv2
%global __provides_exclude_from ^%{_libdir}/lv2/.*$
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gtkmm24-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lv2-devel
BuildRequires:  make
BuildRequires:  non-ntk-devel
# /oreon:deps
%description
Sorcer is a polyphonic wavetable synth LV2 plugin. Its sonic fingerprint is 
one of harsh modulated sub-bass driven walls of sound. Two morphing wavetable
oscillators and one sine oscillator provide the generation routines. The LFO
can be mapped to wavetable modulation as well as filter cutoff. An ADSR allows
for shaping the resulting sound, while a master volume finishes the signal
chain. Easily creating a variety of dubstep basslines and harsh pad sounds.

Additional presets can be found here:
 https://github.com/harryhaaren/openAV-presets

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n openAV-Sorcer-%{commit}
sed -i -e  's|lib/lv2|%{_lib}/lv2|g'  -e 's|\-Wall|%{optflags}|g' \
  -e 's|-Wl,-z,nodelete -Wl,--no-undefined|%{__global_ldflags}|g' CMakeLists.txt
%ifnarch %{ix86} x86_64
sed -i -e 's|-msse2 -mfpmath=sse||g' CMakeLists.txt
%endif

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake .
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
