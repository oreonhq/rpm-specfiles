%global source0_hash 6311797cce81e628cadda29c77fc34c35361d2c9f51debf397a932de48071d07

%global orig_name org.kde.plasma.translator

Name:           plasma-applet-translator
Version: 6.6.5
Release: 1%{?dist}
Summary:        Plasma 5 applet for translate-shell

License:        MIT
URL:            https://store.kde.org/p/1395666
Source0:        http://qml.i-glu4it.ru/%{orig_name}_%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils

Requires:       translate-shell
Requires:       plasma-workspace
Requires:       qt5-qtxmlpatterns

%description
Easy to use translation plasmoid (GUI for translate-shell package).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{orig_name}


%build


%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}
cp -r contents %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/
install -pm 644 metadata.desktop %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%files
%license LICENSE
# %doc add-docs-here
%{_datadir}/plasma/plasmoids/%{orig_name}

%changelog
* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-13
- Prepare for Oreon 11 (RP1)
