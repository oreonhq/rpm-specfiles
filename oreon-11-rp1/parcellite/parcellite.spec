%global source0_hash 17d5283fba13a0392d7978f8aec59cec174868c90ccc89b3b08267cecb928076

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=442473

Name:           parcellite
Version:        1.2.6
Release:        9%{?dist}
Summary:        A lightweight GTK+ clipboard manager

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://%{name}.sf.net/
Source0:        https://github.com/ZaWertun/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# migrate autostart from previous upstream rickyrockrat
Source1:        %{name}-startup.desktop

BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-g++
BuildRequires:  gtk2-devel >= 2.10.0 
BuildRequires:  desktop-file-utils
BuildRequires:  intltool >= 0.23

Requires:       xdotool
Requires:       hicolor-icon-theme

%description
Parcellite is a stripped down, basic-features-only clipboard manager with a 
small memory footprint for those who like simplicity.

In GNOME and Xfce the clipboard manager will be started automatically. For 
other desktops or window managers you should also install a panel with a 
system tray or notification area if you want to use this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n%{name}-%{version}

%build
# TODO: Please submit an issue to upstream (rhbz#2381355)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%make_build -C %{_vpath_builddir}

%install
%make_install -C %{_vpath_builddir}
%find_lang %{name}
desktop-file-edit \
    --remove-category=Application \
    --remove-only-show-in=Old \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install \
    --add-category=TrayIcon \
    --add-only-show-in="GNOME;KDE;LXDE;MATE;Razor;ROX;TDE;Unity;XFCE;" \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    %{SOURCE1}
install -D data/%{name}.appdata.xml %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
%autochangelog
