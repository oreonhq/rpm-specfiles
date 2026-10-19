%global source0_hash 43027da995a8acb6ae51bb4db36eba66e3d656bda4ed3b133736832d4a93434b
%global commit db3337c1f30c1e90cb83ffb89f3679bddf6cd0a9
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251226
Name:           niri-settings
Version:        0.1.0~git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        GUI configuration app for Niri
License:        GPL-2.0-only
URL:            https://github.com/stefonarch/%{name}
Source0:        https://github.com/stefonarch/%{name}/archive/%{commit}/%{name}-db3337c.tar.gz
Patch0:         0001-adjust-paths.patch
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires:       niri >= 25.11
Requires:       python3-pyqt6
Requires:       (qt6-qtwayland if qt6-qtbase < 6.10)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  git-core
# /oreon:deps
%description
niri-settings is a GUI configuration application for the niri wayland
compositor

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
install -Dm755 niri-settings %{buildroot}%{_bindir}/niri-settings
install -Dm644 niri-settings.desktop %{buildroot}%{_datadir}/applications/niri-settings.desktop
install -d %{buildroot}%{_libexecdir}/%{name}/ui
install -Dm755 niri_settings.py %{buildroot}%{_libexecdir}/%{name}/niri_settings.py
install -Dm644 ui/*.py %{buildroot}%{_libexecdir}/%{name}/ui
install -d %{buildroot}%{_datadir}/%{name}/translations
install -Dm644 translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
install -Dm644 niri-settings.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/niri-settings.svg
%find_lang %{name} --all-name --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
