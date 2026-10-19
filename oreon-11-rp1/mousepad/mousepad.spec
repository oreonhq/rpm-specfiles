%global source0_hash e86c59feb08126d4cace368432c16b2dee8e519aaca8a9d2b409ae1cdd200802
%bcond xfce4kbd %{undefined flatpak}
%global minorversion 0.7
Name:           mousepad
Version:        0.7.0
Release:        1%{?dist}
Summary:        Simple text editor for Xfce desktop environment
License:        GPL-2.0-or-later
URL:            https://git.xfce.org/apps/mousepad/about/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.xz
%if %{with xfce4kbd}
%endif
# oreon:deps
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gspell-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  libappstream-glib
BuildRequires:  libxfce4ui-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  xfce4-dev-tools
# /oreon:deps
%description
Mousepad aims to be an easy-to-use and fast editor. It's target is an editor for
quickly editing text files, not a development environment or an editor with a
huge bunch of plugins.

Mousepad is based on Leafpad. The initial reason for Mousepad was to provide
printing support, which would have been difficult for Leafpad for various
reasons.

Although some features are under development, currently Mousepad has following
features:

    * Complete support for UTF-8 text
    * Cut/Copy/Paste and Select All text
    * Search and Replace
    * Font selecton
    * Word Wrap
    * Character coding selection
    * Auto character coding detection (UTF-8 and some codesets)
    * Manual codeset setting
    * Infinite Undo/Redo by word
    * Auto Indent
    * Multi-line Indent
    * Display line numbers
    * Drag and Drop
    * Printing

%package -n libmousepad0
Summary:        Mousepad plugin provider
Group:          System/Libraries
Requires:       %{name} >= %{version}
%description -n libmousepad0
A plugin provider for the Mousepad text editor

%package devel
Summary:        Development files for Mousepad
Group:          Development/Libraries
Requires:       libmousepad0 >= %{version}
%Description devel

Development files for Mousepad plugin development
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson %{!?with_xfce4kbd:-Dshortcuts-plugin=disabled}
%meson_build
%install
%meson_install
%find_lang %{name}
desktop-file-install \
    --remove-category="Application" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/org.xfce.%{name}.desktop
desktop-file-install \
    --remove-category="Application" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/org.xfce.%{name}-settings.desktop
mkdir -p %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles libmousepad0 usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if 0%{?el7}
%post

update-desktop-database &> /dev/null ||:
%postun

update-desktop-database &> /dev/null ||:
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi
%post -n libmousepad0 -p /sbin/ldconfig

%postun -n libmousepad0 -p /sbin/ldconfig

%posttrans

glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%endif
%files -f %{oreon_filedir}/main.list
%files -n libmousepad0 -f %{oreon_filedir}/libmousepad0.list
%files -n mousepad-devel -f %{oreon_filedir}/mousepad-devel.list

%changelog

%autochangelog
