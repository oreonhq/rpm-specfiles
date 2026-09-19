%global source0_hash 8153d3c69e50d8d5e7fe5441901f01535315929fdde5ad15c885c8332c9bd7ca

Name:           mrrescue
Version:        1.02e
Release:        29%{?dist}
Summary:        Arcade-style fire fighting game

#See LICENSE file in source for details
#All code is zlib, excluding slam, AnAL and TSerial, which are MIT
#All assets are CC-BY-SA
# Automatically converted from old format: zlib and CC-BY-SA and MIT - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT
URL:            http://tangramgames.dk/games/mrrescue
Source0:        https://github.com/SimonLarsen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch
#Upstream patches:
#https://github.com/SimonLarsen/mrrescue/commit/ec139833eba2781507cf32d9df30772138a76829
Patch1:         %{name}-%{version}-double-define.patch
#https://github.com/SimonLarsen/mrrescue/commit/ab23031e0c2faecb77fde1be8a41d6f8ea4e6eda
Patch2:         %{name}-%{version}-love11.patch
#https://github.com/SimonLarsen/mrrescue/commit/5a58668d9a1e661f6591bd44a76cf242b3aabf3e
Patch3:         %{name}-%{version}-Fixed-remaining-setColor-statements.patch
#https://github.com/SimonLarsen/mrrescue/commit/a5be73c60acb8d1be506f7b5e48e784492ba96ce
Patch4:         %{name}-%{version}-Updated-conf.lua-to-11.0-template.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  ImageMagick
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le

#From the website (see URL above)
%description
Mr. Rescue is an arcade styled 2d action game centered around evacuating
civilians from burning buildings. The game features fast paced fire
extinguishing action, intense boss battles, a catchy soundtrack and lots of
throwing people around in pseudo-randomly generated buildings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6

%build
#love "binary" files are just zipped sources, but should exclude appdata/docs
zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE -x README.md
#Generate icon (modified splash.png)
convert data/splash.png -crop 256x205+0+0 -background none -gravity center -extent 256x256! %{name}.png

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
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
#Install desktop, icon:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 %{name}.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc README.md
%license LICENSE
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*.appdata.xml

%changelog
%autochangelog
