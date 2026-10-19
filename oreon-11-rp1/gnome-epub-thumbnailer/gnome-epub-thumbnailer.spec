%global source0_hash f90619d58c69902f2eff57b9f0042b4737861083f475921a310fecc612fca017
Name:           gnome-epub-thumbnailer
Version:        1.8
Release:        4%{?dist}
Summary:        Thumbnailers for EPub and MOBI books
License:        GPL-2.0-or-later
URL:            https://git.gnome.org/browse/gnome-epub-thumbnailer
Source0:        http://download.gnome.org/sources/%{name}/1.8/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
Thumbnailers for EPub and MOBI books

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
