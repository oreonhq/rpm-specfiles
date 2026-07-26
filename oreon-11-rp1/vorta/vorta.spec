%global source0_hash 6d5193d21357e7fd7b45c5074d02e10dadcc7658232ae03825a59ad339cb5ea4

Name:           vorta
Version:        0.10.2
Release:        7%{?dist}
Summary:        A GUI for Borg Backup
License:        GPL-3.0-only AND BSD-2-Clause AND OFL-1.1
# src/vorta/qt_single_application.py if BSD-2-Clause
# src/vorta/assets/icons are OFL-1.1
URL:            https://vorta.borgbase.com/
Source0:        https://github.com/borgbase/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       borgbackup
Requires:       hicolor-icon-theme
Requires:       qt5-qtsvg

BuildArch:      noarch

# https://github.com/borgbase/vorta/commit/0cc15e3d3d647bae1782f2c21eafacbf2c8073c6
# should be upstream in > 0.9.1
#Patch:          fix-appdata.xml.patch

%description
Vorta is a backup client for macOS and Linux desktops.
It integrates the mighty BorgBackup with your desktop environment
to protect your data from disk failure, ransomware and theft

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# https://github.com/borgbase/vorta/issues/1690
sed -i 's/platformdirs >=2.6.0/platformdirs >=2.3.0/g' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
# all tests require a GUI (pyqt5) to complete
# so they won't work in mock

%install
%pyproject_install
%pyproject_save_files %{name}
#%%py3_install
install -D -p -m 644 src/vorta/assets/icons/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.borgbase.Vorta.svg
install -D -p -m 644 package/icon-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/com.borgbase.Vorta-symbolic.svg
install -D -p src/vorta/assets/metadata/com.borgbase.Vorta.desktop -t %{buildroot}%{_datadir}/applications/
install -D -p src/vorta/assets/metadata/com.borgbase.Vorta.appdata.xml -t %{buildroot}/%{_metainfodir}/

desktop-file-validate %{buildroot}/%{_datadir}/applications/com.borgbase.Vorta.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{pyproject_files}
%doc README.md CONTRIBUTORS.md
%license LICENSE.txt
%{_bindir}/vorta
%{_datadir}/applications/com.borgbase.Vorta.desktop
%{_metainfodir}/com.borgbase.Vorta.appdata.xml
%{_datadir}/icons/hicolor/*/apps/com.borgbase.Vorta*.svg

%changelog
%autochangelog
