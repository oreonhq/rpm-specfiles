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
# oreon url source checksums begin
%global source0_sha256 072cda4b59dd098bba8c2363a6247299db1fa89411dc221c8b81b8ee8192e623
%global source0_file libepoxy-1.5.10.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libepoxy-1.5.10.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "072cda4b59dd098bba8c2363a6247299db1fa89411dc221c8b81b8ee8192e623" || { echo "oreon: Source0 SHA256 mismatch for libepoxy-1.5.10.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
