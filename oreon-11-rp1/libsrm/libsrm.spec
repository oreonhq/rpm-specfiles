%global source0_hash 2e19a9e95570deffef74090e0b30637fb11ce871c3fb696db17e74960beba008
%global basever 0.6.3
%global origrel 1
%global somajor 0
Name:           libsrm
Version:        %{basever}%{?origrel:_%{origrel}}
Release:        1%{?dist}
Summary:        Library for building DRM/KMS applications
License:        MIT
URL:            https://cuarzosoftware.github.io/SRM/
Source0:        https://github.com/CuarzoSoftware/SRM/archive/v%{basever}-%{origrel}/SRM-%{basever}-%{origrel}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-server)
# /oreon:deps
%description
SRM is a C library that simplifies the development of Linux DRM/KMS
applications.

With SRM, you can focus on the OpenGL ES 2.0 logic of your application.
For each available display, you can start a rendering thread that triggers
common events like initializeGL(), paintGL(), resizeGL(), pageFlipped()
and uninitializeGL().

SRM allows you to use multiple GPUs simultaneously and automatically finds
the most efficient configuration. It also offers functions for creating OpenGL
textures, which are automatically shared among GPUs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example applications using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    examples
The %{name}-examples package contains example applications using
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n SRM-%{basever}%{?origrel:-%{origrel}}

%build

pushd src
%meson
%meson_build
popd
%install
pushd src
%meson_install
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libsrm-devel -f %{oreon_filedir}/libsrm-devel.list
%files -n libsrm-examples -f %{oreon_filedir}/libsrm-examples.list

%changelog

%autochangelog
