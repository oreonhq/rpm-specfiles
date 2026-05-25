Summary: epoxy runtime library
Name: libepoxy
Version: 1.5.10
Release: 12%{?dist}
# SPDX
License: MIT
URL: https://github.com/anholt/libepoxy
Source0: https://download.gnome.org/sources/%{name}/1.5/%{name}-%{version}.tar.xz

# https://github.com/anholt/libepoxy/pull/270
Patch0: Fix-dlwrap-on-riscv64.patch

BuildRequires: meson
BuildRequires: gcc
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(egl)
BuildRequires: libGL-devel
BuildRequires: libEGL-devel
BuildRequires: libX11-devel
BuildRequires: pkgconfig(glesv2)
BuildRequires: python3
BuildRequires: mesa-dri-drivers
BuildRequires: mutter
BuildRequires: xwayland-run

%description
A library for handling OpenGL function pointer management.

%package devel
Summary: Development files for libepoxy
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
# this should be %%meson_test but the macro expands with a bajillion
# embedded newlines for no obvious reason
xwfb-run -c mutter -- ninja -C %{_vpath_builddir} test || \
    (cat %{_vpath_builddir}/meson-logs/testlog.txt ; exit 1)

%files
%license COPYING
%doc README.md
%{_libdir}/libepoxy.so.0*

%files devel
%{_includedir}/epoxy/
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.10-12
- Import
