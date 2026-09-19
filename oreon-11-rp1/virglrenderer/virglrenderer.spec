%global source0_hash 088040d130eaa0458a978fe7867fbfb1fcf1fdff52bf3b27a00658828bc4189f

%ifarch aarch64
%global drm_renderers asahi,msm
%endif

Name:		virglrenderer
Version:	1.3.0
Release:	1%{?dist}

Summary:	Virgl Rendering library.
License:	MIT

Source:         https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/%{version}/virglrenderer-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	libepoxy-devel
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libEGL-devel
BuildRequires:	python3
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  python3-pyyaml

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files

Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server

Requires: %{name}%{?_isa} = %{version}-%{release}

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
  %{?drm_renderers:-Ddrm-renderers=%drm_renderers} \
  -Dvideo=true \
  -Dvenus=true
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libvirglrenderer.so.1{,.*}
%{_libexecdir}/virgl_render_server

%files devel
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/libvirglrenderer.so
%{_libdir}/pkgconfig/virglrenderer.pc

%files test-server
%{_bindir}/virgl_test_server

%changelog
%autochangelog
