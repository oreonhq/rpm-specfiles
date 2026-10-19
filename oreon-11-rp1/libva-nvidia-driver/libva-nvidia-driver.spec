%global source0_hash 7459205cd1719a5865ab9c8969723c27e9863add5e7229e8e56c5f8816017b2a
%global upstream_name nvidia-vaapi-driver
Name:           libva-nvidia-driver
Version:        0.0.18
Release:        1%{?dist}
Summary:        A VA-API implemention using NVIDIA's NVDEC
License:        MIT
URL:            https://github.com/elFarto/nvidia-vaapi-driver
Source0:        https://github.com/elFarto/%{upstream_name}/archive/v%{version}/%{upstream_name}-%{version}.tar.gz
Provides:       nvdec-vaapi-driver = %{version}-%{release}
Conflicts:      libva-vdpau-driver
ExclusiveArch:  x86_64 aarch64 %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
# /oreon:deps
%description
This is an VA-API implementation that uses NVDEC as a backend. This
implementation is specifically designed to be used by Firefox for accelerated
decode of web content, and may not operate correctly in other applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{version}

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
