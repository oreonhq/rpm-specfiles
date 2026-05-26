%global commit0 3acc51828aceba310081c72a18f938f04d4487de
%global date 20250407
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

Name:           egl-wayland
Version:        1.1.21%{!?tag:~%{date}git%{shortcommit0}}
Release:        %autorelease
Summary:        EGLStream-based Wayland external platform
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        https://github.com/NVIDIA/egl-wayland/archive/1.1.21/egl-wayland-1.1.21.tar.gz
%else
Source0:        https://github.com/NVIDIA/egl-wayland/archive/3acc51828aceba310081c72a18f938f04d4487de/egl-wayland-%(c=3acc51828aceba310081c72a18f938f04d4487de;.tar.gz
# oreon url source checksums begin
%global source0_sha256 da232d46ec4553b2f4b057b705acfa63466318f91f7e8de38dcfb30243fb6898
%global source0_file egl-wayland-1.1.21.tar.gz
# oreon url source checksums end
%endif

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  pkgconfig(egl) >= 1.5
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
# Explicit synchronization since 1.34:
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

# Required for directory ownership
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/egl-wayland-1.1.21.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "da232d46ec4553b2f4b057b705acfa63466318f91f7e8de38dcfb30243fb6898" || { echo "oreon: Source0 SHA256 mismatch for egl-wayland-1.1.21.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

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
