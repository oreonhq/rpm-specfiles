%global source0_hash 17d5283fba13a0392d7978f8aec59cec174868c90ccc89b3b08267cecb928076
Name:           parcellite
Version:        1.2.6
Release:        9%{?dist}
Summary:        A lightweight GTK+ clipboard manager
License:        GPL-3.0-or-later
URL:            http://%{name}.sf.net/
Source0:        https://github.com/ZaWertun/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-startup.desktop
Requires:       xdotool
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-g++
BuildRequires:  gtk2-devel
BuildRequires:  intltool
# /oreon:deps
%description
Parcellite is a stripped down, basic-features-only clipboard manager with a 
small memory footprint for those who like simplicity.

In GNOME and Xfce the clipboard manager will be started automatically. For 
other desktops or window managers you should also install a panel with a 
system tray or notification area if you want to use this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
