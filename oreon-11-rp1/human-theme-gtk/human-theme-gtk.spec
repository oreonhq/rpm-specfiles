%global source0_hash ffaa53147c88db491545f5c26b461eeabe7c6a2fbc6b845e07c61b2f1adb50e5
Name:          human-theme-gtk
Version:       3.0.0
Release:        1%{?dist}
Summary:        Human theme for GTK
Summary(fr):   Thème Human pour GTK
License:       GPL-3.0-or-later and LGPL-2.1-or-later and CC-BY-SA-3.0
URL:           https://github.com/luigifab/human-theme
Source0:        https://github.com/luigifab/human-theme/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:     noarch
Recommends:    mate-icon-theme
Recommends:    dmz-cursor-themes
Recommends:    gtk-murrine-engine
Recommends:    qt5-globalqss
Recommends:    qt5-qtsvg
Recommends:    qt6-globalqss
Recommends:    qt6-qtsvg
# oreon:deps
BuildRequires:  aspell-fr
# /oreon:deps
%description %{expand:
This theme is mainly intended for MATE and Xfce desktop environments.

After installation you must restart your session.
After uninstallation be sure to remove the config file:
 /etc/profile.d/human-theme-gtk.sh}

%description -l fr %{expand:
Ce thème est principalement destiné pour les environnements
de bureau MATE et Xfce.

Après l'installation vous devez redémarrer votre session.
Après la désinstallation, veillez à supprimer le fichier de config :
 /etc/profile.d/human-theme-gtk.sh}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n human-theme-%{version}
sed -i 's/IconTheme=gnome/IconTheme=mate/g' src/*/index.theme

%install
install -dm 755 %{buildroot}%{_datadir}/themes/
cp -a src/Human/           %{buildroot}%{_datadir}/themes/
cp -a src/Human-blue/      %{buildroot}%{_datadir}/themes/
cp -a src/Human-green/     %{buildroot}%{_datadir}/themes/
cp -a src/Human-orange/    %{buildroot}%{_datadir}/themes/
install -Dpm 644 data/profile.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
