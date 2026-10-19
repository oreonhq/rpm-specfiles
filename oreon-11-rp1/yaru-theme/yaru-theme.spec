%global source0_hash none
%global forgeurl https://github.com/ubuntu/yaru
%global tag %{version}-0ubuntu1
%global _license COPYING COPYING.LGPL-2.1 COPYING.LGPL-3.0 LICENSE_CCBYSA
Name:       yaru-theme
Version:    25.10.3
%forgemeta
Release:        1%{?dist}
Summary:        All Ubuntu Yaru GNOME themes
BuildArch:  noarch
License:    GPL-3.0-or-later and CC-BY-SA-4.0
URL:        https://community.ubuntu.com/c/desktop/theme-refresh
Source0:        %{forgeurl}/archive/%{tag}/yaru-%{tag}.tar.gz
Requires:   gnome-shell-theme-yaru = %{version}-%{release}
Requires:   yaru-gtk3-theme = %{version}-%{release}
Requires:   yaru-gtk4-theme = %{version}-%{release}
Requires:   yaru-gtksourceview-theme = %{version}-%{release}
Requires:   yaru-icon-theme = %{version}-%{release}
Requires:   yaru-sound-theme = %{version}-%{release}
# oreon:deps
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  sassc
# /oreon:deps
%description

%package     -n gnome-shell-theme-yaru
Summary:        Yaru GNOME Shell Theme
Requires:       gnome-shell-extension-user-theme
Recommends:     yaru-gtk3-theme
Recommends:     yaru-icon-theme
Suggests:       yaru-sound-theme
Suggests:       yaru-theme
%description -n gnome-shell-theme-yaru

This package contains GNOME Shell Theme.

%package     -n yaru-gtk3-theme
Summary:        GTK+ 3 support for the Yaru GTK Theme
Requires:       gtk3
Recommends:     yaru-gtk2-theme
Recommends:     yaru-gtk4-theme
%description -n yaru-gtk3-theme

This package contains GTK+ 3 theme.

%package     -n yaru-gtk4-theme
Summary:        GTK+ 3 support for the Yaru GTK Theme
Requires:       gtk4
Recommends:     yaru-gtk2-theme
Recommends:     yaru-gtk3-theme
%description -n yaru-gtk4-theme

This package contains GTK 4 theme.

%package     -n yaru-icon-theme
Summary:        Yaru icon theme
License:        CC-BY-SA
Requires:       hicolor-icon-theme
Suggests:       gnome-shell-theme-yaru
Suggests:       yaru-gtk3-theme
Suggests:       yaru-sound-theme
%description -n yaru-icon-theme

This package contains the icon theme.

%package     -n yaru-sound-theme
Summary:        Yaru sound theme
License:        CC-BY-SA
%description -n yaru-sound-theme

This package contains the sound theme following the XDG theming specification.

%package     -n yaru-gtksourceview-theme
Summary:        Yaru GtkSourceView theme
License:        CC-BY-SA
%description -n yaru-gtksourceview-theme

This package contains the GtkSourceView theme.

%prep

%forgeautosetup -p1

%build

%meson
%meson_build
%install
%meson_install
rm -rf %{buildroot}%{_datadir}/themes/Yaru-*/gtk-2.0/
rm -rf %{buildroot}%{_datadir}/themes/Yaru/gtk-2.0/
rm  %{buildroot}%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override \
    %{buildroot}%{_datadir}/xsessions/Yaru-xorg.desktop \
    %{buildroot}%{_datadir}/wayland-sessions/Yaru.desktop \
    %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css
touch %{buildroot}%{_datadir}/icons/Yaru/icon-theme.cache
%transfiletriggerin -- %{_datadir}/icons/Yaru
gtk-update-icon-cache --force %{_datadir}/icons/Yaru &>/dev/null || :
%oreon_autofiles gnome-shell-theme-yaru usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles yaru-gtk3-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles yaru-gtk4-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles yaru-icon-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles yaru-sound-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles yaru-gtksourceview-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-shell-theme-yaru -f %{oreon_filedir}/gnome-shell-theme-yaru.list
%files -n yaru-gtk3-theme -f %{oreon_filedir}/yaru-gtk3-theme.list
%files -n yaru-gtk4-theme -f %{oreon_filedir}/yaru-gtk4-theme.list
%files -n yaru-icon-theme -f %{oreon_filedir}/yaru-icon-theme.list
%files -n yaru-sound-theme -f %{oreon_filedir}/yaru-sound-theme.list
%files -n yaru-gtksourceview-theme -f %{oreon_filedir}/yaru-gtksourceview-theme.list

%changelog

%autochangelog
