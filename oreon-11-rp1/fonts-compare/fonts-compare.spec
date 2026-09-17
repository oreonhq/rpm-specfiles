%global source0_hash 5c5eb1bfb35c2f7bf688852979e722a2aa42455b2a6c46623fcdbb6e6c5715da

Name:           fonts-compare
Version:        1.6.0
Release:        3%{?dist}
Summary:        Tool to compare fonts for a language

License:        GPL-2.0-or-later
URL:            https://github.com/sudipshil9862/fonts-compare
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/fonts-compare-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel 
Requires: python3-gobject
Requires: python3-langtable
Requires: python3-langdetect
Requires: fontconfig
Requires: hicolor-icon-theme
Requires: gtk4
Requires: python3-freetype
Requires: libadwaita

%description
Fonts-Compare is a tool that enables individuals
to compare various fonts in a particular language.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -D -m 755 fonts-compare %{buildroot}%{_bindir}/%{name}
install -D -m 755 fonts_compare.py %{buildroot}%{_datadir}/%{name}/
install -m 644 -D org.github.sudipshil9862.fonts-compare.desktop %{buildroot}/%{_datadir}/applications/org.github.sudipshil9862.%{name}.desktop
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
install -D -m 644 logo/16x16/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/
install -D -m 644 logo/22x22/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -D -m 644 logo/32x32/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -D -m 644 logo/48x48/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -D -m 644 logo/64x64/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
install -D -m 644 logo/128x128/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -D -m 644 logo/256x256/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -D -m 644 logo/fonts-compare.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.github.sudipshil9862.%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.github.sudipshil9862.%{name}.desktop
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/64x64/
%dir %{_datadir}/icons/hicolor/128x128/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
%autochangelog
