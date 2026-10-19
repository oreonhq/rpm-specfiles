%global source0_hash 52d2c952506d63708f9a8f1aacd4d6ca176287caf3507c8ff2882fa0390cb391
%global   git 0
Version:  0.6.0
%global   forgeurl https://github.com/ammen99/wf-recorder
%if %{?git}
%global   commit a9725f75dd3469e1434c99e32607ad2b7ef62ace
%global   date 20221225
%endif
%forgemeta
Name:     wf-recorder
Summary:        Screen recorder for wlroots-based compositors eg swaywm
Release:        1%{?dist}
License:  MIT
URL:      %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:   wf-recorder-use-free-codecs.patch
%ifarch ppc64le
%global configure_flags -Dcpp_std=gnu++17
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  ocl-icd-devel
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  scdoc
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
