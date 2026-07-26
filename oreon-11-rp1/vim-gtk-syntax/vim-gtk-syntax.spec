%global source0_hash 0ed92c98554083d05603f9b57b381e7c260e4b288ccedc17890304c8ad0ae1f6

Name:           vim-gtk-syntax
Version:        20130716
Release:        25%{?dist}
Summary:        Vim syntax highlighting for GLib, Gtk+, Gstreamer, and more

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            http://www.vim.org/scripts/script.php?script_id=1000
#Source0:       http://www.vim.org/scripts/download_script.php?src_id=20534
# The source for this package was downloaded from the URL above, and renamed to
# include the version number:
# mv gtk-vim-syntax.tar.gz gtk-vim-syntax-20130716.tar.gz
Source0:        gtk-vim-syntax-20130716.tar.gz
Source1:        vim-gtk-syntax.metainfo.xml

BuildRequires:  /usr/bin/appstream-util
Requires:       vim-filesystem
BuildArch:      noarch

%description
A collection of C extension syntax files for xlib, glib (gobject, gio),
gdk-pixbuf, gtk2 (gdk2), gtk3 (gdk3), atk, at-spi, pango, cairo, clutter, gimp,
gstreamer, dbus-glib, json-glib, libglade, gtksourceview, gnome-desktop,
libgsf, libnotify, librsvg, libunique, libwnck, gtkglext, vte, poppler, evince. 

The xlib one was originally created by Hwanjin Choe (vimscript #570), the
others were generated from gtk-doc declaration lists and support
enabling/disabling of highlighting of deprecated declarations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtk-vim-syntax

%build
# Nothing to build.

%install
install -d %{buildroot}%{_datadir}/vim/vimfiles/syntax
install -pm 0644 *.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%check
appstream-util validate %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml --nonet

%files
%doc c.vim.example README
%{_datadir}/appdata/%{name}.metainfo.xml
%{_datadir}/vim/vimfiles/syntax

%changelog
%autochangelog
