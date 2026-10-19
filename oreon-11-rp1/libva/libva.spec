%global source0_hash 0b4a3649ee8d683b9cce2ef094df4fb039d276c0cef7e49337c43d3b297b9f42
Name:		libva
Version:	2.24.1
Release:        1%{?dist}
Summary:        Video Acceleration (VA) API for Linux
License:	MIT AND HPND-sell-variant AND ICU
URL:		https://github.com/intel/libva
Source0:        https://github.com/intel/libva/archive/refs/tags/2.24.1.tar.gz#/libva-2.23.0.tar.gz
%{!?_without_xorg:
}
%{!?_without_wayland:
}
Requires:	mesa-filesystem%{_isa}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libdrm-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libudev-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  wayland-devel
# /oreon:deps
%description
Libva is a library providing the VA API video acceleration API.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}%{?pre_release}

%build

%meson \
 -Dwith_legacy=nvctrl \
 -Ddriverdir="%{_libdir}/dri-nonfree:%{_libdir}/dri-freeworld:%{_libdir}/dri" \
%{?_without_xorg: -Dwith_glx=no -Dwith_x11=no} \
%{?_without_wayland: -Dwith_wayland=no}
%meson_build
%install
%meson_install
sed -i -e 's|driverdir=.*|driverdir=%{_libdir}/dri|' %{buildroot}%{_libdir}/pkgconfig/libva.pc
mkdir -p %{buildroot}%{_libdir}/dri-{freeworld,nonfree}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libva-devel -f %{oreon_filedir}/libva-devel.list

%changelog

%autochangelog
