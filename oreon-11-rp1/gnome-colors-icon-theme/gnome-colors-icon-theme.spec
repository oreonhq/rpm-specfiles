%global source0_hash 0b03073198dcf98925d20d8793efe4b2ad5afa5786d80ce068a5ef47e926bced
%global real_name gnome-colors
Name: gnome-colors-icon-theme
Summary:        GNOME-Colors icon theme
Version: 5.5.1
Release:        1%{?dist}
Url: http://code.google.com/p/gnome-colors
Source0:        http://%{real_name}.googlecode.com/files/%{real_name}-src-%{version}.tar.gz
License: GPL-2.0-only
BuildArch: noarch
Requires: gnome-icon-theme
Patch1: remove-undefined-filter.patch
%bcond_with prebuilt
Source1: %{real_name}-built-%{version}.tar.gz
%if %{without prebuilt}
%endif
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  icon-naming-utils
BuildRequires:  inkscape
BuildRequires:  make
# /oreon:deps
%description
The GNOME-Colors is a project that aims to make the GNOME desktop as 
elegant, consistent and colorful as possible.

The current goal is to allow full color customization of themes, icons, 
GDM logins and splash screens. There are already seven full color-schemes 
available; Brave (Blue), Human (Orange), Wine (Red), Noble (Purple), Wise 
(Green), Dust (Chocolate) and Illustrious (Pink). An unlimited amount of 
color variations can be rebuilt and recolored from source, so users need 
not stick to the officially supported color palettes.

GNOME-Colors is mostly inspired/based on Tango, GNOME, Elementary, 
Tango-Generator and many other open-source projects. More information 
can be found in the AUTHORS file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -c %{real_name}-icon-theme-%{version}
# Make it build with Inkscape 1.0rc1+
sed -i 's|inkscape --without-gui -f /dev/stdin -e|inkscape --pipe -o|' Makefile

# link the start-here icon to the Fedora icon
for dir in gnome-colors-common/*/places; do
  cd $dir
  ln -sf ../apps/fedora-logo-icon.* start-here.*
  cd -
done
# change name from GNOME -> GNOME-Colors
rename 'gnome' '%{real_name}' themes/*
sed -i -e 's/GNOME/GNOME-Colors/' themes/*

%if %{with prebuilt}
tar -xzf %{SOURCE1}
find gnome-colors-* -type f  -exec touch {} +
%endif

%build

%{make_build}
%install
%{make_install}
%global themes %{_datadir}/icons/gnome-colors-common %{_datadir}/icons/gnome-colors-brave %{_datadir}/icons/gnome-colors-carbonite %{_datadir}/icons/gnome-colors-dust %{_datadir}/icons/gnome-colors-human %{_datadir}/icons/gnome-colors-illustrious %{_datadir}/icons/gnome-colors-noble %{_datadir}/icons/gnome-colors-tribute %{_datadir}/icons/gnome-colors-wine %{_datadir}/icons/gnome-colors-wise
%transfiletriggerin -- %{_datadir}/icons/gnome-colors
for THEME in %themes; do gtk-update-icon-cache --force ${THEME} &>/dev/null || : ; done
%transfiletriggerpostun -- %{_datadir}/icons/gnome-colors
for THEME in %themes; do gtk-update-icon-cache --force ${THEME} &>/dev/null || : ; done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
