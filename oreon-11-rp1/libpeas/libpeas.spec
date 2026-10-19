%global source0_hash 589eca89b437006edf3755478df037c740a2a84cfa5d202dbad6095e828e2488
%global apiver 2
Name:           libpeas
Version:        2.2.1
Release:        1%{?dist}
Summary:        Plug-ins implementation convenience library
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libpeas
Source0:        https://download.gnome.org/sources/%{name}/2.2/%{name}-%{version}.tar.xz
Patch0:        libpeas-fix-py-wrapper-refcount-test.patch
# oreon:deps
BuildRequires:  /usr/bin/vapigen
BuildRequires:  /usr/bin/xmllint
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(mozjs-128)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  python3-devel
# /oreon:deps
%description
libpeas is a convenience library making adding plug-ins support
to glib-based applications.

%package loader-gjs
Summary:        GJS loader for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description loader-gjs
This package contains the GJS loader that is needed to
run JavaScript plugins that use libpeas.

%package loader-python
Summary:        Python loader for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject
%description loader-python
This package contains the Python loader that is needed to
run Python plugins that use libpeas.

%package devel
Summary:        Development files for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development libraries and header files
that are needed to write applications that use libpeas.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libpeas-2.2.1
%oreon_prep
%build

%meson \
  -Dgtk_doc=true \
  -Dlua51=false \
  -Dvapi=true
%meson_build
%check

%ifnarch aarch64
%meson_test
%endif
%install
%meson_install
%find_lang libpeas-%{apiver}
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpeas-loader-gjs -f %{oreon_filedir}/libpeas-loader-gjs.list
%files -n libpeas-loader-python -f %{oreon_filedir}/libpeas-loader-python.list
%files -n libpeas-devel -f %{oreon_filedir}/libpeas-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-1
- Import
