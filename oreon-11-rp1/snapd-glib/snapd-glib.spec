%global source0_hash b7367792b58047da5e8f81d5c3a694a5c141b40f29b5ac2037340c24d9c12e52
Summary:        GLib and Qt library to access snapd
Name:           snapd-glib
Version:        1.72
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:            https://github.com/canonical/snapd-glib
Source0:        https://github.com/canonical/snapd-glib/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
# /oreon:deps
%description
snapd-glib is a library to allow GLib based applications access to snapd,
the daemon that controls snap packages.

%package -n libsnapd-qt
Summary:        Qt library to access snapd
Provides:       snapd-qt = %{version}-%{release}
Provides:       snapd-qt%{?_isa} = %{version}-%{release}
%description -n libsnapd-qt
snapd-qt wraps snapd-glib for Qt and QML applications, used by KDE Discover
to browse and install snaps.

%package -n libsnapd-qt-devel
Summary:        Development files for libsnapd-qt
Provides:       cmake(Snapd) = %{version}
Provides:       cmake(Snapd) = %{version}-%{release}
Requires:       libsnapd-qt%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description -n libsnapd-qt-devel
Headers and CMake config files for building against libsnapd-qt.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers and pkgconfig file for building against snapd-glib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
        -Dintrospection=false \
        -Ddocs=false \
        -Dvala-bindings=false \
        -Dqt5=false \
        -Dqt6=true \
        -Dqml-bindings=true \
        -Dsoup2=true \
        -Dexamples=false \
        -Dtests=false
%meson_build
%install
%meson_install
%oreon_autofiles libsnapd-qt usr/*/lib*.so.*
%oreon_autofiles libsnapd-qt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libsnapd-qt -f %{oreon_filedir}/libsnapd-qt.list
%files -n libsnapd-qt-devel -f %{oreon_filedir}/libsnapd-qt-devel.list
%files -n snapd-glib-devel -f %{oreon_filedir}/snapd-glib-devel.list

%changelog

%autochangelog
