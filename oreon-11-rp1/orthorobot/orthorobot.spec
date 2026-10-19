%global source1_hash e183a603fd22463d71c243948a6a46378399e01ec1c499f942e8d85eed400cb9
%global source0_hash a9ae83bfdac90e726e27a496c7ee1c23c0e9e800294e1908a6cc61ea6f0ed415
Name:           orthorobot
Version:        1.1.1
Release:        1%{?dist}
Summary:        A perspective based puzzle game
License:        WTFPL
URL:            http://stabyourself.net/orthorobot/
Source0:        https://github.com/Stabyourself/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Stabyourself/%{name}/48f07423950b29a94b04aefe268f2f951f55b62e/LICENSE.txt
Patch0:         %{name}-appdata.patch
Patch1:         %{name}-%{version}-love11.patch
BuildArch:      noarch
Requires:       love
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Literally bridging the gap between 2D and 3D games, Ortho Robot is a
perspective based puzzle game, where you flatten the view to move
across gaps. This game is made with LOVE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
#Copy LICENSE, fixed after v1.1.1
cp -f %{SOURCE1} ./LICENSE.txt
#Change version in appdata
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6

%build

zip -r %{name}.love . -x appdata/* -x appdata/ -x README.md -x LICENSE.txt
%install
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 helpplayer.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
