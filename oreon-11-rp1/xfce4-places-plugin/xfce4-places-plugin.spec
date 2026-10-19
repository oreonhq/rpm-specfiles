%global source0_hash 76d95687e0bea267465e832eea6266563a18d2219192f9e8af6f88e899262e43
%global _hardened_build 1
%global minorversion 1.9
%global xfceversion 4.20
Name:           xfce4-places-plugin
Version:        1.9.0
Release:        1%{?dist}
Summary:        Places menu for the Xfce panel
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz
Requires:       xfce4-panel >= %{xfceversion}
# oreon:deps
BuildRequires:  exo-devel
BuildRequires:  gcc-c++
BuildRequires:  libnotify-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel
BuildRequires:  xfconf-devel
# /oreon:deps
%description
A menu with quick access to folders, documents, and removable media. The 
Places plugin brings much of the functionality of GNOME’s Places menu to 
Xfce. It puts a simple button on the panel. Clicking on this button opens up 
a menu with 4 sections:
1) System-defined directories (home folder, trash, desktop, file system)
2) Removable media
3) User-defined bookmarks (reads ~/.gtk-bookmarks)
4) Recent documents submenu (requires GTK v2.10 or greater) 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
