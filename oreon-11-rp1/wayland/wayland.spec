# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 64176eaa46e4969903e286f8e5ef8331affc17fdf03ac9b58381d2b23162b7a3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

# mdbook is not in the tree yet
%bcond book 0

Name:           wayland
Version:        1.26.0
Release:        1%{?dist}
Summary:        Wayland Compositor Infrastructure

License:        MIT
URL:            https://wayland.freedesktop.org/
Source0:        https://gitlab.freedesktop.org/%{name}/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.sig
# Simon Ser, 34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48
Source2:        gpgkey-34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48.gpg

Patch0:         0001-doc-add-option-to-not-build-the-book.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  docbook-style-xsl
BuildRequires:  expat-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
%if %{without bootstrap}
BuildRequires:  doxygen
BuildRequires:  graphviz
%if %{with book}
BuildRequires:  mdbook
%endif
%endif
BuildRequires:  meson
BuildRequires:  pkgconfig(libffi)
BuildRequires:  xmlto
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
Provides:       pkgconfig(wayland-client) = %{version}
Provides:       pkgconfig(wayland-server) = %{version}
Provides:       pkgconfig(wayland-cursor) = %{version}
Provides:       pkgconfig(wayland-egl) = %{version}
Provides:       pkgconfig(wayland-egl-backend) = 3

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Wayland development documentation
BuildArch: noarch
%if %{with book}
Requires: adobe-source-code-pro-fonts
Requires: open-sans-fonts
%endif

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
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%conf
%meson %{!?with_book:-Dbook=false}

%build
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
%autochangelog
