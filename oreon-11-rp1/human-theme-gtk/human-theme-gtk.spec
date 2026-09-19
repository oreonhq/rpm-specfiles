%global source0_hash ffaa53147c88db491545f5c26b461eeabe7c6a2fbc6b845e07c61b2f1adb50e5

Name:          human-theme-gtk
Version:       3.0.0
Release:       1%{?dist}
Summary:       Human theme for GTK
Summary(fr):   Thème Human pour GTK
License:       GPL-3.0-or-later and LGPL-2.1-or-later and CC-BY-SA-3.0
URL:           https://github.com/luigifab/human-theme
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: aspell-fr
Recommends:    mate-icon-theme
Recommends:    dmz-cursor-themes
Recommends:    gtk-murrine-engine
Recommends:    qt5-globalqss
Recommends:    qt5-qtsvg
Recommends:    qt6-globalqss
Recommends:    qt6-qtsvg

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

%files
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%license LICENSE
%doc README.md
# the entire source code is GPL-3.0-or-later, except */metacity-1/* which is LGPL-2.1-or-later,
# and */gtk-2.0/* which is CC-BY-SA-3.0-or-later
%{_datadir}/themes/Human/
%{_datadir}/themes/Human-blue/
%{_datadir}/themes/Human-green/
%{_datadir}/themes/Human-orange/

%changelog
%autochangelog
