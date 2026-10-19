%global source0_hash 1fc7b58933b37f0851b7f5f1f51a38d9cc516b6237816de1d9a226144a512057
Name:  gst-vosk
Version:  0.3.2
Release:        1%{?dist}
Summary:        GStreamer plugin for VOSK voice recognition engine
ExclusiveArch:  x86_64 aarch64 ppc64le
License:  LGPL-2.1-only
URL:      https://github.com/Manish7093/gst-vosk
Source0:        https://github.com/Manish7093/gst-vosk/archive/refs/tags/%{version}.tar.gz
Requires:  vosk-api-devel
Requires:  rnnoise-devel
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  meson
BuildRequires:  rnnoise-devel
BuildRequires:  vosk-api-devel
# /oreon:deps
%description
GStreamer plugin for VOSK voice recognition engine

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# remove prebuilt libvosk
rm -f vosk/libvosk.so

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
