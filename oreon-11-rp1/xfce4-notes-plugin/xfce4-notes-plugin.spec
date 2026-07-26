%global source0_hash 8301fcd397bbc98a3def3d94f04de30cc128b4a35477024d2bcb2952a161a3b5

%global _hardened_build 1
%global minor_version 1.11
%global xfceversion 4.16

Name:           xfce4-notes-plugin
Version:        1.11.2
Release:        %autorelease
Summary:        Notes plugin for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  gtksourceview4-devel
Requires:       xfce4-panel >= %{xfceversion}
Requires:       xfconf >= %{xfceversion}
Requires:       exo

%description
This plugin provides sticky notes for your desktop. You can create a note by 
clicking on the customizable icon with the middle button of your mouse, 
show/hide the notes using the left one, edit the titlebar, change the notes 
background color and much more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/xfce4-notes-autostart.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/xfce4-notes.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/autostart/xfce4-notes-autostart.desktop
%{_bindir}/xfce4-notes
%{_bindir}/xfce4-popup-notes
%{_bindir}/xfce4-notes-settings
%{_libdir}/xfce4/panel/plugins/libnotes.so
%{_datadir}/applications/xfce4-notes.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/xfce4/notes/gtk-3.0/gtk.css

%changelog
%autochangelog
