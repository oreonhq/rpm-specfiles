%global source0_hash abb9e452a1c372133bd3eb8f0bb30d07b2d0a8fb02001c4155cf287555db4040
%bcond qt5 %[%{undefined rhel} || 0%{?rhel} < 10]
Name:           libportal
Version:        0.11.0
Release:        1%{?dist}
Summary:        Flatpak portal library
License:        LGPL-3.0-only AND LGPL-2.1-or-later
Url:            https://github.com/flatpak/libportal
Source0:        https://github.com/flatpak/libportal/releases/download/%{version}/%{name}-%{version}.tar.xz
%if %{with qt5}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  vala
# /oreon:deps
%description
libportal provides GIO-style asynchronous APIs for most Flatpak portals.

%package gtk3
Summary: GTK+ 3 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gtk3
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for GTK+ 3 and %name.

%package gtk4
Summary: GTK 4 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gtk4
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for GTK 4 and %name.

%package qt6
Summary: Qt6 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}
%description qt6
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for Qt 6 and %name.

%if %{with qt5}
%package qt5
Summary: Qt5 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}
%description qt5
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for Qt 5 and %name.
%endif

%package devel
Summary: Development files and libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with %name.

%package gtk3-devel
Summary: GTK+ 3 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}
%description gtk3-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with GTK+ 3 and %name.

%package gtk4-devel
Summary: GTK 4 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk4%{?_isa} = %{version}-%{release}
%description gtk4-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with GTK 4 and %name.

%package qt6-devel
Summary: Qt 6 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with Qt 6 and %name.

%if %{with qt5}
%package qt5-devel
Summary: Qt 5 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with Qt 5 and %name.
%endif

%package devel-doc
Summary: Development documentation for libportal
Recommends: gi-docgen-fonts
BuildArch: noarch
%description devel-doc
libportal provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides development documentations for libportal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
  -Dbackend-gtk3=enabled \
  -Dbackend-gtk4=enabled \
  -Dbackend-qt6=enabled \
%if %{with qt5}
  -Dbackend-qt5=enabled \
%else
  -Dbackend-qt5=disabled \
%endif
  %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libportal-gtk3 -f %{oreon_filedir}/libportal-gtk3.list
%files -n libportal-gtk4 -f %{oreon_filedir}/libportal-gtk4.list
%files -n libportal-qt6 -f %{oreon_filedir}/libportal-qt6.list
%files -n libportal-qt5 -f %{oreon_filedir}/libportal-qt5.list
%files -n libportal-devel -f %{oreon_filedir}/libportal-devel.list
%files -n libportal-gtk3-devel -f %{oreon_filedir}/libportal-gtk3-devel.list
%files -n libportal-gtk4-devel -f %{oreon_filedir}/libportal-gtk4-devel.list
%files -n libportal-qt6-devel -f %{oreon_filedir}/libportal-qt6-devel.list
%files -n libportal-qt5-devel -f %{oreon_filedir}/libportal-qt5-devel.list
%files -n libportal-devel-doc -f %{oreon_filedir}/libportal-devel-doc.list

%changelog

%autochangelog
