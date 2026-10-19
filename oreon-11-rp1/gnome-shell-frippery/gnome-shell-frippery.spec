%global source0_hash 627bae4ed1e4b093356a6cd6b03121dc766de2dd93db798b124d37b1b2a69e25
%global extdir %{_datadir}/gnome-shell/extensions
%global gschemadir %{_datadir}/glib-2.0/schemas
Name:           gnome-shell-frippery
Version:        50.0
Release:        1%{?dist}
Summary:        Extensions to provide a user experience more like that of GNOME 2
License:        GPL-2.0-or-later
URL:            http://frippery.org/extensions
Source0:        http://frippery.org/extensions/%{name}-%{version}.tgz
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
This package contains some GNOME Shell extensions to provide a user experience
more like that of GNOME 2.

%package -n     gnome-shell-extension-frippery-applications-menu
Summary:        Replace Activities button with an Applications menu
Requires:       (gnome-shell-extension-common >= 46 and gnome-shell-extension-common < 50)
%description -n gnome-shell-extension-frippery-applications-menu
This GNOME Shell extension replaces the Activities button in the panel with an
Applications menu.

%package -n     gnome-shell-extension-frippery-bottom-panel
Summary:        Add a bottom panel to the shell
Requires:       (gnome-shell-extension-common >= 49 and gnome-shell-extension-common < 50)
%description -n gnome-shell-extension-frippery-bottom-panel
This GNOME Shell extension adds a bottom panel, including a window list and
workspace switcher.

%package -n     gnome-shell-extension-frippery-move-clock
Summary:        Move clock to left of status menu button
Requires:       (gnome-shell-extension-common >= 46 and gnome-shell-extension-common < 50)
%description -n gnome-shell-extension-frippery-move-clock
This GNOME Shell extension moves the clock from the centre of the panel
towards the right.

%package -n     gnome-shell-extension-frippery-panel-favorites
Summary:        Add launchers for Favorites to the panel
Requires:       (gnome-shell-extension-common >= 49 and gnome-shell-extension-common < 50)
%description -n gnome-shell-extension-frippery-panel-favorites
This GNOME Shell extension places a launcher for each favourite application in
the panel. Right clicking on the icons invokes a menu that lets one perform
various operations on the application.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c %{name}-%{version} -p1

mv .local/share/gnome-shell/extensions .
mv .local/share/gnome-shell/gnome-shell-frippery/* .

%build

%install
mkdir -p %{buildroot}%{extdir}
cp -PR extensions/* %{buildroot}%{extdir}
mkdir -p %{buildroot}%{gschemadir}
cp -P extensions/*/schemas/*.gschema.xml %{buildroot}%{gschemadir}
rm -r %{buildroot}%{extdir}/*/schemas
%find_lang frippery-applications-menu
%find_lang frippery-bottom-panel
%oreon_autofiles gnome-shell-extension-frippery-applications-menu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnome-shell-extension-frippery-bottom-panel usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnome-shell-extension-frippery-move-clock usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnome-shell-extension-frippery-panel-favorites usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-shell-extension-frippery-applications-menu -f %{oreon_filedir}/gnome-shell-extension-frippery-applications-menu.list
%files -n gnome-shell-extension-frippery-bottom-panel -f %{oreon_filedir}/gnome-shell-extension-frippery-bottom-panel.list
%files -n gnome-shell-extension-frippery-move-clock -f %{oreon_filedir}/gnome-shell-extension-frippery-move-clock.list
%files -n gnome-shell-extension-frippery-panel-favorites -f %{oreon_filedir}/gnome-shell-extension-frippery-panel-favorites.list

%changelog

%autochangelog
