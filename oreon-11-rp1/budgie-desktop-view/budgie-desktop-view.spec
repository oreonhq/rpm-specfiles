%global source0_hash 22bfebcb8a2377b17264c03e4f23f686c3217166b83381f1136e49da6f785be7
%global glib2_version 2.64
%global gtk3_version 3.24
%global vala_version 0.48
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}
Name:           budgie-desktop-view
Version:        10.10.3
Release:        1%{?dist}
Summary:        Official Budgie desktop icons application / implementation
License:        Apache-2.0
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop-view
Source0:        https://github.com/BuddiesOfBudgie/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(libxfce4windowing-0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  vala
# /oreon:deps
%description
Official Budgie desktop icons application / implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.buddiesofbudgie.budgie-desktop-view.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
