%global orig_name org.kde.plasma.translator

Name:           plasma-applet-translator
Version:        0.8
Release:        13%{?dist}
Summary:        Plasma 5 applet for translate-shell

License:        MIT
URL:            https://store.kde.org/p/1395666
Source0:        http://qml.i-glu4it.ru/%{orig_name}_%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 fec4b01ea5b0b32173ffd2708965b907565f8ad3ad0b378b203c1ef1b2e00ba4
%global source0_file org.kde.plasma.translator_0.8.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  desktop-file-utils

Requires:       translate-shell
Requires:       plasma-workspace
Requires:       qt5-qtxmlpatterns

%description
Easy to use translation plasmoid (GUI for translate-shell package).

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/org.kde.plasma.translator_0.8.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fec4b01ea5b0b32173ffd2708965b907565f8ad3ad0b378b203c1ef1b2e00ba4" || { echo "oreon: Source0 SHA256 mismatch for org.kde.plasma.translator_0.8.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-13
- Prepare for Oreon 11 (RP1)
