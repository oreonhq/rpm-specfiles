%global source0_hash 0b03073198dcf98925d20d8793efe4b2ad5afa5786d80ce068a5ef47e926bced

%global real_name gnome-colors

Name: gnome-colors-icon-theme
Summary: GNOME-Colors icon theme
Version: 5.5.1
Release: %autorelease
Url: http://code.google.com/p/gnome-colors
Source0: http://%{real_name}.googlecode.com/files/%{real_name}-src-%{version}.tar.gz
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildArch: noarch
Requires: gnome-icon-theme

# https://bugzilla.redhat.com/show_bug.cgi?id=1645368#c19
Patch1: remove-undefined-filter.patch

# the build is segfaulting due to
# https://bugzilla.redhat.com/show_bug.cgi?id=1556793
# so we use prebuilt pngs and svgs instead
# this is content, so strictly speaking this is not forbidden
%bcond_with prebuilt

# `mockbuild -N --without prebuilt` this on Fedora 22
# cd /var/lib/mock/fedora-22-x86_64/root/builddir/build/BUILD/gnome-colors-icon-theme-5.5.1/
# tar -cvzf gnome-colors-built-5.5.1.tar.gz gnome-colors-*
Source1: %{real_name}-built-%{version}.tar.gz

BuildRequires: icon-naming-utils >= 0.8.7
BuildRequires: ImageMagick

%if %{without prebuilt}
BuildRequires: inkscape
%endif
BuildRequires: make

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

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_datadir}/icons/gnome-colors-common/
%ghost %{_datadir}/icons/gnome-colors-common/icon-theme.cache
%{_datadir}/icons/gnome-colors-brave/
%ghost %{_datadir}/icons/gnome-colors-brave/icon-theme.cache
%{_datadir}/icons/gnome-colors-carbonite/
%ghost %{_datadir}/icons/gnome-colors-carbonite/icon-theme.cache
%{_datadir}/icons/gnome-colors-dust/
%ghost %{_datadir}/icons/gnome-colors-dust/icon-theme.cache
%{_datadir}/icons/gnome-colors-human/
%ghost %{_datadir}/icons/gnome-colors-human/icon-theme.cache
%{_datadir}/icons/gnome-colors-illustrious/
%ghost %{_datadir}/icons/gnome-colors-illustrious/icon-theme.cache
%{_datadir}/icons/gnome-colors-noble/
%ghost %{_datadir}/icons/gnome-colors-noble/icon-theme.cache
%{_datadir}/icons/gnome-colors-tribute/
%ghost %{_datadir}/icons/gnome-colors-tribute/icon-theme.cache
%{_datadir}/icons/gnome-colors-wine/
%ghost %{_datadir}/icons/gnome-colors-wine/icon-theme.cache
%{_datadir}/icons/gnome-colors-wise/
%ghost %{_datadir}/icons/gnome-colors-wise/icon-theme.cache

%changelog
%autochangelog
