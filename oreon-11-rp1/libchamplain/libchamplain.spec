# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 a915cd172a0c52944c5579fcb4683f8a878c571bf5e928254b5dafefc727e5a7
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:		libchamplain
Version:	0.12.21
Release:	9%{?dist}
Summary:	Map view for Clutter

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://wiki.gnome.org/Projects/libchamplain
Source0:	https://download.gnome.org/sources/libchamplain/0.12/%{name}-%{version}.tar.xz

BuildRequires:	clutter-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libsoup3-devel
BuildRequires:	meson
BuildRequires:	sqlite-devel
BuildRequires:	gtk3-devel
BuildRequires:	vala

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
%oreon_verify_sources
%setup -q

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets
%ldconfig_scriptlets gtk

%files
%license COPYING
%doc AUTHORS README.md NEWS
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Champlain-0.12.typelib
%{_libdir}/libchamplain-0.12.so.0*

%files devel
%{_includedir}/champlain-0.12/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Champlain-0.12.gir
%{_datadir}/gir-1.0/GtkChamplain-0.12.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/champlain-0.12/
%{_datadir}/vala/vapi/champlain-0.12.deps
%{_datadir}/vala/vapi/champlain-0.12.vapi
%{_datadir}/vala/vapi/champlain-gtk-0.12.deps
%{_datadir}/vala/vapi/champlain-gtk-0.12.vapi
%{_libdir}/libchamplain-0.12.so
%{_libdir}/libchamplain-gtk-0.12.so
%{_libdir}/pkgconfig/champlain-0.12.pc
%{_libdir}/pkgconfig/champlain-gtk-0.12.pc

%files gtk
%{_libdir}/girepository-1.0/GtkChamplain-0.12.typelib
%{_libdir}/libchamplain-gtk-0.12.so.0*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.21-9
- Prepare for Oreon 11 (RP1)
