%global source0_hash 89410e3398d49355ba1ff00e47e93592c28694a46d44d3a96288f23df49804bb

%global commit 311eaaaa473d593c30d118799aa19ac4ad53cd65
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20241006

Name: kmscube
Version: 0
Release: 13.%{commitdate}.git%{shortcommit}%{?dist}
Summary: Example KMS/GBM/EGL application
License: MIT
URL: https://gitlab.freedesktop.org/mesa/kmscube/
Source0: https://gitlab.freedesktop.org/mesa/kmscube/-/archive/%{commit}/kmscube-%{commit}.tar.gz

BuildRequires: gcc gstreamer1-devel gstreamer1-plugins-base-devel
BuildRequires: libdrm-devel libpng-devel mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel mesa-libGLES-devel meson ninja-build

%description
kmscube is a little demonstration program for how to drive bare metal
graphics without a compositor like X11, wayland or similar, using
DRM/KMS (kernel mode setting), GBM (graphics buffer manager) and EGL
for rendering content using OpenGL or OpenGL ES.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/kmscube
%{_bindir}/texturator

%changelog
%autochangelog
