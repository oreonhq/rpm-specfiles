%global source0_hash 59c908867f18c81106385a43065c232e63236e120d5b2596b179ce56340d7b01
Name:           timg
Version:        1.6.3
Release:        1%{?dist}
Summary:        A terminal image and video viewer
License:        GPL-2.0-only AND MIT AND (MIT OR Unlicense)
URL:            https://github.com/hzeller/timg
Source0:        https://github.com/hzeller/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  cairo
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavdevice-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libdeflate-devel
BuildRequires:  libexif-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsixel-devel
BuildRequires:  libswscale-free-devel
BuildRequires:  openslide-devel
BuildRequires:  pandoc
BuildRequires:  pkg-config
BuildRequires:  poppler-glib-devel
BuildRequires:  qoi-devel
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-static
BuildRequires:  turbojpeg-devel
# /oreon:deps
%description
A user-friendly terminal image viewer that uses graphic capabilities of
terminals (Sixel, Kitty or iTerm2), or 24-bit color capabilities and Unicode
character blocks if these are not available. On terminals that implement the
Sixel protocol, the Kitty Graphics Protocol, or the iTerm2 Graphics Protocol,
this displays images in full resolution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
rm -rf third_party

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
