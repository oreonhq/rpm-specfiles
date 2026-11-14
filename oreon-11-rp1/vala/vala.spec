# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5ad7cbbfcc0de61b403d6797c9ef60455bfbebd8e162aec33b5b0b097adfb9d5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global api_ver 0.56

Name: vala
Version: 0.56.19
Release: 2%{?dist}
Summary: A modern programming language for GNOME
License: LGPL-2.1-or-later AND BSD-2-Clause
URL: https://wiki.gnome.org/Projects/Vala
Source0: https://download.gnome.org/sources/vala/%{api_ver}/vala-%{version}.tar.xz
Patch0: vala-warn-on-unknown-xml.patch

BuildRequires: oreon-rpm-macros
BuildRequires: bison
BuildRequires: dbus-x11
BuildRequires: flex
BuildRequires: gcc
%if %{without bootstrap}
BuildRequires: gobject-introspection-devel
BuildRequires: graphviz-devel
%endif
BuildRequires: libxslt
BuildRequires: make
BuildRequires: pkgconfig(gobject-2.0)

Requires: libvala%{?_isa} = %{version}-%{release}
Recommends: gobject-introspection-devel

Provides: vala(api) = %{api_ver}
Provides: valac = %{version}-%{release}
Provides: pkgconfig(vapigen) = %{version}

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.

%package -n libvala
Summary: Vala compiler library

%description -n libvala
This package contains the shared libvala library.

%package -n libvala-devel
Summary: Development files for libvala
Requires: libvala%{?_isa} = %{version}-%{release}
Provides: vala-devel = %{version}-%{release}
Provides: pkgconfig(libvala-%{api_ver}) = %{version}

%description -n libvala-devel
This package contains development files for libvala. This is not
necessary for using the vala compiler.

%package doc
Summary: Documentation for vala
BuildArch: noarch
Requires: vala = %{version}-%{release}

%description doc
This package contains documentation in a devhelp HTML book.

%package -n valadoc
Summary: Vala documentation generator
Requires: vala%{?_isa} = %{version}-%{release}
Requires: libvala%{?_isa} = %{version}-%{release}

%description -n valadoc
Valadoc is a documentation generator for generating API documentation from Vala
source code.

%package -n valadoc-devel
Summary: Development files for valadoc
Requires: valadoc%{?_isa} = %{version}-%{release}
Provides: pkgconfig(valadoc-%{api_ver}) = %{version}

%description -n valadoc-devel
The valadoc-devel package contains libraries and header files for
developing applications that use valadoc.

%prep
%oreon_sha256
%autosetup -p1

%build
%global build_type_safety_c 0
%configure
sed -i 's|/lib /usr/lib|/lib /usr/lib /lib64 /usr/lib64|' libtool
%make_build

%install
%make_install
mv %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}{,-`uname -m`}
echo -e '#!/bin/sh\nexec %{_bindir}/vala-gen-introspect-%{api_ver}-`uname -m` "$@"' > \
    %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}
chmod +x %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}
find %{buildroot} -name '*.la' -delete

%check
export -n VALAFLAGS
%make_build check

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/vala
%{_bindir}/vala-%{api_ver}
%{_bindir}/valac
%{_bindir}/valac-%{api_ver}
%{_bindir}/vala-gen-introspect
%{_bindir}/vala-gen-introspect-%{api_ver}*
%{_bindir}/vapigen
%{_bindir}/vapigen-%{api_ver}
%{_libdir}/pkgconfig/vapigen*.pc
%{_libdir}/vala-%{api_ver}/
%{_datadir}/aclocal/vala.m4
%{_datadir}/aclocal/vapigen.m4
%{_datadir}/vala/
%{_datadir}/vala-%{api_ver}/
%{_mandir}/man1/valac.1*
%{_mandir}/man1/valac-%{api_ver}.1*
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vala-gen-introspect-%{api_ver}.1*
%{_mandir}/man1/vapigen.1*
%{_mandir}/man1/vapigen-%{api_ver}.1*

%files -n libvala
%license COPYING
%{_libdir}/libvala-%{api_ver}.so.*

%files -n libvala-devel
%{_includedir}/vala-%{api_ver}
%{_libdir}/libvala-%{api_ver}.so
%{_libdir}/pkgconfig/libvala-%{api_ver}.pc

%files doc
%doc %{_datadir}/devhelp/books/vala-%{api_ver}

%files -n valadoc
%{_bindir}/valadoc
%{_bindir}/valadoc-%{api_ver}
%{_libdir}/libvaladoc-%{api_ver}.so.0*
%{_libdir}/valadoc-%{api_ver}/
%{_datadir}/valadoc-%{api_ver}/
%{_mandir}/man1/valadoc-%{api_ver}.1*
%{_mandir}/man1/valadoc.1*

%files -n valadoc-devel
%{_includedir}/valadoc-%{api_ver}/
%{_libdir}/libvaladoc-%{api_ver}.so
%{_libdir}/pkgconfig/valadoc-%{api_ver}.pc

%changelog
%autochangelog
