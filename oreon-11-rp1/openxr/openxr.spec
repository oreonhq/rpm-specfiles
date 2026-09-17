%global source0_hash 89105178608351340325177b9d54922cf38db2c0bbf5e13e9b0dc88e9e49f397

%global         pkgname        OpenXR-SDK-Source
%global         libmajor 1

Name:           openxr
Version:        1.1.60
Release:        1%{?dist}
Summary:        Cross-platform VR/AR runtime and API
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/%{pkgname}
Source0:        https://github.com/KhronosGroup/%{pkgname}/archive/refs/tags/release-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  python3dist(jinja2)

%description
OpenXR provides a vendor-neutral API for XR hardware.

%package libs
Summary:        OpenXR runtime loader library

%description libs
Shared library implementing the OpenXR loader.

%package devel
Summary:        Headers and development files of the OpenXR library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and development files for OpenXR.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pkgname}-release-%{version}
%generate_buildrequires

%build
%cmake \
    -DBUILD_ALL_EXTENSIONS=ON \
    -DBUILD_LOADER=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_TESTS=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DDYNAMIC_LOADER=ON \
    -DFILESYSTEM_USE_STD=ON \
    -DGLSLANG_VALIDATOR=$(which glslangValidator)
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

%check
%ctest

%files
%license LICENSE
%doc CHANGELOG.SDK.md README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

%files libs
%{_libdir}/lib%{name}_loader.so.%{libmajor}{,.*}

%files devel
%doc README.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
