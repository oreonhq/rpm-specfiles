%global source0_hash 82892487a01ad67b334eca83b54317a7c86a03a89cfadacfef5211f11a5d0536

Name:           wayland
Version:        1.24.0
Release:        3%{?dist}
Summary:        Wayland Compositor Infrastructure

# SPDX
License:        MIT
URL:            http://wayland.freedesktop.org/
Source0:        https://gitlab.freedesktop.org/%{name}/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source1:        https://gitlab.freedesktop.org/%{name}/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz.sig
Source2:        emersion-gpg-key.asc

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  graphviz
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(libffi)
BuildRequires:  xmlto

# For origin certification
BuildRequires:  gnupg2

%description
Wayland is a protocol for a compositor to talk to its clients as well as a C
library implementation of that protocol. The compositor can be a standalone
display server running on Linux kernel modesetting and evdev input devices,
an X application, or a wayland client itself. The clients can be traditional
applications, X servers (rootless or fullscreen) or other display servers.

%package        devel
Summary:        Development files for %{name}
Requires:       libwayland-client%{?_isa} = %{version}-%{release}
Requires:       libwayland-cursor%{?_isa} = %{version}-%{release}
Requires:       libwayland-egl%{?_isa} = %{version}-%{release}
Requires:       libwayland-server%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libffi)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Wayland development documentation
BuildArch: noarch
%description doc
Wayland development documentation

%package -n libwayland-client
Summary: Wayland client library
%description -n libwayland-client
Wayland client library

%package -n libwayland-cursor
Summary: Wayland cursor library
Requires: libwayland-client%{?_isa} = %{version}-%{release}
%description -n libwayland-cursor
Wayland cursor library

%package -n libwayland-egl
Summary: Wayland egl library
%description -n libwayland-egl
Wayland egl library

%package -n libwayland-server
Summary: Wayland server library
%description -n libwayland-server
Wayland server library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files devel
%{_bindir}/wayland-scanner
%{_includedir}/wayland-*.h
%{_libdir}/pkgconfig/wayland-*.pc
%{_libdir}/libwayland-*.so
%{_datadir}/aclocal/wayland-scanner.m4
%dir %{_datadir}/wayland
%{_datadir}/wayland/wayland-scanner.mk
%{_datadir}/wayland/wayland.xml
%{_datadir}/wayland/wayland.dtd
%{_mandir}/man3/*.3*

%files doc
%doc README.md
%{_datadir}/doc/wayland/

%files -n libwayland-client
%license COPYING
%{_libdir}/libwayland-client.so.0*

%files -n libwayland-cursor
%license COPYING
%{_libdir}/libwayland-cursor.so.0*

%files -n libwayland-egl
%license COPYING
%{_libdir}/libwayland-egl.so.1*

%files -n libwayland-server
%license COPYING
%{_libdir}/libwayland-server.so.0*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.24.0-3
- Import
