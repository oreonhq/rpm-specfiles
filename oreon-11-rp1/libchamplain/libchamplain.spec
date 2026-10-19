%global source0_hash a915cd172a0c52944c5579fcb4683f8a878c571bf5e928254b5dafefc727e5a7
Name:		libchamplain
Version:	0.12.21
Release:        1%{?dist}
Summary:        Map view for Clutter
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://wiki.gnome.org/Projects/libchamplain
Source0:        https://download.gnome.org/sources/libchamplain/0.12/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  clutter-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libsoup3-devel
BuildRequires:  meson
BuildRequires:  sqlite-devel
BuildRequires:  vala
# /oreon:deps
%description
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-gtk%{?_isa} = %{version}-%{release}
Obsoletes:	%{name}-gtk-devel < 0.12.12
Provides:	%{name}-gtk-devel = %{version}-%{release}
Obsoletes:	%{name}-vala < 0.12.8-1
Obsoletes:	%{name}-demos < 0.12.20-1
%description devel
This package contains development files for %{name}.

%package gtk
Summary:	Gtk+ widget wrapper for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description gtk
Libchamplain-gtk is a library providing a GtkWidget to embed %{name}
into Gtk+ applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%ldconfig_scriptlets gtk
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libchamplain-devel -f %{oreon_filedir}/libchamplain-devel.list
%files -n libchamplain-gtk -f %{oreon_filedir}/libchamplain-gtk.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.21-9
- Prepare for Oreon 11 (RP1)
