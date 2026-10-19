%global source0_hash 760a8ecfba1d14ac618b91d666c28734b1a1aea284e35514204732529aae8a4e
Summary:        GUI for editing keybindings in Enlightenment, DR16
Name:           e16-keyedit
Version:        0.10
Release:        1%{?dist}
License:        LicenseRef-Callaway-MIT-with-advertising
URL:            http://www.enlightenment.org/
Source0:        http://downloads.sourceforge.net/enlightenment/e16-keyedit-%{version}.tar.gz
Requires:       e16 >= 1.0.1
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
# /oreon:deps
%description
The e16-keyedit package provides a graphical interface for managing
keybindings in Enlightenment, DR16.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=e16keyedit
Comment=Manage keybindings for e16
Exec=e16keyedit
Terminal=false
Type=Application
Icon=/usr/share/e16/misc/e16
Categories=Settings;DesktopSettings;
EOF
%install
%make_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
