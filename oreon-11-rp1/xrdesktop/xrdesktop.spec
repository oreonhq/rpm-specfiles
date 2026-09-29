Name:           xrdesktop
Version:        0.15.1
Release:        1%{?dist}
Summary:        XR interaction library for desktop compositors
License:        MIT
URL:            https://gitlab.freedesktop.org/xrdesktop/xrdesktop
Source0:        https://gitlab.freedesktop.org/xrdesktop/xrdesktop/-/archive/%{version}/xrdesktop-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gxr-0.15)
BuildRequires:  pkgconfig(gulkan-0.15)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  glslang

%description
xrdesktop provides a library for interacting with traditional desktop
compositors in an XR environment.

%package devel
Summary:        Development files for xrdesktop
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and pkg-config metadata for applications using xrdesktop.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libxrdesktop-0.15.so.*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/xrdesktop/

%files devel
%{_includedir}/xrdesktop-0.15/
%{_libdir}/libxrdesktop-0.15.so
%{_libdir}/pkgconfig/xrdesktop-0.15.pc

%changelog
%autochangelog