%global source0_hash ce659857e96be31dc56e0d46a99b15effd5a05f6324d0b30966decc3e4a1bd41
%global commit0 3acc51828aceba310081c72a18f938f04d4487de
%global shortcommit0 3acc518
Name:           egl-wayland
Version:        1.1.23
Release:        1%{?dist}
Summary:        EGLStream-based Wayland external platform
License:        MIT
URL:            https://github.com/NVIDIA/%{name}
Source0:        https://github.com/NVIDIA/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Requires:       libglvnd-egl%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eglexternalplatform)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n egl-wayland-devel -f %{oreon_filedir}/egl-wayland-devel.list

%changelog

%autochangelog
