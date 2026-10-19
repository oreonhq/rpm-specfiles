%global source0_hash 69f5b244c21f6402831c3ab8af85a01772f72fb118677388436f12f32bfb06d9
%global tarball_version %(echo %{version} | tr '~' '.')
Name:    libdex
Version: 1.2.0
Release:        1%{?dist}
Summary:        a library supporting "Deferred Execution" for GNOME and GTK
License: LGPL-2.1-or-later
URL:     https://gitlab.gnome.org/GNOME/libdex
Source0:        https://download.gnome.org/sources/%{name}/1.2/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/vapigen
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  libatomic
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
# /oreon:deps
%description
Dex is a library supporting "Deferred Execution" with the explicit goal
of integrating with GNOME and GTK-based applications.
It provides primatives for supporting futures in a variety of ways with both
read-only and writable views. Additionally, integration with existing
asynchronous-based APIs is provided through the use of wrapper promises.
"Fibers" are implemented which allows for writing synchronous looking code
which calls asynchronous APIs from GIO underneath.

%package  devel
Summary:  Development files for libdex
Requires: libdex%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries and header files that are needed for
writing applications with libdex.

%package   devel-docs
Summary:   Developer documentation for libdex
BuildArch: noarch
Requires:  libdex = %{version}-%{release}
%description devel-docs
This package contains developer documentation for writing applications with
libdex.

%package -n  python3-libdex
Summary:     Python3 bindings for %{name}
BuildArch:   noarch
Requires:    %{name} = %{version}-%{release}
Requires:    python3-gobject-base-noarch
%description -n python3-libdex
This package contains the python3 bindings for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
  -Ddocs=true \
  -Dexamples=false \
  -Dsysprof=true
%meson_build
%install
%meson_install
%oreon_autofiles python3-libdex usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libdex-devel -f %{oreon_filedir}/libdex-devel.list
%files -n libdex-devel-docs -f %{oreon_filedir}/libdex-devel-docs.list
%files -n python3-libdex -f %{oreon_filedir}/python3-libdex.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1~rc-1
- Prepare for Oreon 11 (RP1)
