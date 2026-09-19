%global source0_hash f0219cd8bd3db45d5173d850619145d55f9e864fe2106f6ceb9e736c575d0e03

Name:           terminator
Version:        2.1.5
Release:        4%{?dist}
Summary:        Store and run multiple GNOME terminals in one window

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/gnome-terminator
Source0:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/terminator-%{version}.tar.gz
Source1:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/terminator-%{version}.tar.gz.asc
Source2:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/gpg-D11A7596F61705480C711598F2FAC7C7BAE930A5.asc

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

Requires:       keybinder3
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       vte291

Patch0:         0000-terminator-fix-desktop-file.patch

%description
Multiple GNOME terminals in one window.  This is a project to produce
an efficient way of filling a large area of screen space with
terminals. This is done by splitting the window into a resizeable
grid of terminals. As such, you can  produce a very flexible
arrangements of terminals for different tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel 

%install
%pyproject_install
%pyproject_save_files terminatorlib
%find_lang %{name}

%check
%py3_check_import terminatorlib
desktop-file-validate %{buildroot}%{_datadir}/applications/terminator.desktop

%files -f %{pyproject_files} -f %{name}.lang
%doc CHANGELOG.md README.md
%license COPYING
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}_config.5.*
%{_bindir}/%{name}
%{_bindir}/remotinator
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/HighContrast/*/*/%{name}*.png
%{_datadir}/icons/HighContrast/*/*/%{name}*.svg
%{_datadir}/icons/HighContrast/16x16/status/terminal-bell.png
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{_datadir}/icons/hicolor/*/*/%{name}*.svg
%{_datadir}/icons/hicolor/16x16/status/terminal-bell.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/

%changelog
%autochangelog
