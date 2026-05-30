%global source0_hash d92f5c1901e5e767a2ddf195cb5300a583dd346e76d6da1bda633f67d6042ed4

%global orig_name org.kde.plasma.translator
%global upstream_version 6.0.0

Name:           plasma-applet-translator
Version: %{upstream_version}
Release: 1%{?dist}
Summary:        Plasma 6 applet for translate-shell

License:        MIT
URL:            https://store.kde.org/p/1395666
Source0:        http://qml.i-glu4it.ru/%{orig_name}_%{version}.tar.gz

BuildArch:      noarch

Requires:       translate-shell
Requires:       plasma-workspace
Requires:       xsel
Recommends:     qt6-qtmultimedia

%description
Easy to use translation plasmoid (GUI for translate-shell package).
Plasma 6 port of the KDE Store widget by Driglu4it.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{orig_name}-%{version}


%build


%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}
cp -a contents %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/
install -pm 644 metadata.json %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/

%files
%doc README.md
%{_datadir}/plasma/plasmoids/%{orig_name}

%changelog
* Wed May 27 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.0.0-1
- Plasma 6 port, drop Russian mirror tarball

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-13
- Prepare for Oreon 11 (RP1)
