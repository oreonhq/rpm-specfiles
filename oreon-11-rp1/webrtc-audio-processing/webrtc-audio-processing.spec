%global source0_hash f44ad4d72ff2919a6a48cf0887f69aef34c338bfdd8931153596e3766d75f654
%bcond_without bundled_absl
%global absl_ver 20250814.1
Name:           webrtc-audio-processing
Version:        2.1
Release:        6%{?dist}
Summary:        Library for echo cancellation
License:        BSD-3-Clause
URL:            https://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:        https://github.com/mesonbuild/wrapdb/releases/download/abseil-cpp_%{absl_ver}-1/abseil-cpp_%{absl_ver}-1_patch.zip
Patch:         0001-Fix-compilation-with-gcc-15.patch
Patch:         0001-arch.h-Add-s390x-support.patch
Patch:         0001-Fix-build-with-abseil-cpp-202508.patch
Patch:         abseil-cpp-wrap.patch
%if %{without bundled_absl}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
# /oreon:deps
%description
%{name} is a library derived from Google WebRTC project that
provides echo cancellation functionality. This library is used by for example
PipeWire to provide echo cancellation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%if %{with bundled_absl}
mkdir -p subprojects/packagefiles
cp %{S:1} subprojects/packagefiles
cp %{S:2} subprojects/packagefiles
%endif

%conf
%meson \
%ifnarch %{arm32} %{arm64}
  -Dneon=disabled \
%endif
  %{nil}

%build

%meson_build
%install
%meson_install
%if %{with bundled_absl}
mv %{buildroot}%{_includedir}/absl %{buildroot}%{_includedir}/webrtc-audio-processing-2/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n webrtc-audio-processing-devel -f %{oreon_filedir}/webrtc-audio-processing-devel.list

%changelog

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-6
- Default %%{with bundled_absl} on (no external libabsl_strings)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-5
- Prepare for Oreon 11 (RP1)
