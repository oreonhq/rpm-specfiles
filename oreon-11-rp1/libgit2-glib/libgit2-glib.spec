%global source0_hash 97423a779002b3be8751c75f9d79049dfccca3616a26159fc162486772ba785f
%global libgit2_version 1.9.0
%global glib2_version 2.44.0
Name:           libgit2-glib
Version:        1.2.1
Release:        1%{?dist}
Summary:        Git library for GLib
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/Libgit2-glib
Source0:        https://download.gnome.org/sources/libgit2-glib/1.2/libgit2-glib-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  libssh2-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
BuildRequires:  vala
# /oreon:deps
%description
libgit2-glib is a glib wrapper library around the libgit2 git access library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libgit2-glib-1.2.1
%oreon_prep
%build

%meson -Dgtk_doc=true \
       -Dpython=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgit2-glib-devel -f %{oreon_filedir}/libgit2-glib-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-1
- Import
