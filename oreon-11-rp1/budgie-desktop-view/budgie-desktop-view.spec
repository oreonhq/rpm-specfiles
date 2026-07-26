%global source0_hash 9c37a6964cd7800d240c74c14338097e5990336995b3c581a3160cbdc575439d

%global glib2_version 2.64
%global gtk3_version 3.24
%global vala_version 0.48

%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}

Name:           budgie-desktop-view
Version:        10.10.1
Release:        1%{?dist}
Summary:        Official Budgie desktop icons application / implementation

License:        Apache-2.0
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop-view
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz

BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gdk-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(libxfce4windowing-0)
BuildRequires:  pkgconfig(vapigen) >= %{vala_version}
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  vala

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}

%description
Official Budgie desktop icons application / implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.buddiesofbudgie.budgie-desktop-view.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSE.md
%{_bindir}/org.buddiesofbudgie.budgie-desktop-view
%{_datadir}/applications/org.buddiesofbudgie.budgie-desktop-view.desktop
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.budgie-desktop-view.gschema.xml
%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.budgie-desktop-view-autostart.desktop

%changelog
%autochangelog
