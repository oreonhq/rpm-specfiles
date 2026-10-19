%global source0_hash d05fdf90bea2f629eaa2d115e909fd356388ac639e54f77b87a018a6d76224bd
Name:           libplacebo
Version:        7.360.1
Release:        1%{?dist}
Summary:        Reusable library for GPU-accelerated video/image rendering primitives
License:        LGPL-2.0-or-later
URL:            https://github.com/haasn/libplacebo
Source0:        https://github.com/haasn/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glad2
BuildRequires:  glslang-devel
BuildRequires:  lcms2-devel
BuildRequires:  libdovi-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libshaderc-devel
BuildRequires:  libunwind-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-mako
BuildRequires:  python3-markupsafe
BuildRequires:  spirv-tools-devel
BuildRequires:  vulkan-devel
BuildRequires:  xxhash-devel
# /oreon:deps
%description
libplacebo is essentially the core rendering algorithms and ideas of
mpv turned into a library. This grew out of an interest to accomplish
the following goals:

- Clean up mpv's internal API and make it reusable for other projects.
- Provide a standard library of useful GPU-accelerated image processing
  primitives based on GLSL, so projects like VLC or Firefox can use them
  without incurring a heavy dependency on `libmpv`.
- Rewrite core parts of mpv's GPU-accelerated video renderer on top of
  redesigned abstractions. (Basically, I wanted to eliminate code smell
  like `shader_cache.c` and totally redesign `gpu/video.c`)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}%{?prerelease}

%build

%meson \
 -Dd3d11=disabled \
 -Ddemos=False
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libplacebo-devel -f %{oreon_filedir}/libplacebo-devel.list

%changelog

%autochangelog
