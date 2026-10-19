%global source0_hash 072cda4b59dd098bba8c2363a6247299db1fa89411dc221c8b81b8ee8192e623
%bcond_with check
Name: libepoxy
Version: 1.5.10
Release:        12%{?dist}
Summary:        epoxy runtime library
License: MIT
URL: https://github.com/anholt/libepoxy
Source0:        https://download.gnome.org/sources/%{name}/1.5/%{name}-%{version}.tar.xz
Patch0:        Fix-dlwrap-on-riscv64.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libEGL-devel
BuildRequires:  libGL-devel
BuildRequires:  libX11-devel
BuildRequires:  mesa-dri-drivers
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  python3
BuildRequires:  xwayland-run
# /oreon:deps
%description
A library for handling OpenGL function pointer management.

%package devel
Summary: Development files for libepoxy
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with check}
xwfb-run -c mutter -- ninja -C %{_vpath_builddir} test || \
    (cat %{_vpath_builddir}/meson-logs/testlog.txt ; exit 1)
%endif
%files -f %{oreon_filedir}/main.list
%files -n libepoxy-devel -f %{oreon_filedir}/libepoxy-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.10-12
- Import
