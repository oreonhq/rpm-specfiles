%global source0_hash 4c6a835f3e02511e07bce6ad2e23e6735864aaf43c52697caa2aa24c0f4dbf6d

Name:           obs-studio-plugin-vaapi
Version:        0.4.2
Release:        %autorelease
Summary:        OBS Studio VAAPI support via GStreamer

License:        GPL-2.0-or-later
URL:            https://github.com/fzwoch/obs-vaapi
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  meson
BuildRequires:  obs-studio-devel
BuildRequires:  pciutils-devel
Requires:       obs-studio

ExcludeArch:    %{ix86}

%description
GStreamer based VAAPI encoder implementation. Taken out of the GStreamer
OBS plugin as a standalone plugin. Simply because the FFMPEG VAAPI
implementation shows performance bottlenecks on some AMD hardware.

Supports H.264, H.265 and AV1.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n obs-vaapi-%{version}

%build
%meson --libdir= --prefix=%{_libdir}/obs-plugins
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/obs-vaapi.so

%changelog
%autochangelog
