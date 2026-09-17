%global source0_hash 799244cab5ace62b6354e429bd56faa83045470c438fbea13690b4d06754eb8b

%global upstream_name nvidia-vaapi-driver

Name:           libva-nvidia-driver
Version:        0.0.16
Release:        %autorelease
Summary:        A VA-API implemention using NVIDIA's NVDEC
License:        MIT
URL:            https://github.com/elFarto/nvidia-vaapi-driver

Source0:        %{url}/archive/v%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(libdrm) >= 2.4.60
BuildRequires:  pkgconfig(libva) >= 1.8.0

# Alternative name that better describes the API involved
Provides:       nvdec-vaapi-driver = %{version}-%{release}

# Only one NVIDIA VA-API shim on a system at a time
Conflicts:      libva-vdpau-driver

# NVIDIA driver architectures
ExclusiveArch:  x86_64 aarch64 %{ix86}

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

%check
%meson_test

%files
%doc README.md
%license COPYING
%{_libdir}/dri/nvidia_drv_video.so

%changelog
%autochangelog
