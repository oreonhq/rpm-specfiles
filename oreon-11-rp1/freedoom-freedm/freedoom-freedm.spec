%global source0_hash b420f13508ef745d7b38e83d15e55e0fc0b09d9a503c96741cddd9773d43f7c9

%global waddir  %{_datadir}/doom

Name:           freedoom-freedm

Version:        0.13.0
Release:        5%{?dist}
Summary:        Doom styled first person shooter deathmatch game

License:        BSD-3-Clause
URL:            https://freedoom.github.io/
Source0:        https://github.com/freedoom/freedoom/releases/download/v%{version}/freedm-%{version}.zip
Source1:        freedoom-freedm.desktop
Source2:        freedoom-freedm.appdata.xml
Source3:        freedoom.png

BuildArch:      noarch
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       prboom hicolor-icon-theme

%description
Freedoom: FreeDM is a 32-level Doom styled first person shooter
game designed for competitive deathmatch play. 

Freedoom: FreeDM uses all Free as in freedoom content combined with
the Open Source Doom engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n freedm-%{version}

%build
# Game data files.  Nothing to build!

%install
install -pD -m 0644 freedm.wad %{buildroot}/%{waddir}/freedm.wad
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/

%files
%doc README.html CREDITS.txt
%license COPYING.txt
%{waddir}/freedm.wad
%{_datadir}/appdata/freedoom-freedm.appdata.xml
%{_datadir}/applications/freedoom-freedm.desktop
%{_datadir}/icons/hicolor/48x48/apps/freedoom.png

%changelog
%autochangelog
