%global source0_hash 38818711bb01c0f4a5a534c7b864436b18939e53412b3fd6c809bd576f746c0c
%global __pytest xwfb-run -- pytest
%global app_id  io.github.fract4d
Name:           gnofract4d
Version:        4.4
Release:        1%{?dist}
Summary:        Gnofract 4D is a Gnome-based program to draw fractals
License:        BSD-3-Clause
URL:            https://fract4d.github.io/gnofract4d/
Source0:        https://github.com/fract4d/gnofract4d/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{app_id}.metainfo.xml
ExcludeArch:    %{ix86}
Requires:       gcc
Requires:       hicolor-icon-theme
Requires:       libgcc%{?_isa}
Requires:       glibc-devel%{?_isa}
Requires:       python3-gobject
Requires:       gobject-introspection
Requires:       gtk4
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gobject-introspection
BuildRequires:  gtk4
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  rsvg-pixbuf-loader
BuildRequires:  xwayland-run
# /oreon:deps
%description
Gnofract 4D is a free, open source program which allows anyone to create
beautiful images called fractals.  The images are automatically created
by the computer based on mathematical principles.  These include the
Mandelbrot and Julia sets and many more.  You don't need to do any math:
you can explore a universe of images just using a mouse.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix python installation
sed -i -e 's|pymod\.find_installation(|&pure: false|' meson.build

# Fix the desktop file
sed -e "s/Categories.*/Categories=Graphics;GTK;GNOME;Education;Science;Math;/" \
    -e "s/MimeType.*/&;/" \
    -i.orig %{app_id}.desktop
touch -r %{app_id}.desktop.orig %{app_id}.desktop
rm %{app_id}.desktop.orig

%build

%meson -Dstrip=false
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
for fil in `find %{buildroot}%{python3_sitearch} -perm 644 -name '*.py'`; do
  sed '\|^#!/usr/bin.*python|d' $fil > $fil.new
  touch -r $fil $fil.new
  mv -f $fil.new $fil
done
rm -rf %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/%{name}.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%check

%pytest -v --ignore fract4dgui/tests/test_main_window.py
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
