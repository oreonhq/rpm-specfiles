%global source0_hash 74844eb99df44984206d6c55b15f1b553e9f122ddb0bad00902a7b7935d0a504

# Review request: https://bugzilla.redhat.com/show_bug.cgi?id=721043

# As pragha is building real plugins the following is needed, else the build fails:
%undefine _strict_symbol_defs_build

Name:           pragha
Version:        1.3.3
Release:        34%{?dist}
Summary:        Lightweight GTK+ music manager

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/pragha-music-player/pragha
#VCS: git:https://github.com/pragha-music-player/pragha.git
Source0:        https://github.com/pragha-music-player/pragha/releases/download/v%{version}/pragha-%{version}.tar.bz2
Patch0: pragha-c99-1.patch
Patch1: pragha-c99-2.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(keybinder-3.0) >= 0.2.0
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(libmtp) >= 1.1.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.38
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(libclastfm) >= 0.5

%if (0%{?fedora} && 0%{?fedora} >= 21) || (0%{?rhel} && 0%{?rhel} >= 7)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 0.11.90
# N/A. Error in configure or not yet packaged?
#BuildRequires:  pkgconfig(gstreamer-interfaces-1.0) >= 0.11.90
%else
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 0.10
BuildRequires:  pkgconfig(gstreamer-interfaces-1.0) >= 0.10
%endif

BuildRequires:  pkgconfig(libcddb) >= 1.3.0
BuildRequires:  pkgconfig(libcdio_paranoia) >= 0.90
BuildRequires:  pkgconfig(libcdio) >= 0.80
#BuildRequires:  libcurl-devel >= 7.18
# libglyr is not yet in Fedora
#BuildRequires:  pkgconfig(libglyr) >= 1.0.1
BuildRequires:  pkgconfig(libclastfm) >= 0.5
BuildRequires:  pkgconfig(libnotify) >= 0.7.5
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.10.0
BuildRequires:  pkgconfig(sqlite3) >= 3.4
BuildRequires:  pkgconfig(taglib_c) >= 1.8
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.0.0
BuildRequires:  totem-pl-parser-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       gstreamer1-plugins-base

%description
Pragha is is a lightweight GTK+ music manager that aims to be fast, bloat-free,
and light on memory consumption. It is written completely in C and GTK+.

Pragha is a fork of Consonance Music Manager, discontinued by the original
author.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Hack to support grilo 0.3
sed -i -e 's/grilo-0\.2/grilo-0.3/g' configure

%build
%configure

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
desktop-file-install                                       \
  --delete-original                                        \
  --add-category=Audio                                     \
  --dir=%{buildroot}%{_datadir}/applications          \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
# remove duplicate docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}

find %{buildroot}%{_libdir}/pragha -name \*.ls -exec rm -f {} \;

%files -f %{name}.lang
%doc ChangeLog COPYING FAQ NEWS README
%{_bindir}/pragha
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}/
%{_mandir}/man1/pragha.1.*
# One include file for plugins. Not sure if its worth splitting into -devel
%{_includedir}/pragha
# All the plugins
%{_libdir}/pragha

%changelog
%autochangelog
