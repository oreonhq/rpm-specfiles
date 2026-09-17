%global source0_hash none

%global commit0 3acc51828aceba310081c72a18f938f04d4487de
%global shortcommit0 3acc518

Name:           egl-wayland
Version:        1.1.21
Release:        %autorelease
Summary:        EGLStream-based Wayland external platform
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  pkgconfig(egl) >= 1.5
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

Requires:       libglvnd-egl%{?_isa}

%description
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

%package devel
Summary:        EGLStream-based Wayland external platform development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

This package contains development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{commit0}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete

%files
%doc README.md
%license COPYING
%{_libdir}/libnvidia-egl-wayland.so.1
%{_libdir}/libnvidia-egl-wayland.so.1.*
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files devel
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.21-1
- Import
