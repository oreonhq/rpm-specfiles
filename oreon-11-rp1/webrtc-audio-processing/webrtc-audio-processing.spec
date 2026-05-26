# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 ae9302824b2038d394f10213cab05312c564a038434269f11dbf68f511f9f9fe
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Always prefer bundled Abseil so the shared library does not pick up distro
# libabsl SONAME drift (pulseaudio links against the bundled copy).
%bcond_without bundled_absl
%global absl_ver 20250814.1

Name:           webrtc-audio-processing
Version:        2.1
Release:        6%{?dist}
Summary:        Library for echo cancellation

License:        BSD-3-Clause
URL:            https://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source:         https://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%{name}-%{version}.tar.xz
Source:         https://github.com/abseil/abseil-cpp/releases/download/%{absl_ver}/abseil-cpp-%{absl_ver}.tar.gz
Source:         https://github.com/mesonbuild/wrapdb/releases/download/abseil-cpp_%{absl_ver}-1/abseil-cpp_%{absl_ver}-1_patch.zip

# Backports from upstream
Patch:         0001-Fix-compilation-with-gcc-15.patch
Patch:         0001-arch.h-Add-s390x-support.patch
Patch:         0001-Fix-build-with-abseil-cpp-202508.patch

# Downstream patches
Patch:         abseil-cpp-wrap.patch

BuildRequires: meson
BuildRequires: gcc gcc-c++
%if %{without bundled_absl}
BuildRequires: abseil-cpp-devel
%endif

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
%oreon_verify_sources
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
%endif


%files
%doc NEWS AUTHORS README.md
%license COPYING
%{_libdir}/libwebrtc-audio-processing-2.so.1*

%files devel
%{_libdir}/libwebrtc-audio-processing-2.so
%{_libdir}/pkgconfig/webrtc-audio-processing-2.pc
%{_includedir}/webrtc-audio-processing-2/


%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-6
- Default %%{with bundled_absl} on (no external libabsl_strings)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-5
- Prepare for Oreon 11 (RP1)
