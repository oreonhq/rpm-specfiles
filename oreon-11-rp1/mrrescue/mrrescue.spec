%global source0_hash 8153d3c69e50d8d5e7fe5441901f01535315929fdde5ad15c885c8332c9bd7ca
Name:           mrrescue
Version:        1.02e
Release:        1%{?dist}
Summary:        Arcade-style fire fighting game
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT
URL:            http://tangramgames.dk/games/mrrescue
Source0:        https://github.com/SimonLarsen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-appdata.patch
Patch1:         %{name}-%{version}-double-define.patch
Patch2:         %{name}-%{version}-love11.patch
Patch3:         %{name}-%{version}-Fixed-remaining-setColor-statements.patch
Patch4:         %{name}-%{version}-Updated-conf.lua-to-11.0-template.patch
BuildArch:      noarch
Requires:       love
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# /oreon:deps
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

zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE -x README.md
convert data/splash.png -crop 256x205+0+0 -background none -gravity center -extent 256x256! %{name}.png
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
install -p -D -m 0644 %{name}.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
