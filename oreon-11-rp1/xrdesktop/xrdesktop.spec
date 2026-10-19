%global source0_hash e7d2372431dc4a229e87daa558a5b62000f39b411f8df9be1625557a31c2411d
Name:           xrdesktop
Version:        0.15.1
Release:        1%{?dist}
Summary:        XR interaction library for desktop compositors
License:        MIT
URL:            https://gitlab.freedesktop.org/xrdesktop/xrdesktop
Source0:        https://gitlab.freedesktop.org/xrdesktop/xrdesktop/-/archive/%{version}/xrdesktop-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gulkan-0.15)
BuildRequires:  pkgconfig(gxr-0.15)
BuildRequires:  pkgconfig(vulkan)
# /oreon:deps
%description
xrdesktop provides a library for interacting with traditional desktop
compositors in an XR environment.

%package devel
Summary:        Development files for xrdesktop
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers and pkg-config metadata for applications using xrdesktop.

%prep
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xrdesktop-devel -f %{oreon_filedir}/xrdesktop-devel.list

%changelog

%autochangelog
