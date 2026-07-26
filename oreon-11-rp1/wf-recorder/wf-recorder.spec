%global source0_hash 52d2c952506d63708f9a8f1aacd4d6ca176287caf3507c8ff2882fa0390cb391

# -*-Mode: rpm-spec -*-
# Use 0 for release and 1 for git
%global   git 0
Version:  0.6.0
%global   forgeurl https://github.com/ammen99/wf-recorder
%if %{?git}
%global   commit a9725f75dd3469e1434c99e32607ad2b7ef62ace
%global   date 20221225
%endif
%forgemeta

Name:     wf-recorder
Summary:  Screen recorder for wlroots-based compositors eg swaywm
Release:  2%{?dist}
License:  MIT
URL:      %{forgeurl}
Source0:  %{forgesource}
Patch0:   wf-recorder-use-free-codecs.patch

%ifarch ppc64le
# fix compilation on ppc64le (gcc#58241)
%global configure_flags -Dcpp_std=gnu++17
%endif

BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: meson
BuildRequires: ocl-icd-devel
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpipewire-0.3) >= 1.0.5
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(wayland-client) >= 1.20
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: scdoc

%description
wf-recorder is a utility program for screen recording of wlroots-based
compositors (more specifically, those that support wlr-screencopy-v1
and xdg-output).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -S git_am

%build
%meson %{?configure_flags}
%meson_build

%install
%meson_install

%files
%{_bindir}/wf-recorder*
%{_datadir}/fish/fish/vendor_completions.d/wf-recorder.fish

%doc README.md
%{_mandir}/man1/%{name}.1.*

%license LICENSE

%changelog
%autochangelog
