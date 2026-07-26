%global source0_hash 9d70953e8f55388e8ff04ae0261e43136ab8c1d105becb208d081aa3da3613d2

%global commit abeb3e9156b553d2e8f5ebbc8b3df833f531ce0f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global prerelease 20181215

Name:           lv2-fabla
Version:        1.3.2
Release:        0.16.%{prerelease}git%{shortcommit}%{?dist}
Summary:        An LV2 drum sequencer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://openavproductions.com/fabla/
Source0:        https://github.com/harryhaaren/openAV-Fabla/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-lv2.patch

BuildRequires:  faust
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(ntk)
BuildRequires:  pkgconfig(sndfile)
# This package uses cairo directly; cairo is a public dependency of ntk, so the
# following line is not strictly required. It serves to document the direct
# dependency.
BuildRequires:  pkgconfig(cairo)
# Contrary to the README, which says cairomm-1.0 is required, only the cairo C
# api is used, and only pkgconfig(cairo)/cairo-devel is required to build this
# package.
BuildRequires:  cmake
Requires:       lv2

%description
%{name} is a drum sampler plugin instrument. It is ideal for loading up your
favorite sampled sounds and bashing away on a MIDI controller. Or if it’s 
crafty beat programming your after that’s cool too! The ADSR envelope allows
the shaping of hi-hats and kicks while the compressor beefs up the sound for 
those thumping kicks!
Additional presets can be found at:
   https://github.com/harryhaaren/openAV-presets

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n openAV-Fabla-%{commit}
sed -i -e  's|lib/|%{_lib}/|g'  -e 's|\-Wall|%{optflags}|g' \
  -e 's|-Wl,-z,nodelete -Wl,--no-undefined|%{__global_ldflags}|g' CMakeLists.txt
%ifnarch %{ix86} x86_64
sed -i -e 's|-msse2 -mfpmath=sse||g' CMakeLists.txt
%endif

%build
# TODO: Please submit an issue to upstream (rhbz#2380886)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake .
%cmake_build

%install
mkdir -p %{buildroot}/%{_libdir}/lv2
%cmake_install

%files
%doc README.md CHANGELOG
%license LICENSE
%{_libdir}/lv2/*

%changelog
%autochangelog
