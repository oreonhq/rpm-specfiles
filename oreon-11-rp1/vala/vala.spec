%global source0_hash 5ad7cbbfcc0de61b403d6797c9ef60455bfbebd8e162aec33b5b0b097adfb9d5
%global api_ver 0.56
%global priority 90
Name:           vala
Version:        0.56.19
Release:        1%{?dist}
Summary:        A modern programming language for GNOME
License:        LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://wiki.gnome.org/Projects/Vala
Source0:        https://download.gnome.org/sources/%{name}/0.56/%{name}-%{version}.tar.xz
Patch0:        https://gitlab.gnome.org/GNOME/vala/-/merge_requests/423.patch#/vala-warn-on-unknown-xml.patch
Requires: libvala%{?_isa} = %{version}-%{release}
Requires: gobject-introspection-devel
Provides: vala(api) = %{api_ver}
Provides: valac = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  dbus-x11
BuildRequires:  flex
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
# /oreon:deps
%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code. It's also planned to generate GIDL files when gobject-
introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.

%package -n     libvala
Summary:        Vala compiler library
%description -n libvala
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains the shared libvala library.

%package -n     libvala-devel
Summary:        Development files for libvala
Requires:       libvala%{?_isa} = %{version}-%{release}
Provides:       vala-devel = %{version}-%{release}
%description -n libvala-devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files for libvala. This is not
necessary for using the %{name} compiler.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    doc
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains documentation in a devhelp HTML book.

%package -n     valadoc
Summary:        Vala documentation generator
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libvala%{?_isa} = %{version}-%{release}
%description -n valadoc
Valadoc is a documentation generator for generating API documentation from Vala
source code.

%package -n     valadoc-devel
Summary:        Development files for valadoc
Requires:       valadoc%{?_isa} = %{version}-%{release}
%description -n valadoc-devel
Valadoc is a documentation generator for generating API documentation from Vala
source code.

The valadoc-devel package contains libraries and header files for
developing applications that use valadoc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles libvala usr/*/lib*.so.*
%oreon_autofiles libvala-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles valadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles valadoc-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export -n VALAFLAGS
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libvala -f %{oreon_filedir}/libvala.list
%files -n libvala-devel -f %{oreon_filedir}/libvala-devel.list
%files -n vala-doc -f %{oreon_filedir}/vala-doc.list
%files -n valadoc -f %{oreon_filedir}/valadoc.list
%files -n valadoc-devel -f %{oreon_filedir}/valadoc-devel.list

%changelog

%autochangelog
