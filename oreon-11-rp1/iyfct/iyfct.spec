%global source0_hash 62a4b99d011895de8f9b0f5e90a7892c2fd02ac9cd41c162ec7f2a4a3c2375da

%global commit ac4555d1f4af4c3755d058a34da126acb9fc58d2
%global shortcommit ac4555d
%global gitdate 20180819

Name:           iyfct
Version:        1.0.2
Release:        %{gitdate}git.%{shortcommit}%{?dist}.18
Summary:        Side scrolling endless runner game

#See LICENSE file in source for details
#All code are GPLv3
#All assets are CC-BY 3.0
# Automatically converted from old format: GPLv3 and CC-BY - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-CC-BY
URL:            https://github.com/SimonLarsen/iyfct
Source0:        https://github.com/SimonLarsen/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  ImageMagick
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le

#From README
%description
The goal of the game is to survive as long as you can.
Jump over trains with closed doors and try (as much as possible) to run
through trains with open doors to avoid birds and tunnels.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6
#Strip some formating out of the README
sed 's/h[[:digit:]]. //g' README.textile > README

%build
#love "binary" files are just zipped sources, but should exclude appdata/docs
zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE -x README -x README.textile
#Generate icon (based on splash.png)
convert gfx/splash.png -crop 128x52+0+0 -background "#ECF3C9" -gravity center -extent 128x128! %{name}.png

%install
#Install love file
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
#Install execution script
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
#Install manpage
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
#Install appdata.xml and verify
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
#Install desktop, icon:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 %{name}.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE
%doc README
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
%autochangelog
